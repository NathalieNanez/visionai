import os
import cv2
from ultralytics import YOLO
from pathlib import Path
import time

# Obtener ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

model_path = BASE_DIR / "models" / "yolov8n.pt"
model = YOLO(str(model_path))

def predict_image(filename, conf_threshold=0.5):
    img_path = BASE_DIR / "images" / filename
    img = cv2.imread(str(img_path))

    if img is None:
        raise ValueError(f"Imagen no válida: {filename}")

    results = model.predict(img, conf=conf_threshold)[0]

    output_dir = BASE_DIR / "images_with_boxes"
    output_dir.mkdir(exist_ok=True)
    
    name, ext = os.path.splitext(filename)
    timestamp = int(time.time())
    output_filename = f"{name}_{timestamp}_wbbox{ext}"
    output_path = output_dir / output_filename
    annotated_frame = results.plot()
    cv2.imwrite(str(output_path), annotated_frame)

    detections = []
    for box in results.boxes:
        cls = model.names[int(box.cls[0])]
        conf = float(box.conf[0])
        if conf >= conf_threshold:
            detections.append({"label": cls, "confidence": round(conf, 2)})

    return output_filename, detections
