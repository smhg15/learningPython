import tkinter as tk

#WINDOWS
windows = tk.Tk() #render blank windows
windows.config(bg='#000000')

#VARIABLES. las variables de Python pueden declararse en un mismo renglón (las de tkinter no). Ejemplo: var1 = var2 = var3 = '' (las 3 variables poseen el valor ''). También se puede asignar distintos valores: var1, var2, var3 = 1, 'perro', false. 
user_entry_var = tk.StringVar()
password_entry_var = tk.StringVar()
text = ''
message_var = tk.StringVar()
title_var = 'My First desk App'
tasklist = []

registered_user_db = input('Please, create your username: ')
registered_password_db = input('Please, create a password: ')
ask_for_task = 'Y'
while ask_for_task == 'Y' or ask_for_task == 'y':
    tasklist.append(input('Please, record a task on your tasklist: '))
    ask_for_task = input('Do you want to record another task? (Y/N): ')

#FUNCTIONS
def login():
    registered_user = user_entry_var.get()
    registered_password = password_entry_var.get()
    
    if registered_user == registered_user_db and registered_password == registered_password_db:
        message.config(text ='Welcome ' + registered_user + '!', fg='#00ff00', bg='#000000', font=('Comic Sans MS',14,'bold'))  
    else:
        message.config(text ='Ups! something is wrong!, this user is yours?... should i call the police?', fg='#ff0000', bg='#000000',font=('Comic Sans MS',14,'bold'))

def to_binary():
    text = textfield.get('1.0',tk.END)
    binary_text= ''
    for character in text:
        binary_text += bin(ord(character))[2:]
    textfield.delete('1.0',tk.END)
    textfield.insert('1.0',binary_text)
        
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

to_binary_title = tk.Label(windows, text='Write a text and see the magic:')
to_binary_title.config(bg='#000000', fg='#00ff00', font=('Comic Sans MS',14, 'bold'))
to_binary_title.pack()

textfield = tk.Text(windows)
textfield.config(width= 50, height= 5)
textfield.pack()

to_binary_button = tk.Button(windows, text='To Binary', command=to_binary)
to_binary_button.config()
to_binary_button.pack()

for task in tasklist:
        tk.Checkbutton(windows,text=task).pack()
        
windows.mainloop()
