from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.endpoints import router
import os

app = FastAPI(
    title="Fruits Detection API",
    description="YOLOv8 + FastAPI para detección de frutas u objetos",
    version="1.0.0"
)

# Obtener ruta absoluta del proyecto
project_root = os.path.dirname(os.path.abspath(__file__))

# Configurar archivos estáticos y plantillas
app.mount("/static", StaticFiles(directory=os.path.join(project_root, "static")), name="static")
app.mount("/output_images", StaticFiles(directory=os.path.join(project_root, "images_with_boxes")), name="output_images")
templates = Jinja2Templates(directory=os.path.join(project_root, "templates"))

# Incluir endpoints API
app.include_router(router)

# Ruta para el frontend
@app.get("/", include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta para mostrar imágenes procesadas (CORREGIDA)
@app.get("/images", include_in_schema=False)
async def show_images(request: Request):
    output_dir = os.path.join(project_root, "images_with_boxes")
    
    # Crear directorio si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    images = [f for f in os.listdir(output_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    images.sort(key=lambda x: os.path.getmtime(os.path.join(output_dir, x)), reverse=True)
    
    return templates.TemplateResponse("images.html", {
        "request": request,
        "images": images
    })
