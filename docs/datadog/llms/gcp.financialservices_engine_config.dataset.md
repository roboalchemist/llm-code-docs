# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.financialservices_engine_config.dataset.md

---
title: Financial Services Engine Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Financial Services Engine Config
---

# Financial Services Engine Config

This table represents the Financial Services Engine Config resource from Google Cloud Platform.

```
gcp.financialservices_engine_config
```

## Fields

| Title                      | ID   | Type          | Data Type                                                                                                                                                                                             | Description |
| -------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string        |
| ancestors                  | core | array<string> |
| create_time                | core | timestamp     | Output only. The timestamp of creation of this resource.                                                                                                                                              |
| datadog_display_name       | core | string        |
| engine_version             | core | string        | Required. The resource name of the EngineVersion used in this model tuning. format: `/projects/{project_num}/locations/{location}/instances/{instance}/engineVersions/{engine_version}`               |
| hyperparameter_source      | core | json          | Optional. Configuration of hyperparameters source EngineConfig.                                                                                                                                       |
| hyperparameter_source_type | core | string        | Optional. The origin of hyperparameters for the created EngineConfig. The default is `TUNING`. In this case, the hyperparameters are selected as a result of a tuning run.                            |
| labels                     | core | array<string> | Labels                                                                                                                                                                                                |
| line_of_business           | core | string        | Output only. The line of business (Retail/Commercial) this engine config is used for. Determined by EngineVersion, cannot be set by user.                                                             |
| name                       | core | string        | Output only. The resource name of the EngineConfig. format: `/projects/{project_num}/locations/{location}/instances/{instance}/engineConfigs/{engine_config}`                                         |
| organization_id            | core | string        |
| parent                     | core | string        |
| performance_target         | core | json          | Optional. PerformanceTarget gives information on how the tuning and training will be evaluated. This field is required if `hyperparameter_source.type` is not `INHERITED`, and output-only otherwise. |
| project_id                 | core | string        |
| project_number             | core | string        |
| region_id                  | core | string        |
| resource_name              | core | string        |
| state                      | core | string        | Output only. State of the EngineConfig (creating, active, deleting, etc.)                                                                                                                             |
| tags                       | core | hstore_csv    |
| tuning                     | core | json          | Optional. Configuration for tuning in creation of the EngineConfig. This field is required if `hyperparameter_source.type` is not `INHERITED`, and output-only otherwise.                             |
| update_time                | core | timestamp     | Output only. The timestamp of the most recent update of this resource.                                                                                                                                |
| zone_id                    | core | string        |
