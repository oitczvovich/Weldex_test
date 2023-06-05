from typing import Optional

from sqlalchemy import and_, between, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.car import Car


class CRUDCar(CRUDBase):
    async def get_car_by_car_id(
            self,
            car_id: str,
            session: AsyncSession,
    ) -> Optional[int]:
        car = await session.execute(
            select(Car).where(
                Car.id == car_id
            )
        )
        car = car.scalars().first()
        return car

car_crud = CRUDCar(Car)
