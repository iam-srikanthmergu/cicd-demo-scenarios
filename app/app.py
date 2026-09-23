from flask import Flask
import os

app = Flask(__name__)

DB_HOST = os.environ["DB_HOST"]

@app.route("/")
def home():
    return "Application is running!"

@app.route("/health")
def health():
    return "Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)