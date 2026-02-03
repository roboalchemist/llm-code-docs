# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_multiplex.dataset.md

---
title: Elemental MediaLive Multiplex
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaLive Multiplex
---

# Elemental MediaLive Multiplex

Elemental MediaLive Multiplex is an AWS resource that enables combining multiple live video channels into a single transport stream for broadcast and distribution. It allows efficient use of encoding resources by sharing infrastructure across channels, while providing features like redundancy, failover, and flexible bitrate allocation. This is commonly used for broadcast television workflows where multiple channels need to be delivered together in a single output stream.

```
aws.medialive_multiplex
```

## Fields

| Title                   | ID   | Type          | Data Type                                       | Description |
| ----------------------- | ---- | ------------- | ----------------------------------------------- | ----------- |
| _key                    | core | string        |
| account_id              | core | string        |
| arn                     | core | string        | The unique arn of the multiplex.                |
| availability_zones      | core | array<string> | A list of availability zones for the multiplex. |
| id                      | core | string        | The unique id of the multiplex.                 |
| multiplex_settings      | core | json          | Configuration for a multiplex event.            |
| name                    | core | string        | The name of the multiplex.                      |
| pipelines_running_count | core | int64         | The number of currently healthy pipelines.      |
| program_count           | core | int64         | The number of programs in the multiplex.        |
| state                   | core | string        | The current state of the multiplex.             |
| tags                    | core | hstore_csv    |
