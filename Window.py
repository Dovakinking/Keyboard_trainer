import tkinter as tk
from Editor import key_pressed


def Window(sent):
    def crutch(event):
        key_pressed(event=event)
        update_label(event)

    def update_label(event):
        text = label["text"]
        if len(text) > 1:
            if text[0] == event.char:
                label["text"] = text[1:]
        else:
            root.destroy()
    root = tk.Tk()
    root.bind("<Key>", crutch)
    root.title("Предложение")
    root.geometry('1200x720')
    label = tk.Label(root, text=sent, font=("Comic Sans MS", 50))
    label.pack()
    label.place(x=400, y=360)  # Зафиксировать надпись на одном месте
