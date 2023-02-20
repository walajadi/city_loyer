FROM python:3.7

RUN mkdir /code

WORKDIR /code

COPY app/requirements.txt .

RUN pip install -r requirements.txt

COPY ./app .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]