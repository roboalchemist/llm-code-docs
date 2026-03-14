# Source: https://docs.anyscale.com/reference/job-api.md

# Source: https://docs.anyscale.com/archive/ref/job-api.md

# Job API Reference (Legacy)

[View Markdown](/archive/ref/job-api.md)

# Job API Reference (Legacy)

warning

These methods are deprecated and will be fully removed from the Anyscale platform on January 29, 2026. To continue using these methods, install Anyscale CLI version 0.26.72 or earlier. Please use the [current APIs](/reference/job-api.md) instead.

## Job SDK[​](#job-sdk "Direct link to Job SDK")

The AnyscaleSDK class must be constructed in order to make calls to the SDK. This class allows you to create an authenticated client in which to use the SDK.

| Param        | Type            | Description                                                                                                                                                                                                                                                                   |
| ------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auth_token` | Optional String | Authentication token used to verify you have permissions to access Anyscale. If not provided, permissions default to the credentials set for your current user. Credentials can be set by following the instructions on this page: <https://console.anyscale.com/credentials> |

**Example**

```
from anyscale import AnyscaleSDK

sdk = AnyscaleSDK()
```

### `create_job`[​](#create_job "Direct link to create_job")

Create an Production Job

Parameters

| Name                    | Type                | Description | Notes |
| ----------------------- | ------------------- | ----------- | ----- |
| `create_production_job` | CreateProductionJob |             |       |

Returns ProductionjobResponse

### `get_production_job`[​](#get_production_job "Direct link to get_production_job")

Get an Production Job

Parameters

| Name                | Type | Description | Notes            |
| ------------------- | ---- | ----------- | ---------------- |
| `production_job_id` | str  |             | Defaults to null |

Returns ProductionjobResponse

### `terminate_job`[​](#terminate_job "Direct link to terminate_job")

Terminate an Production Job

Parameters

| Name                | Type | Description | Notes            |
| ------------------- | ---- | ----------- | ---------------- |
| `production_job_id` | str  |             | Defaults to null |

Returns ProductionjobResponse

### `fetch_job_logs`[​](#fetch_job_logs "Direct link to fetch_job_logs")

Retrieves logs for a Job.

This function may take several minutes if the Cluster this Job ran on has been terminated.

Returns the log output as a string.

Raises an Exception if fetching logs fails.

| Param    | Type   | Description   |
| -------- | ------ | ------------- |
| `job_id` | String | ID of the Job |

**Example**

```
from anyscale import AnyscaleSDK

sdk = AnyscaleSDK(auth_token="sss_YourAuthToken")

job_logs = sdk.fetch_job_logs(job_id="job_id")

print(job_logs)
```

### `fetch_production_job_logs`[​](#fetch_production_job_logs "Direct link to fetch_production_job_logs")

Retrieves logs for a Production Job.

This function may take several minutes if the Cluster this Production Job ran on has been terminated.

Returns the log output as a string.

Raises an Exception if fetching logs fails.

| Param    | Type   | Description   |
| -------- | ------ | ------------- |
| `job_id` | String | ID of the Job |

**Example**

```
from anyscale import AnyscaleSDK

sdk = AnyscaleSDK(auth_token="sss_YourAuthToken")

job_logs = sdk.fetch_production_job_logs(job_id="production_job_id")

