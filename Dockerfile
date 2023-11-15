#! /usr/bin/env python3

FROM python:3.10.12

COPY requirements.txt .

RUN pip3 install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends libopenblas-dev liblapack-dev

COPY Pipfile .
COPY Pipfile.lock .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=summary.py

EXPOSE 80

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "80"]
