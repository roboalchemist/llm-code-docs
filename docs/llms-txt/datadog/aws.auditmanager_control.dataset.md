# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.auditmanager_control.dataset.md

---
title: Audit Manager Control
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Audit Manager Control
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.auditmanager_control.dataset/index.html
---

# Audit Manager Control

Audit Manager Control in AWS represents a specific compliance control within AWS Audit Manager. It provides detailed information about the control, including its objectives, descriptions, and testing procedures. This resource helps organizations map compliance requirements to AWS services and processes, making it easier to assess, monitor, and demonstrate adherence to regulatory frameworks and internal policies.

```
aws.auditmanager_control
```

## Fields

| Title                    | ID   | Type      | Data Type                                                                                                                                                                                                                                              | Description |
| ------------------------ | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                     | core | string    |
| account_id               | core | string    |
| action_plan_instructions | core | string    | The recommended actions to carry out if the control isn't fulfilled.                                                                                                                                                                                   |
| action_plan_title        | core | string    | The title of the action plan for remediating the control.                                                                                                                                                                                              |
| arn                      | core | string    | The Amazon Resource Name (ARN) of the control.                                                                                                                                                                                                         |
| control_mapping_sources  | core | json      | The data mapping sources for the control.                                                                                                                                                                                                              |
| control_sources          | core | string    | The data source types that determine where Audit Manager collects evidence from for the control.                                                                                                                                                       |
| created_at               | core | timestamp | The time when the control was created.                                                                                                                                                                                                                 |
| created_by               | core | string    | The user or role that created the control.                                                                                                                                                                                                             |
| description              | core | string    | The description of the control.                                                                                                                                                                                                                        |
| id                       | core | string    | The unique identifier for the control.                                                                                                                                                                                                                 |
| last_updated_at          | core | timestamp | The time when the control was most recently updated.                                                                                                                                                                                                   |
| last_updated_by          | core | string    | The user or role that most recently updated the control.                                                                                                                                                                                               |
| name                     | core | string    | The name of the control.                                                                                                                                                                                                                               |
| state                    | core | string    | The state of the control. The END_OF_SUPPORT state is applicable to standard controls only. This state indicates that the standard control can still be used to collect evidence, but Audit Manager is no longer updating or maintaining that control. |
| tags                     | core | hstore    |
| testing_information      | core | string    | The steps that you should follow to determine if the control has been satisfied.                                                                                                                                                                       |
| type                     | core | string    | Specifies whether the control is a standard control or a custom control.                                                                                                                                                                               |
