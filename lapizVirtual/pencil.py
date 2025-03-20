import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW ayuda a evitar advertencias en algunas versiones de OpenCV.

# # Definición del color celeste a detectar en formato HSV
colorInicial = np.array([70, 185, 88], np.uint8)  # Límite inferior
colorFinal = np.array([110, 255, 255], np.uint8)  # del color celeste.


# Definición de colores 
colorVerde = (0, 255, 36)
colorAmarillo = (89, 222, 255)
colorCeleste = (255, 113, 82)
colorRosa = (128, 0, 255)

colorBorrador = (0, 0, 255)  # Solo se usará para el cuadro superior de 'Limpiar Pantalla'

# Grosor de línea recuadros superior izquierda (color a dibujar)
grosorVerde = 6
grosorAmarillo = 2
grosorCeleste = 2
grosorRosa = 2

# Grosor de línea recuadros superior derecha (grosor del marcador para dibujar)
grosorPeque = 6
grosorMedio = 1
grosorGrande = 1

#---------Variables para el marcador / lápiz virtual -------------------------
color = colorVerde  # Color de entrada, y variable que asignará el color del marcador
grosor = 3  # Grosor que tendrá el marcador
#------------------------------------------------------------------------------------------

# Variables de estado,  Guardarán las coordenadas previas del marcador para dibujar líneas continuas.
x1 = None
y1 = None
imAux = None  # Imagen auxiliar donde se guardará el dibujo.

while True:

	ret, frame = cap.read()
	if ret == False: break

	frame = cv2.flip(frame,1)  # Se invierte horizontalmente la imagen (efecto espejo).
	frame=cv2.resize(frame,(800,600))
	frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# Creación de la imagen auxiliar
	if imAux is None: imAux = np.zeros(frame.shape, dtype=np.uint8)

	# /////////////////////////// Dibujo de la interfaz gráfica //////////////////////////////////
	cv2.rectangle(frame, (20, 10), (70, 60), colorVerde, grosorVerde)
	cv2.rectangle(frame, (80, 10), (130, 60), colorAmarillo, grosorAmarillo)
	cv2.rectangle(frame, (140, 10), (190, 60), colorCeleste, grosorCeleste)
	cv2.rectangle(frame, (200, 10), (250, 60), colorRosa, grosorRosa)


	
	# Posicion del Borrador
	cv2.rectangle(frame, (550, 10), (650, 60), colorBorrador, 1)
	cv2.putText(frame, 'Borrador', (555, 39), 4, 0.6, colorBorrador, 1, cv2.LINE_AA)
	

	# Cuadrados dibujados en la parte superior derecha (grosor del marcador para dibujar)

	#Grosor Pequeño
	cv2.rectangle(frame, (730, 160), (780, 210), (0, 0, 0), grosorPeque)
	cv2.circle(frame, (756,185 ), 3, (0, 0, 0), -1)
	
	#Grosor Mediano
	cv2.rectangle(frame, (730, 230), (780, 280), (0, 0, 0), grosorMedio)
	cv2.circle(frame, (756, 255), 7, (0, 0, 0), -1)
	
	#Grosor Grande
	cv2.rectangle(frame, (730, 300), (780, 350), (0, 0, 0), grosorGrande)
	cv2.circle(frame, (756, 325), 11, (0, 0, 0), -1)
	#-----------------------------------------------------------------------------------
	
	# Detección del color celeste
	mascaraColor = cv2.inRange(frameHSV, colorInicial, colorFinal)# crea una máscara binaria, donde los píxeles dentro del rango de color definido
	
	#//////////////////////////////Cuando se quiere combinar y detectar varios colores a la vez//////////////////////////////////////////////7
	# mascara_rojo_bajo = cv2.inRange(imagen_hsv, colorInicial_rojo_bajo, colorFinal_rojo_bajo)
	# mascara_rojo_alto = cv2.inRange(imagen_hsv, colorInicial_rojo_alto, colorFinal_rojo_alto)
	# mascara_rojo = cv2.bitwise_or(mascara_rojo_bajo, mascara_rojo_alto)

	# Erosión y dilatación para reducir el ruido.
	mascaraColor = cv2.erode(mascaraColor, None, iterations=1)  # La erosión reduce el tamaño de los objetos blancos en la máscara, eliminando pequeños puntos no deseados(Ruido).
	mascaraColor = cv2.dilate(mascaraColor, None, iterations=2)  # Esto recupera el tamaño de los objetos después de la erosión, pero sin el ruido que se eliminó
	# Filtro de mediana para suavizar los bordes.
	mascaraColor = cv2.medianBlur(mascaraColor, 13)  # suaviza la máscara eliminando puntos aislados (ruido) y haciendo que los bordes sean más suaves.
	
	# Encuentra los contornos de los objetos detectados en la máscara.
	cnts, _ = cv2.findContours(mascaraColor, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # detecta los bordes de los objetos blancos en la máscara.
	# Se ordenan por área y se selecciona solo el más grande.
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]  # ordena los contornos en función de su área. Y [:1]Toma solo el contorno más grande, asumiendo que es el más importante.

	# Seguimiento del objeto
	for c in cnts:
		area = cv2.contourArea(c)
		# Si el área del contorno es mayor a 1000 píxeles, se considera un objeto válido.
		if area > 1000:
			# Se obtiene su posición central.
			x, y2, w, h = cv2.boundingRect(c)
			x2 = x + w // 2
			
			if x1 is not None:
				# Si el usuario mueve el marcador a una zona de color, cambia el color del lápiz.
				if 20 < x2 < 70 and 10 < y2 < 60:
					
					color = colorVerde  
					grosorVerde = 6
					grosorCeleste = 2
					grosorAmarillo = 2
					grosorRosa = 2
				if 80 < x2 < 130 and 10 < y2 < 60:
					color = colorAmarillo  # Color del lápiz/marcador virtual
					grosorAmarillo = 6
					grosorRosa = 2
					grosorVerde = 2
					grosorCeleste = 2
					
				if 140 < x2 < 190 and 10 < y2 < 60:
					color = colorCeleste  
					grosorCeleste = 6
					grosorAmarillo = 2
					grosorRosa = 2
					grosorVerde = 2
				if 200 < x2 < 250 and 10 < y2 < 60:
					color = colorRosa  
					grosorRosa = 6
					grosorAmarillo = 2
					grosorVerde = 2
					grosorCeleste = 2
