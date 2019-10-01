import tests.setup
from app.controllers import PlayerController
import pytest
from app.models import Player
from app.validators import PlayerValidator

class StubRequest:
    def __init__(self):
        self.json = {}

def test_create_player():
    # TODO: this is super ghetto
    Player.query.delete()
    
    valid_request = StubRequest()
    valid_request.json['name'] = 'Alice'
    player_controller = PlayerController(valid_request)

    assert player_controller.create() == ('', 201)
    assert Player.query.get(1).name == 'Alice'
