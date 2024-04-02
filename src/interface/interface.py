import tkinter as tk
from game.tile import WHITE, BLACK, EMPTY
from game.board import Board
from PIL import ImageTk, Image

class MainWindow(tk.Tk):
    
    def __init__(self, size):
        super().__init__("Reversi")
        self.size = size
        self.player_playing = WHITE
        self.board = Board(size)
        self.player_label = tk.Label(self, text="White to play")
        self.player_label.grid(column=0, columnspan=size, row=0)
        self.empty_image = ImageTk.PhotoImage(Image.open("assets/empty.png"))
        self.white_image = ImageTk.PhotoImage(Image.open("assets/white.png"))
        self.black_image = ImageTk.PhotoImage(Image.open("assets/black.png"))
        self.tiles: list[list[tk.Button]] = []

        for i in range(size):
            self.tiles.append([])
            for j in range(size):
                self.tiles[i].append(tk.Button(
                    self,
                    image=self.empty_image,
                    command=lambda i=i, j=j: self.play(i,j),
                    width=90,
                    height=90
                    ))
                self.tiles[i][j].grid(column=j, row=i+1)                
            
        self.display_tiles()
        self.able_disable_buttons()
    
    def play(self, x, y):
        self.board.put_disk(x, y, self.player_playing)
        self.change_player()
        self.able_disable_buttons()
        self.display_tiles()
    
    def change_player(self):
        if not self.board.is_game_over() and (self.board.can_play(WHITE) or self.board.can_play(BLACK)):
            if self.player_playing == WHITE:
                self.player_playing = BLACK
                self.player_label.config(text="BLACK to play")
            else:
                self.player_playing = WHITE
                self.player_label.config(text="WHITE to play")

            if not self.board.can_play(self.player_playing):
                self.change_player()
        else:
                white_count = self.board.count(WHITE)
                black_count = self.board.count(BLACK)
                if white_count > black_count:
                    self.player_label.config(text=f"WHITE wins with {white_count} disks")
                elif black_count > white_count:
                    self.player_label.config(text=f"BLACK wins with {black_count} disks")
                else:
                    self.player_label.config("It's a draw!")
    
    def display_tiles(self):
        tiles = self.board.tiles
        image_dict = {EMPTY: self.empty_image, WHITE: self.white_image, BLACK: self.black_image}
        for i in range(self.size):
            for j in range(self.size):
                color = tiles[i][j].get_color()
                self.tiles[i][j].config(image=image_dict[color])

    def able_disable_buttons(self):
        matrix = self.board.verify_playable_tiles(self.player_playing)
        for i in range(self.size):
            for j in range(self.size):
                if matrix[i][j]:
                    self.tiles[i][j].config(state='normal')
                else:
                    self.tiles[i][j].config(state='disabled')