# ///////////////  toma de fotos y almacenamiento en base de datos !!!!!!!! //////////////


# import cv2
# # from pymongo import MongoClient
# import imutils
# import os
# #se usa para el procesamiento de imágenes de manera más fáci, como Redimensionar imágenes.Rotar imágenes.Transladar imágenes.Recortar regiones de interés (ROI) en imágenes.
# # from bson import Binary
# # BSON es un formato binario utilizado por MongoDB para almacenar 
# # y transferir datos de manera eficiente. La biblioteca bson proporciona
# # herramientas para codificar y decodificar datos en formato BSON.

# # Conectarse a la base de datos MongoDB Atlas
# # client = MongoClient("mongodb+srv://Andrew:BEyKKt0ai4ArRqBQ@cluster0.qj0gkdd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# # Seleccionar la base de datos y la colección
# # db = client["vision_artificial"]
# # usuarios = db["usuarios"]

# clasificador= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")

# # codigo=int(input("Ingrese su ID: "))

# # se crean la carpeta donde se va almacenar las fotos

# NombreUser=input('Ingresa tu nombre: ')

# # dataPath= r'c:\Users\SENA_Aprendiz\Documents\Onixdrew\OpenCV\data'
# dataPath= r'C:\Users\Andrew\Documents\Proyecto_Vision_Artificial\OpenCV\data'
# dirPersona= dataPath + '/' + NombreUser



# if not os.path.exists(dirPersona):
#     os.makedirs(dirPersona)
#     print('caperta creada: ', dirPersona)
    
#     # user=input("Ingrese su nombre: ")
#     # usuarios.insert_one({"codigo":codigo,"Nombre":user,"fotos":[]})

#     # Configurar la cámara
#     camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#     contador=0


#     # listaFotos=[]
    
#     while True:
#         # Capturar un fotograma
#         imgDisponible, frame = camera.read()
        
#         if imgDisponible==False:
#             break
        
#         # Voltear horizontalmente la imagen
#         frameNormal = cv2.flip(frame, 1)
        
#         frame=imutils.resize(frameNormal, width=750)
#         gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         auxFrame=frame.copy()
        
#         # deteccion rostro
#         faces= clasificador.detectMultiScale(gray,1.3,5)
        
#         for (x,y,w,h) in faces:
#             cv2.rectangle(frame,(x,y),(x+w, y+h), (0,255,0), 2)
#             rostro= auxFrame[y:y+h, x:x+w]
#             rostro= cv2.resize(rostro, (720, 720), interpolation=cv2.INTER_CUBIC)
            
#             # Guardar la imagen en en la carpeta local
#             cv2.imwrite(dirPersona + '/rostro_{}.jpg'.format(contador), rostro)
            
            
#             # Guardar la imagen en MongoDB
#             # ret, buffer = cv2.imencode('.jpg', rostro)
#             #  La función cv2.imencode() toma una imagen y la codifica en un formato específico en este caso, .jpg . Esta función devuelve dos valores: ret y buffer. ret es una bandera 
#             # que indica si la codificación fue exitosa (True) o no (False). buffer es un array de bytes que contiene los datos de la imagen codificada en formato JPEG.
            
#             # image_data = buffer.tobytes()
#             #  Convertimos el array de bytes buffer en un objeto bytes utilizando el método tobytes(). Esto nos da los datos de la imagen en formato de bytes.

#             # image_binary = Binary(image_data)
#             # Creamos un objeto Binary de MongoDB utilizando los datos de la imagen en formato de bytes. MongoDB puede almacenar datos binarios como objetos Binary. Este paso es necesario para poder almacenar la imagen en MongoDB.
#             # Los bytes son la unidad básica de almacenamiento y transferencia de datos en sistemas informáticos.
            
#             # usuarios.update_one({ "Nombre":user }, { "$push": { "fotos": image_binary } })
#             contador+=1 
            

        
#         # Mostrar el fotograma 
#         cv2.imshow("Captura del rostro", frame)
        

#         # Esperar la pulsación de la tecla 'q' para salir
#         if cv2.waitKey(1) == ord('q') or contador > 100:
#             print(f'Proceso finalizado, se almacenó {contador -1} fotos')
#             break

#     # Liberar la cámara y cerrar la ventana
#     camera.release()
#     cv2.destroyAllWindows()
#     # print(f'el usuario {user} se registró correctamente')
    
# else:
#     print('ya existe usuario con ese nombre')
    





# ///////////////////// clasificador mediapipe(google) //////////////////////////////////77



# import cv2
# import mediapipe as mp
# import os




# NombreUser=input('Ingresa tu nombre: ')

# dataPath= r'C:\Users\Andrew\Documents\Proyecto_Vision_Artificial\OpenCV\data'
# dirUser= dataPath + '/' + NombreUser

# if not os.path.exists(dirUser):
#     print("carpeta creada")
#     os.makedirs(dirUser)
    
# contador= 1
# detector = mp.solutions.face_detection
# dibujo= mp.solutions.drawing_utils

# camara = cv2.VideoCapture(1)

