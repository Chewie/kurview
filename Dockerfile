FROM python:3-onbuild
MAINTAINER Kévin Sztern <sztern.kevin@gmail.com>
EXPOSE 5000
CMD [ "gunicorn", "-b", "0.0.0.0:5000", "main:app" ]
