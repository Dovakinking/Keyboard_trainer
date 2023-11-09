# -*- coding: cp1251 -*-

import json
from tkinter import messagebox
import time

key = '0'
sentence = ''
i = 0
wr_chr = dict()
dt_strt = 0

# Функция, которая завершает работу программы для считывания нажатий, а также записывает результаты в файл data.txt


def End():
    global dt_strt
    global sentence
    global wr_chr
    dt_end = (time.time_ns() // 1000000)/1000.0
    print()
    time_print = dt_end-dt_strt
    speed = round(len(sentence)/time_print*100)/100.0
    print(time_print)
    print(speed)
    print(wr_chr)

    SaveResult('data.txt', wr_chr)
    message = 'Your print speed is ' + str(speed) + ' characters per second\n'
    if (len(wr_chr) == 0):
        message += 'You coped without mistakes, well done!\n'
    else:
        for i in wr_chr:
            if (wr_chr[i] != 1):
                message += 'You made a mistake in the letter "' + \
                    str(i)+'" '+str(wr_chr[i])+' times\n'
            else:
                message += 'You made a mistake in the letter "' + \
                    str(i)+'" 1 time\n'
        message += 'Try again, you will succeed!\n'
    messagebox.showinfo('Congratulation', message)

# Обработка нажатий на клавиши


def key_pressed(event):
    global key
    global sentence
    global wr_chr
    global i
    global dt_strt
    if len(sentence) == 0:
        sentence = "Пустое предложение"
    key = event.char
    if len(key) > 0:
        if i < len(sentence):
            if key != sentence[i]:
                if sentence[i] in wr_chr:
                    wr_chr[sentence[i]] += 1
                else:
                    wr_chr[sentence[i]] = 1
            else:
                print(sentence[i], end="", flush=True)
                i += 1
            if (dt_strt == 0):
                dt_strt = (time.time_ns() // 1000000)/1000.0
        if i == len(sentence):
            End()

# Сохранение результатов


def SaveResult(old_json, wr_chr):
    with open(old_json) as json_file:
        old_wr_chr = json.load(json_file)
        print(old_wr_chr, ' old letter')
        for i in wr_chr:
            if (i in old_wr_chr):
                old_wr_chr[i] += wr_chr[i]
            else:
                old_wr_chr[i] = wr_chr[i]
        with open(old_json, 'w') as outfile:
            json.dump(old_wr_chr, outfile)

# Запуск приложения


def Start(file_sentence):
    global sentence
    global key
    global sentence
    global wr_chr
    global i
    global dt_strt
    sentence = file_sentence
    key = '0'
    i = 0
    wr_chr = dict()
    dt_strt = 0
    print(sentence)

# Для тестов
# window = tkinter.Tk()
# window.title("New wind")
# window.geometry('1200x720')
# mainmenu = Menu(window)
# window.config(menu=mainmenu)
# filemenu = Menu(mainmenu, tearoff=0)
# filemenu.add_command(label="Go", command=StartText)
# mainmenu.add_cascade(label="File", menu=filemenu)
# window.withdraw()
# window.mainloop()
