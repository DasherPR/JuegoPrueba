import pygame
from pygame.locals import *
from pygame import mixer_music , mixer

reloj = pygame.time.Clock()
pygame.init();

mixer.init();
mixer.music.load("./src/music/ALonelyCherryTree-.wav")
mixer.music.set_volume(0.5)
mixer.music.play()

ventana = pygame.display.set_mode((1280,720));
pygame.display.set_caption("Magic with Luna");
fontTitle = pygame.font.SysFont("Bodoni MT",68)
fuenteBotones = pygame.font.SysFont("Bahnschrift",24)

def texto(text, font, color, surface, x, y): #esta funcion permite poner texto en pantalla
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def menu():
    while True:
        ventana.fill((0,0,0))

        # Esto es para poner el fondo del menu
        fondo = pygame.image.load("./src/imagenes/fondoMenu.png")
        fondoTam = pygame.transform.scale(fondo,(720,720)); #esto pone la imagen del tamaño necesario
        ventana.blit(fondoTam, (280, 0))

        texto("Magic with Luna", fontTitle , (255,255,255) , ventana, 420, 600)


        mouse = pygame.mouse.get_pos(); # con esto se obtiene la posicion del mouse

        

        botonIniciar = pygame.Rect(50, 100 , 200, 50)
        textBtIni = fuenteBotones.render('Jugar', 1, (136, 255, 0))
        botonSalir = pygame.Rect(50, 200 , 200, 50)
        # botonIniciar.blit(textBtIni,(0,0))

        pygame.draw.rect(ventana, (255,0,0), botonIniciar)
        pygame.draw.rect(ventana, (255,0,0), botonSalir)

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
            
            if evento.type == K_ESCAPE:
                pygame.quit()
            
        
        pygame.display.update();
        reloj.tick(60);

        if botonIniciar.collidepoint(mouse):
            if evento.type == MOUSEBUTTONDOWN:
                if evento.button == 1:
                    Juego()
        if botonSalir.collidepoint(mouse):
            if evento.type == MOUSEBUTTONDOWN:
                if evento.button == 1:
                    Salir()
def Juego():
    running = True
    while running:
        ventana.fill((0,0,0))
        texto("Juego",fontTitle, (255,255,255) , ventana , 20, 20)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                running = False
                
            if evento.type == K_ESCAPE:
                running = False
            
        pygame.display.update();
        reloj.tick(60);

def Salir():
    pygame.quit()
            
menu()