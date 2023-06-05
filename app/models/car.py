from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Car(Base):
    car_code: Mapped[str] = mapped_column(String(5), unique=True)
    current_location: Mapped[str] = mapped_column(
        String(5),
        ForeignKey("location.zip")
    )
    capacity_car: Mapped[int] = mapped_column(Integer, nullable=False)
