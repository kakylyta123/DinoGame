import pygame
import random
pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
# меняет название дисплея
pygame.display.set_caption("Run Dino, run!")

# добовление иконки
icon = pygame.image.load("venv/img/icon.ico")
pygame.display.set_icon(icon)

#Массив кактусов
cactus_img = [pygame.image.load(r'venv/img/Cactus0.png'), pygame.image.load(r'venv/img/Cactus1.png'), pygame.image.load(
    r'venv/img/Cactus2.png')]
cactus_options = [69, 449, 37, 410, 40, 420]

#массив камушков
stone_img = [pygame.image.load(r'venv/img/Stone0.png'),
             pygame.image.load(r'venv/img/Stone1.png')]

#Массив облаков
cloud_img=[pygame.image.load(r'venv/img/Cloud0.png'),
           pygame.image.load(r'venv/img/Cloud1.png')]

#Массив нашего динозаврика (спрайты динозавра)
dino_img = [pygame.image.load(r'venv/img/Dino0.png'), pygame.image.load(r'venv/img/Dino1.png'), pygame.image.load(
    r'venv/img/Dino2.png'), pygame.image.load(r'venv/img/Dino3.png'), pygame.image.load(r'venv/img/Dino4.png')]

img_conter = 0

# класс кактс
class Object:
    def __init__(self, x, y, width, image, speed):
        # передача параметров в класс
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        # проверка на экране кактус или нет
        if self.x >= -self.width:
            display.blit(self.image, (self.x,self.y))
            #pygame.draw.rect(display, (224, 121, 31), (self.x, self.y, self.width, self.height))
            self.x -= 4
            return True
        else:
 
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y))


# высота и ширина перса
user_width = 60
user_height = 100


# кординаты персонажа
user_x = display_width // 3
user_y = display_height - user_height - 100


#параметры кактуса
cactus_width = 20
cactus_height = 70
cactus_x = display_width - 50
cactus_y =  display_height - cactus_height - 100


# переменная fps
clock = pygame.time.Clock()

make_jump = False

# точки прыжка
jump_counter = 30

def run_game():
    game = True
    global make_jump
    cactus_arr = []
    create_cactus_arr(cactus_arr)
    land = pygame.image.load(r'venv/img\fon.png')

    stone, cloud = open_random_object()




    while game == True:
        # для любого события если событие выхода то выходи
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        key = pygame.key.get_pressed()
        # клавиша дляя прыжка
        if key[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            jump()


        display.blit(land, (0,0))
        draw_array(cactus_arr)
        move_objects(stone, cloud)




        # функция рисования
        #pygame.draw.rect(display, (27,240,22) , (user_x, user_y, user_width, user_height))
        draw_dino()
        pygame.display.update()

        # ограничение кадров в секунду
        clock.tick(60)

        # функция прыжка
        def jump():
            global user_y, jump_counter,  make_jump
            if jump_counter >= -30:
                user_y -= jump_counter / 2.5
                jump_counter -= 1
            else:
                jump_counter = 30
                make_jump = False

# create 3-ых кактусов
def create_cactus_arr(array):
    choice = random.randrange(0,3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 20, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 300, height,width, img, 4))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 600 , height,width, img, 4))

# функция поиска радиуса
def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x )

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum
    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(200, 350)

    return radius

# движение кактусов
def draw_array(array):
    for cactus in array:
       check =  cactus.move()
       if not check:
            radius = find_radius(array)

            choice = random.randrange(0, 3)
            image = cactus_img[choice]
            width = cactus_options[choice * 2]
            height = cactus_options[choice * 2 + 1]

            cactus.return_self(radius, height, width, image)


#функция открытия рандомного объекта
def open_random_object():
    choice = random.randrange(0, 2)
    img_of_stone = stone_img[choice]

    choice = random.randrange(0, 2)
    img_of_cloud = cloud_img[choice]

    stone = Object(display_width, display_height - 80, 10, img_of_stone, 4)
    cloud = Object(display_width, 80, 70, img_of_cloud, 2)
    return stone, cloud

#функция движения объектов(облака, камни)
def move_objects(stone, cloud):
    check = stone.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_stone = stone_img[choice]
        stone.return_self(display_width, 500 + random.randrange(10, 80),
                          stone.width, img_of_stone)

    check = cloud.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(display_width, random.randrange(10, 200),
                            cloud.width, img_of_cloud)

def draw_dino():
    global img_conter
    if img_conter == 25:
        img_conter = 0

    display.blit(dino_img[img_conter // 5], (user_x, user_y))
    img_conter += 1


# запуск игры
run_game()