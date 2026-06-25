from datetime import datetime
from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator

with DAG(
    dag_id="dataops_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["dataops", "assignment"],
) as dag:

    run_spark_client_job = SSHOperator(
        task_id="run_etl_on_spark_client",
        ssh_conn_id="ssh_spark_client",  # Airflow UI'da oluşturacağımız bağlantı adı
        command="python3 /app/etl_script.py", # git-sync'in dosyayı atacağı varsayılan yer
        cmd_timeout=600,
    )

    run_spark_client_job