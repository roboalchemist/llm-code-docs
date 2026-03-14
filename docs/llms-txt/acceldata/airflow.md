# Source: https://docs.acceldata.io/documentation/airflow.md

# Airflow

## Introduction

Apache Airflow is an open-source workflow management platform for data engineering pipelines. Acceldata Airflow SDK provides APIs, decorators, and operators that allow for fine-grained end-to-end tracking and visibility of Airflow DAGs.

## Features provided by acceldata-airflow-sdk:

- `DAG`: A wrapper built on top of Airflow DAG monitors the beginning and end of pipeline execution
- `Pipeline`: Represents an execution of a pipeline inside Airflow
- `Span`: Logical collection of various tasks within Airflow
- `Job`: Logical representation of a task within Airflow
- `Event`: An event can hold process or business arbitrary data and is sent to the ADOC system for future tracking against a pipeline execution

## Installation

Airflow installation details can be found [here](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html).

Users must ensure that the following python modules are installed in the airflow environment.

- [acceldata-sdk](https://pypi.org/project/acceldata-sdk/)
- [acceldata-airflow-sdk](https://pypi.org/project/acceldata-airflow-sdk/)

```bash
pip install acceldata-sdk
pip install acceldata-airflow-sdk
```



## Prerequisites

To authenticate calls to ADOC, API keys are required.

> Users can generate API keys in the ADOC UI's **Admin Central** by visiting the [auto$](/documentation/api-keys) section.> > The API keys and ADOC URL should be set up as environment variables in Airflow before using **acceldata-airflow-sdk** calls in Airflow DAG.

## Establishing Connection between Airflow and the ADOC Server:

This guide outlines two methods for configuring Airflow to interact with the ADOC Server:

### Method 1: Using Environment Variables

Define the following environment variables within your Airflow environment (for example, in your Docker container, `.env` file, or deployment configuration): 

| Environment Variables | Description | Required | Default | 
| ---- | ---- | ---- | ---- | 
| `TORCH_CATALOG_URL` | URL of your ADOC (Torch) server instance. | ✅ | — | 
| `TORCH_ACCESS_KEY` | API access key generated from the ADOC UI. | ✅ | — | 
| `TORCH_SECRET_KEY` | API secret key generated from the ADOC UI. | ✅ | — | 
| `ENABLE_VERSION_CHECK` | Enables or disables SDK and ADOC version compatibility checks. | ❌ | `False` | 
| `TORCH_CONNECTION_TIMEOUT_MS` | Maximum time (in milliseconds) to wait while establishing a connection to the ADOC server. | ❌ | `5000 ms` | 
| `TORCH_READ_TIMEOUT_MS` | Maximum time (in milliseconds) to wait for a response from the ADOC server after a successful connection. | ❌ | `15000 ms` | 


**Example:**

```bash
export TORCH_CATALOG_URL=https: //your-adoc-server
export TORCH_ACCESS_KEY=<your_access_key>
export TORCH_SECRET_KEY=<your_secret_key>
export ENABLE_VERSION_CHECK=False
export TORCH_CONNECTION_TIMEOUT_MS=10000
export TORCH_READ_TIMEOUT_MS=20000
```



Info These environment variables are automatically picked up by the Airflow SDK during DAG or task execution.

### Method 2: Using Airflow Connection

You can also configure the connection directly in the **Airflow UI** by performing the following steps:

1. **Create an Airflow Connection:**
    - Log in to your Airflow UI.
    - Navigate to the **Admin** &gt; **Connections** section.
    - Click **+ Create** to add a new connection.

2. **Configure Connection Details:**
    - Enter a unique identifier for the connection (e.g., `adoc_conn`).
    - Set the **Conn Type** to `HTTP`.
    - Enter the URL of your ADOC (Torch) server in the **Host** field.
    - Enter the API access key from the ADOC UI in the **Login** field.
    - Enter the API secret key from the ADOC UI in the **Password** field.
    - (Optional) In the **Extra** field, enter the following JSON:

```json
{
  "ENABLE_VERSION_CHECK": false,
  "TORCH_CONNECTION_TIMEOUT_MS": 10000,
  "TORCH_READ_TIMEOUT_MS": 20000
}
```



You can toggle version checking or adjust timeouts as needed:

```json
{"ENABLE_VERSION_CHECK": true}
```



### Steps to Set up Airflow DAG

Before using the features provided by the acceldata-airflow-sdk, users must first set up Airflow DAG scripts with a few steps.

### Minimum Instrumentation Required

### Step 1. Use acceldata-airflow-sdk DAG Object

Acceldata-airflow-sdk tracks the end of the DAG run using customized DAG.

Users must import DAG from `acceldata_airflow_sdk.dag` and replace Airflow DAG with `acceldata-airflow-sdk` DAG in the DAG script. This will enable you to terminate the pipeline run based on the success or failure of the DAG execution in Airflow. This was accomplished by utilizing Airflow's success and failure callbacks.

When utilizing the `acceldata-airflow-sdk` DAG, you must include the pipeline uid, which will be updated in ADOC to track the DAG being performed in Airflow.

```python
from acceldata_airflow_sdk.dag import DAG
pipeline_uid = "torch.airflow.pipeline"
default_args = {'start_date': datetime(2022, 5, 31)}
dag = DAG(
    dag_id='TEST_CUSTOMERS_ETL',
    schedule_interval=None,
    default_args=default_args,
    start_date=datetime(2022, 6, 6)
)
```



### Step 2. Setup TorchInitializer Task

Acceldata-airflow-sdk uses the `TorchInitializer` task to track the beginning of the DAG run by creating a pipeline and pipeline run along with an all-encompassing root span.

Create a task for the `TorchInitializer` operator and add it as the DAG's root (first) task. Inside the `TorchInitializer` operator, Acceldata-airflow-sdk establishes a connection to ADOC using the `TorchClient` class, which employs the credentials specified in the environment variables above. Using the `TorchClient` connection, the `TorchInitializer` operator creates a new pipeline if one does not already exist, a new pipeline run for each DAG run, and a root span to bind the entire pipeline run. Users can create a pipeline in the Torch UI and then provide the UID of that pipeline in `TorchInitializer`. In that case, a new pipeline will not be used.

```python
from acceldata_airflow_sdk.operators.torch_initialiser_operator import TorchInitializer
from acceldata_sdk.models.pipeline import PipelineMetadata
torch_initializer_task = TorchInitializer(
    task_id='torch_pipeline_initializer',
    pipeline_uid=pipeline_uid,
    pipeline_name=pipeline_name,
    connection_id=torch_connection_id,
    meta=PipelineMetadata(owner='Demo', team='demo_team', codeLocation='...'),
    dag=dag
)
```



> ADOC can now track the entire DAG as a single unit after performing these two steps.

## Tracking Each Task

To allow ADOC to provide a fine-grained view of the DAG, users must add more instrumentation to the DAG code, as described in the sections below.

### Tracking Each Task Using Jobs

Each task should be decorated with a job decorator and input, output, and metadata should be passed as arguments to make it visible as a job in the ADOC pipeline. The task's inputs should be described in the inputs list, and the task's output asset should be described in the outputs list. The `job_uid` parameter is used to specify a custom `job_uid`, which is generated by default. Furthermore, if users do not want the job to be bounded by a span, the `bounded_by_span` argument can be set to False.

### Obtaining the Asset's UID for Use in the Input and Output List

![](https://uploads.developerhub.io/prod/Yoq2/08b2qipj2oyt6xdvn1goe53km2cvw59wiuveghy0pct7eum8w7lpd1vlznxenkeu.png)

To obtain the UID of an asset, the user must first open an asset in the ADOC UI. A path to the asset is shown in the asset under the Asset name, as shown in the image above. The first part highlighted in green is the data source name, and the remaining items can be used as asset names by using a period as a field separator. The data source name in this example is `ATHENA-DS`, and the asset name is `AwsDataCatalog.sampledb.elb_logs.request_processing_time`.

This asset can be used as an input with the following syntax: `inputs=[Node(asset uid='ATHENA-DS.AwsDataCatalog.sampledb.elb_logs.request_processing_time')] ,`

### Subdividing a Task into Multiple Spans

Users can represent a single task with multiple steps in multiple child spans with `create_child_span` and send events for those child spans. To create a child span, users must first obtain the parent span context, which returns us to the root span. Users must use the parent span context to call create child span, and it will appear as child span in the ADOC pipelines view.

```python
from acceldata_sdk.models.job import JobMetadata, Node
from acceldata_airflow_sdk.decorators.job import job
@job(
     inputs=[Node(asset_uid=f'{athena_ds}.{athena_table}')],
     outputs=[Node(asset_uid=f'{redshift_ds}.{rs_table_approved_name}'), Node(job_uid='data_quality_check')],
     metadata=JobMetadata('BEN', 'finance', 'https://github.com/finance/reports/rds_customers.kt')
     )
def athena_to_redshift(**context):
    parent_span_context = context['span_context_parent']
    athena_result_span = parent_span_context.create_child_span(
        uid="athena.finance.approved_result",
        context_data={'client_time': str(datetime.now())}
    )
    ...
    athena_result_span.send_event(
        GenericEvent(
            context_data={
                'client_time': str(datetime.now())
            },
            event_uid="finance.athena.approved_result"
        )
    )
    athena_result_span.end(
        context_data={'client_time': str(datetime.now())}
    )

    ....
    redshift_upload_span = parent_span_context.create_child_span(
        uid="redshift.data.approved_upload",
        context_data={'client_time': str(datetime.now())}
    )

    ...
    redshift_upload_span.send_event(
        GenericEvent(
            context_data={
                'client_time': str(datetime.now())
            },
            event_uid="finance.redshift.approved_upload"
        )
    )
    redshift_upload_span.end(
        context_data={'client_time': str(datetime.now())}
    )
```



### Tracking Tasks Created with Airflow Operators

In some cases, users may prefer to use an Airflow operator such as PostgresOperator or ExecutePolicyOperator provided by the Airflow SDK instead of `PythonOperator`. A JobOperator has been provided to wrap such tasks, create the corresponding job, and bind it with span.

> If JobOperator is being used to wrap another operator, such as ExecutePolicyOperator in this case, the DAG argument should not be specified.

```python
from acceldata_airflow_sdk.operators.job_operator import JobOperator
from acceldata_airflow_sdk.operators.execute_policy_operator import ExecutePolicyOperator
from acceldata_sdk.models.job import JobMetadata, Node
import acceldata_sdk.constants as const

syncoperator_task = ExecutePolicyOperator(
    task_id='torch_pipeline_syncop_test',
    rule_type=constants.policy_type,
    rule_id=constants.policy_id,
    failure_strategy=const.FailureStrategy.FailOnWarning,
    sync=True
)

# Wrap the policy operator with the Job operator so that a job is created for the policy execution
sync_operator_wrap_job_task = JobOperator(
    task_id='syncoperator_task',
    inputs=[Node(asset_uid='POSTGRES_LOCAL_DS.pipeline.pipeline.customer_orders2')],
    outputs=[Node(asset_uid='POSTGRES_LOCAL_DS.pipeline.pipeline.customer_orders3')],
    metadata=JobMetadata('name', 'team', 'code_location'),
    operator=syncoperator_task,
    dag=dag
)
```



### Linking a Task with Another Task

In previous examples, each pipeline job takes an asset as input and produces another asset as output, which the next job will use as input. Acceldata-airflow-sdk uses these to connect jobs in the ADOC pipeline UI. However, there may be times when a task does not produce another asset as an output. `ExecutePolicyOperator` is used to execute a policy and generate a result. In such cases, users can provide a job_uid as output instead of an asset to link the next job.

```python
@job(job_uid='data_quality_check',
     outputs=[Node(job_uid='quality.customers.athena')],
     metadata=JobMetadata('BEN', 'finance', 'https://github.com/finance/reports/rds_customers.kt')
     )
def syncoperator_result(**context):
  ...
```



In this getting-started guide, we looked at how to use Acceldata Airflow SDK decorators and operators to make Airflow DAG visible in ADOC pipelines' UI. In addition, we investigated the use of operators to implement Data Quality policies and provide job-to-job linking.