import cv2
import numpy as np

# # Cargar imagen
# imagen = cv2.imread("./img/b4e78271-e3a1-4c03-8236-0502d0760720.jpg")  # Escala de grises el 2do argumento es 0

imagen2 = cv2.imread("./img/zorro.jpg")  # Escala de grises el 2do argumento es 0


# Conversión de colores///////////////////////////////////////

# Convertir a escala de grises
# imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# # Convertir a HSV
# imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# cv2.imshow("imagen_gris", imagen_gris)
# cv2.imshow("imagen_hsv", imagen_hsv)


# cv2.waitKey(0)
# cv2.destroyAllWindows()



# # Aplicar detección de bordes///////////////////////////////////////7
# bordes = cv2.Canny(imagen, 100, 200)

# # Mostrar resultados
# cv2.imshow("Original", imagen)
# cv2.imshow("Bordes", bordes)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# filtro////////////////////////////////77777

# Filtro de desenfoque
# desenfoque = cv2.GaussianBlur(imagen, (15, 15), 0)

# Filtro de suavizado (promedio)
# suavizado = cv2.blur(imagen, (5, 5))

# # Filtro de desenfoque medio
# desenfoque_medio = cv2.medianBlur(imagen, 5)

# cv2.imshow("desenfoque", desenfoque)
# cv2.imshow("suavizado", suavizado)
# cv2.imshow("desenfoque_medio", desenfoque_medio)


# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Detectar bordes/////////////////////////////

# Detectar bordes con Sobel
# bordes_sobelx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)  # Gradiente X
# bordes_sobely = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)  # Gradiente Y

# # Detectar bordes con Laplacian
# bordes_laplacian = cv2.Laplacian(imagen, cv2.CV_64F)

# cv2.imshow("bordes_sobelx", bordes_sobelx)
# cv2.imshow("bordes_sobely", bordes_sobely)
# cv2.imshow("bordes_laplacian", bordes_laplacian)


# cv2.waitKey(0)
# cv2.destroyAllWindows()




# Rotar una imagen////////////////////////////////////////////7777

# Rotar 90 grados en sentido horario
# imagen_rotada = cv2.rotate(imagen, cv2.ROTATE_90_CLOCKWISE)

# # Otras opciones de rotación
# # cv2.ROTATE_90_COUNTERCLOCKWISE
# # cv2.ROTATE_180


# cv2.imshow("imagen_rotada", imagen_rotada)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Crear una imagen en blanco///////////////////777
# blanco = np.ones((500, 500, 3), dtype="uint8") * 255 #blanco
# blanco2 = np.ones((500, 500, 3), dtype="uint8") * 0  #Negro



# cv2.imshow("Imagen en blanco", blanco)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Convertir a escala de grises//////////////////////////////////////////////7
# imagen_gris = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)

# Convertir a HSV
# imagen_hsv = cv2.cvtColor(imagen2, cv2.COLOR_BGR2HSV)

# red=cv2.resize(imagen_hsv,(600,600))



# imagen_redimensionada = cv2.resize(red, None, fx=0.5, fy=0.5, )


# cv2.imshow("Imagen en blanco",red )

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Dibujar texto en la imagen ////////////////////////////////////////
# blanco = np.ones((500, 500, 3), dtype="uint8") * 255 #blanco

# new_picture=cv2.putText(imagen2, "Genial", (100,100), cv2.FONT_HERSHEY_TRIPLEX, 3, (0, 255, 0), 2)

# cv2.imshow("Imagen en blanco",new_picture )

# cv2.waitKey(0)
# cv2.destroyAllWindows()






# //////////////////////////////////////////////////////////
# Enmascarado

import cv2

img = cv2.imread('./img/girasol.webp')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (52,0,0), (65,255,255))

cv2.imshow("Mascara", mask)
cv2.imshow("Imagen", img)
cv2.waitKey(0)
cv2.destroyAllWindows()