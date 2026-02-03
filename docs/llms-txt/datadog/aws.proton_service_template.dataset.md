# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.proton_service_template.dataset.md

---
title: Proton Service Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Proton Service Template
---

# Proton Service Template

An AWS Proton Service Template defines the standardized infrastructure and CI/CD configuration for deploying and managing services. It provides a reusable blueprint that development teams can use to create consistent service instances, ensuring best practices and compliance are followed.

```
aws.proton_service_template
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                      | Description |
| --------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| arn                   | core | string     | The Amazon Resource Name (ARN) of the service template.                                                                                                        |
| created_at            | core | timestamp  | The time when the service template was created.                                                                                                                |
| description           | core | string     | A description of the service template.                                                                                                                         |
| last_modified_at      | core | timestamp  | The time when the service template was last modified.                                                                                                          |
| name                  | core | string     | The name of the service template.                                                                                                                              |
| pipeline_provisioning | core | string     | If pipelineProvisioning is true, a service pipeline is included in the service template. Otherwise, a service pipeline isn't included in the service template. |
| recommended_version   | core | string     | The recommended version of the service template.                                                                                                               |
| tags                  | core | hstore_csv |
