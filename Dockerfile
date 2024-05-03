FROM python:3.10-slim

RUN apt-get update

WORKDIR /app

ENV DEBUG='False'
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main.wsgi:application"]
