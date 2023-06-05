from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.shemas.car import CarBase, CarBaseUpdate, CarDB
from app.crud.car import car_crud
from app.api.validators import check_location_exists, check_car_exists
from app.crud.location import location_crud

router = APIRouter()


@router.patch(
    '/{car_id}',
    response_model=CarDB,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
    summary="Редактирование локуации машины.",
    response_description="Новая локация машины."
)
async def update_car_location(
    car_id: int,
    obj_in: CarBaseUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """
    Запрос для изменения локации автомобиля. \n
    Редактирование машины по **ID**
    локация (определяется по введенному **zip**-коду).
    - **car_code**: Номер машины в формате 1111A (4-цифры, буква A-Z).
    - **new_locatin**: Zip-код новой локации.
    """
    # зделать проверку на локацию
    car = await check_car_exists(car_id, session)
    car_id = await car_crud.update(car, obj_in, session)
    return car_id
