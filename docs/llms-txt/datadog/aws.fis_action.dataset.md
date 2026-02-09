# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.fis_action.dataset.md

---
title: AWS FIS Action
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS FIS Action
---

# AWS FIS Action

AWS FIS Action represents a specific experiment action within AWS Fault Injection Simulator. It defines the parameters and behavior of a fault injection activity, such as stopping instances, throttling APIs, or introducing network latency. This resource allows users to retrieve details about an action, including its description, parameters, and supported targets, enabling controlled chaos experiments to test system resilience and reliability.

```
aws.fis_action
```

## Fields

| Title       | ID   | Type       | Data Type                                     | Description |
| ----------- | ---- | ---------- | --------------------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| arn         | core | string     | The Amazon Resource Name (ARN) of the action. |
| description | core | string     | The description for the action.               |
| id          | core | string     | The ID of the action.                         |
| parameters  | core | string     | The action parameters, if applicable.         |
| tags        | core | hstore_csv |
| targets     | core | string     | The supported targets for the action.         |
