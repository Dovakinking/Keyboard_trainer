import json
import tkinter as tk
from Editor import key_pressed

# Не придумал ничего лучше, чем создание глобальных переменных, отвечающих за время, количество правильных и просто нажатий.
time = 0.0
count_tap = 0.0
right_tap = 0.0

# Сохранение результатов в формате json в statistics.txt


def SaveResult(old_json, time, right_tap, count_tap):
    with open(old_json) as json_file:
        old_result = json.load(json_file)
        print(old_result, ' old letter')
        if ("time" in old_result):
            old_result["time"] += time
        if ("right_tap" in old_result):
            old_result["right_tap"] += right_tap
        if ("right_tap" in old_result):
            old_result["count_tap"] += count_tap
        with open(old_json, 'w') as outfile:
            json.dump(old_result, outfile)


def Window(sent):

    # Функция самовызывается раз в 0.1 секунду и обновляет надпись, в которой отображается статистика
    def update_time():
        if (root.winfo_exists()):
            global time
            global right_tap
            global count_tap
            time += 1
            stat = "Current time: " + str(time/10) + "s\nCorrect letters: " + \
                str(right_tap)+"\n%"+" of correct clicks: " + \
                str(round(10000*right_tap/count_tap) / 100) + \
                "\nNext letter: '" + label["text"][0]+"'"
            label1.config(text=stat)
            root.after(100, update_time)
# Костыль, позволяющий передать event нажатия в две функции а также посчитать количество нажатий

    def crutch(event):
        global count_tap
        count_tap += 1
        key_pressed(event)
        update_label(event)

    def update_label(event):
        text = label["text"]
        global right_tap
        if len(text) > 1:
            if text[0] == event.char:
                right_tap += 1
                if (right_tap == 1):
                    update_time()
                label["text"] = text[1:]
        else:
            global count_tap
            global time
            SaveResult('Statistics.txt', time/10, right_tap, count_tap)
            time = 0
            count_tap = 0
            right_tap = 0
            root.destroy()
    root = tk.Tk()
    root.bind("<Key>", crutch)
    root.title("Предложение")
    root.geometry('1200x720')
    label1 = tk.Label(root, font=("helvetica", 15), anchor='w', justify="left")
    label1.pack()
    label1.place(x=10, y=10)  # Зафиксировать надпись на одном месте
    label = tk.Label(root, text=sent, font=("Comic Sans MS", 50))
    label.pack()
    label.place(x=400, y=360)  # Зафиксировать надпись на одном месте
