'''Main – запуск гри та обробка подій'''
# 6. Імпортуємо все що необхідно для роботи гри
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



# - обробка закртиття вікна
   
#  - обробка подій (натискання та відпускання клавіш)
        
#  - обробка кліку по клавішам
   
#  - відобразити фон, клавіши, оновити вікно
    
    # обробка лкіку по клавішам


