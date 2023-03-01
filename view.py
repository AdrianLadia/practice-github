import tkinter as tk
from main import *



if __name__ == "__main__":

    def speak():
        text = entry.get()
        mp3Creator(text).create()
        Speaker().speak()

    root = tk.Tk()
    frame = tk.Frame(root,bg="red",height=200,width=500)
    entry = tk.Entry(frame)
    label = tk.Label(frame,text="Enter Speech",bg='red')
    label.place(relx=0.5,y=20,anchor='n')
    entry.place(relx=0.5,y=45,anchor='n')
    button = tk.Button(frame,text="Speak",command=speak)
    button.place(relx=0.5,y=70,anchor='n')
    frame.place(relx=0.5,rely=0.5,anchor="center")
    root.mainloop()

    # speak()