#//////////////////////////////////////////////////// Grosor
				if 730 < x2 < 780 and 160 < y2 < 210:
					grosor = 3  # Grosor del lápiz/marcador virtual
					grosorPeque = 6
					grosorMedio = 1
					grosorGrande = 1
				if 730 < x2 < 780 and 230 < y2 < 280:
					grosor = 7 
					grosorPeque = 1
					grosorMedio = 6
					grosorGrande = 1

				if 730 < x2 < 780 and 300 < y2 < 350:
					grosor = 11 
					grosorPeque = 1
					grosorMedio = 1
					grosorGrande = 6
#//////////////////////////////////////////////////// Borrador
				if 550 < x2 < 650 and 0 < y2 < 50:
					cv2.rectangle(frame, (550, 10), (650, 60), colorBorrador, 2)
					cv2.putText(frame, 'Borrador', (555, 39), 4, 0.6, colorBorrador, 2, cv2.LINE_AA)
					imAux = np.zeros(frame.shape, dtype=np.uint8)
				if 0 < y2 < 60 or 0 < y1 < 60:
					imAux = imAux
				else:
					# Si ya hay coordenadas previas (x1, y1), se dibuja una línea desde la posición anterior hasta la nueva.
					imAux = cv2.line(imAux, (x1, y1), (x2, y2), color, grosor)
			# Se dibuja un círculo en la posición actual para visualizar el marcador.
			cv2.circle(frame, (x2, y2), grosor, color, 3)
			x1 = x2
			y1 = y2
		else:
			x1, y1 = None, None
	# Superposición del dibujo en el frame
	imAuxGray = cv2.cvtColor(imAux, cv2.COLOR_BGR2GRAY)
	# Genera una máscara binaria para fusionar imAux con frame.
	# Todo píxel con un valor mayor a 10 se establece en 255 (blanco).
	# Todo píxel con un valor menor o igual a 10 se establece en 0 (negro).
	# th es la imagen binaria resultante, donde las líneas dibujadas son blancas (255) y el fondo es negro (0).
	_, th = cv2.threshold(imAuxGray, 10, 255, cv2.THRESH_BINARY)
	# invierte los valores de la imagen binaria. Los blancos (255) se vuelven negros (0). Ahora, thInv tiene el fondo blanco y las líneas negras.
	thInv = cv2.bitwise_not(th)
 	# Eliminación del fondo del dibujo en el frame,  mantiene solo los píxeles donde thInv es blanco (255) y elimina los píxeles donde es negro (0).
	frame = cv2.bitwise_and(frame, frame, mask=thInv)
	# Fusiona la imAux (que contiene los dibujos) con el frame sin afectar la imagen de la cámara.
	# Las áreas donde había dibujos en imAux se eliminan del frame. El fondo de la cámara se mantiene intacto.
	frame = cv2.add(frame, imAux)
	

	#-------------- Mostrar--------------
	#....Mascara del color detectado
	# cv2.imshow('mascaraColor', mascaraColor)
	#....Lienzo
	# cv2.imshow('imAux', imAux)
	#....Imagen en vivo
	cv2.imshow('Tablero', frame)
	
	
	k = cv2.waitKey(1)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()

