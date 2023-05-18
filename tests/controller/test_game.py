from batalha_naval.controller.game import GameController
from batalha_naval.model.board import InvalidPosition
import pytest


def test_play_turn_with_valid_pos_should_set_char_on_player2():
    game = GameController("player1", "player2")

    game.play_turn((3, 3))
    board = game.player_2.board

    assert board.at((3, 3)) == "O"


def test_play_turn_with_invalid_pos_should_raise():
    game = GameController("player1", "player2")

    with pytest.raises(InvalidPosition):
        game.play_turn((-1, 3))
