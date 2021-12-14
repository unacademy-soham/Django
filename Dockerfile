FROM python:3.8.3-alpine

WORKDIR /app

RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc and-build-dependencies \
    && rm -rf /var/lib/apt/lists/* \
    && pip install cryptography \
    && apt-get purge -y --auto-remove gcc and-build-dependencies
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
