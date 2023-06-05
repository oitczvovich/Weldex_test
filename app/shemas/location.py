from typing import Optional

from pydantic import BaseModel, Extra, Field, root_validator, validator


class LocationBase(BaseModel):

    class Config:
        orm_mode = True


class LocationAnswer(BaseModel):


    class Config:
        orm_mode = True