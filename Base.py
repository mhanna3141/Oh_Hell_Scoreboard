import ttkbootstrap as ttk


# create a window
win = ttk.Window(themename="yeti")
win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

# rename the title of the window
win.title("Mark HannaH is the coolest person EVER!")

# main loop
win.mainloop()