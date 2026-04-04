# Source: https://docs.anyscale.com/reference/image.md

# Source: https://docs.anyscale.com/archive/ref/image.md

# Cluster environment API Reference (Legacy)

[View Markdown](/archive/ref/image.md)

# Cluster environment API Reference (Legacy)

warning

These methods are deprecated and will be fully removed from the Anyscale platform on January 29, 2026. To continue using these methods, install Anyscale CLI version 0.26.72 or earlier. Please use the [current APIs](/reference/image.md) instead.

## Cluster environment CLI[​](#cluster-environment-cli "Direct link to Cluster environment CLI")

### `anyscale image archive` Legacy[​](#anyscale-image-archive-legacy "Direct link to anyscale-image-archive-legacy")

Limited support

This command is not actively maintained. Use with caution.

**Usage**

`anyscale image archive [OPTIONS]`

Archive the specified cluster environment.

**Options**

* **`--name/-n`**: Name of the cluster environment to archive.
* **`--cluster-env-id/--id`**: Id of the cluster environment to archive. Must be provided if a cluster environment name is not given.

### `anyscale image build` Legacy[​](#anyscale-image-build-legacy "Direct link to anyscale-image-build-legacy")

warning

This command is deprecated. Upgrade to anyscale image build.

**Usage**

`anyscale image build [OPTIONS] CLUSTER_ENV_FILE`

Build a new cluster environment from config file.

**Options**

* **`--name/-n`**: Name to save built cluster environment as. Default will be used if not provided

### `anyscale image get` Legacy[​](#anyscale-image-get-legacy "Direct link to anyscale-image-get-legacy")

warning

This command is deprecated. Upgrade to anyscale image get.

**Usage**

`anyscale image get [OPTIONS] [CLUSTER_ENV_NAME]`

Get details about cluster environment build. The `cluster-env-name` argument is a cluster environment name optionally followed by a colon and a build version number. Eg: my\_cluster\_env<!-- -->:1

**Options**

* **`--cluster-env-build-id/--id`**: Get details about cluster environment build by this id.

### `anyscale image list` Legacy[​](#anyscale-image-list-legacy "Direct link to anyscale-image-list-legacy")

Limited support

This command is not actively maintained. Use with caution.

**Usage**

`anyscale image list [OPTIONS]`

List information about cluster environments on Anyscale. By default only list cluster environments you have created.

**Options**

* **`--name/-n`**: List information about all builds of the cluster environment with this name.
* **`--cluster-env-id/--id`**: List information about all builds of the cluster environment with this id.
* **`--include-shared`**: Include all cluster environments you have access to.
* **`--max-items`**: Max items to show in list.

## Cluster environment SDK[​](#cluster-environment-sdk "Direct link to Cluster environment SDK")

The AnyscaleSDK class must be constructed in order to make calls to the SDK. This class allows you to create an authenticated client in which to use the SDK.

| Param        | Type            | Description                                                                                                                                                                                                                                                                   |
| ------------ | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auth_token` | Optional String | Authentication token used to verify you have permissions to access Anyscale. If not provided, permissions default to the credentials set for your current user. Credentials can be set by following the instructions on this page: <https://console.anyscale.com/credentials> |

**Example**

```
from anyscale import AnyscaleSDK

