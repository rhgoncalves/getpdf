from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"message": "Hello World"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # Ensure Flask listens on port 8080

