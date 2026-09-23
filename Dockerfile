FROM python:3.12-slim

WORKDIR /app

RUN pip install flask

COPY app/app.py .

EXPOSE 8080

CMD ["python", "app.py"]