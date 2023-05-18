from batalha_naval.controller.game import GameController
from batalha_naval.model.player import Player
from batalha_naval.model.board import Board, InvalidPosition
from batalha_naval.model.ship import (
    Submarine,
    Small,
    Medium,
    Large,
    InvalidShipPosition,
)
from batalha_naval.view.ascii import ship
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
import os
from sys import platform


class GameView:
    def __init__(self) -> None:
        self.show_logo_screen()
        self.__game = GameController(self.__name1, self.__name2)
        self.__clear()

    def show_logo_screen(self) -> None:
        console = Console()
        self.__clear()
        console.rule("[blue bold]BATALHA NAVAL[/blue bold]")
        console.print(f"[cyan bold]{ship}[/cyan bold]", justify="center")
        console.print("\n\n\n\n\n")
        self.__name1 = console.input(
            "Digite o nome do [underline]Jogador 1[/underline]: "
        )
        self.__name2 = console.input(
            "Digite o nome do [underline]Jogador 2[/underline]: "
        )

    def show_boards(self) -> None:
        self.__clear()
        Console().print(
            Panel(
                Columns(
                    [self.__show_board(1), self.__show_board(2)],
                    expand=True,
                    equal=True,
                    align="center",
                )
            )
        )

    def show_placing_board(self, player_num: int) -> None:
        player = self.__parse_player(player_num)

        def show_board():
            console = Console()
            self.__clear()
            console.rule(
                f"[bold white]Posicionando navios do(a): [blue]{player.name}[/blue][/bold white]"
            )
            console.print(f"\n\n\n{self.__parse_board(player.board)}", justify="center")

        show_board()

        while True:
            try:
                y, x = map(int, input("Digite a posição do seu submarino: ").split(","))
                player.place_ship(Submarine((x, y), (x, y)))
                show_board()
                break
            except InvalidShipPosition:
                show_board()
                print("Posição inválida para um submarino!")
            except InvalidPosition:
                show_board()
                print("Essa posição não existe no tabuleiro!")

        # while True:
        #     try:
        #         y1, x1 = map(int, input("Digite a posição inicial do seu navio pequeno (tamanho 2): ").split(","))
        #         y2, x2 = map(int, input("Digite a posição final do seu navio pequeno (tamanho 2): ").split(","))
        #         player.place_ship(Small((x1, y1), (x2, y2)))
        #         show_board()
        #         break
        #     except InvalidShipPosition:
        #         show_board()
        #         print("Posição inválida para um navio pequeno!")
        #     except InvalidPosition:
        #         show_board()
        #         print("Essa posição não existe no tabuleiro!")

        # while True:
        #     try:
        #         y1, x1 = map(int, input("Digite a posição inicial do seu navio pequeno (tamanho 2): ").split(","))
        #         y2, x2 = map(int, input("Digite a posição final do seu navio pequeno (tamanho 2): ").split(","))
        #         player.place_ship(Small((x1, y1), (x2, y2)))
        #         show_board()
        #         break
        #     except InvalidShipPosition:
        #         show_board()
        #         print("Posição inválida para um navio pequeno!")
        #     except InvalidPosition:
        #         show_board()
        #         print("Essa posição não existe no tabuleiro!")

        # while True:
        #     try:
        #         y1, x1 = map(int, input("Digite a posição inicial do seu navio médio (tamanho 3): ").split(","))
        #         y2, x2 = map(int, input("Digite a posição final do seu navio médio (tamanho 3): ").split(","))
        #         player.place_ship(Medium((x1, y1), (x2, y2)))
        #         show_board()
        #         break
        #     except InvalidShipPosition:
        #         show_board()
        #         print("Posição inválida para um navio médio!")
        #     except InvalidPosition:
        #         show_board()
        #         print("Essa posição não existe no tabuleiro!")

        # while True:
        #     try:
        #         y1, x1 = map(int, input("Digite a posição inicial do seu navio médio (tamanho 3): ").split(","))
        #         y2, x2 = map(int, input("Digite a posição final do seu navio médio (tamanho 3): ").split(","))
        #         player.place_ship(Medium((x1, y1), (x2, y2)))
        #         show_board()
        #         break
        #     except InvalidShipPosition:
        #         show_board()
        #         print("Posição inválida para um navio médio!")
        #     except InvalidPosition:
        #         show_board()
        #         print("Essa posição não existe no tabuleiro!")

        # while True:
        #     try:
        #         y1, x1 = map(int, input("Digite a posição inicial do seu navio grande (tamanho 4): ").split(","))
        #         y2, x2 = map(int, input("Digite a posição final do seu navio grande (tamanho 4): ").split(","))
        #         player.place_ship(Large((x1, y1), (x2, y2)))
        #         show_board()
        #         break
        #     except InvalidShipPosition:
        #         show_board()
        #         print("Posição inválida para um navio grande!")
        #     except InvalidPosition:
        #         show_board()
        #         print("Essa posição não existe no tabuleiro!")

        input("Aperte ENTER para continuar... ")

    def ask_turn(self) -> None:
        player = self.__game.current_player
        console = Console()

        console.print(f"[bold yellow]Vez do(a) {player.name}![/bold yellow]")

        while True:
            y, x = map(int, input("Digite a posição do seu tiro: ").split(","))

            try:
                self.__game.play_turn((x, y))
                break
            except InvalidPosition:
                print("Essa posição não é válida!")

    def __show_board(self, player_num: int) -> str:
        player = self.__parse_player(player_num)
        out = f"[bold]{player.name}[/bold] | {player.remaining_cells} ❤️\n\n"
        out += self.__parse_board(player.board)
        return out

    def __parse_player(self, player: int) -> Player:
        if player == 1:
            return self.__game.player_1
        return self.__game.player_2

    def __parse_board(self, board: Board) -> str:
        out = ""
        for row in range(10):
            for col in range(10):
                cell = board.at((row, col))
                out += f" {self.__parse_cell(cell)} "
            out += "\n\n"
        return out

    def __parse_cell(self, cell: str) -> str:
        if cell == "O":
            return "⬛"
        elif cell == "X":
            return "🟥"
        elif cell == "+":
            return "🟩"
        elif cell == "*":
            return "❌"
        else:
            return "🟦"

    def __clear(self) -> None:
        if platform == "win32":
            os.system("cls")
        else:
            os.system("clear")
