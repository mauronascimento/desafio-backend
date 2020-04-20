FROM python:3.6-slim
EXPOSE 8000
EXPOSE 5432
ENV PYTHON_UNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y python-pip python-dev \
    libpq-dev postgresql postgresql-contrib

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
