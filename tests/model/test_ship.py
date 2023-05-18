from batalha_naval.model.ship import *
import pytest


def test_submarine_with_valid_pos_should_pass():
    Submarine((3, 3), (3, 3))


def test_submarine_with_invalid_pos_should_raise():
    with pytest.raises(InvalidShipPosition):
        Submarine((1, 1), (2, 3))


def test_small_with_valid_pos_should_pass():
    Small((1, 1), (2, 1))


def test_small_with_invalid_pos_should_raise():
    with pytest.raises(InvalidShipPosition):
        Small((1, 1), (4, 1))


def test_medium_with_valid_pos_should_pass():
    Medium((1, 1), (3, 1))


def test_medium_with_invalid_pos_should_raise():
    with pytest.raises(InvalidShipPosition):
        Medium((1, 1), (5, 1))


def test_large_with_valid_pos_should_pass():
    Large((1, 1), (4, 1))


def test_large_with_invalid_pos_should_raise():
    with pytest.raises(InvalidShipPosition):
        Large((1, 1), (6, 1))
