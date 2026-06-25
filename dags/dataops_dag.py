from datetime import datetime
from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator

with DAG(
    dag_id="dataops_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,  # Hatanın çözümü burası! (schedule_interval yerine schedule)
    catchup=False,
    tags=["dataops", "assignment"],
) as dag:

    run_spark_client_job = SSHOperator(
        task_id="run_etl_on_spark_client",
        ssh_conn_id="ssh_spark_client",  
        command="python3 /app/etl_script.py", 
        cmd_timeout=600,
    )