from math import ceil
import random
from gl import *

glInit(width=1000, height=1000)

glColor(r=0,g=0,b=0)

def rellenarPoligono(poligono):


	# Dibujando los puntos en el framebuffer:

	for i in range(len(poligono)):

		glPoint(poligono[i][0], poligono[i][1])

		glColor(r=random.randint(0,255)/255,g=random.randint(0,255)/255,b=random.randint(0,255)/255)

	# Conectando los puntos previamente dibujados:

	puntos_dibujados = []

	for i in range(len(poligono)):

		if i == len(poligono)-1:
			coords = glLine(poligono[i][0],poligono[i][1],poligono[0][0],poligono[0][1])
			for punto in coords:
				puntos_dibujados.append(punto)

		else:
			coords = glLine(poligono[i][0],poligono[i][1],poligono[i+1][0],poligono[i+1][1])
			for punto in coords:
				puntos_dibujados.append(punto)

	# Localizando el centro de la figura:

	puntos_x = []
	puntos_y = []

	for punto in puntos_dibujados:
		puntos_x.append(punto[0])
		puntos_y.append(punto[1])

	centro_x = sum(puntos_x)/len(puntos_x)
	centro_y = sum(puntos_y)/len(puntos_y)

	glPoint(round(centro_x), round(centro_y))

	# Rellenando el poligono desde el centro:

	for punto in puntos_dibujados:

		glLine(round(punto[0]), round(punto[1]), round(centro_x), round(centro_y))

		# Eje ╗ (+1,+1)
		glLine(floor(punto[0]), floor(punto[1]), floor(centro_x) + 1, floor(centro_y) + 1)
		
		# Eje ╚ (-1,-1)

		glLine(ceil(punto[0]), ceil(punto[1]), ceil(centro_x) - 1, ceil(centro_y) - 1)
		
		# Eje ╔ (-1,+1)

		glLine(floor(punto[0]), floor(punto[1]), floor(centro_x) - 1, floor(centro_y) + 1)
		
		# Eje ╝ (+1,-1)
		
		glLine(ceil(punto[0]), ceil(punto[1]), ceil(centro_x) + 1, ceil(centro_y) - 1)

		# glColor(r=random.randint(0,255)/255,g=random.randint(0,255)/255,b=random.randint(0,255)/255)




coordenadas_estrella = [
	(165, 380),(185, 360),(180, 330),(207, 345),(233, 330),(230, 360),(250, 380),(220, 385),(205, 410),(193, 383)
]

coordenadas_cuadrado = [
	(321, 335),(288, 286),(339, 251),(374, 302)
]

coordenadas_triangulo = [
	(377, 249),(411, 197),(436, 249)
]

coordenadas_tetera = [
	(413, 177),
	(448, 159),
	(502, 88),
	(553, 53),
	(535, 36),
	(676, 37),
	(660, 52),
	(750, 145),
	(761, 179),
	(672, 192),
	(659, 214),
	(615, 214),
	(632, 230),
	(580, 230),
	(597, 215),
	(552, 214),
	(517, 144),
	(466, 180)
]

coordenadas_tetera_agarrador = [
	(682, 175),(708, 120),(735, 148),(739, 170)
]

rellenarPoligono(coordenadas_estrella)
rellenarPoligono(coordenadas_cuadrado)
rellenarPoligono(coordenadas_triangulo)
rellenarPoligono(coordenadas_tetera)
rellenarPoligono(coordenadas_tetera_agarrador)

glFinish()
