import json
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def Headmap():
    # Создание данных для тепловой карты
    russian_layout = [['ё', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
                      ['', 'й', 'ц', 'у', 'к', 'е', 'н', 'г',
                          'ш', 'щ', 'з', 'х', 'ъ'],
                      ['', 'ф', 'ы', 'в', 'а', 'п', 'р',
                          'о', 'л', 'д', 'ж', 'э', ''],
                      ['', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '.', '', '']]

    russian_count = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    russian_mask = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]

    english_layout = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
                      ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']'],
                      ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", ''],
                      ['', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '']]

    english_count = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    english_mask = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

    with open('data.txt') as json_file:
        old_wr_chr = json.load(json_file)
        for i in old_wr_chr:
            for k in range(len(russian_layout)):
                for j in range(len(russian_layout[k])):
                    if i.lower() == russian_layout[k][j].lower():
                        russian_count[k][j] = old_wr_chr[i]
            for k in range(len(english_layout)):
                for j in range(len(english_layout[k])):
                    if i.lower() == english_layout[k][j].lower():
                        english_count[k][j] = old_wr_chr[i]
    # Создание тепловой карты
    sns.set(font_scale=1.5)
    sns.set(rc={'figure.figsize': (11.7, 7.27)})

    array_r_2d = np.array(russian_count)
    array_e_2d = np.array(english_count)

    mask_r = np.ones_like(russian_mask)
    for i in range(len(mask_r)):
        for j in range(len(mask_r[i])):
            mask_r[i][j] = russian_mask[i][j]

    mask_e = np.ones_like(english_mask)
    for i in range(len(mask_e)):
        for j in range(len(mask_e[i])):
            mask_e[i][j] = english_mask[i][j]

    fig, ax = plt.subplots(1, 2)
    sns.heatmap(data=array_r_2d, annot=np.array(
        russian_layout), mask=mask_r, fmt="", ax=ax[0])
    ax[0].set_title('Русская раскладка')

    sns.heatmap(data=array_e_2d, annot=np.array(
        english_layout), mask=mask_e, fmt="", ax=ax[1])
    ax[1].set_title('Английская раскладка')

    plt.tight_layout()
    plt.show()
