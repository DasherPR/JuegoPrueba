import pygame
from pygame.locals import *
from pygame import mixer_music , mixer

reloj = pygame.time.Clock() 
pygame.init(); #Con esto se inician los modulos de python

mixer.init(); #con esto se inicia el reproductor de musica
mixer.music.load("./src/music/ALonelyCherryTree-.wav") #aqui se carga la musica
mixer.music.set_volume(0.2) # aqui se ajusta el volumen de la musica
mixer.music.play() # con esto se reproduce la musica

ventana = pygame.display.set_mode((1280,720)); #esto define el tamaño de la pantalla
pygame.display.set_caption("Magic with Luna"); #esto pone el nombre de la ventana
fontTitle = pygame.font.SysFont("Bodoni MT",68) # esta es la fuente del titulo del juego
fuenteBotones = pygame.font.SysFont("Bahnschrift",24) # esta es la fuente para los botones
fuenteTexto = pygame.font.SysFont("Arial",20) # esta es la fuente para el texto
numContexto = 0

def accion(boton): # esta funcion permite dar diferentes funciones a los botones segun su texto
    global numContexto

    if boton == "Iniciar":
        Juego()

    if boton == "Salir":
        Salir()

    if boton == "Siguiente":
        numContexto = numContexto + 1
    
    if boton == "Creditos":
        Creditos()
    
    if boton == "Volver":
        menu()
    
    if boton == "Opcion A":
        numContexto = numContexto + 1
    
    if boton == "Opcion B":
        numContexto = numContexto + 2
    
    if boton == "Continuar":
        numContexto = numContexto + 2

class Boton(): #esta clase tuve que buscarla para facilitarme el hacer botones
	def __init__(self, image, x_pos, y_pos, text_input): #con esto se definen cosas que se le tendran que dar al objeto boton
		self.image = image #esta es la imagen que se le dara al boton
		self.x_pos = x_pos #esta esl a posicion en x del boton
		self.y_pos = y_pos #esta es la posicion en y del boton
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos)) #esto centra la imagen
		self.text_input = text_input #esto dice que sera el texto del boton
		self.text = fuenteBotones.render(self.text_input, True, "white") #esto muestra como se mostrar el texto del boton
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos)) #esto centra el texto

	def update(self): #esto permite que el boton se muestre en la ventana
		ventana.blit(self.image, self.rect)
		ventana.blit(self.text, self.text_rect)

	def checkForInput(self, position): #esto hace que cuando se presione el boton se realice la accion de abajo
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			accion(self.text_input)


def texto(text, font, color, surface, x, y): #esta funcion permite poner texto en pantalla
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def VariasLineas(surf, text, renderer, color, x, y): #esta funcion permite poner varias lineas de texto
    h = renderer.get_height()
    lineas = text.split('\n')
    for i, ll in enumerate(lineas):
        txt_surface = renderer.render(ll, True, color)
        surf.blit(txt_surface, (x, y+(i*h)))


def menu(): #esta funcion es el menu principal para el juego
    while True:
        ventana.fill((0,0,0)) #esto llena la ventana de color negro

        # Esto es para poner el fondo del menu
        fondo = pygame.image.load("./src/imagenes/fondoMenu.png") 
        fondoTam = pygame.transform.scale(fondo,(720,720)); #esto pone la imagen del tamaño necesario
        ventana.blit(fondoTam, (280, 0)) #esto muestra la imagen en la ventana

        texto("Magic with Luna", fontTitle , (255,255,255) , ventana, 420, 600) #este es el titulo del juego

        imagenBoton = pygame.image.load("./src/imagenes/Boton.png") #esta es la imagen del boton
        imagenBoton = pygame.transform.scale(imagenBoton, (200, 50)) #este es el tamaño de la imagen del boton

        botonIniciar = Boton(imagenBoton, 150, 200, "Iniciar") #este es un boton creado a partir del objeto iniciar
        botonIniciar.update() #con esto se muestra el boton en la pantalla

        botonCreditos = Boton(imagenBoton, 150,300, "Creditos")
        botonCreditos.update()

        botonSalir = Boton(imagenBoton, 150,400, "Salir")
        botonSalir.update()

        for evento in pygame.event.get(): #esto permite detectar que eventos ocurren
            if evento.type == QUIT: #cuando se cierre el juego se detiene pygame
                pygame.quit()
            
            if evento.type == K_ESCAPE: 
                pygame.quit()
            
            if evento.type == MOUSEBUTTONDOWN: #cuando se presiona se verifica que boton fue pulsado
                botonIniciar.checkForInput(pygame.mouse.get_pos())
                botonSalir.checkForInput(pygame.mouse.get_pos())
                botonCreditos.checkForInput(pygame.mouse.get_pos())
            
        
        pygame.display.update(); #esto actualiza la pantalla
        reloj.tick(60); 


