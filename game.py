#============================ IMPORTS ============================
import tkinter as tk
from tkinter import *
import winsound
from random import randrange
# ---------------------------------------------------------------------------
#=> CONSTANT
# ---------------------------------------------------------------------------
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 740
root = tk.Tk()
root.geometry(str(SCREEN_WIDTH)+"x"+str(SCREEN_HEIGHT))
root.title('Advanture OF Prince')
canvas = tk.Canvas(root)

# ---------------------------------------------------------------------------
#=> VARIABLES
# ---------------------------------------------------------------------------
game_start=tk.PhotoImage(file='image/bg.png')
game_win=tk.PhotoImage(file='image/Gameover.png')
game_over=tk.PhotoImage(file='image/Gamewin.png')
game_introduction=tk.PhotoImage(file='image/introduction-of-game.png')
game_story=tk.PhotoImage(file='image/story.png')

all_levels=tk.PhotoImage(file='image/all-level.png')
button_help=tk.PhotoImage(file='image/help.png')
button_play=tk.PhotoImage(file='image/start-play.png')
button_exist=tk.PhotoImage(file='image/exist.png')
level1_list=tk.PhotoImage(file='image/level1-list.png',)
level2_list=tk.PhotoImage(file='image/level2-list.png')
level3_list=tk.PhotoImage(file='image/level3-list.png')
level1_bg=tk.PhotoImage(file='image/level1.png')
level2=tk.PhotoImage(file='image/level2.png')
level3=tk.PhotoImage(file='image/level3.png')
story_list=tk.PhotoImage(file='image/story-list.png')
slide1=tk.PhotoImage(file='image/slide1.png')
slide2=tk.PhotoImage(file='image/slide2.png')
slide3=tk.PhotoImage(file='image/slide3.png')
grass=tk.PhotoImage(file='image/grass.png')

hero=tk.PhotoImage(file='image/Ranger.png')
queen=tk.PhotoImage(file='image/queen.png')
coin=tk.PhotoImage(file='image/coin.png')
water=tk.PhotoImage(file='image/water.png')
boom=tk.PhotoImage(file='image/boom.png')
door=tk.PhotoImage(file='image/door.png')
yellow_stone=tk.PhotoImage(file='image/yellow-stone.png')
black_stone=tk.PhotoImage(file='image/black-stone.png')
white_stone=tk.PhotoImage(file='image/white-stone.png')
long_wall=tk.PhotoImage(file='image/long-wall.png')
short_wall=tk.PhotoImage(file='image/short-wall.png')
monster=tk.PhotoImage(file='image/monster.png')
fire=tk.PhotoImage(file='image/fire.png')
all_level_bg= PhotoImage(file="image/all-levels.png")




#=========================== ALL LEVELS =======================

def level1(event):
    canvas.delete("all")
    global player
    # =============   GRASS IMAGES =========

    # ==================  DOOR  ===============

    # ==================  WHITE-STONE IMAGES ===============

    # ==================  BLACK-STONE IMAGES ===============

    # ==================  YELLOW-STONE IMAGES ===============
 
    # ==================  WATER IMAGE ===============

    # ==================  MONSTER IMAGE ===============

    # ==================  LONG STONE IMAGE ===============

    # ==================  SHORT STONE IMAGE ===============

    # ==================  PLAYER ===============
    
# def level2(event):
#     canvas.create_image(1, 0, image=summer_bg, anchor="nw")
#     canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")

# def level3(event):
#     canvas.create_image(1, 0, image=level3_bg, anchor="nw")
#     canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")

# ---------------------------------------------------------------------------
#=> FUNCTIONS GAME
# ---------------------------------------------------------------------------
# ==============> SHOW STORY <==================
def story(event):
    canvas.delete("all")
    canvas.create_image(1, 0, image=game_story, anchor = 'nw')


#=> CREATE GAME SHOW
# ---------------------------------------------------------------------------
def home():
    canvas.create_image(680, 372, image=game_start)
    canvas.create_image(700,670, image=button_play, tags="startgame")
    canvas.create_image(500,665,image=all_levels, tags="level")
    canvas.create_image(900,670,image=button_help, tags="help")
    # winsound.PlaySound("sound/open.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)

#=> ALLOW WINDOWS KEYS AND TAGES BIND
# ---------------------------------------------------------------------------
# canvas.tag_bind("help","<Button-1>",introdution )
# canvas.tag_bind("story","<Button-1>", story)
# canvas.tag_bind("story","<Button-1>", level01)
# canvas.tag_bind("backhome","<Button-1>", back)
# canvas.tag_bind("startgame","<Button-1>", startGame )
# canvas.tag_bind("level1-","<Button-1>", level01 )
# canvas.tag_bind("level2-","<Button-1>", level02 )
# canvas.tag_bind("level3-","<Button-1>", level03 )


# ---------------------------------------------------------------------------
#=> MAIN ROOT
# ---------------------------------------------------------------------------
canvas.pack(expand=True, fill='both')
home()
root.mainloop()










canvas.create_rectangle(100,10,500,100)
