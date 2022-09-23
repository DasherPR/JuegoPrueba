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
fuenteTexto = pygame.font.SysFont("Arial",20)

def accion(boton):
    
    if boton == "Iniciar":
        Juego()

    if boton == "Salir":
        Salir()

class Boton():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = fuenteBotones.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		ventana.blit(self.image, self.rect)
		ventana.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			accion(self.text_input)

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = fuenteBotones.render(self.text_input, True, "green")
		else:
			self.text = fuenteBotones.render(self.text_input, True, "white")



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

        imagenBoton = pygame.image.load("./src/imagenes/Boton.png")
        imagenBoton = pygame.transform.scale(imagenBoton, (200, 50))

        botonIniciar = Boton(imagenBoton, 150, 200, "Iniciar")
        botonIniciar.update()

        botonSalir = Boton(imagenBoton, 150,300, "Salir")
        botonSalir.update()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
            
            if evento.type == K_ESCAPE:
                pygame.quit()
            
            if evento.type == MOUSEBUTTONDOWN:
                botonIniciar.checkForInput(pygame.mouse.get_pos())
                botonSalir.checkForInput(pygame.mouse.get_pos())
            
        
        pygame.display.update();
        reloj.tick(60);


        
def Juego():
    running = True
    contexto = ""
    numContexto = 0
    if numContexto == 0:
        contexto = "Despiertas en un bosque en medio de la noche, no recuerdas exactamente como llegaste."
        

    while running:
        ventana.fill((0,0,0))   
        texto(contexto ,fuenteTexto, (255,255,255) , ventana , 420, 360)
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