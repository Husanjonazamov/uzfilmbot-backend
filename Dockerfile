FROM python:3.11-slim


WORKDIR /code

RUN apt update && apt upgrade -y

COPY . .


RUN pip install -r requirements.txt

CMD sh ./entrypoint.sh