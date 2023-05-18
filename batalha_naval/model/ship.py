from typing import Tuple


class InvalidShipPosition(Exception):
    pass


class Ship:
    def __init__(self, init_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> None:
        self.init_pos = init_pos
        self.end_pos = end_pos

    def __validate_positions():
        pass


class Submarine(Ship):
    def __init__(self, init_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> None:
        super().__init__(init_pos, end_pos)
        self.__validate_positions()

    def __validate_positions(self) -> None:
        if self.init_pos != self.end_pos:
            raise InvalidShipPosition()


class Small(Ship):
    def __init__(self, init_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> None:
        super().__init__(init_pos, end_pos)
        self.__validate_positions()

    def __validate_positions(self):
        is_same_x = self.init_pos[0] == self.end_pos[0]
        is_same_y = self.init_pos[1] == self.end_pos[1]
        dist_x = abs(self.end_pos[0] - self.init_pos[0])
        dist_y = abs(self.end_pos[1] - self.init_pos[1])

        if not (is_same_x or is_same_y and dist_x == 1 or dist_y == 1):
            raise InvalidShipPosition()


class Medium(Ship):
    def __init__(self, init_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> None:
        super().__init__(init_pos, end_pos)
        self.__validate_positions()

    def __validate_positions(self):
        is_same_x = self.init_pos[0] == self.end_pos[0]
        is_same_y = self.init_pos[1] == self.end_pos[1]
        dist_x = abs(self.end_pos[0] - self.init_pos[0])
        dist_y = abs(self.end_pos[1] - self.init_pos[1])

        if not (is_same_x or is_same_y and dist_x == 2 or dist_y == 2):
            raise InvalidShipPosition()


class Large(Ship):
    def __init__(self, init_pos: Tuple[int, int], end_pos: Tuple[int, int]) -> None:
        super().__init__(init_pos, end_pos)
        self.__validate_positions()

    def __validate_positions(self):
        is_same_x = self.init_pos[0] == self.end_pos[0]
        is_same_y = self.init_pos[1] == self.end_pos[1]
        dist_x = abs(self.end_pos[0] - self.init_pos[0])
        dist_y = abs(self.end_pos[1] - self.init_pos[1])

        if not (is_same_x or is_same_y and dist_x == 3 or dist_y == 3):
            raise InvalidShipPosition()
