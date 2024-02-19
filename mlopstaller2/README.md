# TFX Dockerized Application

## Descripción
Este repositorio contiene una aplicación Dockerizada con TensorFlow Extended (TFX) que utiliza un contenedor de TensorFlow con Jupyter Lab para explorar y analizar datos con TensorFlow Data Validation (TFDV).

## Requisitos Previos
- [Docker](https://www.docker.com/)
- Conexión a Internet para descargar las imágenes de Docker.

## Instrucciones de Uso

### 1. Clonar el Repositorio
```bash
git clone https://github.com/c4ttivo/MLOpsTaller1.git
cd mlopstaller2
 ```
### 2. Ejecutar comando de docker-compose 
- Construir la Imagen del Contenedor
```bash
docker-compose build
```
- Ejecutar el Contenedor
```bash
docker-compose up -d
```
### 3. Acceder a Jupyter Lab
Abre tu navegador web y navega a  **_ http://localhost:8888._** 
Utiliza el token de acceso proporcionado en la terminal para iniciar sesión en Jupyter LAB.



