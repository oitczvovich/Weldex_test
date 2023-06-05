import csv
import asyncio
import random

from sqlalchemy import select
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker
)
from contextlib import asynccontextmanager

from app.core.base import Location, Car, Shipment
from app.core.db import get_async_session
from app.services.random_num_car import random_num_car

COUNT_CAR = 20


async def _filling_shipment_db(
        session: async_sessionmaker[AsyncSession],
        ) -> None:
    """ Функция для заполнения БД тестовыми машинами."""
    location_zip = await session.execute(select(Location.zip))
    location_zip = location_zip.scalars().all()

    for shipment in range(30):
        category_obj = Shipment(
            description=f"Description {shipment}",
            location_pickup=str(random.choice(location_zip)),
            location_delivery=str(random.choice(location_zip)),
            shipment_weight=random.randint(1, 1000),
        )
        session.add(category_obj)
    await session.commit()



async def _filling_car_db(
        session: async_sessionmaker[AsyncSession],
        ) -> None:
    """ Функция для заполнения БД тестовыми машинами."""
    location_zip = await session.execute(select(Location.zip))
    location_zip = location_zip.scalars().all()

    for car in range(COUNT_CAR):
        category_obj = Car(
            car_code=random_num_car(),
            current_location=str(random.choice(location_zip)),
            capacity_car=random.randint(1, 1000),
        )
        session.add(category_obj)
    await session.commit()


async def _filling_location_db(
        session: async_sessionmaker[AsyncSession],
        ) -> None:
    """ Функция для заполнения БД тестовыми локациями."""
    with open('uszips.csv', 'r', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            category_obj = Location(
                zip=str(row["zip"]),
                city=row["city"],
                state_name=row["state_name"],
                lat=float(row["lat"]),
                lng=float(row["lng"]),
            )
            session.add(category_obj)
        await session.commit()


async def run():
    session_manager = asynccontextmanager(get_async_session)
    async with session_manager() as session:
        await _filling_location_db(session)
        print("База наполнена данными о локациях.")
        await _filling_car_db(session)
        print("База наполнена данными о машинах.")
        await _filling_shipment_db(session)
        print("База наполнена данными о грузе.")


if __name__ == "__main__":
    asyncio.run(run())