# Ejemplo Visual
# Antes de la operación
# frame: Imagen de la cámara.
# imAux: Contiene el dibujo del lápiz sobre un fondo negro.
# th: Máscara binaria con el dibujo en blanco.
# thInv: Inversión del th, ahora el fondo es blanco y el dibujo es negro.
# Después de bitwise_and
# Se eliminan las áreas donde había dibujo en frame, dejando un espacio vacío.
# Luego, imAux se suma al frame en otro paso (que no se muestra aquí).









#//////////////////////////////////////////////////// Tablero con cursor /////////////////////////////////////////////

# import cv2
# import numpy as np

# # Dimensiones del lienzo
# WIDTH, HEIGHT = 800, 600

# # Creación del lienzo en blanco
# lienzo = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * 255

# # Definición de colores
# colores = {
#     "verde": (0, 255, 36),
#     "amarillo": (89, 222, 255),
#     "celeste": (255, 113, 82),
#     "rosa": (128, 0, 255),
#     "borrador": (255, 255, 255)  # Color del borrador (blanco)
# }

# # Grosor de línea para los recuadros de colores
# grosor_color = {
#     "verde": 6,
#     "amarillo": 2,
#     "celeste": 2,
#     "rosa": 2
# }

# # Grosor de línea para los recuadros de grosor del lápiz
# grosor_lapiz = {
#     "pequeño": 6,
#     "mediano": 1,
#     "grande": 1
# }

# # Variables de dibujo
# color_actual = colores["verde"]
# grosor_actual = 3
# dibujando = False  # Estado del dibujo
# x1, y1 = None, None  # Coordenadas previas

# def dibujar_interface(lienzo):
#     """Dibuja la interfaz gráfica sobre el lienzo."""
#     # Cuadros de selección de colores
#     cv2.rectangle(lienzo, (20, 10), (70, 60), colores["verde"], grosor_color["verde"])
#     cv2.rectangle(lienzo, (80, 10), (130, 60), colores["amarillo"], grosor_color["amarillo"])
#     cv2.rectangle(lienzo, (140, 10), (190, 60), colores["celeste"], grosor_color["celeste"])
#     cv2.rectangle(lienzo, (200, 10), (250, 60), colores["rosa"], grosor_color["rosa"])

