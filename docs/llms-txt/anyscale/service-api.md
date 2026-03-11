# Source: https://docs.anyscale.com/reference/service-api.md

# Source: https://docs.anyscale.com/archive/ref/service-api.md

# Service API Reference (Legacy)

[View Markdown](/archive/ref/service-api.md)

# Service API Reference (Legacy)

warning

These methods are deprecated and will be fully removed from the Anyscale platform on January 29, 2026. To continue using these methods, install Anyscale CLI version 0.26.72 or earlier. Please use the [current APIs](/reference/service-api.md) instead.

## Service CLI[​](#service-cli "Direct link to Service CLI")

### `anyscale service rollout` Deprecated[​](#anyscale-service-rollout-deprecated "Direct link to anyscale-service-rollout-deprecated")

Deprecated

`anyscale service rollout` has been deprecated. and will be removed on 2025-10-01. Please use `anyscale service deploy` instead.

**Usage**

`anyscale service rollout [OPTIONS]`

\[DEPRECATED - use 'deploy' instead] Roll out a service.

**Options**

* **`-f/--config-file/--service-config-file`**: The path of the service configuration file.
* **`--name/-n`**: Name of service.
* **`--version`**: Version of service.
* **`--max-surge-percent`**: Max amount of excess capacity allocated during the rollout (0-100).
* **`--canary-percent`**: The percentage of traffic to send to the canary version of the service.
* **`--rollout-strategy`**: Strategy for rollout.
* **`-i/--in-place`**: Alias for `--rollout-strategy=IN_PLACE`.
* **`--no-auto-complete-rollout`**: Do not complete the rollout (terminate the existing version cluster) after the canary version reaches 100%

## Service SDK[​](#service-sdk "Direct link to Service SDK")

The AnyscaleSDK class must be constructed in order to make calls to the SDK. This class allows you to create an authenticated client in which to use the SDK.

| Param        | Type            | Description                                                                                                                                                                                                                                                                   |
| ------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auth_token` | Optional String | Authentication token used to verify you have permissions to access Anyscale. If not provided, permissions default to the credentials set for your current user. Credentials can be set by following the instructions on this page: <https://console.anyscale.com/credentials> |

**Example**

```
from anyscale import AnyscaleSDK

