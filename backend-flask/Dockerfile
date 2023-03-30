FROM 802193104814.dkr.ecr.eu-west-1.amazonaws.com/cruddur-python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
COPY external-script.sh /
RUN pip3 install -r requirements.txt

COPY . .

# Set Enviroment Variables (Env Vars)
# Inside Container and wil remain set when the container is running
ENV FLASK_DEBUG=1

EXPOSE ${PORT}
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
CMD ["/external-script.sh"]