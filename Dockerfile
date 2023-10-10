FROM python:3.8

COPY /config /config
WORKDIR /config
RUN pip install -r requirements.txt
COPY /src /src
WORKDIR /src
CMD ["python", "hello.py"]