sdk = AnyscaleSDK()
```

### `get_service`[​](#get_service "Direct link to get_service")

Get a Service

Parameters

| Name         | Type | Description | Notes            |
| ------------ | ---- | ----------- | ---------------- |
| `service_id` | str  |             | Defaults to null |

Returns ServicemodelResponse

### `rollback_service`[​](#rollback_service "Direct link to rollback_service")

Rollback a Service

Parameters

| Name                     | Type                 | Description | Notes            |
| ------------------------ | -------------------- | ----------- | ---------------- |
| `service_id`             | str                  |             | Defaults to null |
| `rollback_service_model` | RollbackServiceModel |             |                  |

Returns ServicemodelResponse

### `rollout_service`[​](#rollout_service "Direct link to rollout_service")

Rollout a service

Parameters

| Name                  | Type              | Description | Notes |
| --------------------- | ----------------- | ----------- | ----- |
| `apply_service_model` | ApplyServiceModel |             |       |

Returns ServicemodelResponse

### `terminate_service`[​](#terminate_service "Direct link to terminate_service")

Terminate a Service

Parameters

| Name         | Type | Description | Notes            |
| ------------ | ---- | ----------- | ---------------- |
| `service_id` | str  |             | Defaults to null |

Returns ServicemodelResponse

### `list_services`[​](#list_services "Direct link to list_services")

Parameters

| Name             | Type                            | Description                                                                                                | Notes            |
| ---------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------- |
| `project_id`     | optional str                    | project\_id to filter by                                                                                   | Defaults to null |
| `name`           | optional str                    | name to filter by                                                                                          | Defaults to null |
| `state_filter`   | List\[ServiceEventCurrentState] | A list of Service states to filter by                                                                      | Defaults to \[]  |
| `archive_status` | ArchiveStatus                   | The archive status to filter by. Defaults to unarchived.                                                   | Defaults to null |
| `creator_id`     | optional str                    | creator\_id to filter by                                                                                   | Defaults to null |
| `cloud_id`       | optional str                    | cloud\_id to filter by                                                                                     | Defaults to null |
| `sort_field`     | ServiceSortField                | If absent, the default sorting order is 1. status (active first).2. Last updated at (desc). 3. Name (asc). | Defaults to null |
| `sort_order`     | SortOrder                       | If sort\_field is absent, this field is ignored.If absent, this field defaults to ascending.               | Defaults to null |
| `paging_token`   | optional str                    |                                                                                                            | Defaults to null |
| `count`          | optional int                    |                                                                                                            | Defaults to null |

Returns ServicemodelListResponse

## Service Models[​](#service-models "Direct link to Service Models")

### `ApplyProductionServiceV2Model`[​](#applyproductionservicev2model "Direct link to applyproductionservicev2model")

DEPRECATED. Please do not use this model directly. Use ApplyServiceModel.

| Name                                    | Type                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                          |
| --------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **name**                                | **str**                         | Name of the Service                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | \[default to null]             |
| **description**                         | **str**                         | Description of the Service                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | \[optional] \[default to null] |
| **project\_id**                         | **str**                         | Id of the project this Service will start clusters in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \[optional] \[default to null] |
| **version**                             | **str**                         | A version string that represents the version for this service. Will be populated with the hash of the config if not specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | \[optional] \[default to null] |
| **canary\_percent**                     | **int**                         | A manual target percent for this service. If this field is not set, the service will automatically roll out. If set, this should be a number between 0 and 100. The newly created version will have weight \`canary\_percent\` and the existing version will have \`100 - canary\_percent\`.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | \[optional] \[default to null] |
| **ray\_serve\_config**                  | **object**                      | The Ray Serve config to use for this service. This config defines your Ray Serve application, and will be passed directly to Ray Serve. You can learn more about Ray Serve config files here: <https://docs.ray.io/en/latest/serve/production-guide/config.html>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | \[default to null]             |
| **build\_id**                           | **str**                         | The id of the cluster env build. This id will determine the docker image your Service is run using.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | \[default to null]             |
| **compute\_config\_id**                 | **str**                         | The id of the compute configuration that you want to use. This id will specify the resources required for your ServiceThe compute template includes a \`cloud\_id\` that must be fixed for each service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | \[default to null]             |
| **config**                              | **ServiceConfig**               | Target Service's configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | \[optional] \[default to null] |
| **rollout\_strategy**                   | **RolloutStrategy**             | Strategy for rollout. The ROLLOUT strategy will deploy your Ray Serve configuration onto a newly started cluster, and then shift traffic over to the new cluster. You can manually control the speed of the rollout using the canary\_percent configuration. The IN\_PLACE strategy will use Ray Serve in place upgrade to update your existing cluster in place. When using this rollout strategy, you may only change the ray\_serve\_config field. You cannot partially shift traffic or rollback an in place upgrade. In place upgrades are faster and riskier than rollouts, and we recommend only using them for relatively safe changes (for example, increasing the number of replicas on a Ray Serve deployment). Default strategy is ROLLOUT. | \[optional] \[default to null] |
| **ray\_gcs\_external\_storage\_config** | **RayGCSExternalStorageConfig** | Config for the Ray GCS to connect to external storage. If populated, head node fault tolerance will be enabled for this service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | \[optional] \[default to null] |
| **tracing\_config**                     | **TracingConfig**               | Config for initializing tracing within Anyscale runtime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | \[optional] \[default to null] |
| **auto\_complete\_rollout**             | **bool**                        | Flag to indicate whether or not to complete the rollout after the canary version reaches 100%.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | \[optional] \[default to true] |
| **max\_surge\_percent**                 | **int**                         | Max amount of excess capacity allocated during the rollout (0-100).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | \[optional] \[default to null] |

### `ApplyServiceModel`[​](#applyservicemodel "Direct link to applyservicemodel")

This is the model used to apply a Service.

| Name                                    | Type                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                          |
| --------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **name**                                | **str**                         | Name of the Service                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | \[default to null]             |
| **description**                         | **str**                         | Description of the Service                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | \[optional] \[default to null] |
| **project\_id**                         | **str**                         | Id of the project this Service will start clusters in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | \[optional] \[default to null] |
| **version**                             | **str**                         | A version string that represents the version for this service. Will be populated with the hash of the config if not specified.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | \[optional] \[default to null] |
| **canary\_percent**                     | **int**                         | A manual target percent for this service. If this field is not set, the service will automatically roll out. If set, this should be a number between 0 and 100. The newly created version will have weight \`canary\_percent\` and the existing version will have \`100 - canary\_percent\`.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | \[optional] \[default to null] |
| **ray\_serve\_config**                  | **object**                      | The Ray Serve config to use for this service. This config defines your Ray Serve application, and will be passed directly to Ray Serve. You can learn more about Ray Serve config files here: <https://docs.ray.io/en/latest/serve/production-guide/config.html>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | \[default to null]             |
| **build\_id**                           | **str**                         | The id of the cluster env build. This id will determine the docker image your Service is run using.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | \[default to null]             |
| **compute\_config\_id**                 | **str**                         | The id of the compute configuration that you want to use. This id will specify the resources required for your ServiceThe compute template includes a \`cloud\_id\` that must be fixed for each service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | \[default to null]             |
| **config**                              | **ServiceConfig**               | Target Service's configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | \[optional] \[default to null] |
| **rollout\_strategy**                   | **RolloutStrategy**             | Strategy for rollout. The ROLLOUT strategy will deploy your Ray Serve configuration onto a newly started cluster, and then shift traffic over to the new cluster. You can manually control the speed of the rollout using the canary\_percent configuration. The IN\_PLACE strategy will use Ray Serve in place upgrade to update your existing cluster in place. When using this rollout strategy, you may only change the ray\_serve\_config field. You cannot partially shift traffic or rollback an in place upgrade. In place upgrades are faster and riskier than rollouts, and we recommend only using them for relatively safe changes (for example, increasing the number of replicas on a Ray Serve deployment). Default strategy is ROLLOUT. | \[optional] \[default to null] |
| **ray\_gcs\_external\_storage\_config** | **RayGCSExternalStorageConfig** | Config for the Ray GCS to connect to external storage. If populated, head node fault tolerance will be enabled for this service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | \[optional] \[default to null] |
| **tracing\_config**                     | **TracingConfig**               | Config for initializing tracing within Anyscale runtime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | \[optional] \[default to null] |
| **auto\_complete\_rollout**             | **bool**                        | Flag to indicate whether or not to complete the rollout after the canary version reaches 100%.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | \[optional] \[default to true] |
| **max\_surge\_percent**                 | **int**                         | Max amount of excess capacity allocated during the rollout (0-100).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | \[optional] \[default to null] |

### `ListServiceModel`[​](#listservicemodel "Direct link to listservicemodel")

The list model for Services. Please note that this model can be used for both Service v1 and v2. You can use the `type` field to differentiate between the two.

| Name                             | Type                         | Description                                                                                                               | Notes                          |
| -------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **id**                           | **str**                      |                                                                                                                           | \[default to null]             |
| **name**                         | **str**                      |                                                                                                                           | \[default to null]             |
| **creator\_id**                  | **str**                      | Id of the user who created the Service                                                                                    | \[default to null]             |
| **created\_at**                  | **datetime**                 | Time the Service was created                                                                                              | \[default to null]             |
| **project\_id**                  | **str**                      | Id of the project this Service will start clusters in. This configuration cannot be changed after the service is created. | \[default to null]             |
| **current\_state**               | **ServiceEventCurrentState** | The current state of this service                                                                                         | \[default to null]             |
| **endtime**                      | **datetime**                 |                                                                                                                           | \[optional] \[default to null] |
| **type**                         | **ServiceType**              | Type of the Service                                                                                                       | \[optional] \[default to null] |
| **service\_observability\_urls** | **ServiceObservabilityUrls** | A JSON object with useful urls pointing to Grafana dashboards.                                                            | \[default to null]             |

### `ListservicemodelListResponse`[​](#listservicemodellistresponse "Direct link to listservicemodellistresponse")

A list response form the API. Contains a field "results" which has the contents of the response.

| Name         | Type                        | Description | Notes                          |
| ------------ | --------------------------- | ----------- | ------------------------------ |
| **results**  | **List\[ListServiceModel]** |             | \[default to null]             |
| **metadata** | **ListResponseMetadata**    |             | \[optional] \[default to null] |

### `ProductionServiceV2Model`[​](#productionservicev2model "Direct link to productionservicev2model")

DEPRECATED. Please use ServiceModel with new sdk calls.

| Name                             | Type                                       | Description                                                                                                                                              | Notes                          |
| -------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **id**                           | **str**                                    | Id of the Service                                                                                                                                        | \[default to null]             |
| **name**                         | **str**                                    | Name of the Service                                                                                                                                      | \[default to null]             |
| **description**                  | **str**                                    | Description of the Service                                                                                                                               | \[optional] \[default to null] |
| **project\_id**                  | **str**                                    | Id of the project this Service will start clusters in. This configuration cannot be changed after the service is created.                                | \[default to null]             |
| **cloud\_id**                    | **str**                                    | Id of the cloud this Service belongs to, and will launch clusters in. This configuration cannot be changed.                                              | \[default to null]             |
| **creator\_id**                  | **str**                                    | Id of the user who created the Service                                                                                                                   | \[default to null]             |
| **created\_at**                  | **datetime**                               | Time the Service was created                                                                                                                             | \[default to null]             |
| **hostname**                     | **str**                                    | The hostname of the service                                                                                                                              | \[default to null]             |
| **current\_state**               | **ServiceEventCurrentState**               | The current state of this service                                                                                                                        | \[default to null]             |
| **goal\_state**                  | **ServiceGoalStates**                      | The goal state of this service                                                                                                                           | \[default to null]             |
| **auth\_token**                  | **str**                                    | Token to use for service auth. To use the token, add it as a header with the key 'Authorization' and the value 'Bearer \<token>'                         | \[optional] \[default to null] |
| **auto\_rollout\_enabled**       | **bool**                                   | Whether or not the service is using auto rollout                                                                                                         | \[default to null]             |
| **versions**                     | **List\[ProductionServiceV2VersionModel]** | DEPRECATED. Please use \`primary\_version\` and \`canary\_version\` fields. Active versions of this service, sorted by creation time in ascending order. | \[default to null]             |
| **primary\_version**             | **ProductionServiceV2VersionModel**        | Primary version of this service. If the service is terminated, this field refers to the most recently active version.                                    | \[default to null]             |
| **canary\_version**              | **ProductionServiceV2VersionModel**        | Canary version of this service. Present only if the service is in the \`ROLLING\_OUT\` state.                                                            | \[optional] \[default to null] |
| **service\_observability\_urls** | **ServiceObservabilityUrls**               | A JSON object with useful urls pointing to Grafana dashboards.                                                                                           | \[default to null]             |
| **base\_url**                    | **str**                                    | The base url of this service                                                                                                                             | \[default to null]             |
| **ended\_at**                    | **datetime**                               | Time the Service was terminated                                                                                                                          | \[optional] \[default to null] |

### `ProductionServiceV2VersionModel`[​](#productionservicev2versionmodel "Direct link to productionservicev2versionmodel")

| Name                                    | Type                            | Description                                                                                                                                                                                  | Notes                          |
| --------------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **id**                                  | **str**                         | Id of the Service Version                                                                                                                                                                    | \[default to null]             |
| **created\_at**                         | **datetime**                    | Time the version was created                                                                                                                                                                 | \[default to null]             |
| **weight**                              | **int**                         | The target percentage of traffic sent to this version. This is a number between 0 and 100.                                                                                                   | \[default to null]             |
| **current\_weight**                     | **int**                         | The current percentage of traffic sent to this version. This is a number between 0 and 100.                                                                                                  | \[optional] \[default to null] |
| **version**                             | **str**                         | The version string identifier for this version                                                                                                                                               | \[default to null]             |
| **ray\_serve\_config**                  | **object**                      |                                                                                                                                                                                              | \[default to null]             |
| **ray\_gcs\_external\_storage\_config** | **RayGCSExternalStorageConfig** | Config for the Ray GCS to connect to external storage. If populated, head node fault tolerance is enabled for this service.                                                                  | \[optional] \[default to null] |
| **tracing\_config**                     | **TracingConfig**               | Config for initializing tracing within Anyscale runtime.                                                                                                                                     | \[optional] \[default to null] |
| **build\_id**                           | **str**                         | The id of the cluster env build. This id will determine the docker image your Service is run using.                                                                                          | \[default to null]             |
| **compute\_config\_id**                 | **str**                         | The id of the compute configuration that you want to use. This id will specify the resources required for your Service.The compute template includes a \`cloud\_id\` that cannot be updated. | \[default to null]             |
| **production\_job\_ids**                | **List\[str]**                  | The list of production job ids associated with this service version.                                                                                                                         | \[default to null]             |
| **current\_state**                      | **ServiceVersionState**         | The current state of the service version.                                                                                                                                                    | \[default to null]             |

### `Productionservicev2ModelResponse`[​](#productionservicev2modelresponse "Direct link to productionservicev2modelresponse")

A response from the API. Contains a field "result" which has the contents of the response.

| Name       | Type                         | Description | Notes              |
| ---------- | ---------------------------- | ----------- | ------------------ |
| **result** | **ProductionServiceV2Model** |             | \[default to null] |

### `RollbackServiceModel`[​](#rollbackservicemodel "Direct link to rollbackservicemodel")

The rollback model for Services.

| Name                    | Type    | Description                                       | Notes                          |
| ----------------------- | ------- | ------------------------------------------------- | ------------------------------ |
| **max\_surge\_percent** | **int** | The max\_surge\_percent to use when rolling back. | \[optional] \[default to null] |

### `RolloutStrategy`[​](#rolloutstrategy "Direct link to rolloutstrategy")

An enumeration.

Possible Values: \['ROLLOUT', 'IN\_PLACE']

### `ServiceConfig`[​](#serviceconfig "Direct link to serviceconfig")

| Name                          | Type             | Description                                                                                                                                                              | Notes                          |
| ----------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| **max\_uptime\_timeout\_sec** | **int**          | Auto-termination timeout (in seconds) for target Service to be unconditionally terminated after specified period. Setting this to 0 disables auto-termination (default). | \[optional] \[default to 0]    |
| **access**                    | **AccessConfig** | Access configuration                                                                                                                                                     | \[optional] \[default to null] |
| **protocols**                 | **Protocols**    | Protocol setups for the service                                                                                                                                          | \[optional] \[default to null] |
| **env\_vars**                 | **object**       | Environment variables to set on the service cluster                                                                                                                      | \[optional] \[default to null] |

### `ServiceEventCurrentState`[​](#serviceeventcurrentstate "Direct link to serviceeventcurrentstate")

The possible 'current state' values for a service These states may be shown in the UI as the primary state of the service

Possible Values: \['RUNNING', 'UNHEALTHY', 'SYSTEM\_FAILURE', 'USER\_ERROR\_FAILURE', 'STARTING', 'TERMINATING', 'TERMINATED', 'UPDATING', 'ROLLING\_OUT', 'ROLLING\_BACK']

### `ServiceGoalStates`[​](#servicegoalstates "Direct link to servicegoalstates")

An enumeration.

Possible Values: \['RUNNING', 'TERMINATED']

### `ServiceModel`[​](#servicemodel "Direct link to servicemodel")

This is the Service model returned by the get path.

| Name                             | Type                                       | Description                                                                                                                                              | Notes                          |
| -------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **id**                           | **str**                                    | Id of the Service                                                                                                                                        | \[default to null]             |
| **name**                         | **str**                                    | Name of the Service                                                                                                                                      | \[default to null]             |
| **description**                  | **str**                                    | Description of the Service                                                                                                                               | \[optional] \[default to null] |
| **project\_id**                  | **str**                                    | Id of the project this Service will start clusters in. This configuration cannot be changed after the service is created.                                | \[default to null]             |
| **cloud\_id**                    | **str**                                    | Id of the cloud this Service belongs to, and will launch clusters in. This configuration cannot be changed.                                              | \[default to null]             |
| **creator\_id**                  | **str**                                    | Id of the user who created the Service                                                                                                                   | \[default to null]             |
| **created\_at**                  | **datetime**                               | Time the Service was created                                                                                                                             | \[default to null]             |
| **hostname**                     | **str**                                    | The hostname of the service                                                                                                                              | \[default to null]             |
| **current\_state**               | **ServiceEventCurrentState**               | The current state of this service                                                                                                                        | \[default to null]             |
| **goal\_state**                  | **ServiceGoalStates**                      | The goal state of this service                                                                                                                           | \[default to null]             |
| **auth\_token**                  | **str**                                    | Token to use for service auth. To use the token, add it as a header with the key 'Authorization' and the value 'Bearer \<token>'                         | \[optional] \[default to null] |
| **auto\_rollout\_enabled**       | **bool**                                   | Whether or not the service is using auto rollout                                                                                                         | \[default to null]             |
| **versions**                     | **List\[ProductionServiceV2VersionModel]** | DEPRECATED. Please use \`primary\_version\` and \`canary\_version\` fields. Active versions of this service, sorted by creation time in ascending order. | \[default to null]             |
| **primary\_version**             | **ProductionServiceV2VersionModel**        | Primary version of this service. If the service is terminated, this field refers to the most recently active version.                                    | \[default to null]             |
| **canary\_version**              | **ProductionServiceV2VersionModel**        | Canary version of this service. Present only if the service is in the \`ROLLING\_OUT\` state.                                                            | \[optional] \[default to null] |
| **service\_observability\_urls** | **ServiceObservabilityUrls**               | A JSON object with useful urls pointing to Grafana dashboards.                                                                                           | \[default to null]             |
| **base\_url**                    | **str**                                    | The base url of this service                                                                                                                             | \[default to null]             |
| **ended\_at**                    | **datetime**                               | Time the Service was terminated                                                                                                                          | \[optional] \[default to null] |

### `ServiceObservabilityUrls`[​](#serviceobservabilityurls "Direct link to serviceobservabilityurls")

| Name                                             | Type    | Description                                                                                                         | Notes                          |
| ------------------------------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **service\_dashboard\_url**                      | **str** | URL that points to a dashboard with relevant graphs about the entire service.                                       | \[optional] \[default to null] |
| **service\_dashboard\_embedding\_url**           | **str** | URL that points to a dashboard with relevant graphs about the entire service for embedding.                         | \[optional] \[default to null] |
| **serve\_deployment\_dashboard\_url**            | **str** | URL that points to a dashboard with relevant graphs about a single deployent or replica of a service.               | \[optional] \[default to null] |
| **serve\_deployment\_dashboard\_embedding\_url** | **str** | URL that points to a dashboard with relevant graphs about a single deployent or replica of a service for embedding. | \[optional] \[default to null] |

### `ServiceSortField`[​](#servicesortfield "Direct link to servicesortfield")

An enumeration.

Possible Values: \['STATUS', 'NAME', 'CREATED\_AT']

### `ServiceType`[​](#servicetype "Direct link to servicetype")

An enumeration.

Possible Values: \['V1', 'V2']

### `ServiceVersionState`[​](#serviceversionstate "Direct link to serviceversionstate")

The possible 'current state' values for a service version. These states are used in the UI and SDK/CLI.

Possible Values: \['UNKNOWN', 'STARTING', 'UPDATING', 'RUNNING', 'UNHEALTHY', 'SYSTEM\_FAILURE', 'TERMINATING', 'TERMINATED']

### `ServicemodelListResponse`[​](#servicemodellistresponse "Direct link to servicemodellistresponse")

A list response form the API. Contains a field "results" which has the contents of the response.

| Name         | Type                     | Description | Notes                          |
| ------------ | ------------------------ | ----------- | ------------------------------ |
| **results**  | **List\[ServiceModel]**  |             | \[default to null]             |
| **metadata** | **ListResponseMetadata** |             | \[optional] \[default to null] |

### `ServicemodelResponse`[​](#servicemodelresponse "Direct link to servicemodelresponse")

A response from the API. Contains a field "result" which has the contents of the response.

| Name       | Type             | Description | Notes              |
| ---------- | ---------------- | ----------- | ------------------ |
| **result** | **ServiceModel** |             | \[default to null] |
