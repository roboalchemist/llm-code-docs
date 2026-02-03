# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.gamelift_alias.dataset.md

---
title: GameLift Alias
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GameLift Alias
---

# GameLift Alias

An AWS GameLift Alias is a resource that provides a named reference to a GameLift fleet. It allows you to create a stable identifier for game clients to connect to, while giving you flexibility to redirect traffic to different fleets without changing client configurations. This makes it easier to manage game server deployments, perform updates, or reroute players during scaling and maintenance.

```
aws.gamelift_alias
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                               | Description |
| ----------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| alias_arn         | core | string     | The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift Servers alias resource and uniquely identifies it. ARNs are unique across all Regions. Format is arn:aws:gamelift:<region>::alias/alias-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912. In a GameLift alias ARN, the resource ID matches the alias ID value. |
| alias_id          | core | string     | A unique identifier for the alias. Alias IDs are unique within a Region.                                                                                                                                                                                                                                                |
| creation_time     | core | timestamp  | A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").                                                                                                                                                                    |
| description       | core | string     | A human-readable description of an alias.                                                                                                                                                                                                                                                                               |
| last_updated_time | core | timestamp  | The time that this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").                                                                                                                                                                             |
| name              | core | string     | A descriptive label that is associated with an alias. Alias names do not need to be unique.                                                                                                                                                                                                                             |
| routing_strategy  | core | json       | The routing configuration, including routing type and fleet target, for the alias.                                                                                                                                                                                                                                      |
| tags              | core | hstore_csv |
