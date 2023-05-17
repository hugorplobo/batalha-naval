import pytest
from batalha_naval.model.board import Board, InvalidPlacePosition
from batalha_naval.model.ship import Large


def test_board_should_have_size_10():
    board = Board()
    assert len(board.positions) == 10
    assert len(board.positions[0]) == 10


def test_ship_with_negative_pos_should_raise():
    board = Board()
    ship = Large((-1, 0), (3, 0))

    with pytest.raises(InvalidPlacePosition):
        board.place_ship(ship)


def test_ship_with_exceeding_pos_should_raise():
    board = Board()
    ship = Large((9, 0), (13, 0))

    with pytest.raises(InvalidPlacePosition):
        board.place_ship(ship)


def test_ship_with_valid_pos_should_place_ship_on_board():
    board = Board()
    ship = Large((1, 1), (5, 1))

    board.place_ship(ship)

    for i in range(1, 5):
        assert board.positions[i][1] == "+"


def test_ship_overlapping_should_raise():
    board = Board()
    ship1 = Large((1, 1), (5, 1))
    ship2 = Large((2, 0), (2, 4))

    board.place_ship(ship1)

    with pytest.raises(InvalidPlacePosition):
        board.place_ship(ship2)


def test_receive_shot_on_empty_should_set_O_char_and_return_false():
    board = Board()
    hit = board.receive_shot((1, 1))

    assert not hit
    assert board.positions[1][1] == "O"


def test_receive_shot_on_ship_should_set_X_char_and_return_true():
    board = Board()
    ship = Large((1, 1), (5, 1))

    board.place_ship(ship)
    hit = board.receive_shot((2, 1))

    assert hit
    assert board.positions[2][1] == "X"
