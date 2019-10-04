FROM python:3.6

ENV PORT=8080

COPY requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir -p /app/

COPY *.py /app/

WORKDIR /app

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8080"]
