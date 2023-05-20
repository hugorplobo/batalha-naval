from batalha_naval.model.player import Player
from batalha_naval.model.ship import Submarine
from batalha_naval.model.board import InvalidPosition
import pytest


def test_receive_shot_on_ship_should_decrement_remaining_in_one():
    player = Player("Hugo")
    ship = Submarine((1, 1), (1, 1))

    player.place_ship(ship)
    player.receive_shot((1, 1))
    assert player.remaining_cells == 14


def test_receive_shot_miss_should_not_update_remaining():
    player = Player("Hugo")
    player.receive_shot((1, 1))
    assert player.remaining_cells == 15


def test_receive_shot_with_valid_pos_should_set_O_char():
    player = Player("Hugo")
    player.receive_shot((1, 1))
    assert player.board.at((1, 1)) == "O"


def test_receive_shot_with_invalid_pos_should_raise():
    player = Player("Hugo")

    with pytest.raises(InvalidPosition):
        player.receive_shot((15, 15))


def test_place_invalid_ship_should_raise():
    player = Player("Hugo")

    with pytest.raises(InvalidPosition):
        player.place_ship(Submarine((-1, -1), (-1, -1)))


def test_place_valid_ship_should_set_plus_char():
    player = Player("Hugo")
    player.place_ship(Submarine((3, 3), (3, 3)))
    assert player.board.at((3, 3)) == "+"


def test_has_lost_after_15_shots_should_return_true():
    player = Player("Hugo")

    for i in range(8):
        player.place_ship(Submarine((i, 0), (i, 0)))
        player.receive_shot((i, 0))

    for i in range(7):
        player.place_ship(Submarine((0, i), (0, i)))
        player.receive_shot((0, i))

    assert player.has_lost()


# has not lost after 15 shots or lost before 15 shot should raise a flag ?
def test_has_lost_before_15_shots_should_return_false():
    player = Player("Leo")

    for i in range(7):
        player.place_ship(Submarine((i, 0), (i, 0)))
        player.receive_shot((i, 0))

    for i in range(6):
        player.place_ship(Submarine((0, i), (0, i)))
        player.receive_shot((0, i))

    assert player.has_lost() is False
