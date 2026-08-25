Validation run used for the final TFM security evaluation.
# Seguridad en contenedores - Laboratorio Docker

Proyecto desarrollado como parte del Trabajo Fin de Máster de Formación Permanente en Ciberseguridad y Seguridad de la Información de la Universidad de Castilla-La Mancha.

## Descripción

Este repositorio contiene la aplicación utilizada como laboratorio para las pruebas realizadas durante el TFM.

El entorno está formado por una API sencilla desarrollada con FastAPI y un contenedor Nginx utilizado como reverse proxy. Ambos servicios se despliegan mediante Docker Compose.

La aplicación se ha mantenido deliberadamente pequeña para centrar las pruebas en la seguridad de las imágenes y la configuración de los contenedores, evitando añadir funcionalidad que no fuese necesaria para el trabajo.

## Tecnologías utilizadas

- FastAPI y Uvicorn.
- Nginx.
- Docker.
- Docker Compose.
- GitHub Actions.

## Requisitos

Para ejecutar el laboratorio de forma local es necesario disponer de:

- Git.
- Docker Engine.
- Docker Compose.

## Instalación y ejecución

Clonar el repositorio:

```bash
git clone https://github.com/Alexander-FB/tfm-alexander-container-security.git
cd tfm-alexander-container-security
```

Construir y levantar los servicios:

```bash
docker compose up --build -d
```

Comprobar el estado de los contenedores:

```bash
docker compose ps
```

La API queda accesible a través de Nginx en el puerto `8080`. El endpoint utilizado para comprobar su estado es:

```bash
curl http://localhost:8080/health
```

La respuesta esperada es:

```json
{"status":"ok"}
```

Para detener el entorno:

```bash
docker compose down
```

## GitHub Actions

El repositorio contiene workflows para iniciar los procesos de análisis de seguridad y publicación de releases.

La lógica principal de estas comprobaciones se encuentra separada del código de la aplicación y se ejecuta mediante workflows reutilizables definidos en el repositorio del pipeline de seguridad.

## Estructura del repositorio

```text
tfm-alexander-container-security/
├── .github/
│   └── workflows/
│       ├── security.yml
│       └── release.yml
├── app/
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── nginx/
│   └── nginx.conf
├── .gitignore
├── docker-compose.yml
└── README.md
```