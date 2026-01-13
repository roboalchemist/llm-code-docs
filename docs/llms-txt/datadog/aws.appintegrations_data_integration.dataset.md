# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appintegrations_data_integration.dataset.md

---
title: AppIntegrations Data Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AppIntegrations Data Integration
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.appintegrations_data_integration.dataset/index.html
---

# AppIntegrations Data Integration

AppIntegrations Data Integration in AWS represents a configuration that allows you to bring together data from different applications and services into a unified integration. It provides details about the data integration setup, including its metadata, source configuration, and associated resources. This resource is typically used to streamline data flows between SaaS applications and AWS services, enabling easier data sharing and reducing the need for custom integration code.

```
aws.appintegrations_data_integration
```

## Fields

| Title                  | ID   | Type   | Data Type                                                               | Description |
| ---------------------- | ---- | ------ | ----------------------------------------------------------------------- | ----------- |
| _key                   | core | string |
| account_id             | core | string |
| arn                    | core | string | The Amazon Resource Name (ARN) for the DataIntegration.                 |
| description            | core | string | The KMS key ARN for the DataIntegration.                                |
| file_configuration     | core | json   | The configuration for what files should be pulled from the source.      |
| id                     | core | string | A unique identifier.                                                    |
| name                   | core | string | The name of the DataIntegration.                                        |
| object_configuration   | core | hstore | The configuration for what data should be pulled from the source.       |
| schedule_configuration | core | json   | The name of the data and how often it should be pulled from the source. |
| source_uri             | core | string | The URI of the data source.                                             |
| tags                   | core | hstore |
