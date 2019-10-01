from app.models import Player

class BattleValidator:
    def __init__(self, args, initiating_player_id):
        self.args = args
        self.initiating_player_id = initiating_player_id
        self.errors = []

    def validate(self):
        try:
            if not 'player_id' in self.args:
                self.errors.append('player_id is required')
                return

            player_id = self.args['player_id']

            if type(player_id) != int:
                self.errors.append('player_id must be an int')
                return

            if player_id == self.initiating_player_id:
                self.errors.append('player cannot battle themselves')
                return

            if not Player.query.get(player_id):
                self.errors.append('targetted player not found')
                return

        except Exception as err:
            # TODO: logging service
            print(err)
            self.errors.append('unknown error')

    def is_valid(self):
        return not self.errors
