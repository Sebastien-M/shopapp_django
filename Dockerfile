FROM python:2.7-slim
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
 RUN apt-get update && apt-get install -y libmysqlclient-dev
 RUN apt-get install -y gcc
 RUN pip install mysqlclient
 ADD . /code/