def Juego(): #esta es la pantalla para el juego
    running = True
    mixer.music.stop()
    mixer.init()
    mixer.music.load("./src/music/LostForest.wav")
    mixer.music.set_volume(0.01)
    mixer.music.play()
    contexto = ""
    global numContexto

        

    while running:
        imagenBoton = pygame.image.load("./src/imagenes/Boton.png")
        imagenBoton = pygame.transform.scale(imagenBoton, (200, 50))
        botonSiguiente = Boton(imagenBoton, 640, 690, "Siguiente")
        botonContinuar = Boton(imagenBoton, 640, 500, "Continuar")
        botonA = Boton(imagenBoton, 550 , 600 , "Opcion A")
        botonB = Boton(imagenBoton, 750 , 600 , "Opcion B")
        ventana.fill((0,0,0))   
        
        #todos estos if son simplemente la historia
        if numContexto == 0:
            contexto = "Despiertas en un bosque en medio de la noche, no recuerdas exactamente como llegaste. \nA tu lado puedes observar tu celular que se encuentra roto."
            VariasLineas(ventana, contexto, fuenteTexto , (255,255,255), 360, 300)
            botonSiguiente.update()
        if numContexto == 1:
            contexto = "Intentas encender tu celular, pero no funciona. \n Decides levantarte"
            VariasLineas(ventana, contexto, fuenteTexto , (255,255,255), 360, 300)
            botonSiguiente.update()
        if numContexto == 2:
            contexto = "A lo lejos ves una figura observandote"
            VariasLineas(ventana, contexto, fuenteTexto , (255,255,255), 360, 50)
            figura = pygame.image.load("./src/imagenes/figuraBosque.png") 
            figuraTam = pygame.transform.scale(figura,(640,640)); #esto pone la imagen del tamaño necesario
            ventana.blit(figuraTam, (280, 80))
            botonSiguiente.update()
        if numContexto == 3:
            contexto = "Pero al parpadear ya no esta..."
            VariasLineas(ventana, contexto, fuenteTexto , (255,255,255), 360, 50)
            figura = pygame.image.load("./src/imagenes/noFiguraBosque.png") 
            figuraTam = pygame.transform.scale(figura,(640,640)); #esto pone la imagen del tamaño necesario
            ventana.blit(figuraTam, (280, 80))
            botonSiguiente.update()
        if numContexto == 4:
            contexto = "Por lo que decides centrarte en la pregunta importante...\n¿Que haces aquí?"
            VariasLineas(ventana, contexto, fuenteTexto , (255,255,255), 360, 300)
            botonSiguiente.update()
        if numContexto == 5:
            contexto = "Observas de nuevo al suelo y te fijas de que hay algo nuevo"
            VariasLineas(ventana, contexto, fuenteTexto , (255,255,255), 360, 50)
            figura = pygame.image.load("./src/imagenes/SueloObjetos.png") 
            figuraTam = pygame.transform.scale(figura,(640,640)); #esto pone la imagen del tamaño necesario
            ventana.blit(figuraTam, (280, 80))
            botonSiguiente.update()
        if numContexto == 6:
            contexto = "Tomaste el palo en tus manos, ¡resulta que es una varita!"
            VariasLineas(ventana, contexto, fuenteTexto , (255,255,255), 360, 50)
            figura = pygame.image.load("./src/imagenes/varitaManos.png") 
            figuraTam = pygame.transform.scale(figura,(640,640)); #esto pone la imagen del tamaño necesario
            ventana.blit(figuraTam, (280, 80))
            botonSiguiente.update()
        if numContexto == 7:
            contexto = "¿Sera que podras hacer magia?\nA) La magia no existe, no lo intentes\nB) Intentar hacer Magia"
            VariasLineas(ventana, contexto, fuenteTexto , (255,255,255), 360, 360)
            botonA.update()
            botonB.update()
        if numContexto == 8:
            contexto = "Si... supongo que no tiene sentido intentarlo\nGuardas la varita"
            VariasLineas(ventana, contexto, fuenteTexto , (255,255,255), 360, 50)
            botonContinuar.update()
        if numContexto == 9: #Esta es la opcion A
            contexto = "¡Funciona! Parece que puedes hacer magia... \npero seria mejor estudiar antes de herir a alguien"
            VariasLineas(ventana, contexto, fuenteTexto , (255,255,255), 360, 50)
            botonSiguiente.update()
        
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                running = False
                
            if evento.type == K_ESCAPE:
                running = False
                pygame.quit()

            if evento.type == MOUSEBUTTONDOWN:
                botonSiguiente.checkForInput(pygame.mouse.get_pos())
                botonContinuar.checkForInput(pygame.mouse.get_pos())
                botonA.checkForInput(pygame.mouse.get_pos())
                botonB.checkForInput(pygame.mouse.get_pos())
                #numContexto = numContexto + 1 | en una version anterior se cambiaba con solo el clic del mouse,p or lo que tuve que moverlo de ahi
            
        pygame.display.update();
        reloj.tick(60);

def Salir(): #con esto si se le da al boton salir se cierra el juego
    pygame.quit()

def Creditos(): #aqui creditos por recursos que uso y no son mios
    running = True
    while running:
        ventana.fill((0,0,0))
        CreditosL = "A Lonely Cherry - Pix\nLost Forest - kamera ♪"
        VariasLineas(ventana, CreditosL, fuenteTexto , (255,255,255), 640, 300)


        imagenBoton = pygame.image.load("./src/imagenes/Boton.png") #esta es la imagen del boton
        imagenBoton = pygame.transform.scale(imagenBoton, (200, 50))
        botonVolver = Boton(imagenBoton, 360,690, "Volver")
        botonVolver.update()

        for evento in pygame.event.get():
            if evento.type == MOUSEBUTTONDOWN:
                botonVolver.checkForInput(pygame.mouse.get_pos())
            
            if evento.type == QUIT:
                pygame.quit()

        pygame.display.update();
        reloj.tick(60);
menu() #esto permite que se muestre el menu principal al iniciar el programa.