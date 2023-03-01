from flask import Flask, request, jsonify
from flask_swagger import swagger
from markupsafe import escape
import json
import sys
import traceback
import unidecode
import jsbeautifier
from config import env_config
import os

app = Flask(__name__)


@app.route('/')
def home():
    available_endpoints = {
        'available_endpoints': {
            'go': {
                'language': 'string',
                'word': 'string'
            }
        }
    }

    return jsonify(available_endpoints)


@app.route('/go', methods=['GET'])
def parse_script():
    available_endpoints = {
        'available_endpoints': {
            'go': {
                'language': 'string',
                'word': 'string'
            }
        }
    }
    # print(env)
    # print(f" ---> env '{env}' ")
    # env = os.getenv("FLASK_ENV")
    # app.config.from_object(env_config[env])

    return jsonify(available_endpoints)
