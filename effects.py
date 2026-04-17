'''Ефекти – анімація клавіш і візуальні ефекти'''
from pygame import draw
from settings import BLACK, BLUE, GRAY

def draw_effect(screen, rect, pressed):
    if pressed:
        color = BLUE
    else:
        color = GRAY
    draw.rect(screen, color, rect)
    draw.rect(screen, BLACK, rect, width=4)

# 4. Створити функцію, що відображає ефекти на клавішах:
#  - отримати екран, де малювати
#  - отримати рект клавіші, на якій потрібно відобразити ефект
#  - отримати інформацію про те, чи клавіша натиснута
