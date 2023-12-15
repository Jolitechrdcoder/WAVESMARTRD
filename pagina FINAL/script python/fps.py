import cv2
import os

def extract_frames(video_path, output_folder):
    # Abre el video
    cap = cv2.VideoCapture(video_path)

    # Verifica si el video se abrió correctamente
    if not cap.isOpened():
        print("Error al abrir el video.")
        return

    # Obtiene la tasa de frames por segundo
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Crea la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Inicializa variables
    frame_count = 1

    # Lee y guarda cada fotograma
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Guarda el fotograma en la carpeta de salida
        output_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(output_path, frame)

        frame_count += 1

    # Libera los recursos
    cap.release()
    cv2.destroyAllWindows()

    print(f"Se han extraído {frame_count - 1} fotogramas.")

# Ruta del video de entrada
video_path = 'buoy2.mp4'  # Reemplaza con la ruta de tu video

# Carpeta de salida para los fotogramas
output_folder = 'carpeta_de_salida'  # Reemplaza con la carpeta que desees

# Llama a la función para extraer los fotogramas
extract_frames(video_path, output_folder)
