# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.drs_recovery_instance.dataset.md

---
title: Elastic Disaster Recovery Recovery Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Elastic Disaster Recovery Recovery
  Instance
---

# Elastic Disaster Recovery Recovery Instance

An Elastic Disaster Recovery Recovery Instance in AWS is a temporary compute resource created during failover or recovery testing. It is launched from replicated source servers to provide a functional copy of workloads in the AWS environment. This allows businesses to quickly resume operations after disruptions, validate recovery plans, and minimize downtime.

```
aws.drs_recovery_instance
```

## Fields

| Title                            | ID   | Type       | Data Type                                                                                            | Description |
| -------------------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string     |
| account_id                       | core | string     |
| agent_version                    | core | string     | The version of the DRS agent installed on the recovery instance                                      |
| arn                              | core | string     | The ARN of the Recovery Instance.                                                                    |
| data_replication_info            | core | json       | The Data Replication Info of the Recovery Instance.                                                  |
| ec2_instance_id                  | core | string     | The EC2 instance ID of the Recovery Instance.                                                        |
| ec2_instance_state               | core | string     | The state of the EC2 instance for this Recovery Instance.                                            |
| failback                         | core | json       | An object representing failback related information of the Recovery Instance.                        |
| is_drill                         | core | bool       | Whether this Recovery Instance was created for a drill or for an actual Recovery event.              |
| job_id                           | core | string     | The ID of the Job that created the Recovery Instance.                                                |
| origin_availability_zone         | core | string     | AWS availability zone associated with the recovery instance.                                         |
| origin_environment               | core | string     | Environment (On Premises / AWS) of the instance that the recovery instance originated from.          |
| point_in_time_snapshot_date_time | core | string     | The date and time of the Point in Time (PIT) snapshot that this Recovery Instance was launched from. |
| recovery_instance_id             | core | string     | The ID of the Recovery Instance.                                                                     |
| recovery_instance_properties     | core | json       | Properties of the Recovery Instance machine.                                                         |
| source_outpost_arn               | core | string     | The ARN of the source Outpost                                                                        |
| source_server_id                 | core | string     | The Source Server ID that this Recovery Instance is associated with.                                 |
| tags                             | core | hstore_csv |
