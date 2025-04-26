from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"message": "Hello World test 1"})

# Correct way to run a Flask app in development
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8000)
