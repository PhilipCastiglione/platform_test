from flask import jsonify
from app import db, battle_queue
from app.models import Player
from app.validators import BattleValidator, PlayerValidator
from app.battle_engine import BattleEngine

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
                    luck=10,
                    score=0
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

    def initiate_battle(self, id):
        try:
            initiating_player = Player.query.get(id)

            if not initiating_player:
                return 'Not found', 404

            entry_params = self.request.json

            # TODO:
            # this approach means 2 db queries, one of which is redundant.
            # This should be made more performant.
            battle_validator = BattleValidator(entry_params, int(id))
            battle_validator.validate()

            if battle_validator.is_valid():
                targetted_player = Player.query.get(entry_params['player_id'])
                # TODO: ensure enqueue battle request requirements:
                '''
                i. Battles must happen in the order that they were submitted
                ii. Each battle should only be executed once
                iii. No battles should be missed
                iv. Battles should be processed as soon as possible, but there is no hard requirement
                '''
                job = battle_queue.enqueue(BattleEngine.initiate_battle, initiating_player.id, targetted_player.id)
                # TODO: logging service, what to log about the job?
                print(job)
                return '', 204
            else:
                return jsonify(battle_validator.errors), 422
        except Exception as err:
            # TODO: logging service
            print(err)
            return 'Internal Server Error', 500
