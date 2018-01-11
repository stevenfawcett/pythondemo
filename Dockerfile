FROM python:2

WORKDIR /usr/src/app

COPY example1.py .

CMD [ "python", "example1.py" ]

