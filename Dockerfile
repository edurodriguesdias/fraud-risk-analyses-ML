FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y build-essential

COPY . /app
WORKDIR /app

RUN pip install -r requirements/requirements.txt --ignore-installed

CMD ["tail", "-f", "/dev/null"]