# with detector.FaceDetection(min_detection_confidence=0.75) as rostros:
#     while True:
#         # Capturar un fotograma
#         ret, frame = camara.read()
        
#         # poner el frame a efecto espejo
#         frame = cv2.flip(frame, 1)
        
#         # eliminar el error del color
#         rgb= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        
#         # deteccion de rostros
#         resultado= rostros.process(rgb)
        
#         if resultado.detections is not None:
            
#             for rostro in resultado.detections:
#                 # establece puntos de referencia del rostro
#                 dibujo.draw_detection(frame, rostro)
                
#                 # se exrtraen las coordenadas del frame o ventana
#                 al, an, _ = frame.shape
                
#                 # se exrtraen las coordenadas del rostros detectado
#                 xI= rostro.location_data.relative_bounding_box.xmin
#                 yI= rostro.location_data.relative_bounding_box.ymin
                
#                 ancho= rostro.location_data.relative_bounding_box.width
#                 alto= rostro.location_data.relative_bounding_box.height
                
#                 # se convierte a pixeles. Se redondea a un entero
#                 xi= int(xI*an)
#                 yi=int(yI*al)
#                 ancho=int(ancho*an)
#                 alto= int(alto*al)
                
#                 # hallar coordenadas finales con las coordenadas redondeadas del rostro detectado
#                 xf=xi + ancho
#                 yf=yi + alto
                
#                 # se extraen los pixeles del rostro detectado
#                 cara= frame[yi:yf, xi:xf]
                
#                 # redimencionar las fotos
#                 cara= cv2.resize(cara, (150,200), interpolation=cv2.INTER_CUBIC)
                
#                 # Guardar rostro
#                 cv2.imwrite(dirUser + "/rostro_{}.jpg".format(contador), cara)
#                 contador += 1
                
                
#         # Mostrar el fotograma
#         cv2.imshow("Captura del rostro", frame)
        
#         # Esperar la pulsación de la tecla 'q' para salir o alcanzar el límite de imágenes
#         if cv2.waitKey(1) == ord('q') or contador > 100:
#             break
        
#     # Liberar la cámara y cerrar la ventana
#     camara.release()
#     cv2.destroyAllWindows()
#     print("---Captura exitosa---")




# ////////////////////////////////// mejorado
import cv2
import mediapipe as mp
import os

NombreUser = input('Ingresa tu nombre: ')

dataPath = r'C:\Users\SENA_Aprendiz\Documents\Onixdrew\openCV\data'
# dataPath = r'C:\Users\Andrew\Documents\Proyecto_Vision_Artificial\OpenCV\data'
dirUser = dataPath + '/' + NombreUser

if not os.path.exists(dirUser):
    print("Carpeta creada")
    os.makedirs(dirUser)

contador = 1
detector = mp.solutions.face_detection
dibujo = mp.solutions.drawing_utils

camara = cv2.VideoCapture(0)

with detector.FaceDetection(min_detection_confidence=0.75) as rostros:
    while True:
        # Capturar un fotograma
        ret, frame = camara.read()

        # Poner el frame a efecto espejo
        frame = cv2.flip(frame, 1)

        # Crear una copia del frame antes de dibujar los cuadros de detección
        frame_copia = frame.copy()

        # Convertir a RGB para la detección
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detección de rostros
        resultado = rostros.process(rgb)

        if resultado.detections is not None:
            for rostro in resultado.detections:
                # Establecer puntos de referencia del rostro
                dibujo.draw_detection(frame, rostro)  # Dibuja el cuadro en la imagen que se muestra

                # Extraer las coordenadas del frame o ventana
                al, an, _ = frame.shape

                # Extraer las coordenadas del rostro detectado
                xI = rostro.location_data.relative_bounding_box.xmin
                yI = rostro.location_data.relative_bounding_box.ymin
                ancho = rostro.location_data.relative_bounding_box.width
                alto = rostro.location_data.relative_bounding_box.height

                # Convertir a píxeles y redondear
                xi = int(xI * an)
                yi = int(yI * al)
                ancho = int(ancho * an)
                alto = int(alto * al)

                # Hallar coordenadas finales con las coordenadas redondeadas del rostro detectado
                xf = xi + ancho
                yf = yi + alto

                # Extraer los píxeles del rostro detectado de la copia del frame (sin dibujo)
                cara = frame_copia[yi:yf, xi:xf]

                # Redimensionar la imagen del rostro
                cara = cv2.resize(cara, (150, 200), interpolation=cv2.INTER_CUBIC)

                # Guardar el rostro
                cv2.imwrite(dirUser + "/rostro_{}.jpg".format(contador), cara)
                contador += 1

        # Mostrar el fotograma con los cuadros de detección
        cv2.imshow("Captura del rostro", frame)

        # Esperar la pulsación de la tecla 'q' para salir o alcanzar el límite de imágenes
        if cv2.waitKey(1) == ord('q') or contador > 300:
            break

    # Liberar la cámara y cerrar la ventana
    camara.release()
    cv2.destroyAllWindows()
    print("---Captura exitosa---")


