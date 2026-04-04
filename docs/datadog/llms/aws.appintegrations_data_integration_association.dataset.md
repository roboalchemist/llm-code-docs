# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appintegrations_data_integration_association.dataset.md

---
title: AppIntegrations Data Integration Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > AppIntegrations Data Integration
  Association
---

# AppIntegrations Data Integration Association

AppIntegrations Data Integration Association in AWS represents the link between a data integration and a client resource, such as an application or event source. It defines how data flows from the integration to the target system, enabling seamless connectivity and data sharing across services. This resource helps manage associations so that applications can consume integrated data without needing custom connectors.

```
aws.appintegrations_data_integration_association
```

## Fields

| Title                            | ID   | Type       | Data Type                                                                              | Description |
| -------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string     |
| account_id                       | core | string     |
| client_id                        | core | string     | The identifier for the client that is associated with the DataIntegration association. |
| data_integration_arn             | core | string     | The Amazon Resource Name (ARN) of the DataIntegration.                                 |
| data_integration_association_arn | core | string     | The Amazon Resource Name (ARN) of the DataIntegration association.                     |
| destination_uri                  | core | string     | The URI of the data destination.                                                       |
| execution_configuration          | core | json       | The configuration for how the files should be pulled from the source.                  |
| last_execution_status            | core | json       | The execution status of the last job.                                                  |
| tags                             | core | hstore_csv |
