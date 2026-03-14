# Source: https://docs.acceldata.io/documentation/sdk-apis.md

# SDK APIs

## Introduction

ADOC is a complete solution for monitoring the quality of data in your data lake and warehouse. You can use ADOC to ensure that your business decisions are supported by high-quality data. ADOC provides tools for measuring the quality of data in a data catalog and ensuring that important data sources are never overlooked. All users, including analysts, data scientists, and developers, can rely on ADOC to monitor data flow in the warehouse or data lake and ensure that no data is lost.

The ADOC catalog and pipeline APIs are triggered by the Acceldata SDK.

## Features Provided by Acceldata SDK

- [Pipeline APIs](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/sdk-apis#pipeline-apis)
- [Datasource APIs](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/sdk-apis#datasource-apis) 

## Prerequisites

1. Install the `acceldata-sdk` [PyPI package](https://pypi.org/project/acceldata-sdk/) in a Python environment: `pip install acceldata-sdk`
2. Create ADOC client: ADOC clients are used to send data to ADOC servers. They include several methods for communicating with the server. ADOC clients have access to the APIs for data reliability and pipelines. ADOC URLs and API keys are required to create an ADOC client. Go to the ADOC's UI's settings, and generate keys for the client to generate [API Keys](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/api-keys).

```python
from acceldata_sdk.torch_client import TorchClient

torch_client = TorchClient(url='https://acceldata.host.dev:9999', access_key='******',
                         secret_key='*****************')
```



> The mention of **Torch** denotes ADOC.

## Optional Configuration Parameters

You can customize connection and read timeouts while initializing the `TorchClient` for **v4.8.4** SDK versions and above. These parameters allow you to control how long the client waits while connecting to and communicating with the ADOC server.

| **Parameter** | **Type** | **Description** | **Default** | 
| ---- | ---- | ---- | ---- | 
| `torch_connection_timeout_ms` | `int` | Maximum time (in milliseconds) to wait while establishing a connection to the ADOC server. | `5000 ms` | 
| `torch_read_timeout_ms` | `int` | Maximum time (in milliseconds) to wait for a response from the ADOC server after a successful connection. | `15000 ms` | 


Example:

```json
from acceldata_sdk import TorchClient

torch_client = TorchClient(
    url="<torch_url>",
    access_key="<api_access_key>",
    secret_key="<api_secret_key>",
    torch_connection_timeout_ms=10000,
    torch_read_timeout_ms=20000
)
```



## Pipeline APIs

Acceldata SDK supports a number of pipeline APIs such as, creating a pipeline, adding jobs and spans, initiating pipeline runs, and so on. During the span life cycle, Acceldata SDK can send various events. As a result, Acceldata SDK has complete control over the pipelines.

### Create Pipeline and Job

A pipeline represents the entire ETL (Extract, Transform, Load) pipeline including Asset nodes and Job nodes. The Lineage graph for all data assets is formed by the complete pipeline definition.

A Job node or Process node is an entity that performs a task in the ETL workflow. According to this representation, a job's input is some assets or other jobs, and its output is a few other assets or jobs. ADOC will create the Lineage using the set of jobs definitions in the workflow and track version changes for the Pipeline.

To begin creating pipelines and jobs, create a creation object with the necessary parameters. And, using SDK-supported methods, you can perform corresponding operations on the ADOC server side.

Acceldata SDK (Software Development Kit) provides the CreateJob class which needs to be passed to the create_job function as a parameter to create a job.

The parameters required include:

| Parameter | Description | 
| ---- | ---- | 
| uid | Unique Id of the job. It is a mandatory parameter. | 
| name | Name of the job. It is a mandatory parameter. | 
| pipeline_run_id | Id of the pipeline run for which you want to add the job. This parameter is mandatory if a job is created using a pipeline. It is not required if a job is created using a pipeline run. | 
| description | Description of the job. | 
| inputs | Input for the job. This could be the uid of an asset specified using the asset uid Node object parameter or it could be the uid of another job specified using the job uid Node object parameter. | 
| outputs | Output for the job. This could be the uid of an asset specified using the asset uid Node object parameter or it could be the uid of another job specified using the job uid Node object parameter. | 
| meta | Metadata of the job. | 
| context | Context of the job. | 
| bounded_by_span | This parameter is of boolean value. If the job needs to be bound by a span, this must be set to True. False is the default value. It is an optional parameter. | 
| span_uid | This is the new span's uid, which is a string. If the value of bounded by span is set to True, this parameter is mandatory. | 


```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_sdk.models.job import CreateJob, JobMetadata, Node
from acceldata_sdk.models.pipeline import CreatePipeline, PipelineMetadata, PipelineRunResult, PipelineRunStatus

# Create pipeline
pipeline = CreatePipeline(
    uid='monthly_reporting_pipeline',
    name='Monthly reporting Pipeline',
    description='Pipeline to create monthly reporting tables',
    meta=PipelineMetadata('Vaishvik', 'acceldata_sdk_code', '...'),
    context={'key1': 'value1'}
)
torch_client = TorchClient(url="https://torch.acceldata.local", access_key="*******",
                          secret_key="******************************",do_version_check=False)
pipeline_response = torch_client.create_pipeline(pipeline=pipeline)
pipeline_run = pipeline_response.create_pipeline_run()
# Create a job using pipeline object.
# Passing of pipeline_run_id is mandatory
job = CreateJob(
    uid='monthly_sales_aggregate',
    name='Monthly Sales Aggregate',
    description='Generates the monthly sales aggregate tables for the complete year',
    inputs=[Node(asset_uid='datasource-name.database.schema.table_1')],
    outputs=[Node(job_uid='job2_uid')],
    meta=JobMetadata('vaishvik', 'backend', 'https://github.com/'),
    context={'key21': 'value21'},
    bounded_by_span=True,
    pipeline_run_id=pipeline_run.id,
    span_uid="test_shubh"
)
job_response = pipeline_response.create_job(job)
# Create a job using pipeline_run object.
# Passing of pipeline_run_id is not needed
job = CreateJob(
    uid='monthly_sales_aggregate_r',
    name='Monthly Sales Aggregate',
    description='Generates the monthly sales aggregate tables for the complete year',
    inputs=[Node(asset_uid='datasource-name.database.schema.table_1')],
    outputs=[Node(job_uid='job2_uid')],
    meta=JobMetadata('vaishvik', 'backend', 'https://github.com/'),
    context={'key21': 'value21'}
)
job_response_using_run = pipeline_run.create_job(job)
```



### Create Pipeline Run and Generate Spans and Send Span Events

A pipeline run denotes the pipeline's execution. The same pipeline can be run multiple times, with each execution (run) producing a new snapshot version. A hierarchical span group exists for each pipeline run. A span is a hierarchical way of grouping a number of metrics. It can be as specific as you want. The APIs will allow you to create a span object from a pipeline object, and then start hierarchical spans from parent spans.

A span is typically a process or a task that can be granular. This hierarchical system is capable of simulating highly complex pipeline observability flows. Optionally, a span can also be associated with a job. This way, we can track the start and completion of the job, as well as failure tracking. For a span, start and stop are implicitly tracked.

Acceldata SDK also allows you to create new pipeline runs and add spans to them. SDK can send some custom and standard span events during the span life cycle to collect pipeline run metrics for observability.

The create_span function's parameters available under a pipeline run are:

| Parameter | Description | 
| ---- | ---- | 
| uid | The uid of the span being created. This should be unique. This is a mandatory parameter. | 
| associatedJobUids | List of job uids with which the span needs to be associated with. | 
| context_data | This is dict of key-value pair providing custom context information related to a span. | 


The `create_child_span` function's parameters which are available under `span_context`. By placing a span under another span, this is used to create a hierarchy of spans.

| Parameter | Description | 
| ---- | ---- | 
| uid | The uid of the span being created. This should be unique. This is a mandatory parameter. | 
| context_data | List of job uids with which the span needs to be associated with. | 
| associatedJobUids | List of job uids with which the span needs to be associated with. | 


```python
from acceldata_sdk.events.generic_event import GenericEvent
from datetime import datetime

# create a pipeline run of the pipeline
pipeline_run = pipeline_response.create_pipeline_run()

# get root span of a pipeline run
root_span = pipeline_run.get_root_span()

# create span in the pipeline run
span_context = pipeline_run.create_span(uid='monthly.generate.data.span')

# check current span is root or not
span_context.is_root()

# end the span 
span_context.end()

# check if the current span has children or not
span_context.has_children()

# create a child span
child_span_context = span_context.create_child_span('monthly.generate.customer.span')

# send custom event
child_span_context.send_event(
    GenericEvent(context_data={'client_time': str(datetime.now()), 'row_count': 100}, 
                 event_uid="order.customer.join.result")
)


# abort span
child_span_context.abort()

# failed span
child_span_context.failed()

# update a pipeline run of the pipeline
updatePipelineRunRes = pipeline_run.update_pipeline_run(context_data={'key1': 'value2', 'name': 'backend'},
                                                               result=PipelineRunResult.SUCCESS,
                                                               status=PipelineRunStatus.COMPLETED)
```



### Get Latest Pipeline Run

Acceldata SDK can obtain a pipeline run with a specific pipeline run id. The pipeline run instance allows you to continue the ETL pipeline and add spans, jobs, and events. As a result, Acceldata SDK has full access to the ADOC pipeline service.

The parameters required include:

| Parameter | Description | 
| ---- | ---- | 
| pipeline_run_id | Run Id of the pipeline run. | 
| continuation_id | Continuation Id of the pipeline run. | 
| pipeline_id | Id of the pipeline to which the run belongs to. | 


```python
pipeline_run = torch_client.get_pipeline_run(pipeline_run_id=pipeline_run_id)
pipeline = torch_client.get_pipeline(pipeline_id=pipeline_id)
pipeline_run = torch_client.get_pipeline_run(continuation_id=continuation_id, pipeline_id=pipeline.id)
pipeline_run = pipeline.get_run(continuation_id=continuation_id)
```



### Get Pipeline Details for a Particular Pipeline Run ID

The Acceldata SDK can obtain pipeline details for a specific pipeline run.

```python
pipeline_details = pipeline_run.get_details()
```



### Get All Spans for a Particular Pipeline Run ID

Acceldata SDK can retrieve all spans for a specific pipeline run id.

```python
pipeline_run_spans = pipeline_run.get_spans()
```



### Get Pipeline Runs for a Pipeline

All pipeline runs are accessible via the Acceldata SDK.

The parameters required include:

| Parameter | Description | 
| ---- | ---- | 
| pipeline_id | The ID of the pipeline | 


```python
runs = torch_client.get_pipeline_runs(pipeline_id)
runs = pipeline.get_runs()
```



### Get All Pipelines

All pipelines are accessible via the Acceldata SDK.

```python
torch_client.get_pipelines()
```



### Delete a Pipeline

Acceldata SDK can delete a pipeline.

```python
delete_response = pipeline.delete()
```



### Using Continuation Id to Continue the Same Pipeline Across Different ETL Scripts Example

A new pipeline run is created in this instance of ETL1 using a continuation id, but the pipeline run is not closed.

```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_sdk.models.pipeline import CreatePipeline, PipelineMetadata, PipelineRunResult, PipelineRunStatus
# Create pipeline
pipeline_uid = 'monthly_reporting_pipeline'
pipeline = CreatePipeline(
    uid=pipeline_uid,
    name='Monthly reporting Pipeline',
    description='Pipeline to create monthly reporting tables',
    meta=PipelineMetadata('Vaishvik', 'acceldata_sdk_code', '...'),
    context={'key1': 'value1'}
)
torch_client = TorchClient(url="https://torch.acceldata.local", access_key="*******",
                          secret_key="******************************",do_version_check=False)
pipeline_response = torch_client.create_pipeline(pipeline=pipeline)
# A new continuation id should be generated on every run. Same continuation id cannot be reused.
cont_id = "continuationid_demo_1"
pipeline_run = pipeline_response.create_pipeline_run(continuation_id=cont_id)
# Make sure pipeline_run is not ended using the update_pipeline_run call so that same run can be used in next ETL script
```



ETL2 - This script will carry on the pipeline run that was started by ETL1.

```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_sdk.models.pipeline import PipelineRunResult, PipelineRunStatus
torch_client = TorchClient(url="https://torch.acceldata.local", access_key="*******",
                          secret_key="******************************",do_version_check=False)
pipeline_uid = 'monthly_reporting_pipeline'
# First get the same pipeline using the previously used UID. Then we will get the previously started pipeline_run using the continuation_id
pipeline = torch_client.get_pipeline(pipeline_uid)
# continuation_id should be a same ID used in ETL1 script so that same pipeline_run is continued in the pipeline.
cont_id = "continuationid_demo_1"
pipeline_run = pipeline.get_run(continuation_id=cont_id)
# Use this pipeline run to create span and jobs
# At the end of this script close the pipeline run using update_pipeline_run if we do not want to continue the same pipeline_run further
updatePipelineRunRes = pipeline_run.update_pipeline_run(context_data={'key1': 'value2', 'name': 'backend'},
                                                               result=PipelineRunResult.SUCCESS,
                                                               status=PipelineRunStatus.COMPLETED)
```



## Datasource APIs

Acceldata SDK also has full access to catalog APIs. ADOC can also crawl more than fifteen different data sources.

```python
# Get datasource
ds_res = torch_client.get_datasource('snowflake_ds_local')
ds_res = torch_client.get_datasource(5, properties=True)

# Get datasources based on the type
datasources = torch_client.get_datasources(const.AssetSourceType.SNOWFLAKE)
```



### Crawler Operations

You can start the crawler and check the crawler's status.

```python
# Start a crawler
datasource.start_crawler()
torch_client.start_crawler('datasource_name')

# Get running crawler status
datasource.get_crawler_status()
torch_client.get_crawler_status('datasource_name')
```



## Assets APIs

### Get Asset Details Using an Asset Identifier like Asset ID/UID

Acceldata SDK includes methods for retrieving assets from a given data source.

```python
from acceldata_sdk.models.create_asset import AssetMetadata

# Get asset by id/uid
asset = torchclient.get_asset(1)
asset = torch_client.get_asset('Feature_bag_datasource.feature_1')
```



### Get All Asset Types in ADOC

```python
asset_types = torch_client.get_all_asset_types()
```



### Asset's Tags, Labels, Metadata, and Sample Data

Using the SDK, you can add tags, labels, and custom metadata, as well as obtain sample data for the asset. Tags and labels can be used to quickly filter out assets.

```python
# asset metadata
from acceldata_sdk.models.tags import AssetLabel, CustomAssetMetadata
asset = torch_client.get_asset(asset_id)

# Get metadata of an asset
asset.get_metadata()

# Get all tags
tags = asset.get_tags()

# Add tag asset
tag_add = asset.add_tag(tag='asset_tag')

# Add asset labels
labels = asset.add_labels(labels=[AssetLabel('test1', 'demo1'), AssetLabel('test2', 'demo2')])

# Get asset labels
labels = asset.get_labels()

# Add custom metadata
asset.add_custom_metadata(custom_metadata=[CustomAssetMetadata('testcm1', 'democm1'), CustomAssetMetadata('testcm2', 'democm2')])

# sample data
sample_data = asset.sample_data()
```



### Executing Asset Profiling, Cancelling Profiles, and Retrieving Latest Profiling Status

Crawled assets can be profiled and sampled using spark jobs that run on Livy. Created policies including Reconciliation and Data Quality policies can also be triggered.

```python
# profile an asset, get profile req details, cancel the profile
profile_res = asset.start_profile(profiling_type=ProfilingType.FULL)

profile_req_details = profile_res.get_status()

cancel_profile_res = profile_res.cancel()

profile_res = asset.get_latest_profile_status()

profile_req_details_by_req_id = torch_client.get_profile_status(asset_id=profile_req_details.assetId,req_id=profile_req_details.id)
```



> Here is an example demonstrating how to use all of the pipeline APIs provided by the Python Acceldata SDK:> > [Pipeline APIs](https://bitbucket.org/acceldata/ad-pipelines-integ-example/src/master/python/01example/)

### Trigger Profiling

Note _This feature is supported for_ _**acceldata_sdk**_ _version &gt;=3.8.0._

The `StartProfilingRequest` class is used to initialize and handle requests for starting profiling operations. This class encapsulates the type of profiling to be executed and the configuration for markers.

| Parameter | Type | Description | Default Value | 
| ---- | ---- | ---- | ---- | 
| `profilingType` | `ExecutionType` | The type of profiling to be executed. This parameter is mandatory. (`SELECTIVE`, `FULL`, `INCREMENTAL`) | N/A | 
| `markerConfig` | `MarkerConfig` | The configuration for the markers. This parameter is optional and applicable during SELECTIVE profiling. Currently supports `BoundsIdMarkerConfig`, `BoundsFileEventMarkerConfig`, and `BoundsDateTimeMarkerConfig`. | `None` | 


#### Trigger Full Profiling

Executes profiling across the entire dataset to provide a comprehensive analysis of all data attributes and characteristics.

```python
from acceldata_sdk.models.common_types import ExecutionType
from acceldata_sdk.models.profile import StartProfilingRequest
from acceldata_sdk.torch_client import TorchClient

asset = torch_client.get_asset(identifier=test_const.table_asset_name)
profiling_execution_request = StartProfilingRequest(
        profilingType=ExecutionType.FULL
  )
asset.start_profile(start_profiling_request=profiling_execution_request)
```



#### Trigger Incremental Profiling

Executes profiling based on the configured incremental strategy within the asset, focusing on new or modified data to capture changes incrementally.

```python
from acceldata_sdk.models.common_types import ExecutionType
from acceldata_sdk.models.profile import StartProfilingRequest
from acceldata_sdk.torch_client import TorchClient

asset = torch_client.get_asset(identifier=test_const.table_asset_name)
profiling_execution_request = StartProfilingRequest(profilingType=ExecutionType.INCREMENTAL)
asset.start_profile(start_profiling_request=profiling_execution_request)
```



#### Trigger Selective Profiling

Executes profiling over a subset of data, constrained by the selected incremental strategy, targeting specific data attributes or segments for detailed analysis.

- **ID based selective profiling**: Uses a monotonically increasing column value to select data bounds. For example, it profiles new rows added after the last profiled row. We use BoundsIdMarkerConfig to selectively profile using this approach.

```python
from acceldata_sdk.models.common_types import ExecutionType, BoundsIdMarkerConfig
from acceldata_sdk.models.profile import StartProfilingRequest
from acceldata_sdk.torch_client import TorchClient

markerConfig = BoundsIdMarkerConfig(idColumnName="ID", fromId=0, toId=1000)
profiling_execution_request = StartProfilingRequest(profilingType=ExecutionType.SELECTIVE,
                                                        markerConfig=markerConfig)
asset.start_profile(start_profiling_request=profiling_execution_request)
```



- **DateTime based selective profiling**: Profiles data using an increasing date column to select data bounds. We use `BoundsDateTimeMarkerConfig` to selectively profile using this approach.

```python
from acceldata_sdk.models.common_types import ExecutionType, BoundsDateTimeMarkerConfig
from acceldata_sdk.models.profile import StartProfilingRequest
from acceldata_sdk.torch_client import TorchClient

markerConfig = BoundsDateTimeMarkerConfig(dateColumnName="TO_DATE", format="yyyy-MM-dd",
                                              fromDate="2023-07-01 00:00:00.000", toDate="2024-07-14 23:59:59.999",
                                              timeZoneId="Asia/Calcutta")
profiling_execution_request = StartProfilingRequest(profilingType=ExecutionType.SELECTIVE,
                                                        markerConfig=markerConfig)
asset.start_profile(start_profiling_request=profiling_execution_request)
```



- **File event based selective profiling**: Profiles data based on file events.  We use `BoundsFileEventMarkerConfig` to selectively profile using this approach.

```python
from acceldata_sdk.models.common_types import ExecutionType, BoundsFileEventMarkerConfig
from acceldata_sdk.models.profile import StartProfilingRequest
from acceldata_sdk.torch_client import TorchClient

markerConfig = BoundsFileEventMarkerConfig(
        fromDate="2019-04-01 00:00:00.000", toDate="2024-07-16 23:59:59.999",
        timeZoneId="Asia/Calcutta")
profiling_execution_request = StartProfilingRequest(profilingType=ExecutionType.SELECTIVE,
                                                        markerConfig=markerConfig)
asset.start_profile(start_profiling_request=profiling_execution_request)
```



## Policy APIs

### View All Policies, Retrieve Specific Policy, and List Policy Executions

```python
import acceldata_sdk.constants as const

# Get policy 
from acceldata_sdk.models.ruleExecutionResult import RuleType, PolicyFilter

rule = torch_client.get_policy(const.PolicyType.RECONCILIATION, "auth001_reconciliation")

# List all executions
# List executions by policy id
dq_rule_executions = torch_client.policy_executions(1114, RuleType.DATA_QUALITY)
# List executions by name
dq_rule_executions = torch_client.policy_executions('dq-scala', RuleType.DATA_QUALITY)

# List executions by policy name
recon_rule_executions = rule.get_executions()
filter = PolicyFilter(policyType=RuleType.RECONCILIATION, enable=True)

# List all rules
recon_rules = torch_client.list_all_policies(filter=filter)
```



### Execute Policies Synchronously and Asynchronously

Acceldata SDK includes the utility function `execute_policy`, which can be used to execute policies both synchronously and asynchronously. This will return an object on which `get_result` and `get_status` can be called to obtain the execution's result and status.

#### Parameters for Executing Synchronous Policies

The required parameters include:

| Parameter | Description | 
| ---- | ---- | 
| sync | This is a Boolean parameter that determines whether the policy should be executed synchronously or asynchronously. It is a required parameter. If set to 'True', it will return only after the execution has completed. If 'False', it will return immediately after the execution begins. | 
| policy_type | The policy type is specified using an enum parameter. It is a required parameter. It is an enum that will accept constant values as PolicyType.DATA_QUALITY or PolicyType.RECONCILIATION. | 
| policy_id | The policy id to be executed is specified as a string parameter. It is a required parameter. | 
| incremental | This is a Boolean parameter that specifies whether policy execution should be incremental or full. The default value is False. | 
| pipeline_run_id | The run id of the pipeline run where the policy is being executed is specified by a long parameter. This can be used to link the execution of the policy with a specific pipeline run. | 
| failure_strategy | The enum parameter is used to determine the behavior in the event of a failure. The default value is DoNotFail.\n\n\n\n- `failure_strategy` takes enum of type `FailureStrategy` which can have 3 values: DoNotFail, FailOnError, and FailOnWarning.\n- DoNotFail will never throw and exception. In the event of a failure, the error will be logged.\n- FailOnError will only throw an exception if there is an error. In the event of a warning, it is to return with no errors.\n- FailOnWarning will throw exceptions on both warnings and errors. | 


To get the execution result, you can call `get_policy_execution_result` on `torch_client` or call `get_result` on the execution object which will return a result object.

#### Parameters to Retrieve Policy Execution Results

The required parameters include:

| Parameter | Description | 
| ---- | ---- | 
| policy_type | The policy type is specified using an enum parameter. It is a required parameter. It is an enum that will accept constant values as PolicyType.DATA_QUALITY or PolicyType.RECONCILIATION. | 
| execution_id | The execution id to be queried for the result is specified as a string parameter. It is a required parameter. | 
| failure_strategy | The enum parameter is used to determine the behavior in the event of a failure. The default value is DoNotFail. | 


> For more information on hard linked and soft linked policies, see [Hard Linked and Soft Linked Policies](/documentation/understanding-pipelines#hard-linked-and-soft-linked-policies).

To get the current status, you can call `get_policy_status` on torch_client or call `get_status` on the execution object which will get the current `resultStatus` of the execution.

The required parameters include:

| Parameter | Description | 
| ---- | ---- | 
| policy_type | The policy type is specified using an enum parameter. It is a required parameter. It is an enum that will accept constant values as PolicyType.DATA_QUALITY or PolicyType.RECONCILIATION. | 
| execution_id | The execution id to be queried for the result is specified as a string parameter. It is a required parameter. | 


> `get_status` does not take any parameter.

#### Asynchronous Execution Example

```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_airflow_sdk.initialiser import torch_credentials
import acceldata_sdk.constants as const
from acceldata_sdk.constants import FailureStrategy

torch_client = TorchClient(**torch_credentials)
async_executor = torch_client.execute_policy(const.PolicyType.DATA_QUALITY, 46, sync=False, failure_strategy=FailureStrategy.DoNotFail,policy_execution_request=policy_execution_request)
# Wait for execution to get the final result
execution_result = async_executor.get_result(failure_strategy=FailureStrategy.DoNotFail)
# Get the current status
execution_status = async_executor.get_status()
```



#### Synchronous Execution Example

```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_airflow_sdk.initialiser import torch_credentials
import acceldata_sdk.constants as const
from acceldata_sdk.constants import FailureStrategy

torch_client = TorchClient(**torch_credentials)
# This will wait for execution to get the final result
sync_executor = torch_client.execute_policy(const.PolicyType.DATA_QUALITY, 46, sync=True, failure_strategy=FailureStrategy.DoNotFail)
# Wait for execution to get the final result
execution_result = sync_executor.get_result(FailureStrategy = const.FailureStrategy.DoNotFail)
# Get the current status
execution_status = sync_executor.get_status()
```



#### Cancel Execution Example

```python
execution_result = sync_executor.cancel()
```



### Trigger Policies

Note _This feature is supported for_ _**acceldata_sdk**_ _version &gt;=3.8.0._

The `PolicyExecutionRequest` class is used to initialize and handle requests for policy execution. This class encapsulates various configurations and parameters required for executing a policy, including execution type, marker configurations, rule item selections, and Spark-specific settings.

| Parameter | Type | Description | Default Value | 
| ---- | ---- | ---- | ---- | 
| `executionType` | `ExecutionType` | The type of execution. This parameter is mandatory and defines how the policy execution should be carried out. (`SELECTIVE`, `FULL`, `INCREMENTAL`) | N/A | 
| `markerConfigs` | `Optional[List[AssetMarkerConfig]]` | A list of marker configurations. This parameter is optional. Useful during selective execution. Currently supports `BoundsIdMarkerConfig`, `BoundsFileEventMarkerConfig`,  `BoundsDateTimeMarkerConfig` and `TimestampBasedMarkerConfig`. | `None` | 
| `ruleItemSelections` | `Optional[List[int]]` | A list of rule item selections by their identifiers. This parameter is optional. If not passed all the rule item definitions will be executed. | `None` | 
| `includeInQualityScore` | `bool` | A flag indicating whether to include the execution in the quality score. This parameter is optional. | `True` | 
| `pipelineRunId` | `Optional[int]` | The ID of the pipeline run to which the policy execution is attached. This parameter is optional. | `None` | 
| `sparkSQLDynamicFilterVariableMapping` | `Optional[List[RuleSparkSQLDynamicFilterVariableMapping]]` | A list of Spark SQL dynamic filter variable mappings applicable for a Data Quality policy. This parameter is optional. | `None` | 
| `sparkResourceConfig` | `Optional[SparkResourceConfig]` | The configuration for Spark resources. This parameter is optional. | `None` | 


#### Data Quality Policy Execution Examples

**Trigger Full Data Quality Policy**

To execute a full Data Quality policy across the entire dataset:

```python
from acceldata_sdk.models.common_types import ExecutionType,PolicyExecutionRequest
from acceldata_sdk.torch_client import TorchClient

dq_policy = torch_client.get_policy(identifier=dq_policy_name)
policy_execution_request = PolicyExecutionRequest(executionType=ExecutionType.FULL)
policy_execution_result = torch_client.execute_dq_rule(rule_id=dq_policy.id,policy_execution_request=policy_execution_request)
```



**Trigger Incremental Data Quality Policy**

To execute an incremental Data Quality policy based on a configured incremental strategy:

```python
from acceldata_sdk.models.common_types import ExecutionType,PolicyExecutionRequest
from acceldata_sdk.torch_client import TorchClient
asset = torch_client.get_asset(identifier=test_const.table_asset_name)
policy_execution_request = PolicyExecutionRequest(executionType=ExecutionType.INCREMENTAL)
policy_execution_result = torch_client.execute_dq_rule(rule_id=dq_policy.id,
                                                           policy_execution_request=policy_execution_request)
```



**Trigger Selective Data Quality Policy**

To execute a selective Data Quality policy over a subset of data, as determined by the chosen incremental strategy, you can use `sparkSQLDynamicFilterVariableMapping` and `sparkResourceConfig`, as demonstrated in this optional example. Note that `sparkSQLDynamicFilterVariableMapping` is only relevant if the Data Quality policy includes SQL filters.

- **ID-Based Selective Policy Execution:** Uses a monotonically increasing column value to define data boundaries for policy execution, implemented with **BoundsIdMarkerConfig**.

```python
from acceldata_sdk.models.common_types import ExecutionType,AssetMarkerConfig, YunikornConfig, SparkResourceConfig, \
    RuleSparkSQLDynamicFilterVariableMapping, Mapping, BoundsIdMarkerConfig, PolicyExecutionRequest
from acceldata_sdk.torch_client import TorchClient

dq_policy = torch_client.get_policy(identifier=test_const.spark_sql_policy_name)
markerConfig = BoundsIdMarkerConfig(idColumnName="ID", fromId=0, toId=1000)

#assetId in the marker configuration refers to the unique identifier of the underlying asset on which the Data Quality (DQ) policy is established.
assetMarkerConfig = AssetMarkerConfig(assetId=9667404, markerConfig=markerConfig)
markerConfigs = [assetMarkerConfig]
yunikornConfig = YunikornConfig(minExecutors=1, maxExecutors=2, executorCores=2, executorMemory="2g", driverCores=2,
                                driverMemory="2g")
sparkResourceConfig = SparkResourceConfig(yunikorn=yunikornConfig,
                                          additionalConfiguration={})
ruleItemSelections = []
mapping = Mapping(key="column_name", isColumnVariable=True, value="100")
sparkSQLDynamicFilterVariableMapping = [RuleSparkSQLDynamicFilterVariableMapping(
    ruleName="SelectiveDQPolicysparkSQLDynamicFilterVariable",
    mapping=[mapping])]
policy_execution_request = PolicyExecutionRequest(
    markerConfigs=markerConfigs,
    executionType=ExecutionType.SELECTIVE,
    sparkResourceConfig=sparkResourceConfig,
    sparkSQLDynamicFilterVariableMapping=sparkSQLDynamicFilterVariableMapping,
    ruleItemSelections=ruleItemSelections)
torch_client.execute_dq_rule(rule_id=dq_policy.id,
                                            policy_execution_request=policy_execution_request)
```



- **DateTime-Based Selective Policy Execution:** Utilizes an increasing date column to define data boundaries for policy execution, implemented with `BoundsDateTimeMarkerConfig` 

```python
from acceldata_sdk.models.common_types import ExecutionType, BoundsDateTimeMarkerConfig, AssetMarkerConfig, PolicyExecutionRequest
from acceldata_sdk.torch_client import TorchClient

dq_policy = torch_client.get_policy(identifier=dq_policy_name)
markerConfig = BoundsDateTimeMarkerConfig(dateColumnName="TO_DATE", format="yyyy-MM-dd",
                                          fromDate="2023-07-01 00:00:00.000", toDate="2024-07-14 23:59:59.999",
                                          timeZoneId="Asia/Calcutta")
#assetId in the marker configuration refers to the unique identifier of the underlying asset on which the Data Quality (DQ) policy is established.
assetMarkerConfig = AssetMarkerConfig(assetId=9667404, markerConfig=markerConfig)
markerConfigs = [assetMarkerConfig]
policy_execution_request = PolicyExecutionRequest(
    markerConfigs=markerConfigs,
    executionType=ExecutionType.SELECTIVE)
policy_execution_result = torch_client.execute_dq_rule(rule_id=dq_policy.id,
                                                       policy_execution_request=policy_execution_request)
```



- **File Event-Based Selective Policy Execution:** Uses file events to establish data boundaries for policy execution, implemented with `BoundsFileEventMarkerConfig`.

```python
from acceldata_sdk.models.common_types import ExecutionType, AssetMarkerConfig, BoundsFileEventMarkerConfig, PolicyExecutionRequest 
from acceldata_sdk.torch_client import TorchClient
dq_policy = torch_client.get_policy(identifier=dq_policy_name)
markerConfig = BoundsFileEventMarkerConfig(
    fromDate="2024-07-01 00:00:00.000", toDate="2024-07-01 23:59:59.999",
    timeZoneId="Asia/Calcutta")
#assetId in the marker configuration refers to the unique identifier of the underlying asset on which the Data Quality (DQ) policy is established.
assetMarkerConfig = AssetMarkerConfig(assetId=1202688, markerConfig=markerConfig)
markerConfigs = [assetMarkerConfig]
policy_execution_request = PolicyExecutionRequest(
    markerConfigs=markerConfigs,
    executionType=ExecutionType.SELECTIVE)
policy_execution_result = torch_client.execute_dq_rule(rule_id=dq_policy.id,
                                                       policy_execution_request=policy_execution_request)
```



- **Kafka Timestamp-Based Selective Policy Execution:** Uses offsets associated with specified timestamps to set data boundaries for policy execution, implemented with `TimestampBasedMarkerConfig`.

```python
from acceldata_sdk.models.common_types import ExecutionType, AssetMarkerConfig, TimestampBasedMarkerConfig, PolicyExecutionRequest 
from acceldata_sdk.torch_client import TorchClient

dq_policy = torch_client.get_policy(identifier="kafka_dq_policy")
markerConfig = TimestampBasedMarkerConfig(
    format="yyyy-mm-dd",
    initialOffset="2023-06-01",
    timeZoneId="Asia/Calcutta")

#assetId in the marker configuration refers to the unique identifier of the underlying asset on which the Data Quality (DQ) policy is established.
assetMarkerConfig = AssetMarkerConfig(assetId=5241961, markerConfig=markerConfig)
markerConfigs = [assetMarkerConfig]
policy_execution_request = PolicyExecutionRequest(
    markerConfigs=markerConfigs,
    executionType=ExecutionType.SELECTIVE)
policy_execution_result = torch_client.execute_dq_rule(rule_id=dq_policy.id,
                                                             policy_execution_request=policy_execution_request)
```



#### [Reconciliation Policy Execution Examples](https://docs.acceldata.io/sdk/sdk-apis#reconciliation-policy-execution-examples)

**Trigger Full Reconciliation Policy**

To trigger a full reconciliation policy across the entire dataset:

```python
from acceldata_sdk.models.common_types import ExecutionType,PolicyExecutionRequest
from acceldata_sdk.torch_client import TorchClient

dq_policy = torch_client.get_policy(identifier=dq_policy_name)
policy_execution_request = PolicyExecutionRequest(executionType=ExecutionType.FULL)
policy_execution_result = torch_client.execute_reconciliation_rule(rule_id=dq_policy.id,policy_execution_request=policy_execution_request)
```



**Trigger Incremental Reconciliation Policy**

To trigger an incremental Reconciliation policy based on a configured incremental strategy:

```python
from acceldata_sdk.models.common_types import ExecutionType, PolicyExecutionRequest
from acceldata_sdk.torch_client import TorchClient

asset = torch_client.get_asset(identifier=test_const.table_asset_name)
policy_execution_request = PolicyExecutionRequest(executionType=ExecutionType.INCREMENTAL)
policy_execution_result = torch_client.execute_reconciliation_rule(rule_id=dq_policy.id,
                                                           policy_execution_request=policy_execution_request)
```



**Trigger Selective Reconciliation Policy**

To trigger a selective Reconciliation policy over a subset of data, constrained by the selected incremental strategy:

- **ID-Based Selective Policy Execution:** Uses a monotonically increasing column value to define data boundaries for policy execution, implemented with **BoundsIdMarkerConfig**.

```python
from acceldata_sdk.models.common_types import ExecutionType,AssetMarkerConfig, YunikornConfig, SparkResourceConfig, Mapping, PolicyExecutionRequest, BoundsIdMarkerConfig
from acceldata_sdk.torch_client import TorchClient

recon_policy = torch_client.get_policy(identifier=test_const.recon_policy_name)
markerConfig = BoundsIdMarkerConfig(idColumnName="ID", fromId=0, toId=1000)

#assetId in the marker configuration denotes the unique identifier of the underlying asset on which the Reconciliation policy is based. This could represent either the left or right asset ID.
assetMarkerConfig = AssetMarkerConfig(assetId=9667404, markerConfig=markerConfig)
markerConfigs = [assetMarkerConfig]
yunikornConfig = YunikornConfig(minExecutors=1, maxExecutors=2, executorCores=2, executorMemory="2g", driverCores=2,
                                driverMemory="2g")
sparkResourceConfig = SparkResourceConfig(yunikorn=yunikornConfig,
                                          additionalConfiguration={})
ruleItemSelections = []
policy_execution_request = PolicyExecutionRequest(
    markerConfigs=markerConfigs,
    executionType=ExecutionType.SELECTIVE,
    sparkResourceConfig=sparkResourceConfig,
    sparkSQLDynamicFilterVariableMapping=sparkSQLDynamicFilterVariableMapping,
    ruleItemSelections=ruleItemSelections)
torch_client.execute_reconciliation_rule(rule_id=recon_policy.id,
                                            policy_execution_request=policy_execution_request)
```



- **DateTime-Based Selective Policy Execution:** Utilizes an increasing date column to define data boundaries for policy execution, implemented with `BoundsDateTimeMarkerConfig`.

```python
from acceldata_sdk.models.common_types import ExecutionType, BoundsDateTimeMarkerConfig, AssetMarkerConfig, PolicyExecutionRequest
from acceldata_sdk.torch_client import TorchClient

recon_policy = torch_client.get_policy(identifier=recon_policy_name)
markerConfig = BoundsDateTimeMarkerConfig(dateColumnName="TO_DATE", format="yyyy-MM-dd",
                                          fromDate="2023-07-01 00:00:00.000", toDate="2024-07-14 23:59:59.999",
                                          timeZoneId="Asia/Calcutta")
#assetId in the marker configuration denotes the unique identifier of the underlying asset on which the Reconciliation policy is based. This could represent either the left or right asset ID.
assetMarkerConfig = AssetMarkerConfig(assetId=9667404, markerConfig=markerConfig)
markerConfigs = [assetMarkerConfig]
policy_execution_request = PolicyExecutionRequest(
    markerConfigs=markerConfigs,
    executionType=ExecutionType.SELECTIVE)
policy_execution_result = torch_client.execute_reconciliation_rule(rule_id=recon_policy.id,
                                                       policy_execution_request=policy_execution_request)
```



- **File Event-Based Selective Policy Execution:** Uses file events to establish data boundaries for policy execution, implemented with `BoundsFileEventMarkerConfig`.

```python
from acceldata_sdk.models.common_types import ExecutionType,AssetMarkerConfig, BoundsFileEventMarkerConfig, PolicyExecutionRequest
from acceldata_sdk.torch_client import TorchClient

recon_policy = torch_client.get_policy(identifier=dq_policy_name)
markerConfig = BoundsFileEventMarkerConfig(
    fromDate="2024-07-01 00:00:00.000", toDate="2024-07-01 23:59:59.999",
    timeZoneId="Asia/Calcutta")

#assetId in the marker configuration denotes the unique identifier of the underlying asset on which the Reconciliation policy is based. This could represent either the left or right asset ID.
assetMarkerConfig = AssetMarkerConfig(assetId=1202688, markerConfig=markerConfig)
markerConfigs = [assetMarkerConfig]
policy_execution_request = PolicyExecutionRequest(
    markerConfigs=markerConfigs,
    executionType=ExecutionType.SELECTIVE)
policy_execution_result = torch_client.execute_reconciliation_rule(rule_id=recon_policy.id,
                                                       policy_execution_request=policy_execution_request)
```



- **Kafka Timestamp-Based Selective Policy Execution:** Uses offsets associated with specified timestamps to set data boundaries for policy execution, implemented with `TimestampBasedMarkerConfig`.

```python
from acceldata_sdk.models.common_types import ExecutionType,AssetMarkerConfig, TimestampBasedMarkerConfig, PolicyExecutionRequest
from acceldata_sdk.torch_client import TorchClient

recon_policy = torch_client.get_policy(identifier="kafka_recon_policy")
markerConfig = TimestampBasedMarkerConfig(
    format="yyyy-mm-dd",
    initialOffset="2023-06-01",
    timeZoneId="Asia/Calcutta")

#assetId in the marker configuration denotes the unique identifier of the underlying asset on which the Reconciliation policy is based. This could represent either the left or right asset ID.
assetMarkerConfig = AssetMarkerConfig(assetId=5241961, markerConfig=markerConfig)
markerConfigs = [assetMarkerConfig]
policy_execution_request = PolicyExecutionRequest(
    markerConfigs=markerConfigs,
    executionType=ExecutionType.SELECTIVE)
policy_execution_result = torch_client.execute_reconciliation_rule(rule_id=recon_policy.id,
                                                             policy_execution_request=policy_execution_request)
```

