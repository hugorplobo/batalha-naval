import pytest
from batalha_naval.model.board import Board, InvalidPosition
from batalha_naval.model.ship import Large


def test_get_valid_position_should_return_empty_char():
    board = Board()
    assert board.at((0, 0)) == " "


def test_get_invalid_position_should_raise():
    board = Board()

    with pytest.raises(InvalidPosition):
        board.at((15, 15))


def test_ship_with_negative_pos_should_raise():
    board = Board()
    ship = Large((-1, 0), (2, 0))

    with pytest.raises(InvalidPosition):
        board.place_ship(ship)


def test_ship_with_exceeding_pos_should_raise():
    board = Board()
    ship = Large((9, 0), (12, 0))

    with pytest.raises(InvalidPosition):
        board.place_ship(ship)


def test_ship_with_valid_pos_should_place_ship_on_board():
    board = Board()
    ship = Large((1, 1), (4, 1))

    board.place_ship(ship)

    for i in range(1, 5):
        assert board.at((i, 1)) == "+"


def test_ship_overlapping_should_raise():
    board = Board()
    ship1 = Large((1, 1), (4, 1))
    ship2 = Large((2, 0), (2, 3))

    board.place_ship(ship1)

    with pytest.raises(InvalidPosition):
        board.place_ship(ship2)


def test_receive_shot_on_empty_should_set_O_char_and_return_false():
    board = Board()
    hit = board.receive_shot((1, 1))

    assert not hit
    assert board.at((1, 1)) == "O"


def test_receive_shot_on_ship_should_set_X_char_and_return_true():
    board = Board()
    ship = Large((1, 1), (4, 1))

    board.place_ship(ship)
    hit = board.receive_shot((2, 1))

    assert hit
    assert board.at((2, 1)) == "X"


def test_teste():
    board = Board()
    ship = Large((1, 1), (4, 1))

    board.place_ship(ship)

    board.receive_shot((1, 1))
    board.receive_shot((2, 1))
    board.receive_shot((3, 1))
    board.receive_shot((4, 1))


test_teste()
