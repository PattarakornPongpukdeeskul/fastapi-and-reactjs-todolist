FROM python:3.9-alpine

WORKDIR /usr/src/
COPY ./server .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 2222
CMD   ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "2222", "--reload"]
