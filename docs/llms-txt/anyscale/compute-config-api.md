# Source: https://docs.anyscale.com/reference/compute-config-api.md

# Source: https://docs.anyscale.com/archive/ref/compute-config-api.md

# Compute Config API Reference (Legacy)

[View Markdown](/archive/ref/compute-config-api.md)

# Compute Config API Reference (Legacy)

warning

These methods are deprecated and will be fully removed from the Anyscale platform on January 29, 2026. To continue using these methods, install Anyscale CLI version 0.26.72 or earlier. Please use the [current APIs](/reference/compute-config-api.md) instead.

## Compute Config SDK[​](#compute-config-sdk "Direct link to Compute Config SDK")

The AnyscaleSDK class must be constructed in order to make calls to the SDK. This class allows you to create an authenticated client in which to use the SDK.

| Param        | Type            | Description                                                                                                                                                                                                                                                                   |
| ------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auth_token` | Optional String | Authentication token used to verify you have permissions to access Anyscale. If not provided, permissions default to the credentials set for your current user. Credentials can be set by following the instructions on this page: <https://console.anyscale.com/credentials> |

**Example**

```
from anyscale import AnyscaleSDK

sdk = AnyscaleSDK()
```

### `create_cluster_compute`[​](#create_cluster_compute "Direct link to create_cluster_compute")

Creates a Cluster Compute. If the specified compute config is anonymous, returns an existing compute config if an anonymous one exists with the same config.

Parameters

| Name                     | Type                 | Description | Notes |
| ------------------------ | -------------------- | ----------- | ----- |
| `create_cluster_compute` | CreateClusterCompute |             |       |

Returns ClustercomputeResponse

### `delete_cluster_compute`[​](#delete_cluster_compute "Direct link to delete_cluster_compute")

Deletes a Cluster Compute.

Parameters

| Name                 | Type | Description                          | Notes            |
| -------------------- | ---- | ------------------------------------ | ---------------- |
| `cluster_compute_id` | str  | ID of the Cluster Compute to delete. | Defaults to null |

Returns void (empty response body)

### `get_cluster_compute`[​](#get_cluster_compute "Direct link to get_cluster_compute")

Retrieves a Cluster Compute.

Parameters

| Name                 | Type | Description                            | Notes            |
| -------------------- | ---- | -------------------------------------- | ---------------- |
| `cluster_compute_id` | str  | ID of the Cluster Compute to retrieve. | Defaults to null |

Returns ClustercomputeResponse

### `get_default_cluster_compute`[​](#get_default_cluster_compute "Direct link to get_default_cluster_compute")

Returns a default cluster compute that can be used with a given cloud.

Parameters

| Name       | Type         | Description                                                                                        | Notes            |
| ---------- | ------------ | -------------------------------------------------------------------------------------------------- | ---------------- |
| `cloud_id` | optional str | The cloud id whose default cluster compute you want to fetch. If None, will use the default cloud. | Defaults to null |

Returns ClustercomputeResponse

### `search_cluster_computes`[​](#search_cluster_computes "Direct link to search_cluster_computes")

Lists all Cluster Computes the user has access to, matching the input query.

Parameters

| Name                     | Type                 | Description | Notes |
| ------------------------ | -------------------- | ----------- | ----- |
| `cluster_computes_query` | ClusterComputesQuery |             |       |

Returns ClustercomputeListResponse

## Compute Config Models[​](#compute-config-models "Direct link to Compute Config Models")

### `ClusterCompute`[​](#clustercompute "Direct link to clustercompute")

| Name                   | Type                     | Description | Notes                          |
| ---------------------- | ------------------------ | ----------- | ------------------------------ |
| **id**                 | **str**                  |             | \[default to null]             |
| **name**               | **str**                  |             | \[default to null]             |
| **creator\_id**        | **str**                  |             | \[default to null]             |
| **organization\_id**   | **str**                  |             | \[default to null]             |
| **project\_id**        | **str**                  |             | \[optional] \[default to null] |
| **created\_at**        | **datetime**             |             | \[default to null]             |
| **last\_modified\_at** | **datetime**             |             | \[default to null]             |
| **deleted\_at**        | **datetime**             |             | \[optional] \[default to null] |
| **archived\_at**       | **datetime**             |             | \[optional] \[default to null] |
| **config**             | **ClusterComputeConfig** |             | \[default to null]             |
| **version**            | **int**                  |             | \[default to null]             |
| **anonymous**          | **bool**                 |             | \[default to null]             |

### `ClusterComputeConfig`[​](#clustercomputeconfig "Direct link to clustercomputeconfig")

Configuration of compute resources to use for launching a Cluster. Used when reading a cluster compute.

| Name                                    | Type                                    | Description                                                                                                                                                                                                                                                                                                                     | Notes                           |
| --------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **cloud\_id**                           | **str**                                 | The ID of the Anyscale cloud to use for launching Clusters.                                                                                                                                                                                                                                                                     | \[default to null]              |
| **maximum\_uptime\_minutes**            | **int**                                 | If set to a positive number, Anyscale will terminate the cluster this many minutes after cluster start.                                                                                                                                                                                                                         | \[optional] \[default to null]  |
| **deployment\_configs**                 | **List\[CloudDeploymentComputeConfig]** | A list of cloud deployment-specific configs to use.                                                                                                                                                                                                                                                                             | \[optional] \[default to null]  |
| **max\_workers**                        | **int**                                 | DEPRECATED. This attribute will be ignored - please use the \&quot;max\_resources\&quot; flag to configure resource limits.                                                                                                                                                                                                     | \[optional] \[default to null]  |
| **region**                              | **str**                                 | The region to launch Clusters in, e.g. \&quot;us-west-2\&quot;.                                                                                                                                                                                                                                                                 | \[optional] \[default to null]  |
| **allowed\_azs**                        | **List\[str]**                          | The availability zones that sessions are allowed to be launched in, e.g. \&quot;us-west-2a\&quot;. If not specified or \&quot;any\&quot; is provided as the option, any AZ may be used. If \&quot;any\&quot; is provided, it must be the only item in the list.                                                                 | \[optional] \[default to null]  |
| **head\_node\_type**                    | **ComputeNodeType**                     | Node configuration to use for the head node.                                                                                                                                                                                                                                                                                    | \[default to null]              |
| **worker\_node\_types**                 | **List\[WorkerNodeType]**               | A list of node types to use for worker nodes.                                                                                                                                                                                                                                                                                   | \[optional] \[default to null]  |
| **aws\_advanced\_configurations\_json** | **object**                              | \[DEPRECATED: use advanced\_configurations\_json instead] The advanced configuration json that we pass directly AWS APIs when launching an instance. We may do some validation on this json and reject the json if it is using a configuration that Anyscale does not support.                                                  | \[optional] \[default to null]  |
| **gcp\_advanced\_configurations\_json** | **object**                              | \[DEPRECATED: use advanced\_configurations\_json instead] The advanced configuration json that we pass directly GCP APIs when launching an instance. We may do some validation on this json and reject the json if it is using a configuration that Anyscale does not support.                                                  | \[optional] \[default to null]  |
| **advanced\_configurations\_json**      | **object**                              | Advanced configurations for this compute node type to pass to the cloud provider when launching this instance.                                                                                                                                                                                                                  | \[optional] \[default to null]  |
| **auto\_select\_worker\_config**        | **bool**                                | If set to true, worker node groups will automatically be selected based on workload.                                                                                                                                                                                                                                            | \[optional] \[default to false] |
| **flags**                               | **object**                              | A set of advanced cluster-level flags that can be used to configure a particular workload.                                                                                                                                                                                                                                      | \[optional] \[default to null]  |
| **idle\_termination\_minutes**          | **int**                                 | If set to a positive number, Anyscale will terminate the cluster this many minutes after the cluster is idle. Idle time is defined as the time during which a Cluster is not running a user command or a Ray driver. Time spent running commands on Jupyter or ssh is still considered 'idle'. To disable, set this field to 0. | \[optional] \[default to null]  |

### `ClusterComputesQuery`[​](#clustercomputesquery "Direct link to clustercomputesquery")

| Name                   | Type          | Description                                                                                                                                                                                                                                                                                                                                                                      | Notes                           |
| ---------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **project\_id**        | **str**       | Filters Cluster Computes by project. If this field is absent, no filtering is done.                                                                                                                                                                                                                                                                                              | \[optional] \[default to null]  |
| **creator\_id**        | **str**       | Filters Cluster Computes by creator. If this field is absent, no filtering is done.                                                                                                                                                                                                                                                                                              | \[optional] \[default to null]  |
| **name**               | **TextQuery** | Filters Cluster Computes by name. If this field is absent, no filtering is done.                                                                                                                                                                                                                                                                                                 | \[optional] \[default to null]  |
| **include\_anonymous** | **bool**      | Whether to include anonymous Cluster Computes in the search.                                                                                                                                                                                                                                                                                                                     | \[optional] \[default to false] |
| **paging**             | **PageQuery** | Pagination information.                                                                                                                                                                                                                                                                                                                                                          | \[optional] \[default to null]  |
| **cloud\_id**          | **str**       | Filters Compute Computes by cloud. If this field is absent, no filtering is done.                                                                                                                                                                                                                                                                                                | \[optional] \[default to null]  |
| **version**            | **int**       | Filters Cluster Computes by version. Versions are positive integers. Setting this field to -1 will return only the latest version of each Cluster Compute. Setting this field to -2 will not filter by version. For example, this can be used to fetch all versions of a Cluster Compute. Deprecated behavior: Setting version to None is equivalent to setting version to '-1'. | \[optional] \[default to null]  |

### `ClustercomputeListResponse`[​](#clustercomputelistresponse "Direct link to clustercomputelistresponse")

A list response form the API. Contains a field "results" which has the contents of the response.

| Name         | Type                      | Description | Notes                          |
| ------------ | ------------------------- | ----------- | ------------------------------ |
| **results**  | **List\[ClusterCompute]** |             | \[default to null]             |
| **metadata** | **ListResponseMetadata**  |             | \[optional] \[default to null] |

### `ClustercomputeResponse`[​](#clustercomputeresponse "Direct link to clustercomputeresponse")

A response from the API. Contains a field "result" which has the contents of the response.

| Name       | Type               | Description | Notes              |
| ---------- | ------------------ | ----------- | ------------------ |
| **result** | **ClusterCompute** |             | \[default to null] |

### `ComputeNodeType`[​](#computenodetype "Direct link to computenodetype")

| Name                                    | Type               | Description                                                                                                                                                                                                          | Notes                          |
| --------------------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **name**                                | **str**            | An arbitrary name for this node type, which will be registered with OSS available\_node\_types.                                                                                                                      | \[default to null]             |
| **instance\_type**                      | **str**            | The cloud provider instance type to use for this node.                                                                                                                                                               | \[default to null]             |
| **resources**                           | **Resources**      | Declaration of node resources for Autoscaler.                                                                                                                                                                        | \[optional] \[default to null] |
| **labels**                              | **Dict(str, str)** | Labels to associate the node with for scheduling purposes. Defaults to the list of Ray & Anyscale default labels.                                                                                                    | \[optional] \[default to null] |
| **aws\_advanced\_configurations\_json** | **object**         | The advanced configuration json that we pass directly AWS APIs when launching an instance. We may do some validation on this json and reject the json if it is using a configuration that Anyscale does not support. | \[optional] \[default to null] |
| **gcp\_advanced\_configurations\_json** | **object**         | The advanced configuration json that we pass directly GCP APIs when launching an instance. We may do some validation on this json and reject the json if it is using a configuration that Anyscale does not support. | \[optional] \[default to null] |
| **advanced\_configurations\_json**      | **object**         | Advanced configurations for this compute node type to pass to the cloud provider when launching this instance.                                                                                                       | \[optional] \[default to null] |
| **flags**                               | **object**         | A set of advanced node-level flags that can be used to configure a particular workload.                                                                                                                              | \[optional] \[default to null] |

### `ComputeTemplate`[​](#computetemplate "Direct link to computetemplate")

DEPRECATED: Please use ClusterCompute instead.

| Name                   | Type                      | Description | Notes                          |
| ---------------------- | ------------------------- | ----------- | ------------------------------ |
| **id**                 | **str**                   |             | \[default to null]             |
| **name**               | **str**                   |             | \[default to null]             |
| **creator\_id**        | **str**                   |             | \[default to null]             |
| **organization\_id**   | **str**                   |             | \[default to null]             |
| **project\_id**        | **str**                   |             | \[optional] \[default to null] |
| **created\_at**        | **datetime**              |             | \[default to null]             |
| **last\_modified\_at** | **datetime**              |             | \[default to null]             |
| **deleted\_at**        | **datetime**              |             | \[optional] \[default to null] |
| **archived\_at**       | **datetime**              |             | \[optional] \[default to null] |
| **config**             | **ComputeTemplateConfig** |             | \[default to null]             |
| **version**            | **int**                   |             | \[default to null]             |
| **anonymous**          | **bool**                  |             | \[default to null]             |

### `ComputeTemplateConfig`[​](#computetemplateconfig "Direct link to computetemplateconfig")

DEPRECATED: Please use ClusterCompute and the corresponding ClusterComputeConfig instead. Configuration of compute resources to use for launching a session. Used when reading a compute template.

| Name                                    | Type                                    | Description                                                                                                                                                                                                                                                                                                                     | Notes                           |
| --------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **cloud\_id**                           | **str**                                 | The ID of the Anyscale cloud to use for launching sessions.                                                                                                                                                                                                                                                                     | \[default to null]              |
| **maximum\_uptime\_minutes**            | **int**                                 | If set to a positive number, Anyscale will terminate the cluster this many minutes after cluster start.                                                                                                                                                                                                                         | \[optional] \[default to null]  |
| **deployment\_configs**                 | **List\[CloudDeploymentComputeConfig]** | A list of cloud deployment-specific configs to use.                                                                                                                                                                                                                                                                             | \[optional] \[default to null]  |
| **max\_workers**                        | **int**                                 | DEPRECATED. This attribute will be ignored - please use the \&quot;max\_resources\&quot; flag to configure resource limits.                                                                                                                                                                                                     | \[optional] \[default to null]  |
| **region**                              | **str**                                 | The region to launch sessions in, e.g. \&quot;us-west-2\&quot;.                                                                                                                                                                                                                                                                 | \[optional] \[default to null]  |
| **allowed\_azs**                        | **List\[str]**                          | The availability zones that sessions are allowed to be launched in, e.g. \&quot;us-west-2a\&quot;. If not specified or \&quot;any\&quot; is provided as the option, any AZ may be used. If \&quot;any\&quot; is provided, it must be the only item in the list.                                                                 | \[optional] \[default to null]  |
| **head\_node\_type**                    | **ComputeNodeType**                     | Node configuration to use for the head node.                                                                                                                                                                                                                                                                                    | \[default to null]              |
| **worker\_node\_types**                 | **List\[WorkerNodeType]**               | A list of node types to use for worker nodes.                                                                                                                                                                                                                                                                                   | \[optional] \[default to null]  |
| **aws\_advanced\_configurations\_json** | **object**                              | The advanced configuration json that we pass directly AWS APIs when launching an instance. We may do some validation on this json and reject the json if it is using a configuration that Anyscale does not support.                                                                                                            | \[optional] \[default to null]  |
| **gcp\_advanced\_configurations\_json** | **object**                              | The advanced configuration json that we pass directly GCP APIs when launching an instance. We may do some validation on this json and reject the json if it is using a configuration that Anyscale does not support.                                                                                                            | \[optional] \[default to null]  |
| **advanced\_configurations\_json**      | **object**                              | Advanced configurations for this compute node type to pass to the cloud provider when launching this instance.                                                                                                                                                                                                                  | \[optional] \[default to null]  |
| **auto\_select\_worker\_config**        | **bool**                                | If set to true, worker node groups will automatically be selected based on workload.                                                                                                                                                                                                                                            | \[optional] \[default to false] |
| **flags**                               | **object**                              | A set of advanced cluster-level flags that can be used to configure a particular workload.                                                                                                                                                                                                                                      | \[optional] \[default to null]  |
| **idle\_termination\_minutes**          | **int**                                 | If set to a positive number, Anyscale will terminate the cluster this many minutes after the cluster is idle. Idle time is defined as the time during which a Cluster is not running a user command or a Ray driver. Time spent running commands on Jupyter or ssh is still considered 'idle'. To disable, set this field to 0. | \[optional] \[default to null]  |

### `ComputetemplateResponse`[​](#computetemplateresponse "Direct link to computetemplateresponse")

A response from the API. Contains a field "result" which has the contents of the response.

| Name       | Type                | Description | Notes              |
| ---------- | ------------------- | ----------- | ------------------ |
| **result** | **ComputeTemplate** |             | \[default to null] |

### `ComputetemplateconfigResponse`[​](#computetemplateconfigresponse "Direct link to computetemplateconfigresponse")

A response from the API. Contains a field "result" which has the contents of the response.

| Name       | Type                      | Description | Notes              |
| ---------- | ------------------------- | ----------- | ------------------ |
| **result** | **ComputeTemplateConfig** |             | \[default to null] |

### `CreateClusterCompute`[​](#createclustercompute "Direct link to createclustercompute")

| Name             | Type                           | Description                                                                                                                                | Notes                           |
| ---------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| **name**         | **str**                        |                                                                                                                                            | \[optional] \[default to null]  |
| **project\_id**  | **str**                        |                                                                                                                                            | \[optional] \[default to null]  |
| **config**       | **CreateClusterComputeConfig** |                                                                                                                                            | \[default to null]              |
| **anonymous**    | **bool**                       | An anonymous Cluster Compute does not show up in the list of cluster configs. They can still have a name so they can be easily identified. | \[optional] \[default to false] |
| **new\_version** | **bool**                       | If a Cluster Compute with the same name already exists, create this config as a new version.                                               | \[optional] \[default to false] |

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
