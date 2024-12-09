import pygame
import sys

# Inicialización del módulo pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 700
pantalla = pygame.display.set_mode([ANCHO, ALTO])
pygame.display.set_caption('Juego de Ajedrez')

# Fuentes
fuente = pygame.font.Font('freesansbold.ttf', 16)
fuente_mediana = pygame.font.Font('freesansbold.ttf', 24)
fuente_grande = pygame.font.Font('freesansbold.ttf', 32)
fuente_titulo = pygame.font.Font('freesansbold.ttf', 48)

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)
DORADO = (255, 215, 0)

# Cargar imagen de fondo
fondo = pygame.image.load('img/fondo.jpg')
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Variables del juego
temporizador = pygame.time.Clock()
fps = 60

piezas_blancas = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
ubicaciones_blancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                     (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
piezas_negras = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
               'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
ubicaciones_negras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

piezas_capturadas_blancas = []
piezas_capturadas_negras = []

paso_turno = 0
seleccion = 100
movimientos_validos = []

# Cargar imágenes de las piezas
reina_negra = pygame.image.load('img/B_Queen.png')
reina_negra = pygame.transform.scale(reina_negra, (60, 60))
reina_negra_pequena = pygame.transform.scale(reina_negra, (35, 35))

rey_negro = pygame.image.load('img/B_King.png')
rey_negro = pygame.transform.scale(rey_negro, (60, 60))
rey_negro_pequeno = pygame.transform.scale(rey_negro, (35, 35))

torre_negra = pygame.image.load('img/B_Rook.png')
torre_negra = pygame.transform.scale(torre_negra, (60, 60))
torre_negra_pequena = pygame.transform.scale(torre_negra, (35, 35))

alfil_negro = pygame.image.load('img/B_Bishop.png')
alfil_negro = pygame.transform.scale(alfil_negro, (60, 60))
alfil_negro_pequeno = pygame.transform.scale(alfil_negro, (35, 35))

caballo_negro = pygame.image.load('img/B_Knight.png')
caballo_negro = pygame.transform.scale(caballo_negro, (60, 60))
caballo_negro_pequeno = pygame.transform.scale(caballo_negro, (35, 35))

peon_negro = pygame.image.load('img/B_Pawn.png')
peon_negro = pygame.transform.scale(peon_negro, (50, 50))
peon_negro_pequeno = pygame.transform.scale(peon_negro, (35, 35))

reina_blanca = pygame.image.load('img/W_Queen.png')
reina_blanca = pygame.transform.scale(reina_blanca, (60, 60))
reina_blanca_pequena = pygame.transform.scale(reina_blanca, (35, 35))

rey_blanco = pygame.image.load('img/W_King.png')
rey_blanco = pygame.transform.scale(rey_blanco, (60, 60))
rey_blanco_pequeno = pygame.transform.scale(rey_blanco, (35, 35))

torre_blanca = pygame.image.load('img/W_Rook.png')
torre_blanca = pygame.transform.scale(torre_blanca, (60, 60))
torre_blanca_pequena = pygame.transform.scale(torre_blanca, (35, 35))

alfil_blanco = pygame.image.load('img/W_Bishop.png')
alfil_blanco = pygame.transform.scale(alfil_blanco, (60, 60))
alfil_blanco_pequeno = pygame.transform.scale(alfil_blanco, (35, 35))

caballo_blanco = pygame.image.load('img/W_Knight.png')
caballo_blanco = pygame.transform.scale(caballo_blanco, (60, 60))
caballo_blanco_pequeno = pygame.transform.scale(caballo_blanco, (35, 35))

peon_blanco = pygame.image.load('img/W_Pawn.png')
peon_blanco = pygame.transform.scale(peon_blanco, (50, 50))
peon_blanco_pequeno = pygame.transform.scale(peon_blanco, (35, 35))

imagenes_blancas = [peon_blanco, reina_blanca, rey_blanco,
                  caballo_blanco, torre_blanca, alfil_blanco]
imagenes_blancas_pequenas = [peon_blanco_pequeno, reina_blanca_pequena, rey_blanco_pequeno,
                           caballo_blanco_pequeno, torre_blanca_pequena, alfil_blanco_pequeno]

imagenes_negras = [peon_negro, reina_negra, rey_negro,
                 caballo_negro, torre_negra, alfil_negro]
imagenes_negras_pequenas = [peon_negro_pequeno, reina_negra_pequena, rey_negro_pequeno,
                          caballo_negro_pequeno, torre_negra_pequena, alfil_negro_pequeno]

lista_piezas = ['peon', 'reina', 'rey', 'caballo', 'torre', 'alfil']

# Variables de verificación / contador de parpadeo
contador = 0
ganador = ''
juego_terminado = False

# Función para crear botones
def crear_boton(x, y, ancho, alto, texto, color, color_hover, accion=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + ancho and y < mouse[1] < y + alto:
        pygame.draw.rect(pantalla, color_hover, (x, y, ancho, alto), border_radius=10)
        if click[0] == 1 and accion is not None:
            accion()
    else:
        pygame.draw.rect(pantalla, color, (x, y, ancho, alto), border_radius=10)

    texto_render = fuente_mediana.render(texto, True, NEGRO)
    texto_rect = texto_render.get_rect(center=(x + ancho/2, y + alto/2))
    pantalla.blit(texto_render, texto_rect)

# Función para mostrar el menú principal
def menu_principal():
    ejecutar_menu = True
    while ejecutar_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pantalla.blit(fondo, (0, 0))

        titulo = fuente_titulo.render("Ajedrez", True, BLANCO)
        pantalla.blit(titulo, (ANCHO/2 - titulo.get_width()/2, 50))

        crear_boton(ANCHO/2 - 100, 200, 200, 50, "Nueva Partida", DORADO, (255, 235, 100), iniciar_juego)
        crear_boton(ANCHO/2 - 100, 300, 200, 50, "Reglas", DORADO, (255, 235, 100), mostrar_reglas)
        crear_boton(ANCHO/2 - 100, 400, 200, 50, "Salir", DORADO, (255, 235, 100), salir_juego)

        pygame.display.flip()
        temporizador.tick(fps)

# Función para iniciar el juego
def iniciar_juego():
    global juego_terminado, ganador
    juego_terminado = False
    ganador = ''
    bucle_principal_juego()

# Función para mostrar las reglas
def mostrar_reglas():
    ejecutar_reglas = True
    while ejecutar_reglas:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    ejecutar_reglas = False

        pantalla.blit(fondo, (0, 0))

        titulo = fuente_grande.render("Reglas del Ajedrez", True, BLANCO)
        pantalla.blit(titulo, (ANCHO/2 - titulo.get_width()/2, 50))

        reglas = [
            "1. El ajedrez se juega entre dos jugadores.",
            "2. Cada jugador tiene 16 piezas al inicio.",
            "3. El objetivo es dar jaque mate al rey oponente.",
            "4. Las piezas se mueven de manera específica:",
            "   - Rey: Una casilla en cualquier dirección",
            "   - Reina: Cualquier número de casillas en línea recta",
            "   - Torre: Horizontal y verticalmente",
            "   - Alfil: Diagonalmente",
            "   - Caballo: En forma de 'L'",
            "   - Peón: Avanza una casilla hacia adelante",
            "5. El juego termina en jaque mate o empate.",
            "",
            "Presiona ESC para volver al menú principal"
        ]

        for i, regla in enumerate(reglas):
            texto = fuente.render(regla, True, BLANCO)
            pantalla.blit(texto, (50, 120 + i * 30))

        pygame.display.flip()
        temporizador.tick(fps)

# Función para salir del juego
def salir_juego():
    pygame.quit()
    sys.exit()

# Función para dibujar el tablero principal del juego
def dibujar_tablero():
    for i in range(32):
        columna = i % 4
        fila = i // 4
        if fila % 2 == 0:
            pygame.draw.rect(pantalla, (211, 211, 211), [
                           480 - (columna * 160), fila * 80, 80, 80])
        else:
            pygame.draw.rect(pantalla, (211, 211, 211), [
                           560 - (columna * 160), fila * 80, 80, 80])
    pygame.draw.rect(pantalla, GRIS, [0, 640, ANCHO, 60])
    pygame.draw.rect(pantalla, DORADO, [0, 640, ANCHO, 60], 5)
    pygame.draw.rect(pantalla, DORADO, [640, 0, 160, ALTO], 5)
    textos_estado = ['Blancas: ¡Selecciona una pieza para mover!', 'Blancas: ¡Selecciona un destino!',
                   'Negras: ¡Selecciona una pieza para mover!', 'Negras: ¡Selecciona un destino!']
    pantalla.blit(fuente_mediana.render(
        textos_estado[paso_turno], True, NEGRO), (20, 660))
    for i in range(9):
        pygame.draw.line(pantalla, NEGRO, (0, 80 * i), (640, 80 * i), 2)
        pygame.draw.line(pantalla, NEGRO, (80 * i, 0), (80 * i, 640), 2)
    pantalla.blit(fuente.render('RENDIRSE', True, NEGRO), (650, 660))

# Función para dibujar las piezas en el tablero
def dibujar_piezas():
    for i in range(len(piezas_blancas)):
        indice = lista_piezas.index(piezas_blancas[i])
        x = ubicaciones_blancas[i][0] * 80
        y = ubicaciones_blancas[i][1] * 80
        if piezas_blancas[i] == 'peon':
            pantalla.blit(peon_blanco, (x + 15, y + 20))
        else:
            pantalla.blit(imagenes_blancas[indice], (x + 10, y + 10))
        if paso_turno < 2 and seleccion == i:
            pygame.draw.rect(pantalla, (255, 0, 0), [x + 1, y + 1, 80, 80], 2)

    for i in range(len(piezas_negras)):
        indice = lista_piezas.index(piezas_negras[i])
        x = ubicaciones_negras[i][0] * 80
        y = ubicaciones_negras[i][1] * 80
        if piezas_negras[i] == 'peon':
            pantalla.blit(peon_negro, (x + 15, y + 20))
        else:
            pantalla.blit(imagenes_negras[indice], (x + 10, y + 10))
        if paso_turno >= 2 and seleccion == i:
            pygame.draw.rect(pantalla, (0, 0, 255), [x + 1, y + 1, 80, 80], 2)

# Función para verificar todas las opciones válidas de las piezas en el tablero
def verificar_opciones(piezas, ubicaciones, turno):
    lista_movimientos = []
    lista_todos_movimientos = []
    for i in range((len(piezas))):
        ubicacion = ubicaciones[i]
        pieza = piezas[i]
        if pieza == 'peon':
            lista_movimientos = verificar_peon(ubicacion, turno)
        elif pieza == 'torre':
            lista_movimientos = verificar_torre(ubicacion, turno)
        elif pieza == 'caballo':
            lista_movimientos = verificar_caballo(ubicacion, turno)
        elif pieza == 'alfil':
            lista_movimientos = verificar_alfil(ubicacion, turno)
        elif pieza == 'reina':
            lista_movimientos = verificar_reina(ubicacion, turno)
        elif pieza == 'rey':
            lista_movimientos = verificar_rey(ubicacion, turno)
        lista_todos_movimientos.append(lista_movimientos)
    return lista_todos_movimientos

# Verificar movimientos válidos del rey
def verificar_rey(posicion, color):
    lista_movimientos = []
    if color == 'blancas':
        lista_enemigos = ubicaciones_negras
        lista_amigos = ubicaciones_blancas
    else:
        lista_amigos = ubicaciones_negras
        lista_enemigos = ubicaciones_blancas
    # 8 casillas para verificar para los reyes, pueden ir una casilla en cualquier dirección
    objetivos = [(1, 0), (1, 1), (1, -1), (-1, 0),
               (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        objetivo = (posicion[0] + objetivos[i][0], posicion[1] + objetivos[i][1])
        if objetivo not in lista_amigos and 0 <= objetivo[0] <= 7 and 0 <= objetivo[1] <= 7:
            lista_movimientos.append(objetivo)
    return lista_movimientos

# Verificar movimientos válidos de la reina
def verificar_reina(posicion, color):
    lista_movimientos = verificar_alfil(posicion, color)
    segunda_lista = verificar_torre(posicion, color)
    for i in range(len(segunda_lista)):
        lista_movimientos.append(segunda_lista[i])
    return lista_movimientos

# Verificar movimientos del alfil
def verificar_alfil(posicion, color):
    lista_movimientos = []
    if color == 'blancas':
        lista_enemigos = ubicaciones_negras
        lista_amigos = ubicaciones_blancas
    else:
        lista_amigos = ubicaciones_negras
        lista_enemigos = ubicaciones_blancas
    for i in range(4):  # arriba-derecha, arriba-izquierda, abajo-derecha, abajo-izquierda
        camino = True
        cadena = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while camino:
            if (posicion[0] + (cadena * x), posicion[1] + (cadena * y)) not in lista_amigos and \
                    0 <= posicion[0] + (cadena * x) <= 7 and 0 <= posicion[1] + (cadena * y) <= 7:
                lista_movimientos.append(
                    (posicion[0] + (cadena * x), posicion[1] + (cadena * y)))
                if (posicion[0] + (cadena * x), posicion[1] + (cadena * y)) in lista_enemigos:
                    camino = False
                cadena += 1
            else:
                camino = False
    return lista_movimientos

# Verificar movimientos de la torre
def verificar_torre(posicion, color):
    lista_movimientos = []
    if color == 'blancas':
        lista_enemigos = ubicaciones_negras
        lista_amigos = ubicaciones_blancas
    else:
        lista_amigos = ubicaciones_negras
        lista_enemigos = ubicaciones_blancas
    for i in range(4):  # abajo, arriba, derecha, izquierda
        camino = True
        cadena = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while camino:
            if (posicion[0] + (cadena * x), posicion[1] + (cadena * y)) not in lista_amigos and \
                    0 <= posicion[0] + (cadena * x) <= 7 and 0 <= posicion[1] + (cadena * y) <= 7:
                lista_movimientos.append(
                    (posicion[0] + (cadena * x), posicion[1] + (cadena * y)))
                if (posicion[0] + (cadena * x), posicion[1] + (cadena * y)) in lista_enemigos:
                    camino = False
                cadena += 1
            else:
                camino = False
    return lista_movimientos

# Verificar movimientos válidos del peón
def verificar_peon(posicion, color):
    lista_movimientos = []
    if color == 'blancas':
        if (posicion[0], posicion[1] + 1) not in ubicaciones_blancas and \
                (posicion[0], posicion[1] + 1) not in ubicaciones_negras and posicion[1] < 7:
            lista_movimientos.append((posicion[0], posicion[1] + 1))
        if (posicion[0], posicion[1] + 2) not in ubicaciones_blancas and \
                (posicion[0], posicion[1] + 2) not in ubicaciones_negras and posicion[1] == 1:
            lista_movimientos.append((posicion[0], posicion[1] + 2))
        if (posicion[0] + 1, posicion[1] + 1) in ubicaciones_negras:
            lista_movimientos.append((posicion[0] + 1, posicion[1] + 1))
        if (posicion[0] - 1, posicion[1] + 1) in ubicaciones_negras:
            lista_movimientos.append((posicion[0] - 1, posicion[1] + 1))
    else:
        if (posicion[0], posicion[1] - 1) not in ubicaciones_blancas and \
                (posicion[0], posicion[1] - 1) not in ubicaciones_negras and posicion[1] > 0:
            lista_movimientos.append((posicion[0], posicion[1] - 1))
        if (posicion[0], posicion[1] - 2) not in ubicaciones_blancas and \
                (posicion[0], posicion[1] - 2) not in ubicaciones_negras and posicion[1] == 6:
            lista_movimientos.append((posicion[0], posicion[1] - 2))
        if (posicion[0] + 1, posicion[1] - 1) in ubicaciones_blancas:
            lista_movimientos.append((posicion[0] + 1, posicion[1] - 1))
        if (posicion[0] - 1, posicion[1] - 1) in ubicaciones_blancas:
            lista_movimientos.append((posicion[0] - 1, posicion[1] - 1))
    return lista_movimientos

# Verificar movimientos válidos del caballo
def verificar_caballo(posicion, color):
    lista_movimientos = []
    if color == 'blancas':
        lista_enemigos = ubicaciones_negras
        lista_amigos = ubicaciones_blancas
    else:
        lista_amigos = ubicaciones_negras
        lista_enemigos = ubicaciones_blancas
    # 8 casillas para verificar para caballos, pueden ir dos casillas en una dirección y una en otra
    objetivos = [(1, 2), (1, -2), (2, 1), (2, -1),
               (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        objetivo = (posicion[0] + objetivos[i][0], posicion[1] + objetivos[i][1])
        if objetivo not in lista_amigos and 0 <= objetivo[0] <= 7 and 0 <= objetivo[1] <= 7:
            lista_movimientos.append(objetivo)
    return lista_movimientos

# Verificar movimientos válidos para la pieza seleccionada
def verificar_movimientos_validos():
    if paso_turno < 2:
        lista_opciones = opciones_blancas
    else:
        lista_opciones = opciones_negras
    opciones_validas = lista_opciones[seleccion]
    return opciones_validas

# Dibujar movimientos válidos en la pantalla
def dibujar_validos(movimientos):
    if paso_turno < 2:
        color = (255, 0, 0)
    else:
        color = (0, 0, 255)
    for i in range(len(movimientos)):
        pygame.draw.circle(
            pantalla, color, (movimientos[i][0] * 80 + 40, movimientos[i][1] * 80 + 40), 5)

# Dibujar piezas capturadas al lado de la pantalla
def dibujar_capturadas():
    for i in range(len(piezas_capturadas_blancas)):
        pieza_capturada = piezas_capturadas_blancas[i]
        indice = lista_piezas.index(pieza_capturada)
        pantalla.blit(imagenes_negras_pequenas[indice], (660, 5 + 40 * i))
    for i in range(len(piezas_capturadas_negras)):
        pieza_capturada = piezas_capturadas_negras[i]
        indice = lista_piezas.index(pieza_capturada)
        pantalla.blit(imagenes_blancas_pequenas[indice], (740, 5 + 40 * i))

# Dibujar un cuadrado parpadeante alrededor del rey si está en jaque
def dibujar_jaque():
    if paso_turno < 2:
        if 'rey' in piezas_blancas:
            indice_rey = piezas_blancas.index('rey')
            ubicacion_rey = ubicaciones_blancas[indice_rey]
            for i in range(len(opciones_negras)):
                if ubicacion_rey in opciones_negras[i]:
                    if contador < 15:
                        pygame.draw.rect(pantalla, (139, 0, 0), [ubicaciones_blancas[indice_rey][0] * 80 + 1,
                                                              ubicaciones_blancas[indice_rey][1] * 80 + 1, 80, 80], 5)
    else:
        if 'rey' in piezas_negras:
            indice_rey = piezas_negras.index('rey')
            ubicacion_rey = ubicaciones_negras[indice_rey]
            for i in range(len(opciones_blancas)):
                if ubicacion_rey in opciones_blancas[i]:
                    if contador < 15:
                        pygame.draw.rect(pantalla, (0, 0, 139), [ubicaciones_negras[indice_rey][0] * 80 + 1,
                                                               ubicaciones_negras[indice_rey][1] * 80 + 1, 80, 80], 5)

def dibujar_juego_terminado():
    pygame.draw.rect(pantalla, NEGRO, [160, 200, 320, 70])
    pantalla.blit(fuente.render(
        f'¡{ganador} ganó el juego!', True, BLANCO), (170, 210))
    pantalla.blit(fuente.render(f'Presiona ENTER para Reiniciar!',
                            True, BLANCO), (170, 240))

# Bucle principal del juego
def bucle_principal_juego():
    global paso_turno, seleccion, movimientos_validos, ganador, juego_terminado, contador
    global piezas_blancas, ubicaciones_blancas, piezas_negras, ubicaciones_negras
    global piezas_capturadas_blancas, piezas_capturadas_negras, opciones_negras, opciones_blancas

    opciones_negras = verificar_opciones(piezas_negras, ubicaciones_negras, 'negras')
    opciones_blancas = verificar_opciones(piezas_blancas, ubicaciones_blancas, 'blancas')
    
    ejecutar = True
    while ejecutar:
        temporizador.tick(fps)
        if contador < 30:
            contador += 1
        else:
            contador = 0
        pantalla.fill((64, 64, 64))  # Gris oscuro
        dibujar_tablero()
        dibujar_piezas()
        dibujar_capturadas()
        dibujar_jaque()
        if seleccion != 100:
            movimientos_validos = verificar_movimientos_validos()
            dibujar_validos(movimientos_validos)

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutar = False
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not juego_terminado:
                x_coord = evento.pos[0] // 80
                y_coord = evento.pos[1] // 80
                coordenadas_click = (x_coord, y_coord)
                if paso_turno <= 1:
                    if coordenadas_click == (8, 8) or coordenadas_click == (9, 8):
                        ganador = 'negras'
                    if coordenadas_click in ubicaciones_blancas:
                        seleccion = ubicaciones_blancas.index(coordenadas_click)
                        if paso_turno == 0:
                            paso_turno = 1
                    if coordenadas_click in movimientos_validos and seleccion != 100:
                        ubicaciones_blancas[seleccion] = coordenadas_click
                        if coordenadas_click in ubicaciones_negras:
                            pieza_negra = ubicaciones_negras.index(coordenadas_click)
                            piezas_capturadas_blancas.append(piezas_negras[pieza_negra])
                            if piezas_negras[pieza_negra] == 'rey':
                                ganador = 'blancas'
                            piezas_negras.pop(pieza_negra)
                            ubicaciones_negras.pop(pieza_negra)
                        opciones_negras = verificar_opciones(
                            piezas_negras, ubicaciones_negras, 'negras')
                        opciones_blancas = verificar_opciones(
                            piezas_blancas, ubicaciones_blancas, 'blancas')
                        paso_turno = 2
                        seleccion = 100
                        movimientos_validos = []
                if paso_turno > 1:
                    if coordenadas_click == (8, 8) or coordenadas_click == (9, 8):
                        ganador = 'blancas'
                    if coordenadas_click in ubicaciones_negras:
                        seleccion = ubicaciones_negras.index(coordenadas_click)
                        if paso_turno == 2:
                            paso_turno = 3
                    if coordenadas_click in movimientos_validos and seleccion != 100:
                        ubicaciones_negras[seleccion] = coordenadas_click
                        if coordenadas_click in ubicaciones_blancas:
                            pieza_blanca = ubicaciones_blancas.index(coordenadas_click)
                            piezas_capturadas_negras.append(piezas_blancas[pieza_blanca])
                            if piezas_blancas[pieza_blanca] == 'rey':
                                ganador = 'negras'
                            piezas_blancas.pop(pieza_blanca)
                            ubicaciones_blancas.pop(pieza_blanca)
                        opciones_negras = verificar_opciones(
                            piezas_negras, ubicaciones_negras, 'negras')
                        opciones_blancas = verificar_opciones(
                            piezas_blancas, ubicaciones_blancas, 'blancas')
                        paso_turno = 0
                        seleccion = 100
                        movimientos_validos = []

            if evento.type == pygame.KEYDOWN and juego_terminado:
                if evento.key == pygame.K_RETURN:
                    juego_terminado = False
                    ganador = ''
                    piezas_blancas = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                                      'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
                    ubicaciones_blancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                           (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                    piezas_negras = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                                     'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
                    ubicaciones_negras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                          (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                    piezas_capturadas_blancas = []
                    piezas_capturadas_negras = []
                    paso_turno = 0
                    seleccion = 100
                    movimientos_validos = []
                    opciones_negras = verificar_opciones(
                        piezas_negras, ubicaciones_negras, 'negras')
                    opciones_blancas = verificar_opciones(
                        piezas_blancas, ubicaciones_blancas, 'blancas')

        if ganador != '':
            juego_terminado = True
            dibujar_juego_terminado()

        pygame.display.flip()

    pygame.quit()

# Iniciar el menú principal
menu_principal()

