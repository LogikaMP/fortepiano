'''Звуки – завантаження та відтворення аудіо'''
from pygame.mixer import Sound
from settings import KEYS
from random import choice

def load_sounds():
    sounds = {}
    path_file = "assets/sounds/"
    for key,file in KEYS.items():
        sound = Sound(path_file + file)
        sounds[key] = sound
    return sounds

def load_rand_sounds():
    sounds = {}
    num = [1,2,3,4,5,6,7]
    path_file = "assets/sounds/rand_sounds/"
    for key,file in KEYS.items():
        n = choice(num)
        num.remove(n)
        sound = Sound(path_file + f"rand_0{n}.wav")
        sounds[key] = sound
    return sounds
# 5. Створити функцію що завантажує звуки:

