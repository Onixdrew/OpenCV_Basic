#  ///////////////  Reconocimiento Facial con clasificador en cascada //////////////


# import cv2
# # from pymongo import MongoClient
# import os

# # Cargar el clasificador en cascada para la detección de rostros
#                                     #  módulo en OpenCV que proporciona
#                                     # rutas  predefinidas a los 
#                                     # clasificadores en cascada Haar  +  archivo XML que contiene la información del clasificador en cascada para la detección de rostros frontales
# faceClassifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")


# # Cargar el modelo(clase) de reconocimiento facial LBPH de openCV
# recognizer = cv2.face.LBPHFaceRecognizer_create()

# # Leer el modelo previamente entrenado para el reconocimiento facial
# recognizer.read('modelo_vision_artificial.xml')
# # read(): Este método(funcion) del objeto recognizer se utiliza para cargar un modelo de reconocimiento facial desde un archivo XML

# # Conectarse a la base de datos MongoDB Atlas
# # client = MongoClient("mongodb+srv://Andrew:BEyKKt0ai4ArRqBQ@cluster0.qj0gkdd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# # Seleccionar la base de datos y la colección
# # db = client["vision_artificial"]
# # usuarios = db["usuarios"]

# # dataPath= r'c:\Users\SENA_Aprendiz\Documents\Onixdrew\OpenCV\data'
# dataPath= r'C:\Users\Andrew\Documents\Proyecto_Vision_Artificial\OpenCV\data'
# listaPersonas= os.listdir(dataPath)
# print('lista de usuarios: ', listaPersonas)


# camara = cv2.VideoCapture(0, cv2.CAP_ANY)

# while True:
#     # Leer un fotograma del video
#     ret, frame = camara.read()
    
#     if not ret:
#         print("No se pudo capturar el fotograma")
#         break
        
#     # Voltear horizontalmente la imagen
#     frame= frameNormal = cv2.flip(frame, 1)
    
#     # Convertir la imagen a escala de grises
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     auxFrame=gray.copy()
    
#     # Detectar rostros en la imagen
#     faces = faceClassifier.detectMultiScale(gray, 1.3, 5)
    
#     # Para cada rostro detectado, realizar el reconocimiento facial
#     for (x, y, w, h) in faces:
#         # Dibujar un rectángulo alrededor del rostro detectado
#         # cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
#         rostro= auxFrame[y:y+h, x:x+w]
#         rostro= cv2.resize(rostro,(150,150), interpolation= cv2.INTER_CUBIC)
#         result=recognizer.predict(rostro)
    
        
#         cv2.putText(frame, '{}'.format(result), (x, y-5),1,1.3,(255,255,0),1, cv2.LINE_AA )
        
#         # consultaCodigo=usuarios.find_one({"codigo":result[0]})
#         #  se comprueba la confianza de la prediccion para asignar el nombre de la persona
#         # result[1] es la confianza de prediccion, ya que predict devuelve dos variables(id, conf)
        
#         if result[1] < 80:
            
#             # /////////////////// Mejorar esta linea, aqui se presenta el error
            
#             cv2.putText(frame,'{}'.format(listaPersonas[result[0]]), (x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
#             cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)
            
#         else:
#             cv2.putText(frame,'Desconocido',(x,y-20), 2, 0.8, (0,0,255),1 , cv2.LINE_AA)
#             cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),2)

#         # Realizar el reconocimiento facial en la región del rostro
#                                         #  Esto extrae la región de la imagen que contiene el rostro detectado.
#         # id_, conf = recognizer.predict(gray[y:y+h, x:x+w])
#         # Esta función toma una imagen(o una región de una imagen) como entrada y devuelve dos valores: id_ y conf.
        
#         # id_: Este es el ID asociado a la persona reconocida. En el proceso de entrenamiento, cada persona tiene un ID único asociado con su rostro.
        
#         # conf: Esta es la confianza o certeza de la predicción. Indica cuán seguro está el modelo en su predicción. Generalmente, los valores más bajos indican mayor confianza.
#         # Un valor bajo significa que el modelo encontró una buena coincidencia entre el rostro detectado y las caras en el conjunto de entrenamiento.
        
        
#         # Si la confianza es alta, mostrar el nombre predicho
#         # if conf < 70:
#             # Aquí deberías tener un diccionario o base de datos que asocie los IDs con los nombres de las personas
#         #     nombre = "Persona " + str(id)
#         # else:
#         #     nombre = "Desconocido"
        
#         # Mostrar el nombre predicho sobre el rostro
#         # cv2.putText(frame, nombre, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2, cv2.LINE_AA)
    
  
#     # Mostrar el fotograma resultante
#     cv2.imshow('RECONOCIMENTO FACIAL', frame)
    
#     # Salir del bucle si se presiona 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Liberar la captura y cerrar todas las ventanas
# camara.release()
# cv2.destroyAllWindows()




# # /////////////////////////////////////clasificador mediapipe(google) ///////////////////////////////////////////////////


# import cv2
# import mediapipe as mp
# import os


# dataPath= r'C:\Users\Andrew\Documents\Proyecto_Vision_Artificial\OpenCV\data'
# listaPersonas= os.listdir(dataPath)
# print('lista de Usuarios: ', listaPersonas)

# # se inicializa el modelo
# modelo = cv2.face.LBPHFaceRecognizer_create()

# # se lee el modelo entrenado
# modelo.read("ModeloEntrenado.xml")

# detector = mp.solutions.face_detection
# dibujo= mp.solutions.drawing_utils

# camara = cv2.VideoCapture(1)

# with detector.FaceDetection(min_detection_confidence=0.75) as rostros:
#     while True:
#         # Capturar un fotograma
#         ret, frame = camara.read()
        
