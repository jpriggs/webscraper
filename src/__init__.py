from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def query_wikipedia():
    return jsonify(hello='world')