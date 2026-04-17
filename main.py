'''Main – запуск гри та обробка подій'''
# 6. Імпортуємо все що необхідно для роботи гри
import pygame
from settings import *
from keys import *
from sounds import *
# 7. Ініцилізація та Створити вікно 
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

keys_rect = create_keys()
# 8. Створити список ректів - клавіш

key_pressed = set()
# 9. Створити порожню множину - натиснуті клавіши

key_sounds = load_sounds() 
# 10. Створити список звуків - завантажити звуки нот
run = True

while run:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for key,rect in keys_rect.items():
                if rect.collidepoint(pos):
                    key_sounds[key].play()
                    key_pressed.add(key)

        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            for key,rect in keys_rect.items():
                key_sounds[key].stop()
                key_pressed.discard(key)

        if event.type == pygame.KEYDOWN:
            name_key = pygame.key.name(event.key)
            key_sounds[name_key].play()
            key_pressed.add(key)

        if event.type == pygame.KEYUP:
            name_key = pygame.key.name(event.key)
            key_sounds[name_key].stop()
            key_pressed.discard(key)

    draw_keys(screen, keys_rect, key_pressed)
    pygame.display.flip()
    clock.tick(60)


# - обробка закртиття вікна
   
#  - обробка подій (натискання та відпускання клавіш)
        
#  - обробка кліку по клавішам
   
#  - відобразити фон, клавіши, оновити вікно
    
    # обробка лкіку по клавішам


