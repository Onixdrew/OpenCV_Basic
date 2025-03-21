
import cv2
import imutils #Librería auxiliar para operaciones comunes en imágenes, como cambiar de tamaño.
import os  #ermite manipular archivos y directorios.



#Creación de la carpeta para almacenar imágenes
typeFoto = str(input("Tipo de imagenes: ")) #Cambiar
dataPath=r'C:\Users\fenix\Documents\prueba_OpenCV\DetectObject\Data'
dirFoto= dataPath +"/" + typeFoto

if not os.path.exists(dirFoto):
	print('Carpeta creada: ', typeFoto)
	os.makedirs(dirFoto)

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#Definición de la región de interés (ROI)
x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0
while True:

	ret, frame = cap.read() 
	if ret == False:  break
	frame=cv2.flip(frame,1)
	#Se hace una copia del fotograma para no modificar la imagen original.
	imAux = frame.copy()
	#Dibujo de un rectángulo en la imagen
	cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

	#Extracción del objeto dentro de la región de interés
	objeto = imAux[y1:y2,x1:x2]
	#Se redimensiona objeto para que tenga un ancho de 38 píxeles (manteniendo la proporción).
	# objeto = imutils.resize(objeto, width=38)
	# print(objeto.shape)

	#Si el usuario presiona la tecla 's', la imagen objeto se guarda en la carpeta Datos
	k = cv2.waitKey(1)
	if k == ord('s'):
		cv2.imwrite(dirFoto+'/objeto_{}.jpg'.format(count),objeto)
		print('Imagen almacenada: ', 'objeto_{}.jpg'.format(count))
		count = count + 1
	if k == 27: 
		break

	cv2.imshow('frame',frame)
	# cv2.imshow('objeto',objeto)

cap.release()
cv2.destroyAllWindows()


