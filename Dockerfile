FROM python:3.11-slim

RUN mkdir /code

COPY requirements.txt /code

RUN pip3 install -r /code/requirements.txt

COPY . /code

WORKDIR /code

# RUN chmod a+x start_app.sh
# RUN start_app.sh

# RUN alembic upgrade head

CMD gunicorn app.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000

