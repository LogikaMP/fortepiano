'''Ефекти – анімація клавіш і візуальні ефекти'''
from pygame import image,transform
from settings import BLACK, BLUE, GRAY
key_up = image.load("assets/data/images/key_pressed.png")
key_down = image.load("assets/data/images/key_unpressed.png")
def draw_effect(screen, rect, pressed):
    if pressed:
        img = key_up
    else:
        
        img = key_down
    img = transform.scale(img,(rect.w,rect.h))
    screen.blit(img,rect)

# 4. Створити функцію, що відображає ефекти на клавішах:
#  - отримати екран, де малювати
#  - отримати рект клавіші, на якій потрібно відобразити ефект
#  - отримати інформацію про те, чи клавіша натиснута
