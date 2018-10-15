FROM python:3.7.0-alpine3.8

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "/app/bowling.py"]
