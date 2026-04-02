'''Клавіші – логіка створення та відображення'''
from settings import KEY, X_START, Y_START, KEY_WIDTH, KEY_HEIGHT
from pygame import Rect
from effects import draw_effect
# 2. Створити функцію, що створює список ректів - клавіш:
#  - використати глобальні змінні - кількість лкавіш, ромзір та координати для старту клавіш
# повернути список ректів клавіш
def create_keys():
    keys = {}
    x = X_START
    for key in KEY:
        rect = Rect(x,Y_START,KEY_WIDTH,KEY_HEIGHT)
        keys [key] = rect
        x += KEY_WIDTH + 10
    return keys
# 3. Створити функцію, що відображає клавіші на екрані:
#  - отримати екран, де малювати
# -  отримати список ректів, що потрібно малювати
#  - отримати список  натиснутих клавіш 
def draw_keys(window,keys,keys_pressed):
    for key, rect in keys.items():
        is_pressed = key in keys_pressed
        draw_effect(window,rect,is_pressed)
