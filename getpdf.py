from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"message": "Hello World"})

if __name__ == "__main__":
        app = init_func(None)

try:
        web.run_app(app, host="0.0.0.0", port=CONFIG.PORT)
    except Exception as error:
        raise error
