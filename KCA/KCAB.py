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
 



start_img = pygame.image.load('startbtn.jpg').convert_alpha()
exit_img = pygame.image.load('exitbtn.jpg').convert_alpha()
back_img = pygame.image.load('KCAI.jpg')
def background(back_img):
    size = pygame.transform.scale(back_img, (1000, 600))
    screen.blit(size, (0, 0))
    
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


start_button = Button(400, 350, start_img, 2)
exit_button = Button(400, 450, exit_img, 2)

background(back_img)

run = True
while run:
    timer.tick(fps)
    if start_button.draw():
        import KCAG
    if exit_button.draw():
        run = False
        
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False

       

                    
            

    pygame.display.flip()
pygame.quit()

 

