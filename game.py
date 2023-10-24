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
root.title('Advanture OF Prince')
canvas = tk.Canvas(root)

# ---------------------------------------------------------------------------
#=> VARIABLES
# ---------------------------------------------------------------------------
game_start=tk.PhotoImage(file='image/bg.png')
game_over=tk.PhotoImage(file='image/Gameover.png')
game_win=tk.PhotoImage(file='image/Gamewin.png')
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

hero=tk.PhotoImage(file='image/Ranger.png')
flower=tk.PhotoImage(file='image/flower.png')
queen=tk.PhotoImage(file='image/queen.png')
coin=tk.PhotoImage(file='image/coin.png')
water=tk.PhotoImage(file='image/water.png')
boom=tk.PhotoImage(file='image/boom.png')
door=tk.PhotoImage(file='image/door.png')
long_wall=tk.PhotoImage(file='image/long-wall.png')
monster=tk.PhotoImage(file='image/monster.png')
fire=tk.PhotoImage(file='image/fire.png')
all_level_bg= PhotoImage(file="image/all-levels.png")
button_exists= PhotoImage(file="image/button_exist.png")
button_level=tk.PhotoImage(file='image/button_level.png')
play_again=tk.PhotoImage(file='image/playAgain.png')
retry=tk.PhotoImage(file='image/Retry.png')
back_to_game=tk.PhotoImage(file='image/back.png')

score_id = canvas.create_text(600, 15, text="Score:", font=("bold", 15))
#=========================== ALL LEVELS =======================
def alllevels():
    canvas.delete("all")
    canvas.create_image(1,0, image = all_level_bg, anchor = "nw")
    # ______________________________LEVEL1_____________________________________
    canvas.create_image(200,250, image = level1_list, anchor = "nw", tags="level1-")
    # ______________________________LEVEL2_______________________________________
    canvas.create_image(565,250, image = level2_list, anchor = "nw", tags="level2-")
    # ______________________________LEVEL3_______________________________________
    canvas.create_image(950,250, image = level3_list, anchor = "nw", tags="level3-")
    canvas.create_image(20,20, image =button_exist, anchor = "nw",tags="backhome")
#===========================LEVEL1 =======================
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
    
# ==============> Indroduction <==================
def introdution(event):
    canvas.delete("all")
    canvas.create_image(1, 0, image=game_introduction, anchor = 'nw')
    canvas.create_image(20,20, image =button_exist, anchor = "nw",tags="backhome")
# ---------------------------------------------------------------------------


# ==============> Story <==================
def story(event):
    canvas.delete("all")
    canvas.create_image(1, 0, image=game_story, anchor = 'nw')
    canvas.create_image(20,20, image =button_exist, anchor = "nw",tags="backhome")
# ---------------------------------------------------------------------------
def back(event):
    canvas.delete("all")
    home()
#=> CREATE GAME SHOW
# ---------------------------------------------------------------------------
def home():
    canvas.create_image(1, 0, image=game_start, anchor='nw')
    canvas.create_image(500,500,image=story_list, tags="story")
    canvas.create_image(700,500, image=button_play, tags="startgame")
    canvas.create_image(900,500,image=button_help, tags="help")
    # winsound.PlaySound("sound/open.mp3",winsound.SND_FILENAME | winsound.SND_ASYNC)


####### START GAME ######3
def startGame(event):
    canvas.delete('all')
    showSlid1()
    # winsound .PlaySound("Audioes\space-war.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def showSlid1():
    canvas.create_image(1,0,image=slide1,anchor='nw')
    canvas.after(1000,showSlid2)
def showSlid2():
    canvas.create_image(1,0,image=slide2, anchor='nw')
    canvas.after(1000,showSlid3)
def showSlid3():
    canvas.create_image(1,0,image=slide3, anchor='nw')
    canvas.create_text(700,420,text="Loading...",font=('sansarif',28,'bold'),fill='white')
    canvas.after(2000,alllevels)

#=> ALLOW WINDOWS KEYS AND TAGES BIND
# ---------------------------------------------------------------------------
# root.bind("<w>", movePlayerUp)
# root.bind("<s>", movePlayerDown)
# root.bind("<Button-3>", createBullet)
canvas.tag_bind("help","<Button-1>",introdution )
canvas.tag_bind("story","<Button-1>", story)
canvas.tag_bind("backhome","<Button-1>", back)
canvas.tag_bind("button_level","<Button-1>", alllevels)
canvas.tag_bind("startgame","<Button-1>", startGame )

#=> MAIN ROOT
# ---------------------------------------------------------------------------
canvas.pack(expand=True, fill='both')
home()
root.mainloop()


