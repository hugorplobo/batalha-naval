from batalha_naval.model.player import Player
from typing import Tuple


class GameController:
    def __init__(self, name1: str, name2: str) -> None:
        self.__player1 = Player(name1)
        self.__player2 = Player(name2)
        self.__current_player = self.__player1
        self.__next_player = self.__player2

    def play_turn(self, pos: Tuple[int, int]) -> None:
        self.__next_player.receive_shot(pos)
        self.__switch_turn()

    def __switch_turn(self) -> None:
        self.__current_player, self.__next_player = (
            self.__next_player,
            self.__current_player,
        )

    @property
    def player_1(self):
        return self.__player1

    @property
    def player_2(self):
        return self.__player2

    @property
    def current_player(self):
        return self.__current_player
