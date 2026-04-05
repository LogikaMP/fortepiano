'''Звуки – завантаження та відтворення аудіо'''
from pygame import mixer
from settings import KEY

# 5. Створити функцію що завантажує звуки:
def load_sounds():
    sounds = {}
    path = "assets/sounds/"
    for key, sound in KEY.items():
        sounds[key] = mixer.Sound(path + sound)
    return sounds

