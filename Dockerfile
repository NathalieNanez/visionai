FROM python:3.12-slim
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y     libgl1     libglib2.0-0     && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY . .

# Puerto de la aplicación
EXPOSE 8000

# Comando para ejecutar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
