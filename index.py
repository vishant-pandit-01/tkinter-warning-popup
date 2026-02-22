from tkinter import*
from tkinter import messagebox              #for message box info popup

root=Tk()
root.geometry("300x300")
root.title("warning")
root.config(bg="pink")

def msg():
    messagebox.showinfo("info","show warning:")
    
bt=Button(root,text="press",bd=3,background="pink",command=msg)
bt.pack(pady=20)

root.mainloop()

