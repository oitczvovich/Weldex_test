from sqlalchemy import Integer, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Shipment(Base):
    description: Mapped[str] = mapped_column(Text)
    shipment_weight: Mapped[int] = mapped_column(Integer)  # должно быть ограничение 1-1000
    location_pickup: Mapped[float] = mapped_column(ForeignKey("location.zip"))
    location_delivery: Mapped[float] = mapped_column(ForeignKey("location.zip"))