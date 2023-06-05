from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Location(Base):
    """ Модель локации."""
    zip: Mapped[str] = mapped_column(String(5), unique=True)
    city: Mapped[str] = mapped_column(String(255))
    state_name: Mapped[str] = mapped_column(String(255))
    lat: Mapped[float] = mapped_column(Float)
    lng: Mapped[float] = mapped_column(Float)

    # def __repr__(self) -> str:
    #     return f"Zip {self.zip}, Штат {self.state_name}, Город {self.city}"
