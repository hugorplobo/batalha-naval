from batalha_naval.view.game import GameView


def start():
    view = GameView()
    view.show_placing_board(1)
    view.show_placing_board(2)

    while True:
        view.show_boards()
        view.ask_turn()

    input()
    


if __name__ == "__main__":
    start()
