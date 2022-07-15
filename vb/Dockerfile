FROM python:3.6

RUN apt update && apt install make -y
ADD . /code
WORKDIR /code
RUN make install 
RUN make run 
