# Laboratorio 1 Graficas por computadoras (SR1: Point)

from math import floor
from render import *
from utilities import *

objetoRender = None

def glInit(width, height):
	glCreateWindow(width,height)

def glCreateWindow(width, height):
	global objetoRender
	objetoRender = Render(width, height)

def glViewport(x,y, width, height):

	global objetoRender

	objetoRender.vp_x = x
	objetoRender.vp_y = y
	objetoRender.vp_width = width 
	objetoRender.vp_height = height

	# Dibujando el VP: ForLoop posterior
	for ancho in range(x, width+x):
		for alto in range(y, height+y):
			objetoRender.point(ancho,alto)

def glClear():
	objetoRender.clear()

def glClearColor(r, g, b):
	objetoRender.clear_color = color(round(255*r), round(255*g), round(255*b))
	glClear()

def glVertex(x,y):
	objetoRender.current_color = color(0,255,0)

	# objetoRender.point(objetoRender.vp_x , objetoRender.vp_y)

	# objetoRender.point(objetoRender.vp_x + round(objetoRender.vp_width/2) + round(x * (objetoRender.vp_width/2)), objetoRender.vp_y + y + round(objetoRender.vp_height/2))

	des_x = objetoRender.vp_x
	des_y = objetoRender.vp_y
	width = objetoRender.vp_width
	height = objetoRender.vp_height

	centro_x = round(des_x + (width/2))
	print('Centro en x sin redondear: ', des_x + (width/2))
	print('Centro X redondeado: ', centro_x)
	centro_y = round(des_y + (height/2))
	print('Centro en y sin redondear: ', des_y + (height/2))
	print('Centro Y redondeado: ', centro_x)

	print('')

	movimiento_x = centro_x + floor(x * width/2) 
	print('Movimiento x sin redondear: ', centro_x + x * width/2)
	print('Movimiento x redondeando: ', movimiento_x)
	movimiento_y = centro_y + floor(y * height/2) 
	print('Movimiento y sin redondear: ', centro_y + y * height/2)
	print('Movimiento y redondeando: ', movimiento_y)

	objetoRender.point(x,y)

	# objetoRender.point(objetoRender.vp_x + objetoRender.vp_width - 1, objetoRender.vp_y + objetoRender.vp_height - 1)


def glPoint(x, y):
	objetoRender.point(x,y)

def glColor(r, g, b):
	objetoRender.current_color = color(round(255*r), round(255*g), round(255*b))

def glFinish():
	objetoRender.write('test.bmp')

def glLine(x0, y0, x1, y1):
	return objetoRender.line(x0, y0, x1, y1)

def glCreateLine(x0, y0, x1, y1):
	objetoRender.line(*objetoRender.convertirCoordenadas(x0,y0), *objetoRender.convertirCoordenadas(x1,y1))