print(job_logs)
```

### `get_job_logs_download`[​](#get_job_logs_download "Direct link to get_job_logs_download")

Parameters

| Name       | Type          | Description               | Notes            |
| ---------- | ------------- | ------------------------- | ---------------- |
| `job_id`   | str           |                           | Defaults to null |
| `all_logs` | optional bool | Whether to grab all logs. | Defaults to true |

Returns LogdownloadresultResponse

### `get_job_logs_stream`[​](#get_job_logs_stream "Direct link to get_job_logs_stream")

Parameters

| Name     | Type | Description | Notes            |
| -------- | ---- | ----------- | ---------------- |
| `job_id` | str  |             | Defaults to null |

Returns LogstreamResponse

### `search_jobs`[​](#search_jobs "Direct link to search_jobs")

DEPRECATED: This API is now deprecated. Use list\_production\_jobs instead.

Parameters

| Name         | Type      | Description | Notes |
| ------------ | --------- | ----------- | ----- |
| `jobs_query` | JobsQuery |             |       |

Returns JobListResponse

### `list_production_jobs`[​](#list_production_jobs "Direct link to list_production_jobs")

Parameters

| Name           | Type               | Description                           | Notes            |
| -------------- | ------------------ | ------------------------------------- | ---------------- |
| `project_id`   | optional str       | project\_id to filter by              | Defaults to null |
| `name`         | optional str       | name to filter by                     | Defaults to null |
| `state_filter` | List\[HaJobStates] | A list of session states to filter by | Defaults to \[]  |
| `creator_id`   | optional str       | filter by creator id                  | Defaults to null |
| `paging_token` | optional str       |                                       | Defaults to null |
| `count`        | optional int       |                                       | Defaults to null |

Returns ProductionjobListResponse

## Job Models[​](#job-models "Direct link to Job Models")

### `BaseJobStatus`[​](#basejobstatus "Direct link to basejobstatus")

An enumeration.

Possible Values: \['RUNNING', 'COMPLETED', 'PENDING', 'STOPPED', 'SUCCEEDED', 'FAILED', 'UNKNOWN']

### `CreateClusterComputeConfig`[​](#createclustercomputeconfig "Direct link to createclustercomputeconfig")

Configuration of compute resources to use for launching a Cluster. Used when creating a cluster compute.

| Name                                    | Type                                    | Description                                                                                                                                                                                                                                                                                                                     | Notes                                |
| --------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| **cloud\_id**                           | **str**                                 | The ID of the Anyscale cloud to use for launching Clusters.                                                                                                                                                                                                                                                                     | \[default to null]                   |
| **maximum\_uptime\_minutes**            | **int**                                 | If set to a positive number, Anyscale will terminate the cluster this many minutes after cluster start.                                                                                                                                                                                                                         | \[optional] \[default to null]       |
| **deployment\_configs**                 | **List\[CloudDeploymentComputeConfig]** | A list of cloud deployment-specific configs to use.                                                                                                                                                                                                                                                                             | \[optional] \[default to null]       |
| **max\_workers**                        | **int**                                 | DEPRECATED. This attribute will be ignored - please use the \&quot;max\_resources\&quot; flag to configure resource limits.                                                                                                                                                                                                     | \[optional] \[default to null]       |
| **region**                              | **str**                                 | Deprecated! When creating a cluster compute, a region does not have to be provided. Instead we will use the value from the cloud.                                                                                                                                                                                               | \[optional] \[default to USE\_CLOUD] |
| **allowed\_azs**                        | **List\[str]**                          | The availability zones that sessions are allowed to be launched in, e.g. \&quot;us-west-2a\&quot;. If not specified or \&quot;any\&quot; is provided as the option, any AZ may be used. If \&quot;any\&quot; is provided, it must be the only item in the list.                                                                 | \[optional] \[default to null]       |
| **head\_node\_type**                    | **ComputeNodeType**                     | Node configuration to use for the head node.                                                                                                                                                                                                                                                                                    | \[default to null]                   |
| **worker\_node\_types**                 | **List\[WorkerNodeType]**               | A list of node types to use for worker nodes.                                                                                                                                                                                                                                                                                   | \[optional] \[default to null]       |
| **aws\_advanced\_configurations\_json** | **object**                              | \[DEPRECATED: use advanced\_configurations\_json instead] The advanced configuration json that we pass directly AWS APIs when launching an instance. We may do some validation on this json and reject the json if it is using a configuration that Anyscale does not support.                                                  | \[optional] \[default to null]       |
| **gcp\_advanced\_configurations\_json** | **object**                              | \[DEPRECATED: use advanced\_configurations\_json instead] The advanced configuration json that we pass directly GCP APIs when launching an instance. We may do some validation on this json and reject the json if it is using a configuration that Anyscale does not support.                                                  | \[optional] \[default to null]       |
| **advanced\_configurations\_json**      | **object**                              | Advanced configurations for this compute node type to pass to the cloud provider when launching this instance.                                                                                                                                                                                                                  | \[optional] \[default to null]       |
| **auto\_select\_worker\_config**        | **bool**                                | If set to true, worker node groups will automatically be selected based on workload.                                                                                                                                                                                                                                            | \[optional] \[default to false]      |
| **flags**                               | **object**                              | A set of advanced cluster-level flags that can be used to configure a particular workload.                                                                                                                                                                                                                                      | \[optional] \[default to null]       |
| **idle\_termination\_minutes**          | **int**                                 | If set to a positive number, Anyscale will terminate the cluster this many minutes after the cluster is idle. Idle time is defined as the time during which a Cluster is not running a user command or a Ray driver. Time spent running commands on Jupyter or ssh is still considered 'idle'. To disable, set this field to 0. | \[optional] \[default to 120]        |

### `CreateJobQueueConfig`[​](#createjobqueueconfig "Direct link to createjobqueueconfig")

Specifies configuration of the job being added to a Job Queue

| Name                         | Type             | Description                                                                                                                                                                                                | Notes                          |
| ---------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **priority**                 | **int**          | Job's relative priority (only relevant for Job Queues of type PRIORITY). Valid values range from 0 (highest) to +inf (lowest). Default value is None                                                       | \[optional] \[default to null] |
| **target\_job\_queue\_id**   | **str**          | Identifier of the existing Job Queue this job should be added to. Note, only one of \`target\_job\_queue\_id\`, \`target\_job\_queue\_name\` or \`job\_queue\_spec\` could be provided                     | \[optional] \[default to null] |
| **target\_job\_queue\_name** | **str**          | Existing Job Queue user-provided name (identifier), this job should be added to. Note, only one of \`target\_job\_queue\_id\`, \`target\_job\_queue\_name\` or \`job\_queue\_spec\` could be provided      | \[optional] \[default to null] |
| **job\_queue\_spec**         | **JobQueueSpec** | Spec of the Job Queue definition that should be created and associated with this job. Note, only one of \`target\_job\_queue\_id\`, \`target\_job\_queue\_name\` or \`job\_queue\_spec\` could be provided | \[optional] \[default to null] |

### `CreateProductionJob`[​](#createproductionjob "Direct link to createproductionjob")

| Name                   | Type                          | Description                                                         | Notes                          |
| ---------------------- | ----------------------------- | ------------------------------------------------------------------- | ------------------------------ |
| **name**               | **str**                       | Name of the job                                                     | \[default to null]             |
| **description**        | **str**                       | Description of the job                                              | \[optional] \[default to null] |
| **project\_id**        | **str**                       | Id of the project this job will start clusters in                   | \[optional] \[default to null] |
| **config**             | **CreateProductionJobConfig** |                                                                     | \[default to null]             |
| **job\_queue\_config** | **CreateJobQueueConfig**      | Configuration specifying semantic of the execution using job queues | \[optional] \[default to null] |

### `CreateProductionJobConfig`[​](#createproductionjobconfig "Direct link to createproductionjobconfig")

| Name                     | Type                           | Description                                                                                                                                                                                                                                                                 | Notes                          |
| ------------------------ | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **entrypoint**           | **str**                        | A script that will be run to start your job.This command will be run in the root directory of the specified runtime env. Eg. 'python script.py'                                                                                                                             | \[optional] \[default to ]     |
| **ray\_serve\_config**   | **object**                     | The Ray Serve config to use for this Production service. This config defines your Ray Serve application, and will be passed directly to Ray Serve. You can learn more about Ray Serve config files here: <https://docs.ray.io/en/latest/serve/production-guide/config.html> | \[optional] \[default to null] |
| **runtime\_env**         | **RayRuntimeEnvConfig**        | A ray runtime env json. Your entrypoint will be run in the environment specified by this runtime env.                                                                                                                                                                       | \[optional] \[default to null] |
| **build\_id**            | **str**                        | The id of the cluster env build. This id will determine the docker image your job is run on.                                                                                                                                                                                | \[default to null]             |
| **compute\_config\_id**  | **str**                        | The id of the compute configuration that you want to use. This id will specify the resources required for your job                                                                                                                                                          | \[optional] \[default to null] |
| **compute\_config**      | **CreateClusterComputeConfig** | One-off compute that the cluster will use.                                                                                                                                                                                                                                  | \[optional] \[default to null] |
| **max\_retries**         | **int**                        | The number of retries this job will attempt on failure. Set to None to set infinite retries                                                                                                                                                                                 | \[optional] \[default to 5]    |
| **timeout\_s**           | **int**                        | The timeout in seconds for each job run. Set to None for no limit to be set                                                                                                                                                                                                 | \[optional] \[default to null] |
| **runtime\_env\_config** | **RayRuntimeEnvConfig**        | DEPRECATED: Use runtime\_env                                                                                                                                                                                                                                                | \[optional] \[default to null] |

### `HaJobGoalStates`[​](#hajobgoalstates "Direct link to hajobgoalstates")

An enumeration.

Possible Values: \['SCHEDULED', 'RUNNING', 'TERMINATED', 'SUCCESS']

### `HaJobStates`[​](#hajobstates "Direct link to hajobstates")

An enumeration.

Possible Values: \['PENDING', 'AWAITING\_CLUSTER\_START', 'UPDATING', 'RUNNING', 'SUCCESS', 'ERRORED', 'TERMINATED', 'CLEANING\_UP', 'BROKEN', 'OUT\_OF\_RETRIES', 'RESTARTING']

### `Job`[​](#job "Direct link to job")

| Name                         | Type          | Description                                                            | Notes                                               |
| ---------------------------- | ------------- | ---------------------------------------------------------------------- | --------------------------------------------------- |
| **id**                       | **str**       | Server assigned unique identifier.                                     | \[default to null]                                  |
| **ray\_session\_name**       | **str**       | Name of the Session provided from Ray                                  | \[default to null]                                  |
| **ray\_job\_id**             | **str**       | ID of the Job provided from Ray                                        | \[default to null]                                  |
| **name**                     | **str**       | Name of this Job.                                                      | \[optional] \[default to null]                      |
| **status**                   | **JobStatus** | Status of this Job's execution.                                        | \[default to null]                                  |
| **created\_at**              | **datetime**  | Time at which this Job was created.                                    | \[default to null]                                  |
| **finished\_at**             | **datetime**  | Time at which this Job finished. If absent, this Job is still running. | \[optional] \[default to null]                      |
| **ray\_job\_submission\_id** | **str**       | ID of the submitted Ray Job that this Job corresponds to.              | \[optional] \[default to null]                      |
| **cluster\_id**              | **str**       | ID of the Anyscale Cluster this Job is on.                             | \[default to null]                                  |
| **namespace\_id**            | **str**       | ID of the Anyscale Namespace this Job is using.                        | \[optional] \[default to DEPRECATED\_NAMESPACE\_ID] |
| **runtime\_environment\_id** | **str**       | ID of the Anyscale Runtime Environment this Job is using.              | \[default to null]                                  |
| **project\_id**              | **str**       | ID of the Project this Job belongs to.                                 | \[optional] \[default to null]                      |
| **creator\_id**              | **str**       | ID of the user who created this Job.                                   | \[default to null]                                  |

### `JobListResponse`[​](#joblistresponse "Direct link to joblistresponse")

A list response form the API. Contains a field "results" which has the contents of the response.

| Name         | Type                     | Description | Notes                          |
| ------------ | ------------------------ | ----------- | ------------------------------ |
| **results**  | **List\[Job]**           |             | \[default to null]             |
| **metadata** | **ListResponseMetadata** |             | \[optional] \[default to null] |

### `JobQueueConfig`[​](#jobqueueconfig "Direct link to jobqueueconfig")

Captures job's configuration in the context of its scheduling & execution via Job Queues

| Name         | Type    | Description                                                                                                                                          | Notes                          |
| ------------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **priority** | **int** | Job's relative priority (only relevant for Job Queues of type PRIORITY). Valid values range from 0 (highest) to +inf (lowest). Default value is None | \[optional] \[default to null] |

### `JobQueueExecutionMode`[​](#jobqueueexecutionmode "Direct link to jobqueueexecutionmode")

An enumeration.

Possible Values: \['FIFO', 'LIFO', 'PRIORITY']

### `JobQueueSpec`[​](#jobqueuespec "Direct link to jobqueuespec")

Specifies definition of the Job Queue to be created

| Name                                         | Type                      | Description                                                                                                                                                                     | Notes                          |
| -------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **job\_queue\_name**                         | **str**                   | Optional user-provided identifier of the queue that could be subsequently used to reference the queue when submitting jobs. Note that name has to be unique within the project. | \[optional] \[default to null] |
| **execution\_mode**                          | **JobQueueExecutionMode** | Execution mode of the jobs submitted into the queue (one of: FIFO,LIFO,PRIORITY                                                                                                 | \[optional] \[default to null] |
| **compute\_config\_id**                      | **str**                   | The id of the compute configuration that will be used to create cluster associated with the queue. Defaults to default compute config in the given project                      | \[optional] \[default to null] |
| **cluster\_environment\_build\_id**          | **str**                   | The id of the cluster environment build that will be used to create cluster associated with the queue.                                                                          | \[optional] \[default to null] |
| **max\_concurrency**                         | **int**                   | Max number of jobs to be run concurrently. Defaults to 1, ie running no more than 1 job at a time.                                                                              | \[optional] \[default to 1]    |
| **idle\_timeout\_sec**                       | **int**                   | Max period of time queue will be accepting new jobs, before being sealed off and its associated cluster being shutdown                                                          | \[default to null]             |
| **auto\_termination\_threshold\_job\_count** | **int**                   | Maximum number of jobs the cluster can run before it becomes eligible for termination.                                                                                          | \[optional] \[default to null] |

### `JobRunType`[​](#jobruntype "Direct link to jobruntype")

An enumeration.

Possible Values: \['INTERACTIVE\_SESSION', 'RUN', 'RAY\_SUBMIT']

### `JobStatus`[​](#jobstatus "Direct link to jobstatus")

An enumeration.

Possible Values: \['RUNNING', 'COMPLETED', 'PENDING', 'STOPPED', 'SUCCEEDED', 'FAILED', 'UNKNOWN']

### `JobsSortField`[​](#jobssortfield "Direct link to jobssortfield")

An enumeration.

Possible Values: \['STATUS', 'CREATED\_AT', 'FINISHED\_AT', 'NAME', 'ID']

### `ProductionJob`[​](#productionjob "Direct link to productionjob")

Model of a Production Job for use in the SDK.

| Name                   | Type                             | Description                                                                           | Notes                          |
| ---------------------- | -------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------ |
| **id**                 | **str**                          | The id of this job                                                                    | \[default to null]             |
| **name**               | **str**                          | Name of the job                                                                       | \[default to null]             |
| **description**        | **str**                          | Description of the job                                                                | \[optional] \[default to null] |
| **created\_at**        | **datetime**                     | The time this job was created                                                         | \[default to null]             |
| **creator\_id**        | **str**                          | The id of the user who created this job                                               | \[default to null]             |
| **config**             | **ProductionJobConfig**          | The config that was used to create this job                                           | \[default to null]             |
| **job\_queue\_config** | **JobQueueConfig**               | Job Queue configuration of this job (if applicable)                                   | \[optional] \[default to null] |
| **state**              | **ProductionJobStateTransition** | The current state of this job                                                         | \[default to null]             |
| **project\_id**        | **str**                          | Id of the project this job will start clusters in                                     | \[default to null]             |
| **last\_job\_run\_id** | **str**                          | The id of the last job run                                                            | \[optional] \[default to null] |
| **schedule\_id**       | **str**                          | If the job was launched via Scheduled job, this will contain the id of that schedule. | \[optional] \[default to null] |
| **job\_queue\_id**     | **str**                          | Id of the job queue this job is being enqueued to                                     | \[optional] \[default to null] |

### `ProductionJobConfig`[​](#productionjobconfig "Direct link to productionjobconfig")

| Name                     | Type                           | Description                                                                                                                                                                                                                                                                 | Notes                          |
| ------------------------ | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **entrypoint**           | **str**                        | A script that will be run to start your job.This command will be run in the root directory of the specified runtime env. Eg. 'python script.py'                                                                                                                             | \[optional] \[default to ]     |
| **ray\_serve\_config**   | **object**                     | The Ray Serve config to use for this Production service. This config defines your Ray Serve application, and will be passed directly to Ray Serve. You can learn more about Ray Serve config files here: <https://docs.ray.io/en/latest/serve/production-guide/config.html> | \[optional] \[default to null] |
| **runtime\_env**         | **RayRuntimeEnvConfig**        | A ray runtime env json. Your entrypoint will be run in the environment specified by this runtime env.                                                                                                                                                                       | \[optional] \[default to null] |
| **build\_id**            | **str**                        | The id of the cluster env build. This id will determine the docker image your job is run on.                                                                                                                                                                                | \[default to null]             |
| **compute\_config\_id**  | **str**                        | The id of the compute configuration that you want to use. This id will specify the resources required for your job                                                                                                                                                          | \[default to null]             |
| **compute\_config**      | **CreateClusterComputeConfig** | One-off compute that the cluster will use.                                                                                                                                                                                                                                  | \[optional] \[default to null] |
| **max\_retries**         | **int**                        | The number of retries this job will attempt on failure. Set to None to set infinite retries                                                                                                                                                                                 | \[optional] \[default to 5]    |
| **timeout\_s**           | **int**                        | The timeout in seconds for each job run. Set to None for no limit to be set                                                                                                                                                                                                 | \[optional] \[default to null] |
| **runtime\_env\_config** | **RayRuntimeEnvConfig**        | DEPRECATED: Use runtime\_env                                                                                                                                                                                                                                                | \[optional] \[default to null] |

### `ProductionJobStateTransition`[​](#productionjobstatetransition "Direct link to productionjobstatetransition")

| Name                        | Type                | Description                                                 | Notes                          |
| --------------------------- | ------------------- | ----------------------------------------------------------- | ------------------------------ |
| **id**                      | **str**             | The id of this job state transition                         | \[default to null]             |
| **state\_transitioned\_at** | **datetime**        | The last time the state of this job was updated             | \[default to null]             |
| **current\_state**          | **HaJobStates**     | The current state of the job                                | \[default to null]             |
| **goal\_state**             | **HaJobGoalStates** | The goal state of the job                                   | \[optional] \[default to null] |
| **error**                   | **str**             | An error message that occurred in this job state transition | \[optional] \[default to null] |
| **operation\_message**      | **str**             | The logging message for this job state transition           | \[optional] \[default to null] |
| **cluster\_id**             | **str**             | The id of the cluster the job is running on                 | \[optional] \[default to null] |

### `ProductionjobListResponse`[​](#productionjoblistresponse "Direct link to productionjoblistresponse")

A list response form the API. Contains a field "results" which has the contents of the response.

| Name         | Type                     | Description | Notes                          |
| ------------ | ------------------------ | ----------- | ------------------------------ |
| **results**  | **List\[ProductionJob]** |             | \[default to null]             |
| **metadata** | **ListResponseMetadata** |             | \[optional] \[default to null] |

### `ProductionjobResponse`[​](#productionjobresponse "Direct link to productionjobresponse")

A response from the API. Contains a field "result" which has the contents of the response.

| Name       | Type              | Description | Notes              |
| ---------- | ----------------- | ----------- | ------------------ |
| **result** | **ProductionJob** |             | \[default to null] |

### `RayRuntimeEnvConfig`[​](#rayruntimeenvconfig "Direct link to rayruntimeenvconfig")

A runtime env config. Can be used to start a production job.

| Name                       | Type               | Description                                                                                                                                                                                                                              | Notes                          |
| -------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **working\_dir**           | **str**            | The working directory that your code will run in. Must be a remote URI like an s3 or git path.                                                                                                                                           | \[optional] \[default to null] |
| **py\_modules**            | **List\[str]**     | Python modules that will be installed along with your runtime env. These must be remote URIs.                                                                                                                                            | \[optional] \[default to null] |
| **relative\_working\_dir** | **str**            | Relative path to the working directory that your code will run in. The appropriate cloud deployment object storage will be prepended to this path.                                                                                       | \[optional] \[default to null] |
| **relative\_py\_modules**  | **List\[str]**     | Relative paths to python modules that will be installed along with your runtime env. The appropriate cloud deployment object storage will be prepended to these paths. If \`py\_modules\` are specified, they will be also be installed. | \[optional] \[default to null] |
| **py\_executable**         | **str**            | Specifies the executable used for running the Ray workers. It can include arguments as well.                                                                                                                                             | \[optional] \[default to null] |
| **pip**                    | **List\[str]**     | A list of pip packages to install.                                                                                                                                                                                                       | \[optional] \[default to null] |
| **conda**                  | **object**         | \[Union\[Dict\[str, Any], str]: Either the conda YAML config or the name of a local conda env (e.g., \&quot;pytorch\_p36\&quot;),                                                                                                        | \[optional] \[default to null] |
| **env\_vars**              | **Dict(str, str)** | Environment variables to set.                                                                                                                                                                                                            | \[optional] \[default to null] |
| **config**                 | **object**         | Config for runtime environment. Can be used to setup setup\_timeout\_seconds, the timeout of runtime environment creation.                                                                                                               | \[optional] \[default to null] |
| **image\_uri**             | **str**            | Specifies the image URI of the container in which the job will run.                                                                                                                                                                      | \[optional] \[default to null] |

### `SortByClauseJobsSortField`[​](#sortbyclausejobssortfield "Direct link to sortbyclausejobssortfield")

This model is used in the backend to represent the SQL ORDER BY clauses.

| Name            | Type              | Description | Notes              |
| --------------- | ----------------- | ----------- | ------------------ |
| **sort\_field** | **JobsSortField** |             | \[default to null] |
| **sort\_order** | **SortOrder**     |             | \[default to null] |
