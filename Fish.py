import traceback

import pyautogui as pag
from PIL import ImageGrab
from time import sleep
import numpy as np
from screeninfo import get_monitors, Monitor

pag.FAILSAFE = True

e_count = 0
e_delta = 0
bbox_pergect_fish = (0, 0, 0, 0)
bbox_start_fish = (0, 0, 0, 0)


def def_consts():
    primary_monitor = None
    for monitor in get_monitors():
        monitor: Monitor
        print(f'Обнаружен монитор: {monitor.name} ({monitor.width}x{monitor.height})')
        if monitor.is_primary:
            primary_monitor = monitor
    if primary_monitor:
        print(f'Основной монитор выбран: {primary_monitor.name} ({primary_monitor.width}x{primary_monitor.height})')
    else:
        raise NotImplementedError('Не удалось определить основной монитор')

    global bbox_pergect_fish, bbox_start_fish, e_count, e_delta

    if primary_monitor.width == 2560 and primary_monitor.height == 1440:
        e_count = 126
        e_delta = 5
        e_size = (31, 32)
        start_fish_x, start_fish_y = 1056, 969
        pergect_fish_x, pergect_fish_y = 1144, 969

    elif primary_monitor.width == 1920 and primary_monitor.height == 1080:
        e_count = 65
        e_delta = 5
        e_size = (23, 23)
        start_fish_x, start_fish_y = 793, 727
        pergect_fish_x, pergect_fish_y = 858, 727

    else:
        raise NotImplementedError('Данное разрешение монитора не поддерживается!')

    bbox_pergect_fish = (pergect_fish_x, pergect_fish_y, pergect_fish_x + e_size[0], pergect_fish_y + e_size[1])
    bbox_start_fish = (start_fish_x, start_fish_y, start_fish_x + e_size[0], start_fish_y + e_size[1])


def get_fish():
    pag.keyDown('e')
    sleep(.4)
    pag.keyUp('e')


def detect_e(img):
    img = img.convert('L')
    thresh = 240
    r = img.point(lambda x: 255 if x > thresh else 0, mode='1')
    data = np.asarray(r, dtype="int32")
    e_detected = e_count-e_delta <= data.sum() <= e_count+e_delta
    return e_detected


def get_start_fish():
    img = ImageGrab.grab(bbox=bbox_start_fish)
    return detect_e(img)


def get_perfect_fish():
    img = ImageGrab.grab(bbox=bbox_pergect_fish)
    return detect_e(img)


def move():
    pag.keyDown('w')
    sleep(0.01)
    pag.keyUp('w')

    pag.keyDown('s')
    sleep(0.013)
    pag.keyUp('s')


if __name__ == '__main__':
    print("Инициализация основных переменных...")
    try:
        def_consts()
    except Exception as e:
        print('В ходе работы произошла ошибка:\n')
        print(traceback.format_exc())
        input()
    print('Инициализация завершена. Начало работы макроса:')
    for time in range(3):
        print(3 - time)
        sleep(1)
    fish_count = 0
    while True:
        try:
            if get_start_fish():
                move()
                get_fish()
            if get_perfect_fish():
                fish_count += 1
                print(f"Обнаружена рыба! Всего поймано: {fish_count}")
                get_fish()
        except Exception as e:
            print('В ходе работы произошла ошибка:\n')
            print(traceback.format_exc())
            input()
