from batalha_naval.model.ship import Ship
from typing import Tuple, List


class InvalidPosition(Exception):
    pass


class Board:
    def __init__(self) -> None:
        self.__size = 10
        self.__positions = [
            [" " for _ in range(self.__size)] for _ in range(self.__size)
        ]
        self.__ships = []

    def place_ship(self, ship: Ship) -> None:
        if not self.__is_valid_pos_ship(ship) or not self.__is_place_empty(ship):
            raise InvalidPosition()

        for x in range(ship.init_pos[0], ship.end_pos[0] + 1):
            for y in range(ship.init_pos[1], ship.end_pos[1] + 1):
                self.__positions[x][y] = "+"

        self.__ships.append(ship)

    def receive_shot(self, pos: Tuple[int, int]) -> bool:
        if not self.__is_valid_pos(pos):
            raise InvalidPosition()
        elif self.__positions[pos[0]][pos[1]] == " ":
            self.__positions[pos[0]][pos[1]] = "O"
            return False
        elif self.__positions[pos[0]][pos[1]] == "+":
            self.__positions[pos[0]][pos[1]] = "X"
            self.__calculate_destroyeds()
            return True

    def at(self, pos: Tuple[int, int]):
        if not self.__is_valid_pos(pos):
            raise InvalidPosition()

        return self.__positions[pos[0]][pos[1]]

    def __calculate_destroyeds(self) -> None:
        for ship in self.__ships:
            hit_cells = 0
            dist = (
                max(
                    abs(ship.init_pos[0] - ship.end_pos[0]),
                    abs(ship.init_pos[1] - ship.end_pos[1]),
                )
                + 1
            )
            for i in range(ship.init_pos[0], ship.end_pos[0] + 1):
                if self.__positions[i][ship.init_pos[1]] == "X":
                    hit_cells += 1

            if hit_cells == dist:
                for i in range(ship.init_pos[0], ship.end_pos[0] + 1):
                    if self.__positions[i][ship.init_pos[1]] == "X":
                        self.__positions[i][ship.init_pos[1]] = "*"

            hit_cells = 0
            for i in range(ship.init_pos[1], ship.end_pos[1] + 1):
                if self.__positions[ship.init_pos[0]][i] == "X":
                    hit_cells += 1

            if hit_cells == dist:
                for i in range(ship.init_pos[1], ship.end_pos[1] + 1):
                    if self.__positions[ship.init_pos[0]][i] == "X":
                        self.__positions[ship.init_pos[0]][i] = "*"

    def __is_valid_pos_ship(self, ship: Ship) -> bool:
        is_negative_x = ship.init_pos[0] < 0 or ship.end_pos[0] < 0
        is_negative_y = ship.init_pos[1] < 0 or ship.end_pos[1] < 0
        is_exceeding_x = (
            ship.init_pos[0] >= self.__size or ship.end_pos[0] >= self.__size
        )
        is_exceeding_y = (
            ship.init_pos[1] >= self.__size or ship.end_pos[1] >= self.__size
        )

        return (
            not is_negative_x
            and not is_negative_y
            and not is_exceeding_x
            and not is_exceeding_y
        )

    def __is_valid_pos(self, pos: Tuple[int, int]) -> bool:
        is_negative = pos[0] < 0 or pos[1] < 0
        is_exceeding = pos[0] > self.__size or pos[1] > self.__size

        return not is_negative and not is_exceeding

    def __is_place_empty(self, ship: Ship) -> bool:
        for x in range(ship.init_pos[0], ship.end_pos[0] + 1):
            for y in range(ship.init_pos[1], ship.end_pos[1] + 1):
                if self.__positions[x][y] == "+":
                    return False

        return True
