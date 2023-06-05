from fastapi import APIRouter

from app.api.endpoints import (car_router, shipment_router)

main_router = APIRouter()
main_router.include_router(
    car_router, prefix='/car', tags=['Car']
)
main_router.include_router(
    shipment_router, prefix='/shipment', tags=['Shipment']
)
