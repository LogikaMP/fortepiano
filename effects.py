'''Ефекти – анімація клавіш і візуальні ефекти'''
from pygame import image,transform, draw
from settings import BLACK, BLUE, GRAY, KEYS



def draw_effect(screen, rect, pressed):
    if pressed:
       col = BLUE
    else:
        
        col = GRAY
    draw.rect(screen, col, rect)
    draw.rect(screen, BLACK, rect, 2)

# 4. Створити функцію, що відображає ефекти на клавішах:
#  - отримати екран, де малювати
#  - отримати рект клавіші, на якій потрібно відобразити ефект
#  - отримати інформацію про те, чи клавіша натиснута
