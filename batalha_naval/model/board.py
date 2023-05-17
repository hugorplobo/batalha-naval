from batalha_naval.model.ship import Ship
from typing import Tuple


class InvalidPlacePosition(Exception):
    pass


class Board:
    def __init__(self) -> None:
        self.size = 10
        self.positions = [[" " for _ in range(self.size)] for _ in range(self.size)]

    def place_ship(self, ship: Ship) -> None:
        if not self.__is_valid_pos(ship) or not self.__is_place_empty(ship):
            raise InvalidPlacePosition()

        for x in range(ship.init_pos[0], ship.end_pos[0] + 1):
            for y in range(ship.init_pos[1], ship.end_pos[1] + 1):
                self.positions[x][y] = "+"

    def receive_shot(self, pos: Tuple[int, int]) -> bool:
        if self.positions[pos[0]][pos[1]] == " ":
            self.positions[pos[0]][pos[1]] = "O"
            return False
        else:
            self.positions[pos[0]][pos[1]] = "X"
            return True

    def __is_valid_pos(self, ship: Ship) -> bool:
        is_negative_x = ship.init_pos[0] < 0 or ship.end_pos[0] < 0
        is_negative_y = ship.init_pos[1] < 0 or ship.end_pos[1] < 0
        is_exceeding_x = ship.init_pos[0] >= self.size or ship.end_pos[0] >= self.size
        is_exceeding_y = ship.init_pos[1] >= self.size or ship.end_pos[1] >= self.size

        return (
            not is_negative_x
            and not is_negative_y
            and not is_exceeding_x
            and not is_exceeding_y
        )

    def __is_place_empty(self, ship: Ship) -> bool:
        for x in range(ship.init_pos[0], ship.end_pos[0] + 1):
            for y in range(ship.init_pos[1], ship.end_pos[1] + 1):
                if self.positions[x][y] == "+":
                    return False

        return True
