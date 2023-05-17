from batalha_naval.model.player import Player
from batalha_naval.model.ship import Submarine


def test_receive_shot_should_decrement_remaining_in_one():
    player = Player("Hugo")
    ship = Submarine((1, 1), (1, 1))

    player.place_ship(ship)
    player.receive_shot((1, 1))

    assert player.remaining_cells == 13
