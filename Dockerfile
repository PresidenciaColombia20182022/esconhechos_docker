FROM python:3.8-slim-buster

#ENV PYTHONUNBUFFERED 1

#RUN mkdir /code
WORKDIR /code/

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . .

#EXPOSE 8000
COPY ./entrypoint.sh /

#CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT [ "sh","/entrypoint.sh" ]