#         # se crea una copia del frame. Una para el modelo y otra para el detector de rostro
#         copia= frame.copy()
        
#         # poner el frame a efecto espejo
#         frame = cv2.flip(copia, 1)
        
#         # eliminar el error del color
#         rgb= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         copia2= rgb.copy()
        
#         # deteccion de rostros
#         resultado= rostros.process(copia2)
        
#         if resultado.detections is not None:
            
#             for rostro in resultado.detections:
#                 # establece puntos de referencia del rostro
#                 # dibujo.draw_detection(frame, rostro)
                
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
#                 cara= copia2[yi:yf, xi:xf]
                
#                 # redimencionar las fotos
#                 cara= cv2.resize(cara, (150,200), interpolation=cv2.INTER_CUBIC)
                
#                 # se pasa a escal de grises
#                 cara= cv2.cvtColor(cara, cv2.COLOR_BGR2GRAY)
                
#                 # se realiza la predicción
#                 prediccion= modelo.predict(cara)
                
#                 cv2.putText(frame, '{}'.format(prediccion), (xi, yi - 5),1,1.3,(255,255,0),1, cv2.LINE_AA )
                
#                 # mostrar los resultados en pantalla
#                 # Si la confianza es alta, mostrar el nombre predicho
#                 if prediccion[1] < 77:
#                     cv2.putText(frame, "{}".format(listaPersonas[prediccion[0]]),(xi, yi - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0),2, cv2.LINE_AA )
#                     # cv2.rectangle(frame, (xi, yi), (xf,yf), (255,0,0), 2)
#                     dibujo.draw_detection(frame, rostro)
#                 else:
#                     cv2.putText(frame, "Desconocido",(xi, yi - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2, cv2.LINE_AA)
#                     # cv2.rectangle(frame, (xi, yi), (xf,yf), (0,0,255), 2)
#                     dibujo.draw_detection(frame, rostro)
                    
                    
                
#         # Mostrar el fotograma
#         cv2.imshow("Captura del rostro", frame)
        
#         # Esperar la pulsación de la tecla 'q' para salir o alcanzar el límite de imágenes
#         if cv2.waitKey(1) == ord('q'):
#             break
        
#     # Liberar la cámara y cerrar la ventana
#     camara.release()
#     cv2.destroyAllWindows()





# ////////////////////////////////// mejorado
import cv2
import mediapipe as mp
import os
dataPath = r'C:\Users\SENA_Aprendiz\Documents\Onixdrew\openCV\data'
# dataPath = r'C:\Users\Andrew\Documents\Proyecto_Vision_Artificial\OpenCV\data'
listaPersonas = os.listdir(dataPath)
print('Lista de Usuarios: ', listaPersonas)

# Inicializar el modelo LBPHFaceRecognizer
modelo = cv2.face.LBPHFaceRecognizer_create()

# Leer el modelo entrenado
modelo.read("ModeloEntrenado.xml")

detector = mp.solutions.face_detection
dibujo = mp.solutions.drawing_utils

camara = cv2.VideoCapture(0)

with detector.FaceDetection(min_detection_confidence=0.75) as rostros:
    while True:
        # Capturar un fotograma
        ret, frame = camara.read()

        # Se crea una copia del frame
        copia = frame.copy()

        # Poner el frame a efecto espejo
        frame = cv2.flip(copia, 1)

        # Eliminar el error del color
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        copia2 = rgb.copy()

        # Detección de rostros
        resultado = rostros.process(copia2)

        if resultado.detections is not None:
            for rostro in resultado.detections:
                # Se extraen las coordenadas del frame o ventana
                al, an, _ = frame.shape

                # Se extraen las coordenadas del rostro detectado
                xI = rostro.location_data.relative_bounding_box.xmin
                yI = rostro.location_data.relative_bounding_box.ymin
                ancho = rostro.location_data.relative_bounding_box.width
                alto = rostro.location_data.relative_bounding_box.height

                # Convertir a píxeles (coordenadas redondeadas)
                xi = int(xI * an)
                yi = int(yI * al)
                ancho = int(ancho * an)
                alto = int(alto * al)

                # Hallar coordenadas finales
                xf = xi + ancho
                yf = yi + alto

                # Asegurarse de que las coordenadas estén dentro del frame y que el área del rostro sea válida
                if xi >= 0 and yi >= 0 and xf <= an and yf <= al and ancho > 0 and alto > 0:
                    # Extraer los píxeles del rostro detectado
                    cara = copia2[yi:yf, xi:xf]

                    # Verificar si el rostro fue correctamente extraído antes de redimensionar
                    if cara.size > 0:
                        # Redimensionar la foto
                        cara = cv2.resize(cara, (150, 200), interpolation=cv2.INTER_CUBIC)

                        # Pasar a escala de grises
                        cara = cv2.cvtColor(cara, cv2.COLOR_BGR2GRAY)

                        # Realizar la predicción
                        prediccion = modelo.predict(cara)

                        cv2.putText(frame, '{}'.format(prediccion), (xi, yi - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

                        # Mostrar los resultados en pantalla
                        if prediccion[1] < 70:
                            cv2.putText(frame, "{}".format(listaPersonas[prediccion[0]]), (xi, yi - 25),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2, cv2.LINE_AA)
                            dibujo.draw_detection(frame, rostro)
                        else:
                            cv2.putText(frame, "Desconocido", (xi, yi - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2, cv2.LINE_AA)
                            dibujo.draw_detection(frame, rostro)

        # Mostrar el fotograma
        cv2.imshow("Captura del rostro", frame)

        # Esperar la pulsación de la tecla 'q' para salir o alcanzar el límite de imágenes
        if cv2.waitKey(1) == ord('q'):
            break

    # Liberar la cámara y cerrar la ventana
    camara.release()
    cv2.destroyAllWindows()
