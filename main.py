from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"message": "Hello World"})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

