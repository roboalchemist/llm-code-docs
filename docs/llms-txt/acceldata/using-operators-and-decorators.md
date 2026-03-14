# Source: https://docs.acceldata.io/documentation/using-operators-and-decorators.md

# Using Operators and Decorators

#### Decorators in Python

A decorator is a Python design pattern that allows a user to add new functionality to an existing object without modifying its structure. A decorator accepts a function, adds some functionality, and returns it. The SDK has provided Job and Span decorators to simplify instrumenting an Airflow DAG using this design pattern.

#### Operators in Airflow

An operator is a template for a predefined Task that you can define declaratively within your DAG. Airflow operator tasks could not be used with the decorator design pattern. As a result, the SDK includes JobOperator and SpanOperator to simplify instrumentation for tasks created for operators which do not use PythonOperator.

## Features Provided by Acceldata Airflow SDK

- [Create Job and Span Using Job Decorator](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/using-operators-and-decorators#create-job-and-span-using-job-decorator)
- [Create Span Using Decorator](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/using-operators-and-decorators#create-span-using-decorator)
- [JobOperator OPERATOR](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/using-operators-and-decorators#joboperator-operator)
- [SpanOperator OPERATOR](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/using-operators-and-decorators#spanoperator-operator)

### Create Job and Span Using Job Decorator

To create a job and span in the pipeline, the user must decorate the python function with a job decorator, as shown below.

Object of `Node` should have either asset_uid ( {data source}.{asset path from its root}) or job_uid (Uid of next Job) as parameters.

The parameters for a job decorator include:

| Parameter | Description | 
| ---- | ---- | 
| span_uid | A **String** parameter to specify the UID of the span to be created. The default value is **None**. If `span_uid` is not provided, a span corresponding to the job will be created with the value `job_uid`. | 
| job_uid | A **String** parameter to specify the job UID of the pipeline. The default value is **None**. If `job_uid` is not provided, uid is constructed using the `dag_id`, `task_id` and function name. | 
| inputs | An **Array** parameter of Node type objects being used by the job as input. The default value is an empty array. | 
| outputs | An **Array** parameter of Node type objects being returned by the job as output. The default value is an empty array. | 
| metadata | Parameter of type **JobMetadata** specifying the metadata of the job. The default value is **None**. | 
| xcom_to___event_mapper_ids | A **list** parameter having a list of xcom keys used to send xcom variables in span event. The default value is an empty list. | 
| bounded_by_span | A **Boolean** parameter deciding whether to create a span along with the Job. The default value is **True**. If it is set to `True` to create a span, make sure it has `**context` parameter inside the function argument. Th gives access to the context of the task. Using the context, various span events can be sent inside the function. Use `span_context = context['span_context_parent']` to get you the span context. | 


```python
from acceldata_airflow_sdk.decorators.job import job
from acceldata_sdk.models.job import JobMetadata, Node
@job(job_uid='monthly.order.aggregate.job',
   inputs=[Node(asset_uid='POSTGRES_LOCAL_DS.pipeline.pipeline.customer_orders')],
   outputs=[Node(job_uid='Job2_uid')],
   metadata=JobMetadata(name = 'Vaishvik_brahmbhatt', team = 'backend', code_location ='https://github.com/acme/reporting/report.scala'),
   span_uid='customer.orders.datagen.span',
   xcom_to_event_mapper_ids = ['run_id', 'event_id'],
   bounded_by_span=True
   )
def monthly_order_aggregate(**context):
    pass
```



### Create Span Using Decorator

A span for a python function can be created by decorating a python function with a span decorator that takes span uid as parameters. Add the `**context` parameter inside the function argument to decorate it with span. This provides access to the task's context. Various span events can be sent inside the function using the context. The parent span context can be extracted from the `context` dict using the key name `span_context_parent`, for example `datagen_span_context = context['span context parent']`. It will return be a span context instance that can be used to create child spans and send custom events as shown in the below example.

The parameters for a span decorator include:

| Parameter | Description | 
| ---- | ---- | 
| span_uid | A **String** parameter to specify the UID of the span to be created. It is a mandatory parameter. | 
| xcom_to_event_mapper_ids | A parameter having a list of xcom keys used to send xcom variables in span event. The default value is an empty list. | 


```python
from acceldata_airflow_sdk.decorators.span import span
from acceldata_sdk.events.generic_event import GenericEvent
@span(span_uid='customer.orders.datagen.span',
      associated_job_uids = ['monthly.order.aggregate.transfer'],  xcom_to_event_mapper_ids = ['run_id', 'event_id'] )
def data_gen(**context):
   datagen_span_context = context['span_context_parent']
   customer_datagen_span = datagen_span_context.create_child_span(
       uid="customer.data.gen", 
      context_data= {'client_time': str(datetime.now()) }
   )
   customer_datagen_span.send_event(
      GenericEvent(
         context_data={
            'client_time': str(datetime.now()), 
            'row_count': len(rows)
         }, 
         event_uid="order.customer.join.result"
      )
   )
   customer_datagen_span.end(
       context_data={'client_time': str(datetime.now()), 'customers_count': len(customer_ids) }
   )
```



### JobOperator OPERATOR

In some cases, users may prefer to use an Airflow operator such as `PostgresOperator` or `ExecutePolicyOperator` provided by the Airflow SDK instead of `PythonOperator`. A `JobOperator` has been provided to wrap such tasks, create the corresponding job, and bind it with span in order to instrument them.

`JobOperator` will execute any std operator passed as an `operator` parameter, create a job, and send span start and end events. Simply wrap the std operator in a `JobOperator`. Check that the wrapped operator is not included in the DAG. If the operator is wrapped in a `JobOperator`, the `JobOperator` will handle the operator's task within its execution.

As parameters, `Node` objects should have either `asset_uid` (data source.asset path from its root) or `job_uid` (UID of next job).

The parameters for a JobOperator include:

| Parameter | Description | 
| ---- | ---- | 
| span_uid | A **String** parameter to specify the UID of the span to be created. The default value is **None**. If `span_uid` is not provided, a span corresponding to the job will be created with the value `job_uid`. | 
| job_uid | A **String** parameter to specify the job UID of the pipeline. The default value is **None**. If `job_uid` is not provided, uid is constructed using the `dag_id`, `task_id` and function name. | 
| inputs | An **Array** parameter of Node type objects being used by the job as input. The default value is an empty array. | 
| outputs | An **Array** parameter of Node type objects being returned by the job as output. The default value is an empty array. | 
| metadata | Parameter of type **JobMetadata** specifying the metadata of the job. The default value is **None**. | 
| xcom_to _vent_mapper_ids | A **list** parameter having a list of xcom keys used to send xcom variables in span event. The default value is an empty list. | 
| bounded_by_span | A **Boolean** parameter deciding whether to create a span along with the Job. The default value is **True**. If it is set to `True` to create a span, make sure it has `**context` parameter inside the function argument. Th gives access to the context of the task. Using the context, various span events can be sent inside the function. Use `span_context = context['span_context_parent']` to get you the span context. | 
| operator | A parameter specifying the Standard airflow operator. It is a mandatory parameter. | 


Other parameters will be the same as the base operator for the airflow standard. Make sure that the type of object inside a Node has `asset_uid` (data source.asset path from its root) or `job_uid` (UID of next Job) as parameters.

> Do not specify the `dag` parameter in the std airflow operator being passed as an argument to JobOperator as the execution of the operator task is taken care of by JobOperator.

> If JobOperator is being used to wrap another operator ExecutePolicyOperator in this case, then the ExecutePolicyOperator task should not specify dag argument.

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

# Wrap the policy operator with the JobOperator so that a job is created for the policy execution
sync_operator_wrap_job_task = JobOperator(
    task_id='syncoperator_task',
    inputs=[Node(asset_uid='POSTGRES_LOCAL_DS.pipeline.pipeline.customer_orders2')],
    outputs=[Node(asset_uid='POSTGRES_LOCAL_DS.pipeline.pipeline.customer_orders3')],
    metadata=JobMetadata('name', 'team', 'code_location'),
    operator=syncoperator_task,
    dag=dag
)
```



### SpanOperator OPERATOR

SpanOperator will execute any std operator passed as an `operator` parameter, create a span, and send span start and end events. Simply wrap the std operator with a span operator. Check that the wrapped operator has not been added to the DAG. If the operator is wrapped by a span operator, the span operator will handle the operator task within its execution.

| Parameter | Description | 
| ---- | ---- | 
| span_uid | A **String** parameter to specify the UID of the span to be created. The default value is **None**. If `span_uid` is not provided, a span corresponding to the job will be created with the value `job_uid`. | 
| xcom_to_vent_mapper___ids | A **list** parameter having a list of xcom keys used to send xcom variables in span event. The default value is an empty list. | 
| operator | A parameter specifying the Standard airflow operator. It is a mandatory parameter. | 


Other parameters will be the same as the airflow standard base operator.

> Do not specify the `dag` parameter in std airflow operator being passed as an argument to SpanOperator as the execution of operator task is taken care of by SpanOperator.

```python
from torch_airflow_sdk.operators.span_operator import SpanOperator

get_order_agg_for_q4 = PostgresOperator(
   task_id="get_monthly_order_aggregate_last_quarter",
   postgres_conn_id='example_db',
   sql="select * from information_schema.attributess",
)

get_order_agg_for_q4 = SpanOperator(
   task_id="get_monthly_order_aggregate_last_quarter",
   span_uid='monthly.order.agg.q4.span',
   operator=get_order_agg_for_q4,
   associated_job_uids = ['monthly.order.aggregate.transfer'],  
   xcom_to_event_mapper_ids = ['run_id', 'event_id'] ,
   dag=dag
)
```



### Creating Airflow Connection

If you want to avoid using environment variables, you can create a connection in the Airflow UI as described below, and provide the connection id of that connection in the TorchInitializer. Set the following for the connection:

- Conn id: Create a unique ID for the connection
- Conn Type: HTTP
- Host - URL of the torch catalogue
- Login - API access key generated from torch UI
- Password - API secret key generated from torch UI
- Extra - **{"ENABLE_VERSION_CHECK": true}**. This value will enable or disable the version compatibility checks between Torch and SDK. The default value is 'True'. To disable the version check, set it to 'False'.

### TorchInitializer Operator

At the root of the dag, you must add a task with a TorchInitializer Operator. This operator will build a new pipeline. This will also generate a new pipeline run and root span for that dag run of the Airflow dag.

The parameters for TorchInitializer Operator include:

| Parameter | Description | 
| ---- | ---- | 
| create_pipeline | A Boolean parameter that determines whether to create a pipeline (if one does not already exist) and run the pipeline. The default value is 'True'. If a pipeline or pipeline run was created outside of Airflow DAG, this can be useful. | 
| span_name | A string parameter specifying the name of the Root Span. The default value is 'None'.  If no name is provided, the pipeline_uid.span will be used as the span name. | 
| meta | A parameter that specifies the pipeline's metadata (PipelineMetadata). The default value is 'None'. If it is not provided, PipelineMetadata(owner='sdk/pipeline-user', team='TORCH', codeLocation='...') is set as meta. | 
| pipeline_uid | A string parameter specifying the pipeline's UID. It is a required parameter. | 
| pipeline_name | A string parameter specifying the name of the pipeline. The default value is 'None'. If it is not provided, pipeline_uid will be used as the name. | 
| continuation_id | A string parameter that uniquely identifies a pipeline run. This parameter can accept jinja templates as well. The default value is 'None'. When we want a pipeline run to span multiple DAGs, we can use this parameter. To use it, we must provide a continuation id when creating the pipeline in the first DAG with create_pipeline=True, and then provide the same continuation id when continuing the same pipeline run in the second DAG with create_pipeline=False. | 
| connection_id | A string parameter that uniquely identifies a Torch credentials-storing connection. The default value is 'None'. When we want to use Torch credentials from the Airflow connection instead of environment variables, we can use this parameter. Refer to the **Creating Airflow Connection** section above for more information. | 


```python
from acceldata_airflow_sdk.operators.torch_initialiser_operator import TorchInitializer
from acceldata_sdk.models.pipeline import PipelineMetadata

# example of jinja templates being used in continuation_id
# jinja template to pull value from config json
# continuation_id=f"{{{{ dag_run.conf['continuation_id']  }}}}"
# jinja template to pull value from xcom
# continuation_id=f"{{{{ task_instance.xcom_pull(key='continuation_id') }}}}"

torch_initializer_task = TorchInitializer(
   task_id='torch_pipeline_initializer',
   pipeline_uid='customer.orders.monthly.agg.demo',
   pipeline_name='CUSTOMERS ORDERS MONTHLY AGG',
   continuation_id='heterogeneous_test',
   create_pipeline=True,
   span_name='customer.orders.monthly.agg.demo.span',
   meta=PipelineMetadata(owner='test', team='testing', codeLocation='...'),
   connection_id=torch_connection_id,
   dag=dag
)
```



> Here is an example demonstrating usage of all the decorators and operators provided in airflow-sdk:> > [Decorators and Operators](https://bitbucket.org/acceldata/ad-pipelines-integ-example/src/master/airflow/full_code/05example/)