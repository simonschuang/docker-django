FROM ubuntu:xenial

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y python vim && \
    apt-get clean

ADD get-pip.py /get-pip.py
RUN python /get-pip.py
RUN pip install Django djangorestframework django-rest-swagger django-filter

ADD portal /portal

WORKDIR /portal

CMD ["python", "manage.py", "runserver", "0:80"]
