# 🚀 VisionAI - Object Detection System

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)
![Docker](https://img.shields.io/badge/docker-compose-2.37%2B-blueviolet)
![YOLOv8](https://img.shields.io/badge/YOLOv8-8.3%2B-orange)

## 🌟 Features

- 🖼️ Upload images via drag & drop or file selection
- 🔍 Real-time object detection with YOLOv8
- 📊 Detailed detection results with confidence scores
- 🖥️ Modern responsive web interface
- 📁 Image gallery with history of processed files
- 🐳 Full Docker support

## 🛠️ Installation

### Prerequisites
- Docker Desktop ([Download](https://www.docker.com/products/docker-desktop))
- Git 

```bash
# Clone repository (optional)
git clone https://github.com/yourusername/visionai.git
cd visionai

### Construir y ejecutar con Docker
bash
# Construir las imágenes
docker compose build

# Iniciar los contenedores
docker compose up

# Para ejecutar en segundo plano:
docker compose up -d

### Acceder a la aplicación
Interfaz web: http://localhost:8000

API Docs: http://localhost:8000/docs

Galería de resultados: http://localhost:8000/images
