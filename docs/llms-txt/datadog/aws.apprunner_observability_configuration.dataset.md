# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.apprunner_observability_configuration.dataset.md

---
title: App Runner Observability Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > App Runner Observability
  Configuration
---

# App Runner Observability Configuration

App Runner Observability Configuration in AWS provides details about how observability features, such as logging and tracing, are set up for an App Runner service. It includes information on the configuration's status, associated resources, and whether features like CloudWatch Logs or X-Ray tracing are enabled. This helps monitor, troubleshoot, and gain insights into application performance and behavior.

```
aws.apprunner_observability_configuration
```

## Fields

| Title                                | ID   | Type       | Data Type                                                                                                                                                                                                                                 | Description |
| ------------------------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string     |
| account_id                           | core | string     |
| created_at                           | core | timestamp  | The time when the observability configuration was created. It's in Unix time stamp format.                                                                                                                                                |
| deleted_at                           | core | timestamp  | The time when the observability configuration was deleted. It's in Unix time stamp format.                                                                                                                                                |
| latest                               | core | bool       | It's set to true for the configuration with the highest Revision among all configurations that share the same ObservabilityConfigurationName. It's set to false otherwise.                                                                |
| observability_configuration_arn      | core | string     | The Amazon Resource Name (ARN) of this observability configuration.                                                                                                                                                                       |
| observability_configuration_name     | core | string     | The customer-provided observability configuration name. It can be used in multiple revisions of a configuration.                                                                                                                          |
| observability_configuration_revision | core | int64      | The revision of this observability configuration. It's unique among all the active configurations ("Status": "ACTIVE") that share the same ObservabilityConfigurationName.                                                                |
| status                               | core | string     | The current state of the observability configuration. If the status of a configuration revision is INACTIVE, it was deleted and can't be used. Inactive configuration revisions are permanently removed some time after they are deleted. |
| tags                                 | core | hstore_csv |
| trace_configuration                  | core | json       | The configuration of the tracing feature within this observability configuration. If not specified, tracing isn't enabled.                                                                                                                |
