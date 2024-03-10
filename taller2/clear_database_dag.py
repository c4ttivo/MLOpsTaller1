from airflow import DAG
from airflow.operators.mysql_operator import MySqlOperator
from datetime import datetime

dag = DAG(
    'clear_database_dag',
    description='Borrar contenido de la base de datos',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
)

clear_database_task = MySqlOperator(
    task_id='clear_database_task',
    mysql_conn_id='mysql_default',
    sql='DELETE FROM your_table_name;',
    dag=dag,
)
