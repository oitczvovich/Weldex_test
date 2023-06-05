from typing import Optional

from sqlalchemy import and_, between, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.location import Location


class CRUDLocation(CRUDBase):
    """Функция возвращает локация по Zip-code."""
    async def get_location_by_zip(
            self,
            zip: str,
            session: AsyncSession,
    ):
        location = await session.execute(
            select(Location).where(
                Location.zip == zip
            )
        )
        location = location.scalars().first()
        location = (location.lat, location.lng)
        return location


location_crud = CRUDLocation(Location)
