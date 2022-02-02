import ttkbootstrap as ttk
import tkinter as tk
from tkinter import simpledialog


# runs after clicked add player button
def butt_cmd_addPlayer(event=None):

    # get the new player's name
    playerName = simpledialog.askstring(title="title", prompt="Enter Player's Name: ", parent=win)

    # user didn't give a name
    if playerName is None:
        return

    # add new player to end of the player list
    listbox_players.insert("end", playerName)


# removes selected player
def butt_cmd_removePlayer(event=None):
    listbox_players.delete(listbox_players.curselection())


# create a window
win = ttk.Window(themename="yeti")
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

# rename the title of the window
win.title("Mark HannaH is the coolest person EVER!")

# the dimentions of the window
width = 700
height = 500

# determines the position of where the window appears
xOffSet = 50
yOffSet = 50

# change the dimensions of window and the initial location
win.geometry(str(width) + "x" + str(height) + "+" + str(xOffSet) + "+" + str(yOffSet))

# main frame
frame_main = ttk.Frame(master=win)
frame_main.grid(row=0, column=0)

# list of players
listbox_players = tk.Listbox(master=frame_main, font=("Constantia", 35))
listbox_players.grid(row=1, column=0)

# button to add player to the game
button_addPlayer = ttk.Button(master=frame_main, text="Add Player", command=butt_cmd_addPlayer)
button_addPlayer.grid(row=0, column=0)

# full screen
win.attributes('-fullscreen', True)

# button binds
win.bind("p", butt_cmd_addPlayer)
win.bind("a", butt_cmd_addPlayer)
win.bind("<BackSpace>", butt_cmd_removePlayer)

# main loop
win.mainloop()