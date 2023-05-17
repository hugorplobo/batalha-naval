from typing import Tuple
from batalha_naval.model.board import Board
from batalha_naval.model.ship import Ship


class Player:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__remaining_cells = 14
        self.__board = Board()

    @property
    def name(self):
        return self.__name

    @property
    def remaining_cells(self):
        return self.__remaining_cells

    def place_ship(self, ship: Ship):
        self.__board.place_ship(ship)

    def receive_shot(self, pos: Tuple[int, int]):
        if self.__board.receive_shot(pos):
            self.__remaining_cells -= 1

    def has_lost(self):
        return self.__remaining_cells == 0
