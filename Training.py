import random
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from Editor import Start
from Read_Keys import Headmap
from Window import Window


def Exit():
    main_window.destroy()


def OpenFile():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)


def SaveFile():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)


def RandomSentence():
    with open('storage.txt', "r") as file:
        ran = random.randint(0, 39)
        text = file.readlines()[ran]
        text_editor.delete("1.0", END)
        text_editor.insert("1.0", text)


def StartText():
    sentence = ""
    if (len(text_editor.get("1.0", END)) > 5):
        for i in text_editor.get("1.0", END):
            if (i != '\n'):
                sentence += i
            else:
                break
    else:
        RandomSentence()
        sentence = ""
        for i in text_editor.get("1.0", END):
            if (i != '\n'):
                sentence += i
            else:
                break
    Window(sentence)
    Start(sentence)


def Help():
    messagebox.showinfo(
        'Guide', '  Все активные кнопки расположены в верхнем меню программы в разделе "Программа"\n  Чтобы начать использовать клавиатурный тренажёр, введите нужную фразу в поле ниже или же импортируйте её из текстового файла, после чего начните работу тренажёра с помощью кнопки "Начать" в меню "Программа".\n    Также есть функция "Случайное предложение", которая псевдослучайным образом выбирает предложение из имеющихся в базе программы и вставляет его в текстовое поле.\n    Просмотр клавиш, на которых чаще всего ошибается пользователь, доступен через кнопку "Посмотреть headmap ошибок" в меню "Программа".')


def Null():
    result = messagebox.askyesno(title="Подтвержение операции",
                                 message="Вы действительно хотите обнулить вашу статистику?")
    if result:
        with open('data.txt', "w") as file:
            file.write("{}")
        messagebox.showinfo("Результат", "Статистика обнулена")
    else:
        messagebox.showinfo("Результат", "Статистика сохранена")


main_window = Tk()
main_window.title('Клавиатурный тренажёр')
main_window.geometry('1200x720')
icon = PhotoImage(file="Keyboard1.png")
main_window.iconphoto(False, icon)

main_window.grid_rowconfigure(index=0, weight=1)
main_window.grid_columnconfigure(index=0, weight=1)
main_window.grid_columnconfigure(index=1, weight=1)

frame = Frame(
    main_window,
    padx=10,
    pady=10
)

main_menu = Menu(main_window)
main_window.config(menu=main_menu)


text_editor = Text(width=96, font=("Comic Sans MS", 15))
text_editor.insert("1.0", "Введите сюда предложение, которое хотите напечатать, или выберете файл, из которого импортировать нужное вам предлодение из меню выше. Вы можете экспортировать текст из этого текстового поля в файл.")
text_editor.grid(column=0, columnspan=2, row=0)

main_filemenu = Menu(main_menu, tearoff=0)
main_filemenu.add_command(label="Начать", command=StartText)
main_filemenu.add_command(label="Открыть предложение...", command=OpenFile)
main_filemenu.add_command(
    label="Случайное предложение", command=RandomSentence)
main_filemenu.add_command(label="Сохранить предложение...", command=SaveFile)
main_filemenu.add_command(label="Посмотреть headmap ошибок", command=Headmap)
main_filemenu.add_command(label="Обнулить статистику ошибок", command=Null)
main_filemenu.add_command(label="Выход", command=Exit)

main_helpmenu = Menu(main_menu, tearoff=0)
main_helpmenu.add_command(label="Руководство", command=Help)

main_menu.add_cascade(label="Программа", menu=main_filemenu)
main_menu.add_cascade(label="Справка", menu=main_helpmenu)


main_window.mainloop()
