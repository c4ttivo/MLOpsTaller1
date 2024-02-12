![alt text](https://github.com/c4ttivo/MLOpsTaller1/blob/main/mlopstaller1/imgs/logo.png?raw=true)

# MLOps - Taller 1: Nivel 0
## Autores
*    Daniel Crovo (dcrovo@javeriana.edu.co)
*    Hugo Poveda (h.poveda@javeriana.edu.co)
*    Carlos Trujillo (ca.trujillo@javeriana.edu.co)

## Profesor
*    Cristian Diaz (diaz.cristian@javeriana.edu.co)

## Instrucciones
Clone el repositorio de git usando el siguiente comando en la consola de su sistema operativo:


```
# git clone https://github.com/c4ttivo/MLOpsTaller1.git
```

Una vez ejecutado el comando anterior aparece el folder MLOpsTaller1. Luego es necesario ubicarse en el directorio de trabajo en el que se encuentra el archivo Dockerfile.


```
# cd MLOpsTaller1/mlopstaller1/
```

Ahora es necesario construir el contenedor


```
# docker build -t nivel_0 .
```
En este paso se descarga la imagen de acuerdo con lo especificado en el archivo Dockerfile.

<img src="https://github.com/c4ttivo/MLOpsTaller1/blob/main/mlopstaller1/imgs/console.png?raw=true" width="50%" height="50%" />

Una vez finalizado la creación de la imagen, se procede a levantar la instancia del contenedor con el siguiente comando


```
# docker run --name nivel_0 -p 8989:80 nivel_0
```

Al levantarse la instancia, ahora es posible consumir los servicios expuestos en la URL http://127.0.0.1/docs#/

![alt text](https://github.com/c4ttivo/MLOpsTaller1/blob/main/mlopstaller1/imgs/fastapi.png?raw=true)


# Project Organization
------------

    ├── LICENSE
    ├── README.md          			<- The top-level README for developers using this project.
    ├── imgs             			<- Images used in README
    ├── data
    │   └── penguins_iter.csv      	<- Penguins database
    │
    ├── models             			<- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          			<- Jupyter notebooks. 
    │
    ├── requirements.txt   			<- The requirements file for reproducing the analysis environment, e.g.
    │                         		   generated with `pip freeze > requirements.txt`
    │
    ├── src                			<- Source code for use in this project.
    │   ├── app         			<- FastAPI Implementation	
    │   ├── models         			<- Scripts to train models and then use trained models to make
    │   │   │                 		   predictions
    │   │   └── train.py
    │
    └── Dockerfile            		<- Dockerfile to build docker


--------
