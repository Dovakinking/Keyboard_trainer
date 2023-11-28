import random
from tkinter import END, Frame, Menu, PhotoImage, Text, Tk, filedialog, messagebox
from Editor import Start
from Read_Keys import Headmap
from Window import Window
import json


def Exit():  # Завершение работы программы
    main_window.destroy()


def OpenFile():  # Открытие файла с помощью filedialog
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)


def SaveFile():  # Сохранение файла
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)


def RandomSentence():  # Выборка случайного предложения из файла storage
    with open('storage.txt', "r") as file:
        ran = random.randint(0, 39)
        text = file.readlines()[ran]
        text_editor.delete("1.0", END)
        text_editor.insert("1.0", text)


def StartText():  # Запуск  тренажёна
    sentence = ""
    # Если длина предложения больше 5 символов, то считываем его до момента, пока в тексте не встретится перенос на следующую строку
    if (len(text_editor.get("1.0", END)) > 5):
        for i in text_editor.get("1.0", END):
            if (i != '\n'):
                sentence += i
            else:
                break
    # Если же длина предложения не больше 4 символов, то вставляем случайное предложение из нашего файла
    else:
        RandomSentence()
        sentence = ""
        for i in text_editor.get("1.0", END):
            if (i != '\n'):
                sentence += i
            else:
                break
    # Запуск программы, которая отвечает за написание внутри неё предложения
    Window(sentence)
    # Запуск программы, которая отвечает за реализацию клавиатурного тренажёра
    Start(sentence)


# Окно с краткой инструкцией к приложению
def Help():
    messagebox.showinfo(
        'Guide', '  Все активные кнопки расположены в верхнем меню программы в разделе "Программа"\n  Чтобы начать использовать клавиатурный тренажёр, введите нужную фразу в поле ниже или же импортируйте её из текстового файла, после чего начните работу тренажёра с помощью кнопки "Начать" в меню "Программа".\n    Также есть функция "Случайное предложение", которая псевдослучайным образом выбирает предложение из имеющихся в базе программы и вставляет его в текстовое поле.\n    Просмотр клавиш, на которых чаще всего ошибается пользователь, доступен через кнопку "Посмотреть headmap ошибок" в меню "Программа".')


# Окно со статистикой
def Stat():
    with open('Statistics.txt', "r") as json_file:
        statistics = json.load(json_file)
    messagebox.showinfo(
        'Statistics', '    Всего вы правильно напечатали ' + str(int(statistics["right_tap"])) + ' символов из ' + str(int(statistics["count_tap"])) + ' за ' + str(round(100*statistics["time"])/100) + ' с. Это ' + str(round(10000*statistics["right_tap"]/(statistics["count_tap"]+0.001)) / 100) + ' %'+' попадания по клавишам')

# Обнуление статистики


def Null():
    result = messagebox.askyesno(title="Подтвержение операции",
                                 message="Вы действительно хотите обнулить вашу статистику?")
    if result:
        with open('data.txt', "w") as file:
            file.write("{}")
        with open('Statistics.txt', "w") as file:
            file.write('{"time": 0, "right_tap": 0}')
        messagebox.showinfo("Результат", "Статистика обнулена")
    else:
        messagebox.showinfo("Результат", "Статистика сохранена")


if __name__ == '__main__':
    # Создание основного окна и настройка его параметров
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

    # Создание "шаблонного" предложения
    text_editor = Text(width=96, font=("Comic Sans MS", 15))
    text_editor.insert("1.0", "Введите сюда предложение, которое хотите напечатать, или выберете файл, из которого импортировать нужное вам предложение из меню выше. Вы можете экспортировать текст из этого текстового поля в файл.")
    text_editor.grid(column=0, columnspan=2, row=0)

    # Создание меню с соотв. вкладками
    main_filemenu = Menu(main_menu, tearoff=0)
    main_filemenu.add_command(label="Начать", command=StartText)
    main_filemenu.add_command(label="Открыть предложение...", command=OpenFile)
    main_filemenu.add_command(
        label="Случайное предложение", command=RandomSentence)
    main_filemenu.add_command(
        label="Сохранить предложение...", command=SaveFile)
    main_filemenu.add_command(
        label="Посмотреть headmap ошибок", command=Headmap)
    main_filemenu.add_command(label="Посмотреть статистику", command=Stat)
    main_filemenu.add_command(label="Обнулить статистику ошибок", command=Null)
    main_filemenu.add_command(label="Выход", command=Exit)

    # Инструкция по работе в тренажёре
    main_helpmenu = Menu(main_menu, tearoff=0)
    main_helpmenu.add_command(label="Руководство", command=Help)

    main_menu.add_cascade(label="Программа", menu=main_filemenu)
    main_menu.add_cascade(label="Справка", menu=main_helpmenu)

    main_window.mainloop()
