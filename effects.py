'''Ефекти – анімація клавіш і візуальні ефекти'''
from pygame import  draw
from settings import BLACK, GREY, BLUE

# 4. Створити функцію, що відображає ефекти на клавішах:
#  - отримати екран, де малювати
#  - отримати рект клавіші, на якій потрібно відобразити ефект
#  - отримати інформацію про те, чи клавіша натиснута
def draw_effect(window, rect, is_pressed):
    if is_pressed:
        color = BLUE
    else:
        color = GREY
    draw.rect(window, color, rect, border_radius=8)
    draw.rect(window, BLACK, rect, width=4, border_radius=8) 
