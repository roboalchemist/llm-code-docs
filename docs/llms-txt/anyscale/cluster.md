# Source: https://docs.anyscale.com/archive/ref/cluster.md

# Cluster API Reference (Legacy)

[View Markdown](/archive/ref/cluster.md)

# Cluster API Reference (Legacy)

warning

These methods are deprecated and will be fully removed from the Anyscale platform on January 29, 2026. To continue using these methods, install Anyscale CLI version 0.26.72 or earlier.

## Cluster CLI[​](#cluster-cli "Direct link to Cluster CLI")

### `anyscale cluster start` Legacy[​](#anyscale-cluster-start-legacy "Direct link to anyscale-cluster-start-legacy")

warning

This command is deprecated. Upgrade to anyscale workspace\_v2 start.

**Usage**

`anyscale cluster start [OPTIONS]`

Start or update and restart a cluster on Anyscale.

**Options**

* **`--name/-n`**: Name of new or existing cluster to start or update.
* **`--env`**: Set the Anyscale app config to use for the cluster. This is a cluster environment name optionally followed by a colon and a build version number. Eg: my\_cluster\_env
  <!-- -->
  :1
* **`--docker`**: Custom docker image name.
* **`--python-version`**: Python version for the custom docker image.
* **`--ray-version`**: Ray version for the custom docker image.
* **`--compute`**: Name of compute config that is already registered with Anyscale. To use specific version, use the format `compute_name:version`.
* **`--compute-file`**: The YAML file of the compute config to launch this cluster with. An example can be found at <https://docs.anyscale.com/configure/compute-configs/overview>.
* **`--cluster-id/--id`**: Id of existing cluster to restart. This argument can be used to interact with any cluster you have access to in any project.
* **`--project-id`**: Override project id used for this cluster. If not provided, the Anyscale project context will be used if it exists. Otherwise a default project will be used.
* **`--project`**: Override project name used for this cluster. If not provided, the Anyscale project context will be used if it exists. Otherwise a default project will be used.
* **`--cloud-name`**: Name of cloud to create a default compute config with. If a default cloud needs to be used and this is not provided, the organization default cloud will be used.
* **`--idle-timeout`**: DEPRECATED: Please specify the idle\_termination\_minutes field in the compute config. Idle timeout (in minutes), after which the cluster is stopped. Idle time is defined as the time during which a cluster is not running a user command and does not have an attached driver. Time spent running Jupyter commands, or commands run through ssh, is still considered 'idle'. -1 means no timeout. Default: 120 minutes
* **`--user-service-access`**: Whether user service (eg: serve deployment) can be accessed by public internet traffic. If public, a user service endpoint can be queried from the public internet with the provided authentication token. If private, the user service endpoint can only be queried from within the same Anyscale cloud and will not require an authentication token.

### `anyscale cluster terminate` Legacy[​](#anyscale-cluster-terminate-legacy "Direct link to anyscale-cluster-terminate-legacy")

warning

This command is deprecated. Upgrade to anyscale workspace\_v2 terminate.

**Usage**

`anyscale cluster terminate [OPTIONS]`

Terminate a cluster on Anyscale.

**Options**

* **`--name/-n`**: Name of existing cluster to terminate.
* **`--cluster-id/--id`**: Id of existing cluster to termiante. This argument can be used to interact with any cluster you have access to in any project.
* **`--project-id`**: Override project id used for this cluster. If not provided, the Anyscale project context will be used if it exists. Otherwise a default project will be used.
* **`--project`**: Override project name used for this cluster. If not provided, the Anyscale project context will be used if it exists. Otherwise a default project will be used.
* **`--cloud-id`**: Use cloud ID to disambiguate only when selecting a cluster to terminate with `--name`that doesn't belong to any project. This requires cloud isolation to be enabled.
* **`--cloud`**: Use cloud to disambiguate only when selecting a cluster to terminate with `--name`that doesn't belong to any project. This requires cloud isolation to be enabled.

## Cluster SDK[​](#cluster-sdk "Direct link to Cluster SDK")

The AnyscaleSDK class must be constructed in order to make calls to the SDK. This class allows you to create an authenticated client in which to use the SDK.

| Param        | Type            | Description                                                                                                                                                                                                                                                                   |
| ------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auth_token` | Optional String | Authentication token used to verify you have permissions to access Anyscale. If not provided, permissions default to the credentials set for your current user. Credentials can be set by following the instructions on this page: <https://console.anyscale.com/credentials> |

**Example**

```
from anyscale import AnyscaleSDK

