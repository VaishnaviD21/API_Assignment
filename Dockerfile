FROM python:3.9
ENV PYTHONUNBUFFERED 1

      WORKDIR /code_api

      COPY requirements.txt /code_api/
      RUN pip install -r requirements.txt

      COPY . /code_api/