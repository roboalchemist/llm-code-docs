# Source: https://docs.anyscale.com/archive/ref.md

# Legacy CLI and SDK methods

[View Markdown](/archive/ref.md)

# Legacy CLI and SDK methods

Anyscale has deprecated methods for the CLI and SDK as documented in the following pages. To continue using these methods, install Anyscale CLI version 0.26.72 or earlier.

These methods will be fully removed from the Anyscale platform on February 28, 2026.

## Legacy API reference[​](#legacy-api-reference "Direct link to Legacy API reference")

* [Cloud API (legacy)](/archive/ref/cloud.md)
* [Cluster API (legacy)](/archive/ref/cluster.md)
* [Compute config API (legacy)](/archive/ref/compute-config-api.md)
* [Image API (legacy)](/archive/ref/image.md)
* [Job API (legacy)](/archive/ref/job-api.md)
* [Other API (legacy)](/archive/ref/other.md)
* [Schedule API (legacy)](/archive/ref/schedule-api.md)
* [Service API (legacy)](/archive/ref/service-api.md)
* [Workspaces API (legacy)](/archive/ref/workspaces.md)

## Methods removed in version 0.26.88[​](#02688 "Direct link to Methods removed in version 0.26.88")

Anyscale CLI version 0.26.88 removes support for the following legacy SDK methods. There are no CLI command removals in this version.

### SDK methods[​](#sdk-methods "Direct link to SDK methods")

The following tables list SDK methods removed in this version, organized by category.

#### Image (cluster environment) methods[​](#image-cluster-environment-methods "Direct link to Image (cluster environment) methods")

