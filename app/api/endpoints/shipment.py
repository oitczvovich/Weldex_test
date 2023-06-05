from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session

from app.crud.shipment import shipment_crud
from app.shemas.shipment import (
    ShipmentBase,
    ShipmentDB,
    ShipmentCreate,
    ShipmentUpdate,
    Ship
)
from app.shemas.location import LocationAnswer
from app.api.validators import check_location_exists, check_exists_shipment
from app.crud.location import location_crud
from app.crud.car import car_crud
from app.services.distance_to_car import get_list_distance_to_car
from app.services.distance_to_car import count_car_near

router = APIRouter()


@router.get(
    '/',
    # response_model=list[Ship],
    summary="Список грузов в радиусе 450 миль."
)
async def get_all_shipments(
    session: AsyncSession = Depends(get_async_session)
):
    """
    Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль));
    """
    res = await count_car_near(session)
    return res


@router.get(
    '/{shipment_id}',
    # response_model=ShipmentBase,
    summary="Узнать о грузе по ID",
)
async def get_shipment(
    shipment_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Получение информации о конкретном грузе по ID 
    (локации pick-up, delivery, вес, описание, список номеров 
    ВСЕХ машин с расстоянием до выбранного груза);
    """
    # перенести все в функцию get_list_distance_to_car
    shipment = await shipment_crud.get(obj_id=shipment_id, session=session)
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
    return shipment, distance_list


@router.post(
    '/',
    summary="Создание нового груза.",
    response_description="Новый груз создан."
)
async def create_shipment(
    shipment: ShipmentCreate,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Создание нового груза (характеристики локаций pick-up,\n
    delivery определяются по введенному zip-коду).
    - **description**: Описание груза. Опция скорее всего
    - **shipment_weight**: Вес груза.
    - **location_pickup**: Zip-код места загрузки.
    - **location_delivery**: Zip-код места доставки.
    """
    new_shipment = await shipment_crud.create(shipment, session)
    return new_shipment


@router.patch(
    '/{shipment_id}',
    # response_model=ShipmentBase,
    # response_model_execlude_none=True,
    summary="Изменения груза."
)
async def update_shipment(
    shipment_id: int,
    obj_in: ShipmentUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Редактирование груза по ID (вес, описание).
    """
    shipment = await check_exists_shipment(
        shipment_id, session
    )

    shipment = await shipment_crud.update(
        shipment, obj_in, session
    )
    return shipment


@router.delete(
    '/{shipment_id}',
    response_model=ShipmentDB,
    response_model_exclude_none=True,
    summary="Удаление груза."
)
async def delete_shipment(
    shipment_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Удаление груза по ID.
    """
    shipment = await check_exists_shipment(
        shipment_id, session
    )
    shipment = await shipment_crud.remove(
        shipment, session
    )
    return shipment
