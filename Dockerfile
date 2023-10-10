FROM python:3.8

COPY /config /config
WORKDIR /config
RUN pip install -r requirements.txt
RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y netcat-traditional
RUN apt-get install docker.io -y
COPY /src /src
COPY /config/.env /src/.env
WORKDIR /src
COPY /entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
