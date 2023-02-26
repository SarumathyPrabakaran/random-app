FROM python:3.8

WORKDIR /random-app

ADD app.py .

RUN pip install flask 

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]