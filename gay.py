from tkinter import Tk, Label, Button, messagebox
import random

def yes():
    messagebox.showinfo('Sim', 'Uau... valeu.')
    root.destroy()

def motion_mouse(event):
    btn_yes.place(x=random.randint(0, 500), y=random.randint(0, 500))

def no():
    messagebox.showinfo('Não', 'Ah tá bom... certo.')
    root.destroy()

root = Tk()
root.geometry('600x600')
root.title('Ué')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text='Você é gay?', font='Arial 20 bold', bg='white')
label.pack()

btn_yes = Button(root, text='Não', font='Arial 20 bold', command=no)
btn_yes.place(x=170, y=100)
btn_yes.bind('<Enter>', motion_mouse)

btn_no = Button(root, text='Sim', font='Arial 20 bold', command=yes)
btn_no.place(x=350, y=100)

root.mainloop()
