from tkinter import *
from tkinter import font

root = Tk()
root.title('ATM')
# root.attributes('-fullscreen', True)
root.geometry("400x240")






# labels

font_settings = "MS Sans Serif", 20, "bold"
title_label = Label(root, text="ATM Terminal", font=font_settings, fg='red')
intro = Label(root, text="Welcome", fg='blue')
option_text = Label(root, text='Select your account type', fg='blue')


# defining functions
def exit_func():
    root.destroy()


# buttons
Deposit = Button(root, text="Deposit", width=7, height=2, bg="#87CEEB", fg='red', )
Withdraw = Button(root, text="Withdraw", width=7, height=2, bg='#87CEEB', fg='red',)
exit = Button(root, text='EXIT', width=7, height=2, fg="red", command=exit_func)

# On-screen positioning - buttons
exit.pack(side=RIGHT, padx=10)
saving.pack(side=RIGHT, padx=10, pady=80)
current.pack(side=RIGHT, padx=10, pady=80)

# On-screen positioning - labels
intro.pack()
title_label.pack(pady=10)

root.mainloop()
