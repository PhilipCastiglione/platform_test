from flask import jsonify
from app import db
from app.models import Player
from app.validators import PlayerValidator

# TODO: error handling
# implement an error handler that looks at the error rather than throwing a 500
# put failsafe endpoint error handling in a decorator

class PlayerController:
    def __init__(self, request):
        self.request = request

    def show(self, id):
        try:
            player = Player.query.get(id)
            if player:
                return jsonify(player.to_dict()), 200
            else:
                return 'Not found', 404
        except Exception as err:
            # TODO: logging service
            print(err)
            return 'Internal Server Error', 500

    def create(self):
        try:
            entry_params = self.request.json

            player_validator = PlayerValidator(entry_params)
            player_validator.validate()

            if player_validator.is_valid():
                player = Player(
                    name=entry_params['name'],
                    gold=0,
                    attack_strength=70,
                    hit_points=100,
                    luck=10
                )
                db.session.add(player)
                db.session.commit()

                return '', 201
            else:
                return jsonify(player_validator.errors), 422
        except Exception as err:
            # TODO: logging service
            print(err)
            return 'Internal Server Error', 500