#     # Botón del borrador
#     cv2.rectangle(lienzo, (550, 10), (650, 60), (0, 0, 255), 2)
#     cv2.putText(lienzo, 'Borrador', (555, 39), 4, 0.6, (0, 0, 255), 2, cv2.LINE_AA)

#     # Cuadros de selección de grosor del lápiz
#     cv2.rectangle(lienzo, (730, 160), (780, 210), (0, 0, 0), grosor_lapiz["pequeño"])
#     cv2.circle(lienzo, (756, 185), 3, (0, 0, 0), -1)

#     cv2.rectangle(lienzo, (730, 230), (780, 280), (0, 0, 0), grosor_lapiz["mediano"])
#     cv2.circle(lienzo, (756, 255), 7, (0, 0, 0), -1)

#     cv2.rectangle(lienzo, (730, 300), (780, 350), (0, 0, 0), grosor_lapiz["grande"])
#     cv2.circle(lienzo, (756, 325), 11, (0, 0, 0), -1)

# # Función de evento del mouse
# def dibujar(event, x, y, flags, param):
#     global x1, y1, dibujando, color_actual, grosor_actual, lienzo

#     if event == cv2.EVENT_LBUTTONDOWN:
#         # Verifica si se seleccionó un color
#         if 20 < x < 70 and 10 < y < 60:
#             cambiar_color("verde")
#         elif 80 < x < 130 and 10 < y < 60:
#             cambiar_color("amarillo")
#         elif 140 < x < 190 and 10 < y < 60:
#             cambiar_color("celeste")
#         elif 200 < x < 250 and 10 < y < 60:
#             cambiar_color("rosa")

#         # Verifica si se seleccionó un grosor
#         elif 730 < x < 780 and 160 < y < 210:
#             cambiar_grosor("pequeño")
#         elif 730 < x < 780 and 230 < y < 280:
#             cambiar_grosor("mediano")
#         elif 730 < x < 780 and 300 < y < 350:
#             cambiar_grosor("grande")

#         # Verifica si se presionó el botón del borrador
#         elif 550 < x < 650 and 10 < y < 60:
#             lienzo[:, :, :] = 255  # Borra el lienzo
#         else:
#             dibujando = True
#             x1, y1 = x, y

#     elif event == cv2.EVENT_MOUSEMOVE and dibujando:
#         if x1 is not None and y1 is not None:
#             cv2.line(lienzo, (x1, y1), (x, y), color_actual, grosor_actual)
#             x1, y1 = x, y

#     elif event == cv2.EVENT_LBUTTONUP:
#         dibujando = False
#         x1, y1 = None, None

# def cambiar_color(nombre_color):
#     """Cambia el color del lápiz y actualiza la interfaz."""
#     global color_actual, grosor_color
#     color_actual = colores[nombre_color]

#     # Restablece el grosor de los bordes
#     for key in grosor_color.keys():
#         grosor_color[key] = 2
#     grosor_color[nombre_color] = 6

# def cambiar_grosor(tipo):
#     """Cambia el grosor del lápiz y actualiza la interfaz."""
#     global grosor_actual, grosor_lapiz
#     grosores = {"pequeño": 3, "mediano": 7, "grande": 11}
#     grosor_actual = grosores[tipo]

#     # Restablece el grosor de los bordes
#     for key in grosor_lapiz.keys():
#         grosor_lapiz[key] = 1
#     grosor_lapiz[tipo] = 6

# # Configuración de la ventana y eventos del mouse
# cv2.namedWindow("Tablero")
# cv2.setMouseCallback("Tablero", dibujar)

# while True:
#     lienzo_temp = lienzo.copy()
#     dibujar_interface(lienzo_temp)
#     cv2.imshow("Tablero", lienzo_temp)

#     key = cv2.waitKey(1) & 0xFF
#     if key == 27:  # Presiona 'Esc' para salir
#         break

# cv2.destroyAllWindows()













