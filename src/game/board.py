"""The board is a set of sizexsize tiles on which the players put disks."""

from .tile import WHITE, EMPTY, BLACK, Tile

class Board:

    def __init__(self, size) -> None:
        self.tiles = [[Tile() for _ in range(size)] for _ in range(size)]
        self.tiles[size//2-1][size//2].set_color(WHITE)
        self.tiles[size//2][size//2-1].set_color(WHITE)
        self.tiles[size//2-1][size//2-1].set_color(BLACK)
        self.tiles[size//2][size//2].set_color(BLACK)
        self.size = size
    
    def __str__(self) -> str:
        return "\n".join([str([self.tiles[i][j].get_color() for j in range(self.size)]) for i in range(self.size)])
    
    def count(self, color):
        return sum(sum(1 for j in range(self.size) if self.tiles[i][j].get_color() == color) for i in range(self.size))

    def is_on_board(self, x, y):
        return (not x is None) and (not y is None) and ( 0 < x < self.size and 0 < y < self.size)

    def is_game_over(self):
        return self.count(EMPTY) == 0
    
    def __turn_tiles_matrix(self, x: int, y: int, color: int) -> list[list[bool]]:
        matrix = [[False for _ in range(self.size)] for _ in range(self.size)]
        if not self.tiles[x][y].get_color():
            translations = [(1,1), (1,0), (1,-1), (0,-1), (0,1), (-1,1), (-1,0), (-1,-1)]
            for dx, dy in translations: # loop over the directions.
                i = 1 # the distance to the position (x,y)
                # Increment i to scan the direction, looking for another disk of the same color
                while self.is_on_board(x + dx*i, y + dy*i) and self.tiles[x + dx*i][y + dy*i].get_color() not in [EMPTY, color] :
                    i += 1
                # If i > 1, we found one (if the stop condition was not the exit of the board but the finding of a disk of the same color.)
                # In this case, we take every disk on the range and set the return matrix to true.
                if i > 1 and self.is_on_board(x + dx*i, y + dy*i) and self.tiles[x + dx*i][y + dy*i].get_color() == color:

                    for k in range(1, i):
                        matrix[x + dx*k][y + dy*k] = True
        return matrix

    def verify_playable_tiles(self, color: int):
        matrix = [[False for _ in range(self.size)] for _ in range(self.size)]
        for x in range(self.size):
            for y in range(self.size):
                turn_tiles_matrix = self.__turn_tiles_matrix(x, y, color)
                if any(any(turn_tiles_matrix[i][j] for j in range(self.size)) for i in range(self.size)):
                    matrix[x][y] = True
        return matrix

    def put_disk(self, x: int, y: int, color: int):
        turn_tiles_matrix = self.__turn_tiles_matrix(x, y, color)
        for i in range(self.size):
            for j in range(self.size):
                if turn_tiles_matrix[i][j]:
                    self.tiles[i][j].turn_color()
        self.tiles[x][y].set_color(color)

    def can_play(self, color: int) -> bool:
        matrix = self.verify_playable_tiles(color)
        return any(any(matrix[i][j] for j in range(self.size)) for i in range(self.size))

if __name__ == '__main__':
    SIZE = 8
    board = Board(SIZE)
    board.put_disk(2, 3, WHITE)
    board.put_disk(4, 2, WHITE)
    print(board)

