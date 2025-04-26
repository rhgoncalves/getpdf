from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"message": "Hello World"})

# Don't need the app.run() for Azure deployment.
# Azure will use Gunicorn to run this app in production.
