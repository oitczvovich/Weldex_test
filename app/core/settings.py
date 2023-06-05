from pathlib import Path
from typing import Optional

from pydantic import BaseSettings
from pydantic.tools import lru_cache

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = None
if Path.exists(BASE_DIR / ".env"):
    ENV_FILE = BASE_DIR / ".env"


class Settings(BaseSettings):
    APP_TITLE: str = 'Test'
    DESCRIPTION: str = 'Test'

    # Формат валидации номера машины
    FORMAT_CAR_ID = '^\d{4}[A-Z]$'

    # Радиус поиска машин для груза
    RADIUS_LOCATION = 450

    # Параметры подключения к БД
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str = 'db'
    DB_PORT: str = '5432'

    @property
    def database_url(self) -> str:
        """Получить ссылку для подключения к DB."""
        return (
            "postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = ENV_FILE


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
