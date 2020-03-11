FROM python:3.8.2-slim-buster

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3","run-api.py"]