FROM python:3.8

WORKDIR /random-app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD app.py .

EXPOSE 3000

CMD [ "python3", "app.py"]