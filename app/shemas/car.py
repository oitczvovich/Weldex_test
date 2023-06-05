import re
from typing import Optional

from pydantic import BaseModel, Extra, Field, root_validator, validator, PositiveInt
from app.core.settings import settings


class CarBase(BaseModel):
    """ Базовый класс машины."""
    car_code: str
    current_location: str  # Zip-code, Штат, город
    capacity_car: PositiveInt = Field(
        ...,
        title="Грузоподемность.",
        description="Грузоподемность машины от 1 до 1000.",
    )

    class Config:
        schema_extra = {
            "example": {
                "car_code": "1111A",
                "current_location": "Zip-code, State, City",
                "capacity_car": "333"
            }
        }


class CarBaseUpdate(BaseModel):
    """ Схема для обновления локации машины."""
    current_location: str = Field(
        ...,
        alias="New location",
        title="Zip-code.",
        description="Укажите zip-code новой локации.",
        # max_length=5
        )  # Zip-code, Штат, город
    # capacity_car: int = Field(
    #     ...,
    #     title="Грузоподемность.",
    #     description="Грузоподемность машины от 1 до 1000.",
    #     # min_length=1,
        # max_length=1000
    # )

    # @validator("")
    # def check_value_car_id(cls, value: str):
    #     "Проверка коректного car_code формат - '1111A'."
    #     if re.search(settings.FORMAT_CAR_ID, value):
    #         return ValueError("car_code должен быть формата 1111A'")
    #     return value

    # @validator('new_location')
    # def check_size_value(cls, value):
    #     if len(value) != 5:
    #         return ValueError("car_code должен быть формата 1111A'")
    #     return value


class CarDB(CarBase):
    car_code: Optional[str]
    current_location: Optional[str]
    capacity_car: Optional[int]

    class Config:
        orm_mode = True
