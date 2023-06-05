# Weldex_Test
### Тестовое задание. API: Сервис поиска ближайших машин для перевозки грузов. 

![](https://img.shields.io/badge/Python-3.11-blue) 
![](https://img.shields.io/badge/FastAPI-0.95.2-yellow)
![](https://img.shields.io/badge/SQLAlchemy-2.0.16-green)
![](https://img.shields.io/badge/Alembic-1.11.1-red)
![](https://img.shields.io/badge/Geopy-2.3.0-9cf)
![](https://img.shields.io/badge/Docker-3.8-ff55df)
![](https://img.shields.io/badge/Gunicorn-20.1.0-gf55df)
<br>

## Описание

Это API для поиска и бронирования машин для перевозки грузов. Сервис позволяет находить ближайшие машины в радиусе 450 миль.

## Запуск приложения с помощью Docker Compose
Запуск приложения с помощью Docker Compose
Для установки и запуска приложения вам потребуется [Docker](https://www.docker.com/get-started/) и [Docker Compose](https://docs.docker.com/compose/install/).

1. Клонируйте репозиторий:

```bash
git clone https://github.com/oitczvovich/Weldex_Test
```

2. Создайте файл .env и установите значения переменных. Пример файле .env.example: 

```bash
APP_TITLE= # Название проекта
DESCRIPTION= # API: Сервис поиска ближайших машин для перевозки грузов.
POSTGRES_DB= # Название базы данных
POSTGRES_USER= # Имя юзер
POSTGRES_PASSWORD= # Пароль для БД
DB_HOST= # Имя хоста 
DB_PORT= # Номера порта

```

3. Запустите приложение и базу данных:
```bash 
docker-compose up -d --build 
```

4. Миграция моделей БД.
```bash
docker-compose exec app alembic upgrade head

```

5. Наполнения тестовыми данными.
```bash
docker-compose exec app python fill_db.py
```

Проект доступен по адресу [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


Авто: Скалацкий Владимир<br>
e-mail: skalakcii@yandex.ru<br>
https://github.com/oitczvovich<br>
https://t.me/OitcZvovich