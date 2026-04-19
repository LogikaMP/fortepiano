'''Напиши клас для слайдера'''
import pygame

# підключи бібліотеку pygame для роботи з графікою
# імпортуй чорний колір з файлу налаштувань
from settings import BLACK
# клас повзунка (Slider)
#аргументи - координати, розмір, мак.число повзунка, колір повзунка, колір поінтера
class Slider:                        
    def __init__(self,x,y,w,h,max_num,col_slider,col_pointer):
        self.max_num = max_num

        # зберіхи у властивість максимальне значення повзунка
        
        # створи прямокутник основи повзунка - координати та розмір із конструктора
        self.slider = pygame.Rect(x,y,w,h)
        # створи повзунок (кнопкуб поінтер): 
        # х такий самийб у - половина висоти слайдера 
        # вистоа, ширина(квадрат) - висота слайдера*2
        self.pointer = pygame.Rect(x,y-h//2,h*2,h*2)

        # встанови початкову позицію центра повзунка по X 
        self.pointer.centerx = x
        self.col_pointer = col_pointer
        self.col_slider = col_slider

        # задай колір основи
     
        # задай колір повзунка
       
        # встанови початкове значення (0) сладйера
        self.value = 0
        # створи прапорець перетягування (спочатку False)
        self.draging = False
        # створи змінну для зсуву миші
        self.offset_x = 0
        # запам’ятай початок повзунка х
        self.start_x = x
        # запам’ятай кінець повзунка: х + ширина слайдера
        self.end_x = x + w
        # створи шрифт для відображення значення розмір шрифта=вистоа слайдера
        self.font = pygame.font.Font(None,h*2)
        # одразу виклич метод для оновлення даних тексту сладйера, його значення
        self.update_value()

    def draw(self, screen):
        # намалюй основу повзунка
        pygame.draw.rect(screen,self.col_slider,self.slider,border_radius=10)
        # додай рамку
        pygame.draw.rect(screen,BLACK,self.slider,border_radius=10,width=5)
        # намалюй сам повзунок
        pygame.draw.rect(screen,self.col_pointer,self.pointer,border_radius=10)
        # додай рамку повзунка
        pygame.draw.rect(screen,BLACK,self.slider,border_radius=10,width=10)
        
        # обчисли позицію тексту по X : 
        #х.поінтера + ширина повзунка // 2.6
        x = self.pointer.x + self.pointer.w//2.6
        # обчисли позицію тексту по Y : 
        #у.поінтера + ширина повзунка // 3
        y = self.pointer.y + self.pointer.w//3
        # виведи текст значення на екран
        screen.blit(self.txt,(x,y))
   

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
                self.offset_x = self.pointer.x - pos[0]
        # перевіремо подію мишка  не натиснута
        if event.type == pygame.MOUSEBUTTONUP:
            self.draging = False
        
            # вимкни режим перетягування

        # перевіремо подію мишка рухається
        if event.type == pygame.MOUSEMOTION:

            # обчисли нову позицію по X: 
            # зсув миші + х.миші
            newx = self.offset_x + event.pos[0]       
            # перевір межі руху та якщо режим перетягуванн:
            #нова позиція миші більша за початкову та менша за кінцеву
            if newx > self.start_x and newx < self.end_x:

                # перемісти повзунок: ценрт_х = новий х
                self.pointer.centerx = newx   
                # онови значення  = викликати метод
                self.update_value()       
    def update_value(self):
        # знайди значення повзунка:
        #координати х поінтера повзунка - стартове значення(стартова координата)
        newx = self.pointerx - self.start_x
        # переведи  у значення: 
        self.value = newx/ self.slider.w
        # знайдене значення ділимо на ширину слайдера та множимо на максимальне значення слайдера
        #округлити значення
        
        
        # створити текст значення
        self.txt = self.font.render(self.value,True,BLACK)
