"""The tiles are parts of the board, where players put disks."""

# The tile can have three color: white, black, empty.
EMPTY = 0 # an empty tile don't have any disk on it
WHITE = 1 # A white tile has a white disk on it.
BLACK = 2 # A black tile hase a black disk on it.

class Tile:

    def __init__(self, color = EMPTY) -> None:
        self.__color = color
    
    def set_color(self, color) -> None:
        """Set the color of the tile."""
        self.__color = color
    
    def get_color(self) -> int:
        """Return the color of the tile."""
        return self.__color

    def turn_color(self) -> None:
        """Change the color of the tile."""
        if self.__color:
            self.__color = {WHITE : BLACK, BLACK : WHITE}[self.__color]