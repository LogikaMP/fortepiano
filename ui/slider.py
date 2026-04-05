'''Напиши клас для слайдера'''

# підключи бібліотеку pygame для роботи з графікою
# імпортуй чорний колір з файлу налаштувань
import pygame
from settings import BLACK
# клас повзунка (Slider)
#аргументи - координати, розмір, мак.число повзунка, колір повзунка, колір поінтера
class Slider:                        
    def __init__(self, x, y, w, h, max_num, col_slider, col_pointer):
        # зберіхи у властивість максимальне значення повзунка
        self.max_num = max_num
        # створи прямокутник основи повзунка - координати та розмір із конструктора
        self.slider = pygame.Rect(x,y,w,h)
        # створи повзунок (кнопкуб поінтер): 
        # х такий самийб у - половина висоти слайдера 
        # вистоа, ширина(квадрат) - висота слайдера*2
        self.pointer = pygame.Rect(x,y - h//2, h*2, h*2)
        # встанови початкову позицію центра повзунка по X 
        self.pointer.centerx = x
        # задай колір основи
        self.col_slider = col_slider
        # задай колір повзунка
        self.col_pointer = col_pointer
        # встанови початкове значення (0) сладйера
        self.value = 0
        # створи прапорець перетягування (спочатку False)
        self.draging = False
        # створи змінну для зсуву миші
        self.offset_x = 0
        # запам’ятай початок повзунка х
        self.start = x
        # запам’ятай кінець повзунка: х + ширина слайдера
        self.end = x + w
        # створи шрифт для відображення значення розмір шрифта=вистоа слайдера
        self.font = pygame.font.Font(None,h)
        # одразу виклич метод для оновлення даних тексту сладйера, його значення
        self.update_value()         

    def draw(self, screen):
        # намалюй основу повзунка
        pygame.draw.rect(screen,self.col_slider,self.slider,border_radius=5)
        # додай рамку
        pygame.draw.rect(screen,BLACK,self.slider,width=10,border_radius=5)

        # намалюй сам повзунок
        pygame.draw.rect(screen, self.col_pointer, self.pointer,border_radius=5)
        # додай рамку повзунка
        pygame.draw.rect(screen, BLACK, self.pointer, width=10, border_radius=5)
        
        # обчисли позицію тексту по X : 
        #х.поінтера + ширина повзунка // 2.6
        x = self.pointer.x + self.slider.w // 2.6
        # обчисли позицію тексту по Y : 
        #у.поінтера + ширина повзунка // 3
        y = self.pointer.y + self.slider.w // 3
        # виведи текст значення на екран
        screen.blit(self.value_txt,(x,y))
    def update(self, event):
        # перевіремо подію мишка натиснута та якщо вже не натиснута
        if event.type == pygame.MOUSEBUTTONDOWN and not self.draging:
            # отримай позицію кліку миші
            pos = event.pos
            # перевір чи натиснули саме на повзунок
            if self.pointer.collidepoint(pos):
                # увімкни режим перетягування
                    self.draging = True
                # обчисли зсув курсора: х.поінтер - х.миші
                    self.offset_x = self.pointer.centerx - pos[0]
        # перевіремо подію мишка  не натиснута
        if event.type == pygame.MOUSEBUTTONUP:
            # вимкни режим перетягування
            self.draging = False
        # перевіремо подію мишка рухається
        if event.type == pygame.MOUSEMOTION:
            # обчисли нову позицію по X: 
            # зсув миші + х.миші
            new_x = self.offset_x + pos[0]
            # перевір межі руху та якщо режим перетягуванн:
            #нова позиція миші більша за початкову та менша за кінцеву
            if new_x > self.start and new_x < self.end:
                # перемісти повзунок: ценрт_х = новий х
                self.pointer.centerx = new_x
                # онови значення  = викликати метод
                self.update_value()
    def update_value(self):
        # знайди значення повзунка:
        #координати х поінтера повзунка - стартове значення(стартова координата)
        value = self.pointer.centerx - self.start
        # переведи  у значення: 
        # знайдене значення ділимо на ширину слайдера та множимо на максимальне значення слайдера
        #округлити значення
        self.value = int((value/self.slider.w) * self.max_num)
        # створити текст значення
        self.value_txt = self.font.render(str(self.value),True,BLACK)