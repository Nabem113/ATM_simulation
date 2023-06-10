from tkinter import *
from tkinter import font

root = Tk()
root.title('ATM')
# root.attributes('-fullscreen', True)
root.geometry("400x240")

# *Pin verification window*
def enter_pin():

    root.withdraw()

    enter_pin.new_root = Toplevel(root)
    #enter_pin.geometry('460x390')


# Button functions
    def input_text(text):
        entry_box.insert('end', text)

    def back_space():
        entry_box.delete(0)

    # labels and buttons
    lbl = Label(enter_pin.new_root, text='Enter your PIN', fg="red")
    entry_box = Entry(enter_pin.new_root, show="*")

    btn1 = Button(enter_pin.new_root, text='1', pady=15, padx=30, font='cour15', command=lambda: input_text('1'))
    btn2 = Button(enter_pin.new_root, text='2', pady=15, padx=30, font='cour15', command=lambda: input_text('2'))
    btn3 = Button(enter_pin.new_root, text='3', pady=15, padx=30, font='cour15', command=lambda: input_text('3'))
    btn4 = Button(enter_pin.new_root, text='4', pady=15, padx=30, font='cour15', command=lambda: input_text('4'))
    btn5 = Button(enter_pin.new_root, text='5', pady=15, padx=30, font='cour15', command=lambda: input_text('5'))
    btn6 = Button(enter_pin.new_root, text='6', pady=15, padx=30, font='cour15', command=lambda: input_text('6'))
    btn7 = Button(enter_pin.new_root, text='7', pady=15, padx=30, font='cour15', command=lambda: input_text('7'))
    btn8 = Button(enter_pin.new_root, text='8', pady=15, padx=30, font='cour15', command=lambda: input_text('8'))
    btn9 = Button(enter_pin.new_root, text='9', pady=15, padx=30, font='cour15', command=lambda: input_text('9'))
    btn0 = Button(enter_pin.new_root, text='0', pady=15, padx=30, font='cour15', command=lambda: input_text('0'))
    btn_clear = Button(enter_pin.new_root, pady=15, padx=30, font='cour15', text='⌫', command=back_space)
    btn_enter = Button(enter_pin.new_root, pady=15, padx=30, font='cour15', text='↵')

    # Labels and buttons on screen
    lbl.grid(row=1, columnspan=3, column=0)
    entry_box.grid(row=2, columnspan=3, column=0)

    btn1.grid(row=3, column=0)
    btn2.grid(row=3, column=1)
    btn3.grid(row=3, column=2)

    btn4.grid(row=4, column=0)
    btn5.grid(row=4, column=1)
    btn6.grid(row=4, column=2)

    btn7.grid(row=5, column=0)
    btn8.grid(row=5, column=1)
    btn9.grid(row=5, column=2)

    btn_clear.grid(row=6, column=0)
    btn0.grid(row=6, column=1)
    btn_enter.grid(row=6, column=2)

# *Opening window*

# labels

font_settings = "MS Sans Serif", 20, "bold"
title_label = Label(root, text="ATM Terminal", font=font_settings, fg='red')
intro = Label(root, text="Welcome", fg='blue')
option_text = Label(root, text='Select your account type', fg='blue')


#defining functions
def exit_func():
    root.destroy()


# buttons
saving = Button(root, text="Savings", width=7, height=2, bg="#87CEEB", fg='red', command=enter_pin)
current = Button(root, text="Current", width=7, height=2, bg='#87CEEB', fg='red', command=enter_pin)
exit = Button(root, text='EXIT', width=7, height=2, fg="red", command=exit_func)

# On-screen positioning - buttons
exit.pack(side=RIGHT, padx=10)
saving.pack(side=RIGHT, padx=10, pady=80)
current.pack(side=RIGHT, padx=10, pady=80)

# On-screen positioning - labels
intro.pack()
title_label.pack(pady=10)


root.mainloop()