sdk = AnyscaleSDK()
```

### `launch_cluster`[​](#launch_cluster "Direct link to launch_cluster")

Starts a Cluster in the specified Project.

If a Cluster with the specified name already exists, we will update that Cluster. Otherwise, a new Cluster will be created.

Returns the started Cluster object.

Raises an Exception if starting Cluster fails or times out.

| Param                          | Type             | Description                                                                                                   |
| ------------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------- |
| `project_id`                   | String           | ID of the Project the Cluster belongs to                                                                      |
| `cluster_name`                 | String           | Name of the Cluster                                                                                           |
| `cluster_environment_build_id` | String           | ID of the Cluster Environment Build to start this Cluster with                                                |
| `cluster_compute_id`           | Optional String  | ID of the Cluster Compute to start this Cluster with                                                          |
| `cluster_compute_config`       | Optional Dict    | One-off Cluster Compute that this Cluster will use, with same fields as ClusterComputeConfig                  |
| `poll_rate_seconds`            | Optional Integer | seconds to wait when polling cluster operation status; defaults to 15                                         |
| `idle_timeout_minutes`         | Optional Integer | Idle timeout (in minutes), after which the Cluster is terminated; Defaults to 120 minutes.                    |
| `timeout_seconds`              | Optional Integer | maximum number of seconds to wait for cluster operation to complete before timing out; defaults to no timeout |

**Example**

```
from anyscale import AnyscaleSDK

sdk = AnyscaleSDK(auth_token="sss_YourAuthToken")

cluster = sdk.launch_cluster(
    project_id="project_id",
    cluster_name="my-cluster",
    cluster_environment_build_id="cluster_environment_build_id",
    cluster_compute_id="cluster_compute_id")

print(f"Cluster started successfully: {cluster}")
```

### `launch_cluster_with_new_cluster_environment`[​](#launch_cluster_with_new_cluster_environment "Direct link to launch_cluster_with_new_cluster_environment")

Builds a new Cluster Environment, then starts a Cluster in the specified Project with the new build.

If a Cluster with the specified name already exists, we will update that Cluster. Otherwise, a new Cluster will be created.

Returns the started Cluster object.

Raises an Exception if building Cluster Environment fails or starting the Cluster fails.

| Param                        | Type                     | Description                                                                                            |
| ---------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------ |
| `project_id`                 | String                   | ID of the Project the Cluster belongs to                                                               |
| `cluster_name`               | String                   | Name of the Cluster                                                                                    |
| `create_cluster_environment` | CreateClusterEnvironment | CreateClusterEnvironment object                                                                        |
| `cluster_compute_id`         | Optional String          | Cluster Compute to start this Cluster with                                                             |
| `cluster_compute_config`     | Optional Dict            | One-off Cluster Compute that this Cluster will use, with same fields as ClusterComputeConfig           |
| `poll_rate_seconds`          | Optional Integer         | seconds to wait when polling operation status; defaults to 15                                          |
| `timeout_seconds`            | Optional Integer         | maximum number of seconds to wait for operations to complete before timing out; defaults to no timeout |

**Example**

```
from anyscale import AnyscaleSDK
from anyscale.sdk.anyscale_client.models.create_cluster_environment import (
    CreateClusterEnvironment,
)

sdk = AnyscaleSDK(auth_token="sss_YourAuthToken")

create_cluster_environment = CreateClusterEnvironment(
    name="my-cluster-environment",
    config_json={"base_image": "anyscale/ray:1.4.1-py37"}
)

cluster = sdk.launch_cluster_with_new_cluster_environment(
    project_id="project_id",
    cluster_name="my-cluster",
    create_cluster_environment=create_cluster_environment,
    cluster_compute_id="cluster_compute_id",
)

