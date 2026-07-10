from flask import Flask, jsonify  #flask is a micro web framework written in python. and jsonify is a function that converts the data to json format.

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello!")

@app.route("/health")
def health():
    return jsonify(status="ok")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)