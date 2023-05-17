from typing import Tuple
from batalha_naval.model.player import Player


class Game:
    def __init__(self, name1: str, name2: str) -> None:
        self.__player1 = Player(name1)
        self.__player2 = Player(name2)
        self.__current_player = self.__player1
        self.__next_player = self.__player2

    def switch_turn(self) -> None:
        self.__player1, self.__player2 = self.__player2, self.__player1

    def play_turn(self, pos: Tuple[int, int]) -> None:
        self.__next_player.receive_shot(pos)
