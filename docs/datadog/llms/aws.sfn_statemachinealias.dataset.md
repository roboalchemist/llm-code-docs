# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sfn_statemachinealias.dataset.md

---
title: Step Functions State Machine Alias
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Step Functions State Machine Alias
---

# Step Functions State Machine Alias

This table represents the Step Functions State Machine Alias resource from Amazon Web Services.

```
aws.sfn_statemachinealias
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                    | Description |
| ----------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| creation_date           | core | timestamp  | The date the state machine alias was created.                                                                                |
| description             | core | string     | A description of the alias.                                                                                                  |
| name                    | core | string     | The name of the state machine alias.                                                                                         |
| routing_configuration   | core | json       | The routing configuration of the alias.                                                                                      |
| state_machine_alias_arn | core | string     | The Amazon Resource Name (ARN) of the state machine alias.                                                                   |
| tags                    | core | hstore_csv |
| update_date             | core | timestamp  | The date the state machine alias was last updated. For a newly created state machine, this is the same as the creation date. |
