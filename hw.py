#Classes for shapes
#Calling pygame library
import pygame
pygame.init()

#Set up output screen
screen = pygame.display.set_mode((800,800))
screen.fill("pink")

#Circle class
class Circle():
    def __init__(self, color, center, radius):
        self.color = color #filled color
        self.center = center #x position, y position, width, height
        self.radius = radius
        self.screen = screen #screen in which rectangles will appear on
        
    #Draw circle function
    def draw_circle(self):
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)

#Objcts for circle class
c1 = Circle((0, 0, 0), (500, 500), 25)
c1.draw_circle() #No need to pass 'self' in function brackets

c2 = Circle((130, 252, 121), (600, 600), 25)
c2.draw_circle()

c3 = Circle((250, 250, 250), (400, 400), 25)
c3.draw_circle()

c4 = Circle((157, 252, 193), (300, 300), 25)
c4.draw_circle()

c5 = Circle((91, 232, 245), (700, 700), 25)
c5.draw_circle()

c6 = Circle((245, 51, 51), (25, 25), 25)
c6.draw_circle()

c7 = Circle((102, 102, 242), (100, 100), 25)
c7.draw_circle()

c8 = Circle((252, 121, 248), (200, 200), 25)
c8.draw_circle()

#VERY IMPORTANT!!!!!!!
#Display and close window
while True:
    pygame.display.update()
    #Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()