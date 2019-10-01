from flask import request, render_template, jsonify
from app import app
from app.controllers import PlayerController
from app.models import Player

@app.route('/')
@app.route('/index')
@app.route('/heartbeat')
def index():
    return jsonify({"message": "Hello, World!"}), 200

@app.route('/player', methods=['POST'])
def create_player():
    return PlayerController(request).create()

@app.route('/player/<id>', methods=['GET'])
def show_player(id):
    return PlayerController(request).show(id)

@app.route('/player/<id>/battle', methods=['POST'])
def initiate_battle(id):
    return PlayerController(request).initiate_battle(id)
