FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY . .
RUN pip3 install -r requirements.txt 

EXPOSE 3000
CMD [ "python3", "application.py" ]