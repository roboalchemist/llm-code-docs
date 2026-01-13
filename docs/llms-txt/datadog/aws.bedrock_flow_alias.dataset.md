# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_flow_alias.dataset.md

---
title: Bedrock Flow Alias
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Flow Alias
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.bedrock_flow_alias.dataset/index.html
---

# Bedrock Flow Alias

This table represents the Bedrock Flow Alias resource from Amazon Web Services.

```
aws.bedrock_flow_alias
```

## Fields

| Title                     | ID   | Type      | Data Type                                                                        | Description |
| ------------------------- | ---- | --------- | -------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string    |
| account_id                | core | string    |
| arn                       | core | string    | The Amazon Resource Name (ARN) of the flow.                                      |
| concurrency_configuration | core | json      | The configuration that specifies how nodes in the flow are executed in parallel. |
| created_at                | core | timestamp | The time at which the flow was created.                                          |
| description               | core | string    | The description of the flow.                                                     |
| flow_id                   | core | string    | The unique identifier of the flow that the alias belongs to.                     |
| id                        | core | string    | The unique identifier of the alias of the flow.                                  |
| name                      | core | string    | The name of the alias.                                                           |
| routing_configuration     | core | json      | Contains information about the version that the alias is mapped to.              |
| tags                      | core | hstore    |
| updated_at                | core | timestamp | The time at which the alias was last updated.                                    |
