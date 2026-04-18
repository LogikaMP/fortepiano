'''Звуки – завантаження та відтворення аудіо'''
<<<<<<< HEAD
from pygame.mixer import Sound
from settings import KEYS
def load_sounds():
    sounds = {}
    path_file ="assets/sounds/"
    for key,file in KEYS.items():
        sound = Sound(path_file + file)
        sounds[key]=sound
    return sounds
=======
from pygame import mixer
from settings import KEY
>>>>>>> Saha

# 5. Створити функцію що завантажує звуки:
def load_sound():
    sounds = {}
    path_file = "assets/sounds/"
    for key, sound in KEY.items():
        sounds [key] = mixer.Sound(path_file + sound)
    return sounds