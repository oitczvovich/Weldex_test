from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.car import car_crud
from app.crud.location import location_crud
from app.crud.shipment import shipment_crud
from app.models import Car, Location, Shipment


async def check_car_exists(
        id: int,
        session: AsyncSession,
) -> Car:
    car = await car_crud.get(
        id, session
    )
    if car is None:
        raise HTTPException(
            status_code=404,
            detail='Машина не найдена!'
        )
    return car


async def check_location_exists(
        zip: str,
        session: AsyncSession,
) -> Location:
    location = await location_crud.get_location_by_zip(
        zip, session
    )
    if location is None:
        raise HTTPException(
            status_code=404,
            detail='Пункт не найдена!'
        )
    return location


async def check_exists_shipment(
        id: int,
        session: AsyncSession,
) -> Shipment:
    shipment = await shipment_crud.get(
        obj_id=id, session=session)
    if not shipment:
        raise HTTPException(status_code=404, detail="Груз не найден!")
    return shipment
