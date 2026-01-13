# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appintegrations_application_association.dataset.md

---
title: AppIntegrations Application Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > AppIntegrations Application
  Association
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.appintegrations_application_association.dataset/index.html
---

# AppIntegrations Application Association

AppIntegrations Application Association in AWS represents the link between an AppIntegrations application and another resource, such as a data integration or event source. It allows applications to connect with external services or data flows, enabling seamless integration and data sharing across systems. This association helps manage how applications interact with connected resources, supporting use cases like event-driven workflows and data synchronization.

```
aws.appintegrations_application_association
```

## Fields

| Title                       | ID   | Type   | Data Type                                                                          | Description |
| --------------------------- | ---- | ------ | ---------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string |
| account_id                  | core | string |
| application_arn             | core | string | The Amazon Resource Name (ARN) of the Application.                                 |
| application_association_arn | core | string | The Amazon Resource Name (ARN) of the Application Association.                     |
| client_id                   | core | string | The identifier for the client that is associated with the Application Association. |
| tags                        | core | hstore |
