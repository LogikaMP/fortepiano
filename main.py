'''Main – запуск гри та обробка подій'''
# 6. Імпортуємо все що необхідно для роботи гри
import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE, KEY
from keys import create_keys, draw_keys
from sounds import load_sound
'''Додай імопрт класу меню'''
from ui.settingsUi import SettingsMenu

# 7. Ініцилізація та Створити вікно 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# 8. Створити список ректів - клавіш
keys = create_keys()
# 9. Створити порожню множину - натиснуті клавіши
key_pressed = set()
# 10. Створити список звуків - завантажити звуки нот
sounds = load_sound()

'''Створи обєкт меню:
координати - 20,20,
розмір - 100, 40
кольри - GREY, WHITE, BLUE'''
settings_menu = SettingsMenu(20,20,100,40,GRAY,WHITE,BLUE)
# 11. Головний цикл гри:
run = True
while run:
# - обробка закртиття вікна
   for event in pygame.event.get():
      '''виклич метод оновлення меню - передай подію event'''
      settings_menu.update(event)
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
   '''виклич метод малювати меню'''
   settings_menu.draw(window)
   '''перепиши список клавіш :
   виклич метод їх стоврення передавши значення кільксоті клавіш з меню'''
   
   '''додай умову - малювати якщо стангри=гра(перевір значення властивості меню)'''
   if settings_menu.game_part == "game": 
      draw_keys(window,keys,key_pressed)
   pygame.display.flip()
    # обробка лкіку по клавішам


