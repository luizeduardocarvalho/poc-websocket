FROM python:3.7-alpine3.7

COPY ./requirements.txt /requirements.txt

RUN apk add build-base
RUN pip3 install -r /requirements.txt

COPY . /app

WORKDIR /app

CMD [ "python", "app.py" ]