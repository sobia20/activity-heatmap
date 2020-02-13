FROM python:3.7.0-alpine3.7

MAINTAINER Sobia Khalid "sobia.khalid.2126@gmail.com"

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt 

COPY . /

ENV FLASK_APP app.py

CMD [ "flask", "run", "--host", "0.0.0.0"  ]
 
