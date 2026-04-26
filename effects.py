'''Ефекти – анімація клавіш і візуальні ефекти'''
from pygame import image,transform, draw
from settings import BLACK, BLUE, GRAY, KEYS

key_ap = image.load('assets/images/notes/key_unpressed.png')
key_down = image.load('assets/images/notes/key_pressed.png')

def draw_effect(screen, rect, pressed):
    if pressed:
       img = key_down
    else:
         img = key_ap
        
    img = transform.scale(img, (rect.width, rect.height))
    screen.blit(img, rect )

    

# 4. Створити функцію, що відображає ефекти на клавішах:
#  - отримати екран, де малювати
#  - отримати рект клавіші, на якій потрібно відобразити ефект
#  - отримати інформацію про те, чи клавіша натиснута
