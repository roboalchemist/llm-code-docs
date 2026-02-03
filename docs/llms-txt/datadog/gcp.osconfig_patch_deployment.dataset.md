# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.osconfig_patch_deployment.dataset.md

---
title: OS Config Patch Deployment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > OS Config Patch Deployment
---

# OS Config Patch Deployment

OS Config Patch Deployment in Google Cloud automates the process of applying operating system patches across virtual machine instances. It allows administrators to define patch configurations, schedules, and target instance groups to ensure systems remain secure and up to date. The service supports both Linux and Windows environments and integrates with OS Config for compliance tracking and reporting.

```
gcp.osconfig_patch_deployment
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Time the patch deployment was created. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.                                                                                                    |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Description of the patch deployment. Length of the description is limited to 1024 characters.                                                                                                                             |
| duration             | core | string        | Optional. Duration of the patch. After the duration ends, the patch times out.                                                                                                                                                      |
| instance_filter      | core | json          | Required. VM instances to patch.                                                                                                                                                                                                    |
| labels               | core | array<string> |
| last_execute_time    | core | timestamp     | Output only. The last time a patch job was started by this deployment. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.                                                                                 |
| name                 | core | string        | Unique name for the patch deployment resource in a project. The patch deployment name is in the form: `projects/{project_id}/patchDeployments/{patch_deployment_id}`. This field is ignored when you create a new patch deployment. |
| one_time_schedule    | core | json          | Required. Schedule a one-time execution.                                                                                                                                                                                            |
| organization_id      | core | string        |
| parent               | core | string        |
| patch_config         | core | json          | Optional. Patch configuration that is applied.                                                                                                                                                                                      |
| project_id           | core | string        |
| project_number       | core | string        |
| recurring_schedule   | core | json          | Required. Schedule recurring executions.                                                                                                                                                                                            |
| region_id            | core | string        |
| resource_name        | core | string        |
| rollout              | core | json          | Optional. Rollout strategy of the patch job.                                                                                                                                                                                        |
| state                | core | string        | Output only. Current state of the patch deployment.                                                                                                                                                                                 |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Time the patch deployment was last updated. Timestamp is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.                                                                                               |
| zone_id              | core | string        |
