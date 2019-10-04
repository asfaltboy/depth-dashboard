FROM python:3.6

COPY requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir -p /app/

COPY *.py /app/

CMD ["python3", "/app/app.py"]
