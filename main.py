'''Main – запуск гри та обробка подій'''
# 6. Імпортуємо все що необхідно для роботи гри
<<<<<<< HEAD
import pygame 
from settings import *
from keys import*
from sounds import*


# 7. Ініцилізація та Створити вікно 
pygame.init()
screen = pygame.display.set_mode((WHINDOW_WIDTH,WHINDOW_HIEGHT))
clock = pygame.time.Clock()
# 8. Створити список ректів - клавіш
rect_keys = create_keys()
# 9. Створити порожню множину - натиснуті клавіши
key_pressed = set()
# 10. Створити список звуків - завантажити звуки нот
sounds_keys = load_sounds()

# 11. Головний цикл гри:
run = True
while run:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for key,rect in rect_keys.items():
                if rect.collidepoint(pos):
                    sounds_keys[key].play()
                    key_pressed.add(key)
        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            for key,rect in rect_keys.items():
                sounds_keys[key].stop()
                key_pressed.discard(key)
        if event.type == pygame.KEYDOWN:
            name_key =pygame.key.name(event.key)
            sounds_keys[name_key].play()
            key_pressed.add(name_key)
        if event.type == pygame.KEYUP:
            name_key = pygame.key.name(event.key)
            sounds_keys[name_key].stop()
            key_pressed.discard(name_key)
    draw_keys(screen,rect_keys,key_pressed)
    pygame.display.flip()
    clock.tick(40)



=======
import pygame
from settings import GRAY, WINDOW_WIDTH, WINDOW_HEIGHT, WHITE,GRAY,BLUE ,KEY
from keys import create_keys, draw_keys
from sounds import load_sound
'''Додай імопрт класу меню'''
from ui.settingsUi import SettingsMenu
# 7. Ініцилізація та Створити вікно 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# 8. Створити список ректів - клавіш
keys_rect = create_keys()
# 9. Створити порожню множину - натиснуті клавіши
keys_pressed = set()
# 10. Створити список звуків - завантажити звуки нот
keys_sounds = load_sound()

'''Створи обєкт меню:
координати - 20,20,
розмір - 100, 40
кольри - GREY, WHITE, BLUE'''
setting = SettingsMenu(20,20,100,40,GRAY,WHITE,BLUE)
# 11. Головний цикл гри:
run = True
while run:
   setting.update()
>>>>>>> Saha
# - обробка закртиття вікна
   for event in pygame.event.get():
      '''виклич метод оновлення меню - передай подію event'''
      setting.update(event)
      if event.type == pygame.QUIT:
         run = False
#  - обробка подій (натискання та відпускання клавіш)
      if event.type == pygame.KEYDOWN and setting.game_part=="game":
         key_name = pygame.key.name(event.key)
         keys_sounds [key_name].play()
         keys_pressed.add(key_name)
      if event.type == pygame.KEYUP:
         key_name = pygame.key.name(event.key)
         keys_pressed.discard(key_name)  
#  - обробка кліку по клавішам  
      if event.type == pygame.MOUSEBUTTONDOWN and setting.game_part=="game":
         pos = event.pos
         for key, rect in keys_rect.items():
            if rect.collidepoint(pos) and not key in keys_pressed:
               keys_sounds[key].play()
               keys_pressed.add(key)
      if event.type == pygame.MOUSEBUTTONUP:
         pos = event.pos
         for key,rect in keys_rect.items():
            if rect.collidepoint(pos) and key in keys_pressed:
               keys_pressed.discard(key)
    
#  - відобразити фон, клавіши, оновити вікно
   window.fill(WHITE)
   '''виклич метод малювати меню'''
   setting.darw(window)
   '''перепиши список клавіш :
   виклич метод їх стоврення передавши значення кільксоті клавіш з меню'''

   '''додай умову - малювати якщо стангри=гра(перевір значення властивості меню)'''
   if setting.game_part == "game":
      draw_keys(window,keys_rect,keys_pressed)
   pygame.display.flip()
    # обробка лкіку по клавішам


