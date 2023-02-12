# #set display
# display_width = 960
# display_height = 640
# display=pygame.display.set_mode(display_width,display_height)
# pygame.display.set_caption("Let's make a platform game!")

# #Set game clock
# FPS = 60
# clock = pygame.time.Clock(FPS)

# #Set images

import pygame, os
os.chdir("D:\Python Files\App Proj")
print(os.getcwd())

pygame.init()

#set display
display_w = 500
diplay_h = 500
display = pygame.display.set_mode((500,500))
pygame.display.set_caption("WHaT?? It's a Calculator!")

#set assets

#Definitions
k=0
m=0
m2={1:"+",2:"-",3:"*",4:"/"}
n=''

#Set fonts
Roboto = pygame.font.SysFont("bold", 50)


main_button_group = pygame.sprite.Group()
string_group = pygame.sprite.Group()

class button(pygame.sprite.Sprite):
    def __init__ (self, x, y, operation, num=None):
        super().__init__()
        self.num = num
        if operation == "num":
            self.image = pygame.image.load("button.png")
        elif operation == "operator":
            self.image = pygame.image.load("gray.png")
        elif operation == "equal_sign":
            self.image = pygame.image.load("orange.png")

        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        main_button_group.add(self)        

    def update(self):
        self.add_string()

    def add_string(self):
        button_num = Roboto.render(f"{self.num}",True,(0,0,0))
        button_num_rect = button_num.get_rect()
        button_num_rect.center = (self.rect.center)
        # string_group.add(button_num)
        display.blit(button_num, button_num_rect)
    
        

calculator_map = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,2,2],
    [1,1,1,2,2],
    [1,1,1,0,3],
]

for i in range(len(calculator_map)):
    for j in range(len(calculator_map[i])):
        if calculator_map[i][j] == 1:
            k += 1
            button(j*100, i*100, "num",k)
        if calculator_map[i][j] == 2:
            m += 1
            print(m2[1])
            print(m2[2])
            print(m2[3])
            button(j*100, i*100, "operator",m2[m])
        if calculator_map[i][j] == 3:
            button(j*100, i*100, "equal_sign")
        
# class calculator:
#     def __init__(self,*args,operation):
#         total = 0

    
# def equation_typer(self, *args, )


#Game Engine

running = True
while running:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         if event.type == pygame.K_LEFT:
             print("helloooo")
             running = False

    display.fill((0,0,0))

    main_button_group.draw(display)
    main_button_group.update()
    # string_group.draw(display)
    pygame.display.update()

pygame.quit


