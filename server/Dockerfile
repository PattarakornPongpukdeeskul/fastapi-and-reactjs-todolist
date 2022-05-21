FROM python:3.8.6-slim


WORKDIR /usr/src
COPY . /usr/src


RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 2222
CMD   ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "2222", "--reload"]
