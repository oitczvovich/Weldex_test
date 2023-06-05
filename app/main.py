from fastapi import FastAPI

from app.api.routers import main_router
from app.core.settings import settings

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.DESCRIPTION,
)

app.include_router(main_router)

# @app.on_event('startup')
# async def startup():
#     await create_first_superuser()
