import pygame
pygame.init()

fps = 120
timer=pygame.time.Clock()
WIDTH = 1000
HEIGHT = 600
active_size = 0
active_colour = 'white'
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('paint')
painting = []
screen.fill('blue')

def draw_menu(size, colour):
    pygame.draw.line(screen, 'black', (700, 100), (700, HEIGHT), 3)
    pygame.draw.line(screen, 'black', (0, 100), (WIDTH, 100), 3)
    pygame.draw.line(screen, 'black', (700, 500), (WIDTH, 500), 3)
    xl_brush = pygame.draw.rect(screen, 'black', [715, 110, 50, 50])
    pygame.draw.circle(screen, 'white', (740, 135), 20)
    l_brush = pygame.draw.rect(screen, 'black', [785, 110, 50, 50])
    pygame.draw.circle(screen, 'white', (810, 135), 15)
    m_brush = pygame.draw.rect(screen, 'black', [855, 110, 50, 50])
    pygame.draw.circle(screen, 'white', (880, 135), 10)
    s_brush = pygame.draw.rect(screen, 'black', [925, 110, 50, 50])
    pygame.draw.circle(screen, 'white', (950, 135), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]
    if size == 20:
        pygame.draw.rect(screen, 'green', [715, 110, 50, 5])
    elif size == 15:
        pygame.draw.rect(screen, 'green', [785, 110, 50, 5])
    elif size == 10:
        pygame.draw.rect(screen, 'green', [855, 110, 50, 5])
    elif size == 5:
        pygame.draw.rect(screen, 'green', [925, 110, 50, 5])


    pygame.draw.circle(screen, colour, (700, 195), 15)
    pygame.draw.circle(screen, 'dark gray', (700, 195), 15, 3)

    white = pygame.draw.rect(screen, (0, 0, 0), [715, 170, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [715, 200, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [745, 170, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [745, 200, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [775, 170, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [775, 200, 25, 25])
    blue = pygame.draw.rect(screen, (0, 0, 255), [805, 170, 25, 25])
    black = pygame.draw.rect(screen, (255, 255, 255), [805, 200, 25, 25])
    orange = pygame.draw.rect(screen, (255, 100, 10), [835, 170, 25, 25])
    lime = pygame.draw.rect(screen, (180, 255, 100), [835, 200, 25, 25])
    gray = pygame.draw.rect(screen, (127, 127, 127), [865, 170, 25, 25])
    brown = pygame.draw.rect(screen, (100, 40, 0), [865, 200, 25, 25])
    pink = pygame.draw.rect(screen, (255, 100, 180), [895, 170, 25, 25])
    light_gray = pygame.draw.rect(screen, (200, 200, 200), [925, 170, 25, 25])
    dark_gray = pygame.draw.rect(screen, (50, 50, 50), [925, 200, 25, 25])
    tan = pygame.draw.rect(screen, (230, 220, 170), [955, 200, 25, 25])
    navy_blue = pygame.draw.rect(screen, (0, 0, 100), [955, 170, 25, 25])
    forest_green = pygame.draw.rect(screen, (0, 50, 0), [895, 200, 25, 25])
    colour_rect = [white, red, green, yellow, teal, purple, blue, black, orange, lime, gray, brown, pink, light_gray, dark_gray, tan, navy_blue, forest_green]
    rgb_list = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (0, 0, 255), (255, 255, 255), (255, 100, 10), (180, 255, 100), (127, 127, 127),
                (100, 40, 0), (255, 100, 180), (200, 200, 200), (50, 50, 50), (230, 220, 170), (0, 0, 100), (0, 50, 0)]
    return brush_list, colour_rect, rgb_list

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])


menu_img = pygame.image.load('menubtn.jpg').convert_alpha()
exit_img = pygame.image.load('exitbtn.jpg').convert_alpha()
draw_img = pygame.image.load('drawimg.jpg').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        


        
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


menu_button = Button(350, 35, menu_img, 1.5)
exit_button = Button(500, 35, exit_img, 1.5)

screen.blit(draw_img, (0,100))
pygame.display.update()

run = True
while run:
    timer.tick(fps)
    if menu_button.draw():
        import KCAB
    if exit_button.draw():
        run = False
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if left_click and mouse[0] < 680 and mouse[1] > 120:
        painting.append((active_colour, mouse, active_size))
    draw_painting(painting)
    if mouse[0] < 700 and mouse[1] > 100:
        pygame.draw.circle(screen, active_colour, mouse, active_size)
    brushes, colours, rgbs = draw_menu(active_size, active_colour)
   


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)

            for i in range(len(colours)):
                if colours[i].collidepoint(event.pos):
                    active_colour = rgbs[i] 


                    
            

    pygame.display.flip()
pygame.quit()

 


