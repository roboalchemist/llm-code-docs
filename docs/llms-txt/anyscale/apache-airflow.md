# Source: https://docs.anyscale.com/ci-cd/apache-airflow.md

# Airflow

[View Markdown](/ci-cd/apache-airflow.md)

# Airflow

Airflow is a platform to programmatically author, schedule, and monitor workflows.

Anyscale provides a [native integration](https://astronomer.github.io/astro-provider-anyscale/) with Airflow to orchestrate:

* **Anyscale jobs**: Submit and monitor an Anyscale job using the operator.
* **Anyscale services**: Deploy and roll out Anyscale services using the operator.

The operators from this integration use deferrable polling to check the status of the Anyscale job or service. This way, they don't occupy a full worker slot while waiting for the job to finish or the service to be deployed.

## Installation[​](#installation "Direct link to Installation")

Install the Anyscale provider using the command below:

```
pip install astro-provider-anyscale
```

## Connect Anyscale to Airflow[​](#connect "Direct link to Connect Anyscale to Airflow")

### Generate an Anyscale API key[​](#generate-an-anyscale-api-key "Direct link to Generate an Anyscale API key")

1. Go to the Anyscale console.
2. Click on your username in the top right corner and select **API Keys**.
3. Click **Create**.

### Airflow connection configuration[​](#connection-config "Direct link to Airflow connection configuration")

To integrate Airflow with Anyscale, configure an Airflow connection with a unique name and set the password to the API token copied from the Anyscale console.

1. **Access Airflow Web UI**: Open the Airflow web interface and log in using your Airflow credentials.

2. **Create a new connection in Airflow**: Go to the **Admin** tab and select **Connections** from the dropdown menu. Click the **Add a new record** button to create a new connection.

3. **Configure the connection**:

   <!-- -->

   1. **Conn Id**: Enter a unique identifier for the connection, example: `anyscale_conn`.
   2. **Conn Type**: Select Anyscale.
   3. **Password**: Paste the API token you copied from the Anyscale console.

4. **Save the connection**: After filling in the required details, click the **Save** button at the bottom of the form to save the new connection.

## Usage[​](#usage "Direct link to Usage")

### Orchestrate an Anyscale job[​](#orchestrate-job "Direct link to Orchestrate an Anyscale job")

To orchestrate an Anyscale job within an Airflow DAG, use the [`SubmitAnyscaleJob`](https://astronomer.github.io/astro-provider-anyscale/api/anyscale_provider.operators.html#anyscale_provider.operators.anyscale.SubmitAnyscaleJob) operator.

```
from datetime import datetime, timedelta
from pathlib import Path

from airflow import DAG

from anyscale_provider.operators.anyscale import SubmitAnyscaleJob

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 4, 2),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the Anyscale connection
ANYSCALE_CONN_ID = "anyscale_conn"

# Constants
FOLDER_PATH = Path(__file__).parent / "ray_scripts"

dag = DAG(
    "sample_anyscale_job_workflow",
    default_args=default_args,
    description="A DAG to interact with Anyscale triggered manually",
    schedule=None,  # This DAG is not scheduled, only triggered manually
    catchup=False,
)

submit_anyscale_job = SubmitAnyscaleJob(
    task_id="submit_anyscale_job",
    conn_id=ANYSCALE_CONN_ID,
    name="AstroJob",
    image_uri="IMAGE_URI",
    compute_config="COMPUTE_CONFIG",
    working_dir=str(FOLDER_PATH),
    entrypoint="python ray-job.py",
    requirements=["requests", "pandas", "numpy", "torch"],
    max_retries=1,
    job_timeout_seconds=3000,
    poll_interval=30,
    dag=dag,
)


# Defining the task sequence
submit_anyscale_job
```

### Orchestrate an Anyscale service[​](#orchestrate-service "Direct link to Orchestrate an Anyscale service")

To orchestrate an Anyscale service within an Airflow DAG, use the [`RolloutAnyscaleService`](https://astronomer.github.io/astro-provider-anyscale/api/anyscale_provider.operators.html#anyscale_provider.operators.anyscale.RolloutAnyscaleService) operator.

```
import uuid
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

from anyscale_provider.hooks.anyscale import AnyscaleHook
from anyscale_provider.operators.anyscale import RolloutAnyscaleService

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 4, 2),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the Anyscale connection
ANYSCALE_CONN_ID = "anyscale_conn"
SERVICE_NAME = f"AstroService-CICD-{uuid.uuid4()}"

dag = DAG(
    "sample_anyscale_service_workflow",
    default_args=default_args,
    description="A DAG to interact with Anyscale triggered manually",
    schedule=None,  # This DAG is not scheduled, only triggered manually
    catchup=False,
)

deploy_anyscale_service = RolloutAnyscaleService(
    task_id="rollout_anyscale_service",
    conn_id=ANYSCALE_CONN_ID,
    name=SERVICE_NAME,
    image_uri="IMAGE_URI",
    compute_config="COMPUTE_CONFIG",
    working_dir="https://github.com/anyscale/docs_examples/archive/refs/heads/main.zip",
    applications=[{"import_path": "sentiment_analysis.app:model"}],
    requirements=["transformers", "requests", "pandas", "numpy", "torch"],
    in_place=False,
    canary_percent=None,
    service_rollout_timeout_seconds=600,
    poll_interval=30,
    dag=dag,
)


def terminate_service():
    hook = AnyscaleHook(conn_id=ANYSCALE_CONN_ID)
    result = hook.terminate_service(service_name=SERVICE_NAME, time_delay=5)
    print(result)


terminate_anyscale_service = PythonOperator(
    task_id="initialize_anyscale_hook",
    python_callable=terminate_service,
    trigger_rule=TriggerRule.ALL_DONE,
    dag=dag,
)

# Defining the task sequence
deploy_anyscale_service >> terminate_anyscale_service
```

## Learn more[​](#learn-more "Direct link to Learn more")

* [`astro-provider-anyscale` documentation](https://astronomer.github.io/astro-provider-anyscale/#).
* [Demo](https://github.com/anyscale/demo-airflow-anyscale).
* [API Reference](https://astronomer.github.io/astro-provider-anyscale/api/anyscale_provider.html).
* [Changelog](https://astronomer.github.io/astro-provider-anyscale/CHANGELOG.html).
