from app.models import Player

class PlayerValidator:
    def __init__(self, args):
        self.args = args
        self.errors = []

    def validate(self):
        # TODO: gold must be less than 1bn (currently always 0)

        try:
            if not 'name' in self.args:
                self.errors.append('name is required')
                return

            name = self.args['name']

            if type(name) != str:
                self.errors.append('name must be a string')
                return

            if len(name) > 20:
                self.errors.append('name must be 20 chars or less')
                return

            if Player.query.filter_by(name=name).all():
                self.errors.append('name must be unique')
                return

        except Exception as err:
            # TODO: logging service
            print(err)
            self.errors.append('unknown error')

    def is_valid(self):
        return not self.errors
