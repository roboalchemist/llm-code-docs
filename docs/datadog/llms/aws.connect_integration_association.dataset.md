# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.connect_integration_association.dataset.md

---
title: Connect Integration Association
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Connect Integration Association
---

# Connect Integration Association

Connect Integration Association in AWS represents the link between an Amazon Connect instance and an external application or service. It allows you to integrate third-party tools, such as customer relationship management systems or workforce management solutions, with your contact center. This association helps streamline workflows, improve agent efficiency, and enhance customer experiences by enabling seamless data and functionality sharing between Amazon Connect and the integrated system.

```
aws.connect_integration_association
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                                                      | Description |
| --------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                        | core | string     |
| account_id                  | core | string     |
| instance_id                 | core | string     | The identifier of the Amazon Connect instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance. |
| integration_arn             | core | string     | The Amazon Resource Name (ARN) for the AppIntegration.                                                                         |
| integration_association_arn | core | string     | The Amazon Resource Name (ARN) for the AppIntegration association.                                                             |
| integration_association_id  | core | string     | The identifier for the AppIntegration association.                                                                             |
| integration_type            | core | string     | The integration type.                                                                                                          |
| source_application_name     | core | string     | The user-provided, friendly name for the external application.                                                                 |
| source_application_url      | core | string     | The URL for the external application.                                                                                          |
| source_type                 | core | string     | The name of the source.                                                                                                        |
| tags                        | core | hstore_csv |
