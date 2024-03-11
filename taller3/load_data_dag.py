from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def load_data():
    # Lógica para cargar datos de penguins sin preprocesamiento
    pass

dag = DAG(
    'load_data_dag',
    description='Carga datos de penguins',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
)

load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_data,
    dag=dag,
)
