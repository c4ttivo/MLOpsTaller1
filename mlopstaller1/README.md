![alt text](https://github.com/c4ttivo/MLOpsTaller1/mlopstaller1/imgs/main/logo.png?raw=true)

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


![alt text](https://github.com/c4ttivo/MLOpsTaller1/mlopstaller1/imgs/main/console.png?raw=true)

Una vez finalizado la creación de la imagen, se procede a levantar la instancia del contenedor con el siguiente comando


```
# docker run --name nivel_0 -p 8989:80 nivel_0
```

Al levantarse la instancia, ahora es posible consumir los servicios expuestos en la URL http://127.0.0.1/docs#/

![alt text](https://github.com/c4ttivo/MLOpsTaller1/mlopstaller1/imgs/main/fastapi.png?raw=true)

api predictions

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
