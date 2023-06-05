import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from geopy import distance as d
from geopy.adapters import AioHTTPAdapter
from geopy.geocoders import Nominatim
from app.crud.location import location_crud
from app.crud.shipment import shipment_crud
from app.crud.car import car_crud
from app.core.settings import settings


async def get_list_distance_to_car(
    shipment_coordinates: list,
    cars_list: list,
    session: AsyncSession,
) -> dict:
    """Функция возвращает список номер машины и расстояние до груза."""
    distance_list = []
    for car in cars_list:
        number = car.car_code
        zip = car.current_location
        car_coordinates = await location_crud.get_location_by_zip(zip, session)
        dist = await count_distance(shipment_coordinates, car_coordinates)
        res = number, dist
        distance_list.append(res)
    return distance_list


async def count_distance(
        shipment_coordinates,
        car_coordinates,
        ):
    """Функция для получения расстояния между локациями."""
    distance = d.distance(shipment_coordinates, car_coordinates).miles
    return int(distance)



async def count_car_near(
    session: AsyncSession,
):
    shipments = await shipment_crud.get_multi(session)
    res = []
    for shipment in shipments:
        shipment_coordinates = await location_crud.get_location_by_zip(
            shipment.location_pickup,
            session,
        )
        cars_list = list(items for items in await car_crud.get_multi(session))
        distance_list = await get_list_distance_to_car(
            shipment_coordinates,
            cars_list,
            session,
        )

        # проходимся по distance_list считаем все что меньще 450
        count_shipments_near = 0
        for x in distance_list:
            if x[1] <= settings.RADIUS_LOCATION:
                count_shipments_near += 1
        result = (
            shipment.location_pickup,
            shipment.location_delivery,
            count_shipments_near)
        res.append(result)
    return res
