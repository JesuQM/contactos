# Usa una imagen base de Python ligera
FROM python:3.10-slim

# Evita escribir archivos pyc y que la salida se almacene en búfer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos y actualiza pip
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del código del proyecto
COPY . /app/

# Expone el puerto en el que se ejecuta Django (usualmente 8000)
EXPOSE 8000

# Comando para iniciar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
