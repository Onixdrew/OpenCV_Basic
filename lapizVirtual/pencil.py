import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # cv2.CAP_DSHOW ayuda a evitar advertencias en algunas versiones de OpenCV.

# Definición del color celeste a detectar en formato HSV
celesteBajo = np.array([75, 185, 88], np.uint8)  # Límite inferior
celesteAlto = np.array([112, 255, 255], np.uint8)  # del color celeste.

# Definición de colores 
colorCeleste = (255, 113, 82)
colorAmarillo = (89, 222, 255)
colorRosa = (128, 0, 255)
colorVerde = (0, 255, 36)

colorLimpiarPantalla = (29, 112, 246)  # Solo se usará para el cuadro superior de 'Limpiar Pantalla'

# Grosor de línea recuadros superior izquierda (color a dibujar)
grosorCeleste = 6
grosorAmarillo = 2
grosorRosa = 2
grosorVerde = 2

# Grosor de línea recuadros superior derecha (grosor del marcador para dibujar)
grosorPeque = 6
grosorMedio = 1
grosorGrande = 1

#---------Variables para el marcador / lápiz virtual -------------------------
color = colorCeleste  # Color de entrada, y variable que asignará el color del marcador
grosor = 3  # Grosor que tendrá el marcador
#------------------------------------------------------------------------------------------

# Variables de estado,  Guardarán las coordenadas previas del marcador para dibujar líneas continuas.
x1 = None
y1 = None
imAux = None  # Imagen auxiliar donde se guardará el dibujo.

while True:

	ret, frame = cap.read()
	if ret == False: break

	frame = cv2.flip(frame, 1)  # Se invierte horizontalmente la imagen (efecto espejo).
	frame=cv2.resize(frame,(900,670))
	frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# Creación de la imagen auxiliar
	if imAux is None: imAux = np.zeros(frame.shape, dtype=np.uint8)

	# Dibujo de la interfaz gráfica
	#------------------------ Sección Superior ------------------------------------------
	# Cuadrados dibujados en la parte superior izquierda (representan el color a dibujar)
	cv2.rectangle(frame, (0, 0), (50, 50), colorAmarillo, grosorAmarillo)
	cv2.rectangle(frame, (50, 0), (100, 50), colorRosa, grosorRosa)
	cv2.rectangle(frame, (100, 0), (150, 50), colorVerde, grosorVerde)
	cv2.rectangle(frame, (150, 0), (200, 50), colorCeleste, grosorCeleste)

	# Rectángulo superior central, que nos ayudará a limpiar la pantalla
	cv2.rectangle(frame, (300, 0), (400, 50), colorLimpiarPantalla, 1)
	cv2.putText(frame, 'Limpiar', (320, 20), 6, 0.6, colorLimpiarPantalla, 1, cv2.LINE_AA)
	cv2.putText(frame, 'pantalla', (320, 40), 6, 0.6, colorLimpiarPantalla, 1, cv2.LINE_AA)

	# Cuadrados dibujados en la parte superior derecha (grosor del marcador para dibujar)
	cv2.rectangle(frame, (490, 0), (540, 50), (0, 0, 0), grosorPeque)
	cv2.circle(frame, (515, 25), 3, (0, 0, 0), -1)
	cv2.rectangle(frame, (540, 0), (590, 50), (0, 0, 0), grosorMedio)
	cv2.circle(frame, (565, 25), 7, (0, 0, 0), -1)
	cv2.rectangle(frame, (590, 0), (640, 50), (0, 0, 0), grosorGrande)
	cv2.circle(frame, (615, 25), 11, (0, 0, 0), -1)
	#-----------------------------------------------------------------------------------
	
	# Detección del color celeste
	maskCeleste = cv2.inRange(frameHSV, celesteBajo, celesteAlto)# crea una máscara binaria, donde los píxeles dentro del rango de color definido
	
	# Erosión y dilatación para reducir el ruido.
	maskCeleste = cv2.erode(maskCeleste, None, iterations=1)  # La erosión reduce el tamaño de los objetos blancos en la máscara, eliminando pequeños puntos no deseados(Ruido).
	maskCeleste = cv2.dilate(maskCeleste, None, iterations=2)  # Esto recupera el tamaño de los objetos después de la erosión, pero sin el ruido que se eliminó
	# Filtro de mediana para suavizar los bordes.
	maskCeleste = cv2.medianBlur(maskCeleste, 13)  # suaviza la máscara eliminando puntos aislados (ruido) y haciendo que los bordes sean más suaves.
	
	# Encuentra los contornos de los objetos detectados en la máscara.
	cnts, _ = cv2.findContours(maskCeleste, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # detecta los bordes de los objetos blancos en la máscara.
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
				if 0 < x2 < 50 and 0 < y2 < 50:
					color = colorAmarillo  # Color del lápiz/marcador virtual
					grosorAmarillo = 6
					grosorRosa = 2
					grosorVerde = 2
					grosorCeleste = 2
				if 50 < x2 < 100 and 0 < y2 < 50:
					color = colorRosa  # Color del lápiz/marcador virtual
					grosorAmarillo = 2
					grosorRosa = 6
					grosorVerde = 2
					grosorCeleste = 2
				if 100 < x2 < 150 and 0 < y2 < 50:
					color = colorVerde  # Color del lápiz/marcador virtual
					grosorAmarillo = 2
					grosorRosa = 2
					grosorVerde = 6
					grosorCeleste = 2
				if 150 < x2 < 200 and 0 < y2 < 50:
					color = colorCeleste  # Color del lápiz/marcador virtual
					grosorAmarillo = 2
					grosorRosa = 2
					grosorVerde = 2
					grosorCeleste = 6
				if 490 < x2 < 540 and 0 < y2 < 50:
					grosor = 3  # Grosor del lápiz/marcador virtual
					grosorPeque = 6
					grosorMedio = 1
					grosorGrande = 1
				if 540 < x2 < 590 and 0 < y2 < 50:
					grosor = 7  # Grosor del lápiz/marcador virtual
					grosorPeque = 1
					grosorMedio = 6
					grosorGrande = 1
				if 590 < x2 < 640 and 0 < y2 < 50:
					grosor = 11  # Grosor del lápiz/marcador virtual
					grosorPeque = 1
					grosorMedio = 1
					grosorGrande = 6
				if 300 < x2 < 400 and 0 < y2 < 50:
					cv2.rectangle(frame, (300, 0), (400, 50), colorLimpiarPantalla, 2)
					cv2.putText(frame, 'Limpiar', (320, 20), 6, 0.6, colorLimpiarPantalla, 2, cv2.LINE_AA)
					cv2.putText(frame, 'pantalla', (320, 40), 6, 0.6, colorLimpiarPantalla, 2, cv2.LINE_AA)
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
	# cv2.imshow('maskCeleste', maskCeleste)
	#....Lienzo
	# cv2.imshow('imAux', imAux)
	#....Imagen en vivo
	cv2.imshow('frame', frame)
	
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
