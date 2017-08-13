FROM python:3
MAINTAINER Kévin Sztern <sztern.kevin@gmail.com>
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "gunicorn", "-b", "0.0.0.0:5000", "main:app" ]
