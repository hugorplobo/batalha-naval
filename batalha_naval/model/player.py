from typing import Tuple
from batalha_naval.model.board import Board
from batalha_naval.model.ship import Ship


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.board = Board()

    def place_ship(self, ship: Ship):
        self.board.place_ship(ship)

    def receive_shot(pos: Tuple[int, int]):
        pass
