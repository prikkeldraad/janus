FROM python:3.8-alpine

APK ADD make
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN make run 