print(f"Cluster started successfully: {cluster}")
```

info

The OpenAPI schemas for types below can be found at the [Anyscale OpenAPI Documentation](https://api.anyscale.com/v0/docs#)

All of the following functions are synchronous by default. To make an asynchronous HTTP request, please pass async\_req=True. The return value for the asynchronous calls is a thread.

```
thread = api.create_cloud(create_cloud, async_req=True)
result = thread.get()
```

### `create_cluster`[​](#create_cluster "Direct link to create_cluster")

Creates a Cluster.

Parameters

| Name             | Type          | Description | Notes |
| ---------------- | ------------- | ----------- | ----- |
| `create_cluster` | CreateCluster |             |       |

Returns ClusterResponse

### `delete_cluster`[​](#delete_cluster "Direct link to delete_cluster")

Deletes a Cluster.

Parameters

| Name         | Type | Description                  | Notes            |
| ------------ | ---- | ---------------------------- | ---------------- |
| `cluster_id` | str  | ID of the Cluster to delete. | Defaults to null |

Returns void (empty response body)

### `get_cluster`[​](#get_cluster "Direct link to get_cluster")

Retrieves a Cluster.

Parameters

| Name         | Type | Description                    | Notes            |
| ------------ | ---- | ------------------------------ | ---------------- |
| `cluster_id` | str  | ID of the Cluster to retreive. | Defaults to null |

Returns ClusterResponse

### `search_clusters`[​](#search_clusters "Direct link to search_clusters")

Searches for all Clusters the user has access to that satisfies the query.

Parameters

| Name             | Type          | Description | Notes |
| ---------------- | ------------- | ----------- | ----- |
| `clusters_query` | ClustersQuery |             |       |

Returns ClusterListResponse

### `start_cluster`[​](#start_cluster "Direct link to start_cluster")

Initializes workflow to transition the Cluster into the Running state. This is a long running operation. Clients will need to poll the operation's status to determine completion. The options parameter is DEPRECATED.

Parameters

| Name                    | Type                | Description                 | Notes            |
| ----------------------- | ------------------- | --------------------------- | ---------------- |
| `cluster_id`            | str                 | ID of the Cluster to start. | Defaults to null |
| `start_cluster_options` | StartClusterOptions |                             |                  |

Returns ClusteroperationResponse

### `terminate_cluster`[​](#terminate_cluster "Direct link to terminate_cluster")

Initializes workflow to transition the Cluster into the Terminated state. This is a long running operation. Clients will need to poll the operation's status to determine completion.

Parameters

| Name                        | Type                    | Description                     | Notes            |
| --------------------------- | ----------------------- | ------------------------------- | ---------------- |
| `cluster_id`                | str                     | ID of the Cluster to terminate. | Defaults to null |
| `terminate_cluster_options` | TerminateClusterOptions |                                 |                  |

Returns ClusteroperationResponse

### `update_cluster`[​](#update_cluster "Direct link to update_cluster")

Updates a Cluster.

Parameters

| Name             | Type          | Description                  | Notes            |
| ---------------- | ------------- | ---------------------------- | ---------------- |
| `cluster_id`     | str           | ID of the Cluster to update. | Defaults to null |
| `update_cluster` | UpdateCluster |                              |                  |

Returns ClusterResponse

## Cluster Models[​](#cluster-models "Direct link to Cluster Models")

### `ClusterHeadNodeInfo`[​](#clusterheadnodeinfo "Direct link to clusterheadnodeinfo")

Details about the head node of a running Cluster.

| Name            | Type    | Description                                   | Notes              |
| --------------- | ------- | --------------------------------------------- | ------------------ |
| **url**         | **str** | URL for the head node of this Cluster.        | \[default to null] |
| **ip\_address** | **str** | IP address for the head node of this Cluster. | \[default to null] |

### `ClusterListResponse`[​](#clusterlistresponse "Direct link to clusterlistresponse")

A list response form the API. Contains a field "results" which has the contents of the response.

| Name         | Type                     | Description | Notes                          |
| ------------ | ------------------------ | ----------- | ------------------------------ |
| **results**  | **List\[Cluster]**       |             | \[default to null]             |
| **metadata** | **ListResponseMetadata** |             | \[optional] \[default to null] |

### `ClusterManagementStackVersions`[​](#clustermanagementstackversions "Direct link to clustermanagementstackversions")

An enumeration.

Possible Values: \['v1', 'v2']

### `ClusterOperation`[​](#clusteroperation "Direct link to clusteroperation")

Describes a long running Cluster operation that will eventually complete.

| Name                         | Type                     | Description                                                                                                                                     | Notes                          |
| ---------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **id**                       | **str**                  | ID of this operation.                                                                                                                           | \[default to null]             |
| **completed**                | **bool**                 | Boolean indicating if this operation is completed.                                                                                              | \[default to null]             |
| **progress**                 | **OperationProgress**    | Details about the progress of this operation at the time of the request. This will be absent for completed operations.                          | \[optional] \[default to null] |
| **result**                   | **OperationResult**      | The result of this operation after it has completed. This is always provided when the operation is complete.                                    | \[optional] \[default to null] |
| **cluster\_id**              | **str**                  | ID of the Cluster that is being updated.                                                                                                        | \[default to null]             |
| **cluster\_operation\_type** | **ClusterOperationType** | The variety of operation being performed: start sets the Cluster's goal state to Running, terminate sets the Cluster's goal state to Terminated | \[default to null]             |

### `ClusterResponse`[​](#clusterresponse "Direct link to clusterresponse")

A response from the API. Contains a field "result" which has the contents of the response.

| Name       | Type        | Description | Notes              |
| ---------- | ----------- | ----------- | ------------------ |
| **result** | **Cluster** |             | \[default to null] |

### `ClusterServicesUrls`[​](#clusterservicesurls "Direct link to clusterservicesurls")

URLs for additional services running in the Cluster. (ex/ Jupyter, Ray Dashboard). This fields can only be populated after the Cluster has finished starting. An absent field indicates the service is not available.

| Name                                           | Type    | Description                                                                          | Notes                          |
| ---------------------------------------------- | ------- | ------------------------------------------------------------------------------------ | ------------------------------ |
| **webterminal\_auth\_url**                     | **str** | URL to authenticate with the webterminal                                             | \[optional] \[default to null] |
| **metrics\_dashboard\_url**                    | **str** | URL for Grafana (metrics) dashboard.                                                 | \[optional] \[default to null] |
| **data\_metrics\_dashboard\_url**              | **str** | URL for the data Grafana dashboard.                                                  | \[optional] \[default to null] |
| **train\_metrics\_dashboard\_url**             | **str** | URL for the train Grafana dashboard.                                                 | \[optional] \[default to null] |
| **serve\_metrics\_dashboard\_url**             | **str** | URL for the serve Grafana dashboard.                                                 | \[optional] \[default to null] |
| **serve\_deployment\_metrics\_dashboard\_url** | **str** | URL for the serve deployment Grafana dashboard.                                      | \[optional] \[default to null] |
| **serve\_llm\_metrics\_dashboard\_url**        | **str** | URL for the serve LLM Grafana dashboard.                                             | \[optional] \[default to null] |
| **persistent\_metrics\_url**                   | **str** | URL for the persistent Grafana (metrics) dashboard in the non-running cluster state. | \[optional] \[default to null] |
| **connect\_url**                               | **str** | URL for Anyscale connect.                                                            | \[optional] \[default to null] |
| **jupyter\_notebook\_url**                     | **str** | URL for Jupyter Lab.                                                                 | \[optional] \[default to null] |
| **ray\_dashboard\_url**                        | **str** | URL for Ray dashboard.                                                               | \[optional] \[default to null] |
| **service\_proxy\_url**                        | **str** | URL for web services proxy (e.g. jupyter, tensorboard, etc).                         | \[optional] \[default to null] |
| **user\_service\_url**                         | **str** | URL to access user services (e.g. Ray Serve)                                         | \[optional] \[default to null] |

### `ClusterState`[​](#clusterstate "Direct link to clusterstate")

Possible States for a Cluster.

Possible Values: \['Terminated', 'StartingUp', 'StartupErrored', 'Running', 'Updating', 'UpdatingErrored', 'Terminating', 'AwaitingStartup', 'TerminatingErrored', 'Unknown']

### `ClusterStatus`[​](#clusterstatus "Direct link to clusterstatus")

An enumeration.

Possible Values: \['STARTING', 'RUNNING', 'RECOVERING', 'RESTARTING', 'TERMINATING', 'TERMINATED']

### `ClusterStatusDetails`[​](#clusterstatusdetails "Direct link to clusterstatusdetails")

ClusterStatusDetails is a more granular status than ClusterStatus.

Possible Values: \['LAUNCHING\_NODES', 'CONFIGURING\_HEAD\_NODE', 'UPDATING\_CONTAINERS']

### `ClusteroperationResponse`[​](#clusteroperationresponse "Direct link to clusteroperationresponse")

A response from the API. Contains a field "result" which has the contents of the response.

| Name       | Type                 | Description | Notes              |
| ---------- | -------------------- | ----------- | ------------------ |
| **result** | **ClusterOperation** |             | \[default to null] |

### `ClustersQuery`[​](#clustersquery "Direct link to clustersquery")

Query model used to filter Clusters.

| Name                | Type                    | Description                                                                             | Notes                          |
| ------------------- | ----------------------- | --------------------------------------------------------------------------------------- | ------------------------------ |
| **project\_id**     | **str**                 | Filters Clusters belonging to a Project. If this field is absent, no filtering is done. | \[optional] \[default to null] |
| **name**            | **TextQuery**           | Filters Clusters by name. If this field is absent, no filtering is done.                | \[optional] \[default to null] |
| **paging**          | **PageQuery**           | Pagination information.                                                                 | \[optional] \[default to null] |
| **state\_filter**   | **List\[ClusterState]** | Filter Sessions by Session State. If this field is an empty set, no filtering is done.  | \[optional] \[default to \[]]  |
| **archive\_status** | **ArchiveStatus**       | The archive status to filter by. Defaults to unarchived.                                | \[optional] \[default to null] |

### `CreateCluster`[​](#createcluster "Direct link to createcluster")

Model used to create a new Cluster.

| Name                                 | Type                           | Description                                                                                                                                                                                                                                                                                                                          | Notes                           |
| ------------------------------------ | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| **name**                             | **str**                        | Name of this Cluster.                                                                                                                                                                                                                                                                                                                | \[default to null]              |
| **project\_id**                      | **str**                        | Project that this Cluster belongs to. If none, this Cluster will use the default Project.                                                                                                                                                                                                                                            | \[optional] \[default to null]  |
| **cluster\_environment\_build\_id**  | **str**                        | Cluster Environment Build that this Cluster is using.                                                                                                                                                                                                                                                                                | \[default to null]              |
| **cluster\_compute\_id**             | **str**                        | Cluster Compute that this Cluster is using.                                                                                                                                                                                                                                                                                          | \[optional] \[default to null]  |
| **cluster\_compute\_config**         | **CreateClusterComputeConfig** | One-off cluster compute that this cluster is using.                                                                                                                                                                                                                                                                                  | \[optional] \[default to null]  |
| **idle\_timeout\_minutes**           | **int**                        | Idle timeout (in minutes), after which the Cluster is terminated. Idle time is defined as the time during which a Cluster is not running a user command (through 'anyscale exec' or the Web UI), and does not have an attached driver. Time spent running Jupyter commands, or commands run through ssh, is still considered 'idle'. | \[optional] \[default to null]  |
| **allow\_public\_internet\_traffic** | **bool**                       | Whether public internet traffic can access Serve endpoints or if an authentication token is required.                                                                                                                                                                                                                                | \[optional] \[default to false] |
| **user\_service\_access**            | **UserServiceAccessTypes**     | Whether user service can be accessed by public internet traffic.                                                                                                                                                                                                                                                                     | \[optional] \[default to null]  |
| **user\_service\_token**             | **str**                        | User service token that is used to authenticate access to public user services. This must be a valid 32 byte URL safe string and can be generated by calling \`secrets.token\_urlsafe(32))\`. This is ignored if the user service has private access. If not specified for a public user service, a token is autogenerated.          | \[optional] \[default to null]  |
| **ha\_job\_id**                      | **str**                        | This is used internally by Anyscale to associate clusters to a job. It is set automatically and should *not* be used directly.                                                                                                                                                                                                       | \[optional] \[default to null]  |

### `StartClusterOptions`[​](#startclusteroptions "Direct link to startclusteroptions")

Options to set when starting a Cluster.

| Name                                 | Type     | Description                                                                                                                                          | Notes                          |
| ------------------------------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **cluster\_environment\_build\_id**  | **str**  | Cluster Environment Build used to start Cluster.                                                                                                     | \[optional] \[default to null] |
| **cluster\_compute\_id**             | **str**  | Cluster Compute used to start the Cluster.                                                                                                           | \[optional] \[default to null] |
| **allow\_public\_internet\_traffic** | **bool** | Whether public internet traffic can access Serve endpoints or if an authentication token is required. Will not update current value if not provided. | \[optional] \[default to null] |

### `TerminateClusterOptions`[​](#terminateclusteroptions "Direct link to terminateclusteroptions")

Options to set when terminating a Cluster.

| Name               | Type     | Description                                                                                                                                              | Notes                           |
| ------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **take\_snapshot** | **bool** | DEPRECATED: Snapshotting is no longer supported.For reproducible environments between clusters, please use Cluster Environments or Runtime Environments. | \[optional] \[default to false] |

### `UpdateCluster`[​](#updatecluster "Direct link to updatecluster")

Model used to update a Cluster. A field will not be updated if its value is absent.

| Name                                | Type    | Description                                                                                                                                                                                                                | Notes                          |
| ----------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **name**                            | **str** | Name of this Cluster.                                                                                                                                                                                                      | \[optional] \[default to null] |
| **idle\_timeout\_minutes**          | **int** | Idle timeout in minutes.                                                                                                                                                                                                   | \[optional] \[default to null] |
| **cluster\_environment\_build\_id** | **str** | Cluster Environment Build that this Cluster is using. This property may only be changed if the Cluster is in the Terminated state.Use the Start Cluster operation if you wish to change this for a non-Terminated Cluster. | \[optional] \[default to null] |
| **cluster\_compute\_id**            | **str** | Cluster Compute that this Cluster is using. This property may only be changed if the Cluster is in the Terminated state. Use the Start Cluster operation if you wish to change this for a non-Terminated Cluster.          | \[optional] \[default to null] |
