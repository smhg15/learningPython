import tkinter as tk



#FUNCTIONS
def hiToYou():
    yourName.configure(text='hi '+nombreEntry.get()+'!')

#WINDOWS
windows = tk.Tk() #render blank windows
windows.config(bg='#000000')

#VARIABLES.
nombreEntry = tk.StringVar()

#CONTENT
title = tk.Label(windows,text='This is my first desk App', bg='#000000', fg='#00ff00', font=('Comic Sans MS',28,'bold'))#config content: title
title.pack(padx=40, pady=10) #render content: title

yourName = tk.Label(windows,text='write your name:', fg='#ff0000', bg='#000000', font=('Comic Sans MS',14,'bold'))
yourName.pack(padx=20, pady=10)

entry = tk.Entry(windows, fg='#0000ff', bg='#fafafa', font=('Comic Sans MS',14,'bold'), textvariable=nombreEntry)
entry.pack(padx=20, pady=20)

changeNameButton = tk.Button(windows, text='Hi you', command=hiToYou)
changeNameButton.pack(padx=20, pady=20)

windows.mainloop()
