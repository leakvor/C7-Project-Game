#============================ IMPORTS ============================
import tkinter as tk
from tkinter import *
from typing import Self
# from PIL import ImageTk, Image
import winsound
from random import randrange

# ---------------------------------------------------------------------------
#=> CONSTANT
# ---------------------------------------------------------------------------
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title('Group 13 - Game Pro')
canvas = tk.Canvas(root)

# ---------------------------------------------------------------------------
#=> VARIABLES
# ---------------------------------------------------------------------------
game_play=tk.PhotoImage(file='image/bg.jpg')
game_start=tk.PhotoImage(file='image/start-play.png')
game_win=tk.PhotoImage(file='image/Gameover.jpg')
game_over=tk.PhotoImage(file='image/Game.jpg')
game_introduction=tk.PhotoImage(file='image/introduction')
game_story=tk.PhotoImage(file='image/story.jpg')

all_levels=tk.PhotoImage(file='image/all-level.png')
help=tk.PhotoImage(file='image/help.png')
level1_list=tk.PhotoImage(file='image/level1-list.jpg')
level2_list=tk.PhotoImage(file='image/level2-list.jpg')
level3_list=tk.PhotoImage(file='image/level3-list.jpg')
level1=tk.PhotoImage(file='image/level1.jpg')
level2=tk.PhotoImage(file='image/level2.jpg')
level3=tk.PhotoImage(file='image/level3.jpg')

hero=tk.PhotoImage(file='image/Ranger.png')
queen=tk.PhotoImage(file='image/queen1.png')
coin=tk.PhotoImage(file='image/coin.png')
water=tk.PhotoImage(file='image/water.png')
boom=tk.PhotoImage(file='image/boom.png')
yellow_stone=tk.PhotoImage(file='image/yellow-stone.png')
black_stone=tk.PhotoImage(file='image/black-stone.png')
white_stone=tk.PhotoImage(file='image/white-stone.png')
long_wall=tk.PhotoImage(file='image/long-wall.jpg')
small_wall=tk.PhotoImage(file='image/short-wall.jpg')
monster=tk.PhotoImage(file='image/monster.png')



