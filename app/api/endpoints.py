from fastapi import APIRouter, UploadFile, File
from app.core.model import predict_image
import shutil
from pathlib import Path
import os

router = APIRouter()

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Guardar imagen en carpeta 'images'
    images_dir = BASE_DIR / "images"
    images_dir.mkdir(exist_ok=True)
    
    # Validar extensión del archivo
    filename = file.filename
    ext = os.path.splitext(filename)[1].lower()
    if ext not in [".jpg", ".jpeg", ".png"]:
        return {"error": "Formato de imagen no soportado. Use JPG, JPEG o PNG"}
    
    image_path = images_dir / filename
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Procesar imagen
    try:
        output_filename, detections = predict_image(filename)
        return {
            "output_image": output_filename,
            "detections": detections
        }
    except Exception as e:
        return {"error": str(e)}
