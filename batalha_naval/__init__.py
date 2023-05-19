from batalha_naval.view.game import GameView
import sys


def start():
    try:
        view = GameView()
        view.show_placing_board(1)
        view.show_placing_board(2)

        while True:
            view.show_boards()
            view.ask_turn()
            if view.game.player_1.has_lost():
                view.show_end_game(view.game.player_2)
                break
            elif view.game.player_2.has_lost():
                view.show_end_game(view.game.player_1)
                break
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    start()
