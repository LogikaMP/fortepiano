'''Main – запуск гри та обробка подій'''
# 6. Імпортуємо все що необхідно для роботи гри
import pygame
from settings import WINDOWS_WIDTH , WINDOWS_HIGHT, WHITE, KEY
from keys import*
from sounds import load_sounds
# 7. Ініцилізація та Створити вікно 
pygame.init()
window = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HIGHT))

# 8. Створити список ректів - клавіш
keys = create_keys()
# 9. Створити порожню множину - натиснуті клавіши
key_pressed = set()
# 10. Створити список звуків - завантажити звуки нот
sounds = load_sounds()

# 11. Головний цикл гри:
run = True
while run:
# - обробка закртиття вікна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#  - обробка подій (натискання та відпускання клавіш)
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            sounds[key_name].play()
            key_pressed.add(key_name)
        if event.type == pygame.KEYUP:
            key_name = pygame.key.name(event.key)
            key_pressed.discard(key_name)
#  - обробка кліку по клавішам
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for key in keys:
                if keys[key].collidepoint(pos) and not key in key_pressed:
                    sounds[key].play()
                    key_pressed.add(key)
        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            for key in keys:
                if keys[key].collidepoint(pos):
                    key_pressed.discard(key)
#  - відобразити фон, клавіши, оновити вікно
    window.fill(WHITE)
    draw_keys(window, keys, key_pressed)
    pygame.display.flip()
    # обробка лкіку по клавішам


