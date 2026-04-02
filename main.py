'''Main – запуск гри та обробка подій'''
# 6. Імпортуємо все що необхідно для роботи гри
import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, KEY
from keys import create_keys, draw_keys
from sounds import load_sound
# 7. Ініцилізація та Створити вікно 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# 8. Створити список ректів - клавіш
keys = create_keys()
# 9. Створити порожню множину - натиснуті клавіши
key_pressed = set()
# 10. Створити список звуків - завантажити звуки нот
sounds = load_sound()

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
         sounds [key_name].play()
         key_pressed.add(key_name)
      if event.type == pygame.KEYUP:
         key_name = pygame.key.name(event.key)
         key_pressed.discard(key_name)  
#  - обробка кліку по клавішам  
      if event.type == pygame.MOUSEBUTTONDOWN:
         pos = event.pos
         for key, rect in keys.items():
            if rect.collidepoint(pos) and not key in key_pressed:
               sounds [key_name].play()
               key_pressed.add(key)
      if event.type == pygame.MOUSEBUTTONUP:
         pos = event.pos
         for key,rect in keys.items():
            if rect.collidepoint(pos) and key in key_pressed:
               key_pressed.discard(key_name)
    
#  - відобразити фон, клавіши, оновити вікно
   window.fill(WHITE)
   draw_keys(window,keys,key_pressed)
   pygame.display.flip()
    # обробка лкіку по клавішам


