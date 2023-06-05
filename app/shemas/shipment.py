from typing import Optional

from pydantic import BaseModel, Extra, Field, root_validator, validator


class ShipmentBase(BaseModel):
    pass


class ShipmentCreate(ShipmentBase):
    description: Optional[str] = Field(title="Описание груза.")
    shipment_weight: int = Field(...)  # min_length=1, max_length=1000)
    location_pickup: str = Field(...)  # здесь вводи ZIP-code 
    location_delivery: str = Field(...)  # здесь вводи ZIP-code


class Ship(ShipmentBase):
    location_pickup: str
    location_delivery: str
    count_car_near: int


class ShipmentUpdate(ShipmentBase):
    description: Optional[str] = Field()
    shipment_weight: Optional[int] = Field()


class ShipmentDB(ShipmentBase):
    pass

    class Config:
        orm_mode = True
