FROM python:3.9.5-slim

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD ["gunicorn","--workers=4", "wsgi:application", "-b", "0.0.0.0:5000"]