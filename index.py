import pygame
from pygame.locals import *

reloj = pygame.time.Clock()
pygame.init();

ventana = pygame.display.set_mode((1280,720));
pygame.display.set_caption("Magic with Luna");
fontTitle = pygame.font.SysFont("Freestyle Script",68)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:

        ventana.fill((0,0,0))
        draw_text("Magic with Luna", fontTitle , (255,255,255) , ventana, 440, 20)

        botonIniciar = pygame.Rect(50, 100 , 200, 50)
        botonSalir = pygame.Rect(50, 100 , 200, 50)
        pygame.draw.rect(ventana, (255,0,0), botonIniciar)
        pygame.draw.rect(ventana, (255,0,0), botonSalir)

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
            
            if evento.type == K_ESCAPE:
                pygame.quit()
        pygame.display.update();
        reloj.tick(60);
        
main_menu()