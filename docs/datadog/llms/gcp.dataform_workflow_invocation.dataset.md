# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dataform_workflow_invocation.dataset.md

---
title: Dataform Workflow Invocation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dataform Workflow Invocation
---

# Dataform Workflow Invocation

Dataform Workflow Invocation in Google Cloud is a resource that represents the execution of a Dataform workflow. It allows users to programmatically trigger, monitor, and manage workflow runs that transform and manage data in BigQuery. This resource helps automate data pipeline operations, ensuring consistent and repeatable data transformations within the Dataform environment.

```
gcp.dataform_workflow_invocation
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                                                                               | Description |
| --------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| ancestors                   | core | array<string> |
| compilation_result          | core | string        | Immutable. The name of the compilation result to use for this invocation. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.                           |
| data_encryption_state       | core | json          | Output only. Only set if the repository has a KMS Key.                                                                                                                                  |
| datadog_display_name        | core | string        |
| internal_metadata           | core | string        | Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string. |
| invocation_config           | core | json          | Immutable. If left unset, a default InvocationConfig will be used.                                                                                                                      |
| invocation_timing           | core | json          | Output only. This workflow invocation's timing details.                                                                                                                                 |
| labels                      | core | array<string> |
| name                        | core | string        | Output only. The workflow invocation's name.                                                                                                                                            |
| organization_id             | core | string        |
| parent                      | core | string        |
| project_id                  | core | string        |
| project_number              | core | string        |
| region_id                   | core | string        |
| resolved_compilation_result | core | string        | Output only. The resolved compilation result that was used to create this invocation. Will be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.               |
| resource_name               | core | string        |
| state                       | core | string        | Output only. This workflow invocation's current state.                                                                                                                                  |
| tags                        | core | hstore_csv    |
| workflow_config             | core | string        | Immutable. The name of the workflow config to invoke. Must be in the format `projects/*/locations/*/repositories/*/workflowConfigs/*`.                                                  |
| zone_id                     | core | string        |
