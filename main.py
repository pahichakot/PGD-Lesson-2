#Classes for shapes
#Calling pygame library
import pygame
pygame.init()

#Set up output screen
screen = pygame.display.set_mode((800,800))
screen.fill("pink")

#Colors for rectangles - following rgb
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (107, 63, 140)

#Rectangle class
class Rectangle():
    def __init__(self, color, dimension):
        self.color = color #filled color
        self.dimension = dimension #x position, y position, width, height
        self.screen = screen #screen in which rectsngles will appear on
        
    #Draw rectangle function
    def draw_rectangle(self):
        self.draw_rect = pygame.draw.rect(self.screen, self.color, self.dimension)

#Objcts for rectangle class
r1 = Rectangle(black, (20, 20, 100, 50)) #x, y, width, height
r1.draw_rectangle() #No need to pass 'self' in function brackets

r2 = Rectangle(white, (80, 80, 50, 100))
r2.draw_rectangle()

r3 = Rectangle(red, (500, 500, 80, 80))
r3.draw_rectangle()

r4 = Rectangle(green, (700, 10, 30, 30))
r4.draw_rectangle()

r5 = Rectangle(blue, (10, 700, 30, 30))
r5.draw_rectangle()

r6 = Rectangle(yellow, (300, 200, 40, 80))
r6.draw_rectangle()

r7 = Rectangle(purple, (500, 200, 250, 70))
r7.draw_rectangle()

#Can pass color value withoug=t using rgb as well
r8 = Rectangle("orange", (200, 500, 50, 50))
r8.draw_rectangle()

#VERY IMPORTANT!!!!!!!
#Display and close window
while True:
    pygame.display.update()
    #Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()