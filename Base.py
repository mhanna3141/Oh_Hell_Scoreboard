import ttkbootstrap as ttk
import tkinter as tk
from tkinter import simpledialog, messagebox
import re


# a class for what need to be in each tab
class gameRounds:
    def __init__(self, frame_gameRoundX):

        # add the frame, put it somewhere
        self.frame_gameRoundX = frame_gameRoundX
        self.frame_gameRoundX.grid(row=0, column=0)

        # add frame to notebook
        notebook_gameRounds.add(child=self.frame_gameRoundX, text=str(currentGameRound))


# adds a tab for a new round
def addRoundTab(event=None):
    global currentGameRound

    # next round
    currentGameRound += 1

    # create new tab in the game rounds notebook
    frame_newRoundTab = ttk.Frame(master=frame_main)
    gameRounds(frame_newRoundTab)


# runs after clicked add player button
def butt_cmd_addPlayer(event=None):

    # get the new player's name
    playerName = simpledialog.askstring(title="Add Player", prompt="Enter Player's Name: ", parent=win)

    # user changed their mind
    if playerName is None:
        return

    # user didn't give a name
    elif playerName == "":
        messagebox.showerror("Nameless Player", "People have names you animal! (You didn't give a name).")
        return

    # something other than numbers 0 through 9, and letters
    elif re.findall("[^0-9a-zA-Z ]", playerName):
        messagebox.showerror("Name Error", "You can only use numbers, spaces, and letter characters!")
        return

    # make sure the new name is unique
    for player in playerScores:
        if playerName.lower() == player.lower():
            messagebox.showerror("Name Exists", "That name already exists, try adding their last name or initials too.")
            return

    # add new player to end of the player list
    listbox_players.insert("end", playerName + " (0)")
    playerScores[playerName] = 0


# removes selected player
def cmd_removePlayer(event=None):
    print(listbox_players.get(listbox_players.curselection()))
    del playerScores[listbox_players.curselection()]
    listbox_players.delete(listbox_players.curselection())


# starts the game
def cmd_startGame(event=None):

    # there are 0 or less than 0 players
    if listbox_players.size() == 0:

        messagebox.showerror("Player Count Error", "You have 0 friends, get some friends or get lost! \n"
                                                   "(Press the 'Add Player' button to add people in.)")
        return

    # playing with one person
    elif listbox_players.size() == 1:

        messagebox.showerror("Player Count Error", "You can't play by yourself that's just sad. Go outside and make some friends. \n"
                                                   "(You need more than one person to play, add more people)")
        return

    # double check if user wants to start game
    startGameConformation = messagebox.askyesno("Start Game", "Are you sure you want to start the game?\n There are " + str(listbox_players.size()) + " players.")

    # don't start game
    if startGameConformation == "no":
        return

    # unbind the add, and remove player hot keys
    win.unbind("p")
    win.unbind("a")
    win.unbind("<BackSpace>")

    # hide the add player and start game buttons
    button_addPlayer.grid_forget()
    button_startGame.grid_forget()

    # start a new round
    addRoundTab()


# create a window
win = ttk.Window(themename="yeti")
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

# rename the title of the window
win.title("Mark HannaH is the coolest person EVER!")

# the dimensions of the window
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

# button starts game
button_startGame = ttk.Button(master=frame_main, text="Start Game", command=cmd_startGame)
button_startGame.grid(row=0, column=3)

# full screen
win.attributes('-fullscreen', True)

# button binds
win.bind("p", butt_cmd_addPlayer)
win.bind("a", butt_cmd_addPlayer)
win.bind("<BackSpace>", cmd_removePlayer)
win.bind("y", addRoundTab)

# tabs with each round of the game
notebook_gameRounds = ttk.Notebook(master=frame_main)
notebook_gameRounds.grid(row=0, column=1)

# keeps track of which round we're on
currentGameRound = 0

# a dictionary of the score of each player
playerScores = {}

# main loop
win.mainloop()