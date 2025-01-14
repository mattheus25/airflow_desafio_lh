from datetime import datetime

from airflow.models import DAG
from airflow.providers.dbt.cloud.operators.dbt import DbtCloudRunJobOperator

### Update these ids to match your account ###
DBT_CLOUD_CONN_ID = "dbt_cloud_desafio"
ACCOUNT_ID = "70471823414386"
JOB_ID = "70471823416476"

with DAG(
    dag_id="dbt_cloud_run_job",
    default_args={"dbt_cloud_conn_id": DBT_CLOUD_CONN_ID, "account_id": ACCOUNT_ID},
    start_date=datetime(2021, 1, 1),
    schedule_interval="0 9 * * *",
    catchup=False,
) as dag:
    trigger_dbt_cloud_job_run = DbtCloudRunJobOperator(
        task_id="trigger_dbt_cloud_job_run",
        job_id=JOB_ID,
        check_interval=10,
        timeout=300,
        retry_from_failure=True,
    )

    trigger_dbt_cloud_job_run