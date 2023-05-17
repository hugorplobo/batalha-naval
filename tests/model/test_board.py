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
        assert board.positions[i][1] == "X"


def test_ship_overlapping_should_raise():
    board = Board()
    ship1 = Large((1, 1), (5, 1))
    ship2 = Large((2, 0), (2, 4))

    board.place_ship(ship1)

    with pytest.raises(InvalidPlacePosition):
        board.place_ship(ship2)