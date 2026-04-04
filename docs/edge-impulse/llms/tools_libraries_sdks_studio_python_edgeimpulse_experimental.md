# Source: https://docs.edgeimpulse.com/tools/libraries/sdks/studio/python/edgeimpulse/experimental/index.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse.experimental

## Modules

* [edgeimpulse.experimental.api](/tools/libraries/sdks/studio/python/edgeimpulse/experimental/api)
* [edgeimpulse.experimental.data](/tools/libraries/sdks/studio/python/edgeimpulse/experimental/data)
* [edgeimpulse.experimental.impulse](/tools/libraries/sdks/studio/python/edgeimpulse/experimental/impulse)
* [edgeimpulse.experimental.tuner](/tools/libraries/sdks/studio/python/edgeimpulse/experimental/tuner)
* [edgeimpulse.experimental.util](/tools/libraries/sdks/studio/python/edgeimpulse/experimental/util)

## Classes

### EdgeImpulseApi

```python  theme={"system"}
edgeimpulse.experimental.EdgeImpulseApi(
	host: str | None = None,
	key: str | None = None,
	key_type: str = 'api'
)
```

Initialize the Edge Impulse Api.

| Parameters |                      |
| ---------- | -------------------- |
| `host`     | `str \| None = None` |
| `key`      | `str \| None = None` |
| `key_type` | `str = 'api'`        |

| Instance variables            |                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| `classify`                    | `edgeimpulse_api.api.classify_api.ClassifyApi`                                     |
| `client`                      | `edgeimpulse_api.api_client.ApiClient`                                             |
| `deployment`                  | `edgeimpulse_api.api.deployment_api.DeploymentApi`                                 |
| `devices`                     | `edgeimpulse_api.api.devices_api.DevicesApi`                                       |
| `dsp`                         | `edgeimpulse_api.api.dsp_api.DSPApi`                                               |
| `export`                      | `edgeimpulse_api.api.export_api.ExportApi`                                         |
| `host`                        | `str \| None`                                                                      |
| `impulse`                     | `edgeimpulse_api.api.impulse_api.ImpulseApi`                                       |
| `jobs`                        | `edgeimpulse_api.api.jobs_api.JobsApi`                                             |
| `learn`                       | `edgeimpulse_api.api.learn_api.LearnApi`                                           |
| `login`                       | `edgeimpulse_api.api.login_api.LoginApi`                                           |
| `optimization`                | `edgeimpulse_api.api.optimization_api.OptimizationApi`                             |
| `organization_blocks`         | `edgeimpulse_api.api.organization_blocks_api.OrganizationBlocksApi`                |
| `organization_create_project` | `edgeimpulse_api.api.organization_create_project_api.OrganizationCreateProjectApi` |
| `organization_data`           | `edgeimpulse_api.api.organization_data_api.OrganizationDataApi`                    |
| `organization_data_campaigns` | `edgeimpulse_api.api.organization_data_campaigns_api.OrganizationDataCampaignsApi` |
| `organization_jobs`           | `edgeimpulse_api.api.organization_jobs_api.OrganizationJobsApi`                    |
| `organization_pipelines`      | `edgeimpulse_api.api.organization_pipelines_api.OrganizationPipelinesApi`          |
| `organization_portals`        | `edgeimpulse_api.api.organization_portals_api.OrganizationPortalsApi`              |
| `organizations`               | `edgeimpulse_api.api.organizations_api.OrganizationsApi`                           |
| `performance_calibration`     | `edgeimpulse_api.api.performance_calibration_api.PerformanceCalibrationApi`        |
| `projects`                    | `edgeimpulse_api.api.projects_api.ProjectsApi`                                     |
| `raw_data`                    | `edgeimpulse_api.api.raw_data_api.RawDataApi`                                      |
| `upload_portal`               | `edgeimpulse_api.api.upload_portal_api.UploadPortalApi`                            |
| `user`                        | `edgeimpulse_api.api.user_api.UserApi`                                             |

***

**METHODS**

#### authenticate

```python  theme={"system"}
edgeimpulse.experimental.EdgeImpulseApi.authenticate(
	self,
	key: str,
	key_type: str = 'api',
	host: str | None = None
) ‑> None
```

Authenticate against Edge Impulse.

| Parameters |                      |
| ---------- | -------------------- |
| `self`     | ` `                  |
| `key`      | `str`                |
| `key_type` | `str = 'api'`        |
| `host`     | `str \| None = None` |

| Returns |
| ------- |
| `None`  |

#### default\_project\_id

```python  theme={"system"}
edgeimpulse.experimental.EdgeImpulseApi.default_project_id(
	self
) ‑> int
```

Get the default project ID from the provided API key.

Returns:
int: The project associated with the api key.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |

| Returns |
| ------- |
| `int`   |

#### run\_organization\_job\_until\_completion

```python  theme={"system"}
edgeimpulse.experimental.EdgeImpulseApi.run_organization_job_until_completion(
	self,
	organization_id: int,
	job_id: int,
	data_cb=None,
	client=None,
	timeout_sec: int | None = None
) ‑> None
```

Runs an organization job until completion.

| Parameters        |                      |
| ----------------- | -------------------- |
| `self`            | ` `                  |
| `organization_id` | `int`                |
| `job_id`          | `int`                |
| `data_cb=None`    | ` `                  |
| `client=None`     | ` `                  |
| `timeout_sec`     | `int \| None = None` |

| Returns |
| ------- |
| `None`  |

#### run\_project\_job\_until\_completion

```python  theme={"system"}
edgeimpulse.experimental.EdgeImpulseApi.run_project_job_until_completion(
	self,
	job_id: int,
	data_cb=None,
	client=None,
	project_id: int | None = None,
	timeout_sec: int | None = None
) ‑> None
```

Runs a project job until completion.

| Parameters     |                      |
| -------------- | -------------------- |
| `self`         | ` `                  |
| `job_id`       | `int`                |
| `data_cb=None` | ` `                  |
| `client=None`  | ` `                  |
| `project_id`   | `int \| None = None` |
| `timeout_sec`  | `int \| None = None` |

| Returns |
| ------- |
| `None`  |

#### set\_client

```python  theme={"system"}
edgeimpulse.experimental.EdgeImpulseApi.set_client(
	self,
	client: edgeimpulse_api.api_client.ApiClient
) ‑> None
```

Set the API client and initialize the APIs wit that client.

| Parameters |                                        |
| ---------- | -------------------------------------- |
| `self`     | ` `                                    |
| `client`   | `edgeimpulse_api.api_client.ApiClient` |

| Returns |
| ------- |
| `None`  |


Built with [Mintlify](https://mintlify.com).