import os
from dotenv import load_dotenv

from flask import Flask, jsonify

load_dotenv()
app = Flask(__name__)
app.config['SECRET'] = os.environ.get('SECRET')


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"message": f"Hello from API server. Current version is: {os.environ.get('APP_VERSION')}"}), 200


if __name__ == '__main__':
    app.run()