sdk = AnyscaleSDK()
```

### `create_byod_cluster_environment_build`[​](#create_byod_cluster_environment_build "Direct link to create_byod_cluster_environment_build")

Creates and starts a BYOD Cluster Environment Build.

Parameters

| Name                                    | Type                              | Description | Notes |
| --------------------------------------- | --------------------------------- | ----------- | ----- |
| `create_byod_cluster_environment_build` | CreateBYODClusterEnvironmentBuild |             |       |

Returns ClusterenvironmentbuildoperationResponse

### `create_cluster_environment_build`[​](#create_cluster_environment_build "Direct link to create_cluster_environment_build")

Creates and starts a Cluster Environment Build. This is a long running operation.

Parameters

| Name                               | Type                          | Description | Notes |
| ---------------------------------- | ----------------------------- | ----------- | ----- |
| `create_cluster_environment_build` | CreateClusterEnvironmentBuild |             |       |

Returns ClusterenvironmentbuildoperationResponse

### `find_cluster_environment_build_by_identifier`[​](#find_cluster_environment_build_by_identifier "Direct link to find_cluster_environment_build_by_identifier")

Looks for a cluster environment build given a cluster environment identifier. Identifiers are in the format my-cluster-env<!-- -->:1

Parameters

| Name         | Type | Description                                                                                       | Notes            |
| ------------ | ---- | ------------------------------------------------------------------------------------------------- | ---------------- |
| `identifier` | str  | Identifier of the cluster env to look for. Identifiers are in the format my-cluster-env<!-- -->:1 | Defaults to null |

Returns ClusterenvironmentbuildResponse

### `get_cluster_environment_build`[​](#get_cluster_environment_build "Direct link to get_cluster_environment_build")

Retrieves a Cluster Environment Build.

Parameters

| Name                           | Type | Description                                      | Notes            |
| ------------------------------ | ---- | ------------------------------------------------ | ---------------- |
| `cluster_environment_build_id` | str  | ID of the Cluster Environment Build to retrieve. | Defaults to null |

Returns ClusterenvironmentbuildResponse

### `get_default_cluster_environment_build`[​](#get_default_cluster_environment_build "Direct link to get_default_cluster_environment_build")

Retrieves a default cluster environment with the preferred attributes.

Parameters

| Name             | Type          | Description                                                                                                                                                                              | Notes            |
| ---------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `python_version` | PythonVersion | Python version for the cluster environment                                                                                                                                               | Defaults to null |
| `ray_version`    | str           | Ray version to use for this cluster environment. Should match a version string found in the ray version history on pypi. See here for full list: <https://pypi.org/project/ray/#history> | Defaults to null |

Returns ClusterenvironmentbuildResponse

### `list_cluster_environment_builds`[​](#list_cluster_environment_builds "Direct link to list_cluster_environment_builds")

Lists all Cluster Environment Builds belonging to an Cluster Environment.

Parameters

| Name                     | Type          | Description                                       | Notes             |
| ------------------------ | ------------- | ------------------------------------------------- | ----------------- |
| `cluster_environment_id` | str           | ID of the Cluster Environment to list builds for. | Defaults to null  |
| `desc`                   | optional bool | Orders the list of builds from latest to oldest.  | Defaults to false |
| `paging_token`           | optional str  |                                                   | Defaults to null  |
| `count`                  | optional int  |                                                   | Defaults to 10    |

Returns ClusterenvironmentbuildListResponse

### `create_byod_cluster_environment`[​](#create_byod_cluster_environment "Direct link to create_byod_cluster_environment")

Creates a BYOD Cluster Environment.

Parameters

| Name                              | Type                         | Description | Notes |
| --------------------------------- | ---------------------------- | ----------- | ----- |
| `create_byod_cluster_environment` | CreateBYODClusterEnvironment |             |       |

Returns ClusterenvironmentResponse

### `create_cluster_environment`[​](#create_cluster_environment "Direct link to create_cluster_environment")

Creates a Cluster Environment.

Parameters

| Name                         | Type                     | Description | Notes |
| ---------------------------- | ------------------------ | ----------- | ----- |
| `create_cluster_environment` | CreateClusterEnvironment |             |       |

Returns ClusterenvironmentResponse

### `get_cluster_environment`[​](#get_cluster_environment "Direct link to get_cluster_environment")

Retrieves a Cluster Environment.

Parameters

| Name                     | Type | Description                                | Notes            |
| ------------------------ | ---- | ------------------------------------------ | ---------------- |
| `cluster_environment_id` | str  | ID of the Cluster Environment to retrieve. | Defaults to null |

Returns ClusterenvironmentResponse

### `search_cluster_environments`[​](#search_cluster_environments "Direct link to search_cluster_environments")

Lists all Cluster Environments that the logged in user has permissions to access.

Parameters

| Name                         | Type                     | Description | Notes |
| ---------------------------- | ------------------------ | ----------- | ----- |
| `cluster_environments_query` | ClusterEnvironmentsQuery |             |       |

Returns ClusterenvironmentListResponse

## Cluster environment Models[​](#cluster-environment-models "Direct link to Cluster environment Models")

### `ClusterEnvironment`[​](#clusterenvironment "Direct link to clusterenvironment")

| Name                   | Type         | Description                                                         | Notes                           |
| ---------------------- | ------------ | ------------------------------------------------------------------- | ------------------------------- |
| **id**                 | **str**      | Server assigned unique identifier.                                  | \[default to null]              |
| **name**               | **str**      | Name of the Cluster Environment.                                    | \[default to null]              |
| **project\_id**        | **str**      | ID of the Project this Cluster Environment is for.                  | \[optional] \[default to null]  |
| **organization\_id**   | **str**      | ID of the Organization this Cluster Environment was created in.     | \[default to null]              |
| **creator\_id**        | **str**      | ID of the User that created this record.                            | \[default to null]              |
| **created\_at**        | **datetime** | Timestamp of when this record was created.                          | \[default to null]              |
| **last\_modified\_at** | **datetime** | Timestamp of when this record was last updated.                     | \[default to null]              |
| **deleted\_at**        | **datetime** | Timestamp of when this record was deleted.                          | \[optional] \[default to null]  |
| **anonymous**          | **bool**     | True if this is an anonymous Cluster Environment.                   | \[optional] \[default to false] |
| **is\_default**        | **bool**     | True if this Cluster Environment is created and managed by anyscale | \[optional] \[default to false] |

### `ClusterEnvironmentBuild`[​](#clusterenvironmentbuild "Direct link to clusterenvironmentbuild")

Usable Cluster Environment Build to start a Cluster.

| Name                         | Type                              | Description                                                                                                                                                                                                                                                                                                                                                                                        | Notes                          |
| ---------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **cluster\_environment\_id** | **str**                           | ID of the Cluster Environment this Build belongs to.                                                                                                                                                                                                                                                                                                                                               | \[default to null]             |
| **config\_json**             | **AppConfigConfigSchema**         | Config JSON used to create this Cluster Environment Build.                                                                                                                                                                                                                                                                                                                                         | \[optional] \[default to null] |
| **containerfile**            | **str**                           | The containerfile used to build the image.                                                                                                                                                                                                                                                                                                                                                         | \[optional] \[default to null] |
| **docker\_image\_name**      | **str**                           | The name of the docker image for this Build.                                                                                                                                                                                                                                                                                                                                                       | \[optional] \[default to null] |
| **registry\_login\_secret**  | **str**                           | The name or identifier of a secret containing credentials to authenticate to the docker registry hosting the image.                                                                                                                                                                                                                                                                                | \[optional] \[default to null] |
| **ray\_version**             | **str**                           | The Ray version to use for this build.                                                                                                                                                                                                                                                                                                                                                             | \[optional] \[default to null] |
| **id**                       | **str**                           | Server assigned unique identifier.                                                                                                                                                                                                                                                                                                                                                                 | \[default to null]             |
| **revision**                 | **int**                           | Auto incrementing version number for this Build                                                                                                                                                                                                                                                                                                                                                    | \[default to null]             |
| **creator\_id**              | **str**                           | ID of the user who created this Build.                                                                                                                                                                                                                                                                                                                                                             | \[default to null]             |
| **error\_message**           | **str**                           | Detailed error message. This will only be populated if the Build operation failed.                                                                                                                                                                                                                                                                                                                 | \[optional] \[default to null] |
| **status**                   | **ClusterEnvironmentBuildStatus** | Status of the Build. \`pending\` - Build operation is queued and has not started yet. \`in\_progress\` - Build operation is in progress. \`succeeded\` - Build operation completed successfully. \`failed\` - Build operation completed unsuccessfully. \`pending\_cancellation\` - Build operation is marked for cancellation. \`cancelled\` - Build operation was cancelled before it completed. | \[default to null]             |
| **created\_at**              | **datetime**                      | Timestamp of when this Build was created.                                                                                                                                                                                                                                                                                                                                                          | \[default to null]             |
| **last\_modified\_at**       | **datetime**                      | Timestamp of when this Build was last updated.                                                                                                                                                                                                                                                                                                                                                     | \[default to null]             |
| **deleted\_at**              | **datetime**                      | Timestamp of when this Build was deleted.                                                                                                                                                                                                                                                                                                                                                          | \[optional] \[default to null] |
| **is\_byod**                 | **bool**                          | True if the image URI used in this build was user-specified.                                                                                                                                                                                                                                                                                                                                       | \[default to null]             |
| **cloud\_id**                | **str**                           | The build cloud associated with this build. If None, the build is a v1 build.                                                                                                                                                                                                                                                                                                                      | \[optional] \[default to null] |
| **digest**                   | **str**                           | The digest of the image for this Build.                                                                                                                                                                                                                                                                                                                                                            | \[optional] \[default to null] |

### `ClusterEnvironmentBuildOperation`[​](#clusterenvironmentbuildoperation "Direct link to clusterenvironmentbuildoperation")

Describes a long running operation that will eventually complete. Consider this an abstract class. Specific kinds of operations should subclass this.

| Name                                | Type                  | Description                                                                                                            | Notes                          |
| ----------------------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **id**                              | **str**               | ID of this operation.                                                                                                  | \[default to null]             |
| **completed**                       | **bool**              | Boolean indicating if this operation is completed.                                                                     | \[default to null]             |
| **progress**                        | **OperationProgress** | Details about the progress of this operation at the time of the request. This will be absent for completed operations. | \[optional] \[default to null] |
| **result**                          | **OperationResult**   | The result of this operation after it has completed. This is always provided when the operation is complete.           | \[optional] \[default to null] |
| **cluster\_environment\_build\_id** | **str**               | ID of the Cluster Environment Build this operation is for.                                                             | \[default to null]             |

### `ClusterEnvironmentBuildStatus`[​](#clusterenvironmentbuildstatus "Direct link to clusterenvironmentbuildstatus")

An enumeration.

Possible Values: \['pending', 'in\_progress', 'succeeded', 'failed', 'pending\_cancellation', 'canceled']

### `ClusterEnvironmentsQuery`[​](#clusterenvironmentsquery "Direct link to clusterenvironmentsquery")

| Name                   | Type          | Description                                                                                                                                                                                                                                        | Notes                           |
| ---------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **project\_id**        | **str**       | Filters Cluster Environments by project id. If absent, no filtering is done.                                                                                                                                                                       | \[optional] \[default to null]  |
| **creator\_id**        | **str**       | Filters Cluster Environments by creator id. If absent, no filtering is done.                                                                                                                                                                       | \[optional] \[default to null]  |
| **name**               | **TextQuery** | Filters Cluster Environments by name. Currently only contains is supported.If absent, no filtering is done.                                                                                                                                        | \[optional] \[default to null]  |
| **image\_name**        | **TextQuery** | Filters Cluster Environments by image name. Image name is a virtual concept. It starts with 'anyscale/image' (for customer-built images) or 'anyscale/ray' (default images).Currently only contains is supported. If absent, no filtering is done. | \[optional] \[default to null]  |
| **paging**             | **PageQuery** | Pagination information.                                                                                                                                                                                                                            | \[optional] \[default to null]  |
| **include\_archived**  | **bool**      | Whether to include archived Cluster Environments in the results.                                                                                                                                                                                   | \[optional] \[default to false] |
| **include\_anonymous** | **bool**      | Whether to include anonymous Cluster Environments in the results.                                                                                                                                                                                  | \[optional] \[default to false] |

### `ClusterenvironmentListResponse`[​](#clusterenvironmentlistresponse "Direct link to clusterenvironmentlistresponse")

A list response form the API. Contains a field "results" which has the contents of the response.

| Name         | Type                          | Description | Notes                          |
| ------------ | ----------------------------- | ----------- | ------------------------------ |
| **results**  | **List\[ClusterEnvironment]** |             | \[default to null]             |
| **metadata** | **ListResponseMetadata**      |             | \[optional] \[default to null] |

### `ClusterenvironmentResponse`[​](#clusterenvironmentresponse "Direct link to clusterenvironmentresponse")

A response from the API. Contains a field "result" which has the contents of the response.

| Name       | Type                   | Description | Notes              |
| ---------- | ---------------------- | ----------- | ------------------ |
| **result** | **ClusterEnvironment** |             | \[default to null] |

### `ClusterenvironmentbuildListResponse`[​](#clusterenvironmentbuildlistresponse "Direct link to clusterenvironmentbuildlistresponse")

A list response form the API. Contains a field "results" which has the contents of the response.

| Name         | Type                               | Description | Notes                          |
| ------------ | ---------------------------------- | ----------- | ------------------------------ |
| **results**  | **List\[ClusterEnvironmentBuild]** |             | \[default to null]             |
| **metadata** | **ListResponseMetadata**           |             | \[optional] \[default to null] |

### `ClusterenvironmentbuildoperationResponse`[​](#clusterenvironmentbuildoperationresponse "Direct link to clusterenvironmentbuildoperationresponse")

A response from the API. Contains a field "result" which has the contents of the response.

| Name       | Type                                 | Description | Notes              |
| ---------- | ------------------------------------ | ----------- | ------------------ |
| **result** | **ClusterEnvironmentBuildOperation** |             | \[default to null] |

### `CreateBYODClusterEnvironment`[​](#createbyodclusterenvironment "Direct link to createbyodclusterenvironment")

Model used to create a BYOD Cluster Environment.

| Name             | Type                                                | Description                                                  | Notes                           |
| ---------------- | --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------- |
| **name**         | **str**                                             | Name of the Cluster Environment.                             | \[default to null]              |
| **config\_json** | **CreateBYODClusterEnvironmentConfigurationSchema** | Config JSON to use to create a new BYOD Cluster Environment. | \[default to null]              |
| **anonymous**    | **bool**                                            | True if this is an anonymous Cluster Environment.            | \[optional] \[default to false] |

### `CreateBYODClusterEnvironmentBuild`[​](#createbyodclusterenvironmentbuild "Direct link to createbyodclusterenvironmentbuild")

Model used to create a BYOD Cluster Environment Build.

| Name                         | Type                                       | Description                                          | Notes              |
| ---------------------------- | ------------------------------------------ | ---------------------------------------------------- | ------------------ |
| **cluster\_environment\_id** | **str**                                    | ID of the Cluster Environment this Build belongs to. | \[default to null] |
| **config\_json**             | **CreateBYODAppConfigConfigurationSchema** | Config JSON to use to create a new BYOD Build.       | \[default to null] |

### `CreateBYODClusterEnvironmentConfigurationSchema`[​](#createbyodclusterenvironmentconfigurationschema "Direct link to createbyodclusterenvironmentconfigurationschema")

| Name                        | Type       | Description                                                                                                         | Notes                          |
| --------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **docker\_image**           | **str**    | The custom container base image used in the Cluster Environment.                                                    | \[default to null]             |
| **ray\_version**            | **str**    | The version of Ray used in the customer docker image.                                                               | \[default to null]             |
| **env\_vars**               | **object** | Environment variables in the docker image that will be used at runtime.                                             | \[optional] \[default to null] |
| **registry\_login\_secret** | **str**    | The name or identifier of a secret containing credentials to authenticate to the docker registry hosting the image. | \[optional] \[default to null] |

### `CreateClusterEnvironment`[​](#createclusterenvironment "Direct link to createclusterenvironment")

Model used to create an Cluster Environment.

| Name              | Type                                            | Description                                               | Notes                           |
| ----------------- | ----------------------------------------------- | --------------------------------------------------------- | ------------------------------- |
| **name**          | **str**                                         | Name of the Cluster Environment.                          | \[default to null]              |
| **project\_id**   | **str**                                         | ID of the Project this Cluster Environment is for.        | \[optional] \[default to null]  |
| **config\_json**  | **CreateClusterEnvironmentConfigurationSchema** | Config JSON to use to create a new Cluster Environment.   | \[optional] \[default to null]  |
| **containerfile** | **str**                                         | Containerfile to use to create a new Cluster Environment. | \[optional] \[default to null]  |
| **anonymous**     | **bool**                                        | True if this is an anonymous Cluster Environment.         | \[optional] \[default to false] |

### `CreateClusterEnvironmentBuild`[​](#createclusterenvironmentbuild "Direct link to createclusterenvironmentbuild")

Model used to create a Cluster Environment Build.

| Name                         | Type                                   | Description                                                                                                         | Notes                          |
| ---------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **cluster\_environment\_id** | **str**                                | ID of the Cluster Environment this Build belongs to.                                                                | \[default to null]             |
| **config\_json**             | **CreateAppConfigConfigurationSchema** | Config JSON to use to create a new Build.                                                                           | \[optional] \[default to null] |
| **containerfile**            | **str**                                | The containerfile used to build the image.                                                                          | \[optional] \[default to null] |
| **docker\_image\_name**      | **str**                                | The name of the docker image for this Build.                                                                        | \[optional] \[default to null] |
| **registry\_login\_secret**  | **str**                                | The name or identifier of a secret containing credentials to authenticate to the docker registry hosting the image. | \[optional] \[default to null] |
| **ray\_version**             | **str**                                | The Ray version to use for this build.                                                                              | \[optional] \[default to null] |

### `CreateClusterEnvironmentConfigurationSchema`[​](#createclusterenvironmentconfigurationschema "Direct link to createclusterenvironmentconfigurationschema")

| Name                  | Type                        | Description                                                                                                                                  | Notes                          |
| --------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **base\_image**       | **SUPPORTEDBASEIMAGESENUM** | The base image to use to create a new Cluster Environment. It needs to be one of the images that we currently support (SupportedBaseImages). | \[default to null]             |
| **env\_vars**         | **object**                  | Environment varibles in the docker image that'll be used at runtime.                                                                         | \[optional] \[default to null] |
| **debian\_packages**  | **List\[str]**              | List of debian packages that'll be included in the image.                                                                                    | \[optional] \[default to null] |
| **python**            | **PythonModules**           | Python related dependencies.                                                                                                                 | \[optional] \[default to null] |
| **post\_build\_cmds** | **List\[str]**              | List of post build commands that'll be included in the image.                                                                                | \[optional] \[default to null] |

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
