'''Клавіші – логіка створення та відображення'''
from pygame import Rect, image, transform
from settings import KEYS, KEY_WIDTH, KEY_HEIGHT, X_KEY_START, Y_KEY_START
from effects import draw_effect


def create_keys(num_keys):
    keys = {}
    sounds_img = {}
    x = X_KEY_START
    data = dict(list(KEYS.items())[:num_keys ])
    for key in data:
        r = Rect(x, Y_KEY_START, KEY_WIDTH, KEY_HEIGHT)
        keys[key] = r
        x += KEY_WIDTH + 10
        
    return keys

def draw_keys(screen, keys, is_pressed):
    for key,rect in keys.items():
        pressed = key in is_pressed
        draw_effect(screen, rect, pressed)

def load_sounds_img():
    sounds_img = {}
    x = X_KEY_START + 15
    y = Y_KEY_START
    for key in KEYS:
        img = image.load(f"assets/images/notes/{key}.png")
        img = transform.scale(img,(25, 50))
        sounds_img[key] = {"img":img,
                           "draw":False,
                           "x":x,
                            "y":y,
                            "start_y":y}
        x += KEY_WIDTH + 10
    return sounds_img
# 2. Створити функцію, що створює список ректів - клавіш:
#  - використати глобальні змінні - кількість лкавіш, ромзір та координати для старту клавіш
# повернути список ректів клавіш


# 3. Створити функцію, що відображає клавіші на екрані:
#  - отримати екран, де малювати
# -  отримати список ректів, що потрібно малювати
#  - отримати список  натиснутих клавіш 

