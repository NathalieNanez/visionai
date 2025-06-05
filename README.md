🚀 VisionAI - Sistema de Detección de Objetos con YOLOv8
Python
FastAPI
Docker
YOLOv8

📌 Tabla de Contenidos
Características

Instalación

Uso

Estructura del Proyecto

Despliegue

Contribución

Licencia

🌟 Características
🖼️ Interfaz web moderna para carga de imágenes

🔍 Detección de objetos en tiempo real con YOLOv8

📊 Visualización de resultados con cuadros delimitadores

🏗️ Arquitectura modular con FastAPI

🐳 Dockerizado para fácil despliegue

📁 Historial de imágenes procesadas

🛠️ Instalación
Prerrequisitos
Docker Desktop (Descargar)

Git (opcional)

bash
# Clonar repositorio
git clone https://github.com/NathalieNanez/visionai.git
cd visionai
Con Docker (recomendado)
bash
# Construir imágenes
docker compose build

# Iniciar servicios
docker compose up -d

# Ver logs
docker compose logs -f
Sin Docker (solo desarrollo)
bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
uvicorn main:app --reload
🌐 Uso
Accede a la interfaz web: http://localhost:8000

Sube una imagen usando drag & drop o el botón de selección

Visualiza los resultados de la detección

Explora el historial en: http://localhost:8000/images

Endpoints API:

POST /predict - Procesar imagen

GET /images - Listar imágenes procesadas

🗂 Estructura del Proyecto
visionai/
├── app/
│   ├── api/          # Endpoints de FastAPI
│   └── core/         # Lógica de detección
├── static/           # CSS/JS
├── templates/        # Plantillas HTML
├── images/           # Imágenes subidas
├── images_with_boxes # Resultados
├── models/           # Modelos YOLO
├── Dockerfile        # Configuración Docker
├── docker-compose.yml # Orquestación
└── requirements.txt  # Dependencias
🚀 Despliegue
Producción con Docker
bash
docker compose -f docker-compose.prod.yml up --build -d
Variables de entorno
Crea .env en la raíz:

ini
PYTHONUNBUFFERED=1
YOLO_CONFIG_DIR=/app/.config

🤝 Contribución
Haz fork del proyecto

Crea tu rama (git checkout -b feature/mejora)

Haz commit de tus cambios (git commit -m 'Add some feature')

Haz push a la rama (git push origin feature/mejora)

Abre un Pull Request
