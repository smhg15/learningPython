import tkinter as tk

"""
TKINTER AND PYTHON METHODS
<variable>.get()
if... and... ==...: else:
<variable> = tk.Label(windows,text='', bg='#000000', fg='#00ff00', font=('Comic Sans MS',28,'bold'))
<variable>.pack(padx=40, pady=10)
tk.Entry(windows, fg='#0000ff', bg='#fafafa', font=('Comic Sans MS',14,'bold'), textvariable=<variable>)
<variable> = tk.Button(windows, text='', command=<function>)
"""


#WINDOWS
windows = tk.Tk() #render blank windows
windows.config(bg='#000000')

#VARIABLES.
user_entry_var = tk.StringVar()
password_entry_var = tk.StringVar()
message_var = tk.StringVar()
title_var = 'My First desk App'

#FUNCTIONS
def login():
    registered_user = user_entry_var.get()
    registered_password = password_entry_var.get()
    
    if registered_user == 'admin' and registered_password == '1234':
        message.config(text ='Welcome ' + registered_user + '!', fg='#00ff00', bg='#000000', font=('Comic Sans MS',14,'bold'))  
    else:
        message.config(text ='Ups! something is wrong!, this user is yours?...
                       should i call the police?', fg='#ff0000', bg='#000000',font=('Comic Sans MS',14,'bold'))
    
#CONTENT
title = tk.Label(windows, text=title_var)
title.config(bg='#000000', fg='#00ff00', font=('Comic Sans MS',28,'bold'))
title.pack()

user = tk.Label(windows, text='Username: ')
user.config(bg='#000000', fg='#0000ff', font=('Comic Sans MS',14))
user.pack()

user_entry = tk.Entry(windows, textvariable=user_entry_var)
user_entry.config()
user_entry.pack()

password = tk.Label(windows, text='Password: ')
password.config(bg='#000000', fg='#0000ff', font=('Comic Sans MS',14))
password.pack()

password_entry = tk.Entry(windows, textvariable=password_entry_var)
password_entry.config()
password_entry.pack()

login_button = tk.Button(windows, text='Login', command=login)
login_button.config()
login_button.pack()

message = tk.Message(windows, text='')
message.config(bg='#000000')
message.pack()

#LOOP
windows.mainloop()