| Deprecated method                       | Replacement                                                                                                                                                                                                                                          |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_default_cluster_environment_build` | Use `anyscale.image.get`, `anyscale.image.list`, and `anyscale.compute_config.get_default` for image and compute config lookup. See [Image API Reference](/reference/image.md) and [Compute Config API Reference](/reference/compute-config-api.md). |

#### Job methods[​](#job-methods "Direct link to Job methods")

| Deprecated method                                                                                         | Replacement              |
| --------------------------------------------------------------------------------------------------------- | ------------------------ |
| `create_job`                                                                                              | `anyscale.job.submit`    |
| `terminate_job`                                                                                           | `anyscale.job.terminate` |
| `search_jobs`                                                                                             | `anyscale.job.list`      |
| `fetch_job_logs`<br />`fetch_production_job_logs`<br />`get_job_logs_download`<br />`get_job_logs_stream` | `anyscale.job.get_logs`  |

#### Schedule methods[​](#schedule-methods "Direct link to Schedule methods")

| Deprecated method           | Replacement                   |
| --------------------------- | ----------------------------- |
| `create_or_update_schedule` | `anyscale.schedule.apply`     |
| `get_schedule`              | `anyscale.schedule.status`    |
| `list_schedules`            | `anyscale.schedule.list`      |
| `pause_schedule`            | `anyscale.schedule.set_state` |
| `run_schedule`              | `anyscale.schedule.trigger`   |

#### Cluster methods[​](#cluster-methods "Direct link to Cluster methods")

| Deprecated method                             | Replacement                                                                                               |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `launch_cluster`                              | Use `anyscale workspace_v2 start` or the API client for cluster creation and start.                       |
| `launch_cluster_with_new_cluster_environment` | Use `anyscale.image.build` (or register) then workspace or API client to start a cluster with that image. |
| `create_cluster`                              | Use the Anyscale API client or workspace APIs.                                                            |
| `start_cluster`                               | `anyscale workspace_v2 start`                                                                             |
| `terminate_cluster`                           | `anyscale workspace_v2 terminate`                                                                         |
| `search_clusters`                             | Use the Anyscale API client.                                                                              |
| `delete_cluster`                              | Use the Anyscale API client.                                                                              |
| `update_cluster`                              | Use the Anyscale API client or `anyscale workspace_v2 start` to update and restart.                       |

## Methods removed in version 0.26.85[​](#02685 "Direct link to Methods removed in version 0.26.85")

Anyscale CLI version 0.26.85 removes support for the following legacy commands and SDK methods.

### CLI commands[​](#cli-commands "Direct link to CLI commands")

The following table lists CLI commands removed in this version:

| Deprecated command        | Replacement | Notes                                                                                                                                             |
| ------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `anyscale machine list`   | N/A         | Customer-managed machine pools are deprecated. See [Customer-managed on-prem machine pools (legacy)](/archive/customer-managed-machine-pools.md). |
| `anyscale machine delete` | N/A         | Customer-managed machine pools are deprecated. See [Customer-managed on-prem machine pools (legacy)](/archive/customer-managed-machine-pools.md). |

### SDK methods[​](#sdk-methods-1 "Direct link to SDK methods")

The following tables list SDK methods removed in this version, organized by category.

#### Service methods[​](#service-methods "Direct link to Service methods")

| Deprecated method   | Replacement                  |
| ------------------- | ---------------------------- |
| `get_service`       | `anyscale.service.status`    |
| `list_services`     | `anyscale.service.list`      |
| `rollback_service`  | `anyscale.service.rollback`  |
| `rollout_service`   | `anyscale.service.deploy`    |
| `terminate_service` | `anyscale.service.terminate` |

#### Cloud methods[​](#cloud-methods "Direct link to Cloud methods")

| Deprecated method   | Replacement                  |
| ------------------- | ---------------------------- |
| `get_cloud`         | `anyscale.cloud.get`         |
| `get_default_cloud` | `anyscale.cloud.get_default` |
| `search_clouds`     | `anyscale.cloud.list`        |

#### Other methods[​](#other-methods "Direct link to Other methods")

The following methods were previously shared directly with some customers for administrative tasks. There is no replacement in the modern SDK. Contact [Anyscale support](mailto:support@anyscale.com) if you need assistance with tasks previously associated with these methods.

| Deprecated method             | Replacement |
| ----------------------------- | ----------- |
| `partial_update_organization` | N/A         |
| `upsert_sso_config`           | N/A         |
| `upsert_test_sso_config`      | N/A         |

## Methods removed in version 0.26.83[​](#02683 "Direct link to Methods removed in version 0.26.83")

Anyscale CLI version 0.26.83 removes support for the following legacy commands and SDK methods.

### CLI commands[​](#cli-commands-1 "Direct link to CLI commands")

The following table lists CLI commands removed in this version:

| Deprecated command           | Replacement                       | Notes                                                          |
| ---------------------------- | --------------------------------- | -------------------------------------------------------------- |
| `anyscale cluster-env *`     | `anyscale image *`                | All cluster environment commands replaced with image commands. |
| `anyscale cluster start`     | `anyscale workspace_v2 start`     |                                                                |
| `anyscale cluster terminate` | `anyscale workspace_v2 terminate` |                                                                |

### SDK methods[​](#sdk-methods-2 "Direct link to SDK methods")

The following tables list SDK methods removed in this version, organized by category.

#### Compute config methods[​](#compute-config-methods "Direct link to Compute config methods")

| Deprecated method             | Replacement                           |
| ----------------------------- | ------------------------------------- |
| `create_cluster_compute`      | `anyscale.compute_config.create`      |
| `delete_cluster_compute`      | `anyscale.compute_config.archive`     |
| `get_cluster_compute`         | `anyscale.compute_config.get`         |
| `get_default_cluster_compute` | `anyscale.compute_config.get_default` |
| `search_cluster_computes`     | `anyscale.compute_config.list`        |

#### Image (cluster environment) methods[​](#image-cluster-environment-methods-1 "Direct link to Image (cluster environment) methods")

| Deprecated method                              | Replacement               |
| ---------------------------------------------- | ------------------------- |
| `create_byod_cluster_environment_build`        | `anyscale.image.register` |
| `create_cluster_environment_build`             | `anyscale.image.build`    |
| `find_cluster_environment_build_by_identifier` | `anyscale.image.get`      |
| `get_cluster_environment_build`                | `anyscale.image.get`      |
| `list_cluster_environment_builds`              | `anyscale.image.list`     |
| `create_byod_cluster_environment`              | `anyscale.image.register` |
| `create_cluster_environment`                   | `anyscale.image.build`    |
| `get_cluster_environment`                      | `anyscale.image.get`      |
| `search_cluster_environments`                  | `anyscale.image.list`     |

## Commands removed in version 0.26.77[​](#02677 "Direct link to Commands removed in version 0.26.77")

Anyscale CLI version 0.26.77 removes support for a number of legacy commands, including the following:

* The full set of legacy `anyscale workspace` commands, replaced by `anyscale workspace_v2`.
* The full set of `anyscale list` commands, replaced by resource-specific list commands.

The following table recommends how to migrate legacy commands:

| Deprecated command             | Supported command                   | Notes                                                                                                    |
| ------------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `anyscale workspace create`    | `anyscale workspace_v2 create`      |                                                                                                          |
| `anyscale workspace run`       | `anyscale workspace_v2 run_command` |                                                                                                          |
| `anyscale workspace ssh`       | `anyscale workspace_v2 ssh`         |                                                                                                          |
| `anyscale workspace start`     | `anyscale workspace_v2 start`       |                                                                                                          |
| `anyscale workspace terminate` | `anyscale workspace_v2 terminate`   |                                                                                                          |
| `anyscale workspace pull`      | `anyscale workspace_v2 pull`        |                                                                                                          |
| `anyscale workspace push`      | `anyscale workspace_v2 push`        |                                                                                                          |
| `anyscale workspace list`      | `anyscale workspace_v2 list`        |                                                                                                          |
| `anyscale workspace clone`     | `anyscale workspace_v2 pull`        |                                                                                                          |
| `anyscale workspace tags`      | `anyscale workspace_v2 tags`        |                                                                                                          |
| `anyscale workspace cp`        | `anyscale workspace_v2 pull`        | Pulls files under working directory only. No alternative exists for files outside the working directory. |
| `anyscale workspace activate`  | N/A                                 | `workspace_v2` commands don't require activation.                                                        |
| `anyscale list clouds`         | `anyscale cloud list`               |                                                                                                          |
| `anyscale list projects`       | `anyscale project list`             |                                                                                                          |
| `anyscale list sessions`       | `anyscale cluster list`             |                                                                                                          |
| `anyscale list ips`            | N/A                                 | Use the Anyscale console to view cluster node information.                                               |
| `anyscale service rollout`     | `anyscale service deploy`           |                                                                                                          |
| `anyscale project init`        | `anyscale project create`           |                                                                                                          |
| `anyscale exec`                | `anyscale job submit`               | Runs your script as a job in a cluster.                                                                  |
| `anyscale schedule create`     | `anyscale schedule apply`           |                                                                                                          |
| `anyscale schedule update`     | `anyscale schedule apply`           |                                                                                                          |
