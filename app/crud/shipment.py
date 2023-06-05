from app.core.db import AsyncSessionLocal

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.shipment import Shipment
from app.shemas.shipment import ShipmentBase


class CRUDShipment(CRUDBase):
    pass


shipment_crud = CRUDShipment(Shipment)
