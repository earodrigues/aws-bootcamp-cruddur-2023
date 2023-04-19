FROM 802193104814.dkr.ecr.eu-west-1.amazonaws.com/cruddur-python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
COPY external-script.sh /
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE ${PORT}
#CMD [ "python3", "-m", "-u", "flask", "run", "--host=0.0.0.0", "--port=4567", "--debug"]
CMD ["/external-script.sh"]