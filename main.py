from tkinter import *
from tkinter import font

root = Tk()
root.title('ATM')
#root.attributes('-fullscreen', True)
root.geometry("400x240")

#Opening window

#labels
font_settings = "MS Sans Serif", 20, "bold"
title_label = Label(root, text="ATM Terminal", font=font_settings, fg='red')
intro = Label(root, text="Welcome", fg='blue')
option_text = Label(root, text='Select your account type', fg='blue')

#buttons
saving = Button(root, text="Savings", width=7, height=2, bg="#87CEEB", fg='red')
current = Button(root, text="Current", width=7, height=2, bg='#87CEEB', fg='red')
exit = Button(root, text='EXIT', width=7, height=2, fg="red")

#On-screen positioning - buttons
exit.pack(side=RIGHT, padx=10)
saving.pack(side=RIGHT, padx=10, pady=80)
current.pack(side=RIGHT, padx=10, pady=80)


#On-screen positioning - labels
intro.pack()
title_label.pack(pady=10)

root.mainloop()