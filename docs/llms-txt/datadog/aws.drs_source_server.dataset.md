# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.drs_source_server.dataset.md

---
title: Elastic Disaster Recovery Source Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Elastic Disaster Recovery Source
  Server
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.drs_source_server.dataset/index.html
---

# Elastic Disaster Recovery Source Server

Elastic Disaster Recovery Source Server in AWS represents a machine that is being protected and replicated by AWS Elastic Disaster Recovery (DRS). It is the source system from which data and configurations are continuously replicated to AWS, enabling quick recovery in case of outages or failures. This resource tracks the state, replication status, and recovery readiness of the original server.

```
aws.drs_source_server
```

## Fields

| Title                                | ID   | Type   | Data Type                                                                                                                                                                    | Description |
| ------------------------------------ | ---- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string |
| account_id                           | core | string |
| agent_version                        | core | string | The version of the DRS agent installed on the source server                                                                                                                  |
| arn                                  | core | string | The ARN of the Source Server.                                                                                                                                                |
| data_replication_info                | core | json   | The Data Replication Info of the Source Server.                                                                                                                              |
| last_launch_result                   | core | string | The status of the last recovery launch of this Source Server.                                                                                                                |
| life_cycle                           | core | json   | The lifecycle information of this Source Server.                                                                                                                             |
| recovery_instance_id                 | core | string | The ID of the Recovery Instance associated with this Source Server.                                                                                                          |
| replication_direction                | core | string | Replication direction of the Source Server.                                                                                                                                  |
| reversed_direction_source_server_arn | core | string | For EC2-originated Source Servers which have been failed over and then failed back, this value will mean the ARN of the Source Server on the opposite replication direction. |
| source_cloud_properties              | core | json   | Source cloud properties of the Source Server.                                                                                                                                |
| source_network_id                    | core | string | ID of the Source Network which is protecting this Source Server's network.                                                                                                   |
| source_properties                    | core | json   | The source properties of the Source Server.                                                                                                                                  |
| source_server_id                     | core | string | The ID of the Source Server.                                                                                                                                                 |
| staging_area                         | core | json   | The staging area of the source server.                                                                                                                                       |
| tags                                 | core | hstore |
