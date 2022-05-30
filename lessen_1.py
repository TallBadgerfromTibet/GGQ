# class Transport:
#
#     def __init__(self, model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color
#
#
# def change_color(self, new_color):
#     self.color = new_color
#
#
# def show(self):
#     print(f"Model: {self.model}\n"
#           f"Year: {self.year}\n"
#           f"Color: {self.color}\n")
#
#
# class Rocket(Transport):
#
#     def __init__(self, model, year, color):
#         # super().__init__(model, year, color)
#         Transport.__init__(self, model, year, color)
#
#
# class Chair:
#     def __init__(self, material, ves):
#         self.material = material
#         self.ves = ves
#
#
# class Car(Transport):  # Чертеж
#
#     wheels = 4  # Аттрибут класса
#
#     def __init__(self, model, year, color, chair, penalties=0.0):  # Конструктор
#         Transport.__init__(self, model, year, color)
#         self.penalties = penalties
#         self.chair = chair
#
#     def drive(self, city):  # Метод (Что делать?)
#         print(f"Машина {self.model}, едет в город {city}")
#
#     def show(self):
#         print(f"Model: {self.model}\n"
#               f"Year: {self.year}\n"
#               f"Color: {self.color}\n"
#               f"Penalties: {self.penalties}\n")
#
#
# def f():  # Обычная функция
#     print("hello")
#
#
# class Truck(Car):
#
#     def __init__(self, model, year, color, chair, penalties, load_capacity):
#         super().__init__(model, year, color, chair, penalties)
#         self.load_capacity = load_capacity
#
#     def load_cargo(self, product, weight):
#         if weight <= self.load_capacity:
#             print(f"Продукт {product} ({weight} kg) был успешно загружен на {self.model}")
#         else:
#             print(f"Я не резиновый! Максимальная грузоподъемность {self.load_capacity} kg")
#
#     def show(self):
#         print(f"Model: {self.model}\n"
#               f"Year: {self.year}\n"
#               f"Color: {self.color}\n"
#               f"Penalties: {self.penalties}\n"
#               f"Load capacity: {self.load_capacity}\n")
#
#
# man_truck = Truck("Man 3", 2013, "Red", Chair("Material", 20), 1500, 2000)
# man_truck.show()
# man_truck.load_cargo("Яблоко", 200)
# man_truck.drive("Tokio")
#
# # chair_for_car = Chair("Skin", 50)
# #
# # car_mers = Car("Mersedes-Benz E220", 2003, "Black", chair_for_car, 100.5)
# # car_lada = Car(model="Lada 9", year=1998, color="Red", chair=chair_for_car)
#
#
# # car_mers.show()
#
# # nasa = Rocket("Rocket M1", 2022, "White")
# # nasa.show()
#
# # car_mers.drive('Bishkek')
# # car_lada.drive("Osh")
#
#
# # print(car_mers) # Сыылка на объект
# # print(f"{car_mers.model} {car_mers.year} {car_mers.color} {car_mers.penalties} {car_mers.wheels}")
# # car_mers.color = "Blue"
# # car_mers.change_color(new_color="Red")
# # print(f"{car_mers.model} {car_mers.year} {car_mers.color} {car_mers.penalties} {car_lada.wheels}")
# # print(f"{car_lada.model} {car_lada.year} {car_lada.color} {car_lada.penalties}")
#
# # Car.wheels = 6  # Переопределиние аттрибута класса
# #
# # gelik = Car("Mers G-class", 2022, "Black", 150.0)
# # # print(f"{gelik.model} {gelik.year} {gelik.color} {gelik.penalties} {gelik.wheels}")
# # gelik.show()
# # car_lada.show()
# # car_mers.show()

# Игра Shmup - 1 часть
# Cпрайт игрока и управление
import pygame
import random

WIDTH = 480
HEIGHT = 600
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
