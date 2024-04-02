from .board import Board, BLACK, WHITE

def main(size):
    board = Board(size)
    color = WHITE
    for _ in range(4, size**2):
        print(board)
        if board.can_play(color):
            playable_matrix = board.verify_playable_tiles(color)
            x, y = None, None
            while not board.is_on_board(x, y) or not playable_matrix[x][y]:
                if not x is None:
                    print("You can't play here!")
                x, y = input(f"Player {color} to chose a position to play (Seperate the two coordinates by a white space).").split(' ')
                x = int(x)
                y = int(y)
            board.put_disk(x, y, color)
        else:
            print(f"Player {color} can't play")
        print(f"Player {color} has now {board.count(color)} disks.")
        color = {WHITE : BLACK, BLACK : WHITE}[color]