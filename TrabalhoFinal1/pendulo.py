import pygame                  
import math                     
import time
from aeropendulo import saida # import tempo e posição de aeropendulo.py
 


pygame.init()

clock = pygame.time.Clock()
closed = False

width, height = (1000, 600) # largura e altura
window = pygame.display.set_mode((width, height)) # ajustando a janela da simulação
pygame.display.set_caption('Simulação Aeropêndulo') # mudando o nome da janela na simulação

ang = 0
user_text = ''

class massa(): # aeropêndulo
    def __init__(self):
        self.tempo, self.xx = saida(ang) # chamada de código aeropêndulo -> tempo, posição do aeropêndulo
    def draw(self, bg, i):
        self.x = round(width/2 + 300*math.sin(self.xx[0, i]))
        self.y = round(300*math.cos(self.xx[0, i]))
        for j in range(25, width, 25): # grid
            pygame.draw.lines(bg, 'blue', False, [(j, 0), (j, height)])
        for w in range(25, height, 25): # grid
            pygame.draw.lines(bg, 'blue', False, [(0, w), (width, w)])
        
        pygame.draw.lines(bg, (0, 0, 0), False, [(width/2,0), (self.x, self.y)], 4)
        pygame.draw.circle(bg, (0, 0, 0), (self.x, self.y), 25)
        pygame.draw.circle(bg, (255, 255, 255), (self.x, self.y), 23)
        pygame.draw.circle(bg, (160, 50, 50), (self.x, self.y), 10)

    def check (self,ang):
        self.tempo, self.xx =  saida(ang)   

# white = (255, 255, 255)
# blue = (0, 0, 255)
# red = (255, 0, 0)
# green = (0, 255, 0)

i = 0
haste = massa()

while not closed: 
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closed = True 
        if event.type == pygame.KEYDOWN:
            print(user_text)
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                user_text = ''
                
                ang = 0 

            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode 
                try:
                    ang = int(user_text)
                    haste.check(ang)
                except ValueError:
                    ang = 30   

    window.fill((255, 255, 255))
    haste.draw(window, i)
    i = i + 1
    
    pygame.display.update()

pygame.quit()