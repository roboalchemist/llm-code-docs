# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.emr_instance_group.dataset.md

---
title: EMR Instance Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EMR Instance Group
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.emr_instance_group.dataset/index.html
---

# EMR Instance Group

An EMR Instance Group in AWS defines a set of Amazon EC2 instances within an Amazon EMR cluster that share the same configuration. It allows you to specify instance type, count, and purchasing option (On-Demand or Spot). Instance groups can be designated as master, core, or task nodes, each serving different roles in cluster operations. This resource helps manage compute capacity and cost for big data processing workloads.

```
aws.emr_instance_group
```

## Fields

| Title                                            | ID   | Type   | Data Type                                                                                                                                                                                                                                                                                         | Description |
| ------------------------------------------------ | ---- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                             | core | string |
| account_id                                       | core | string |
| auto_scaling_policy                              | core | json   | An automatic scaling policy for a core instance group or task instance group in an Amazon EMR cluster. The automatic scaling policy defines how an instance group dynamically adds and terminates Amazon EC2 instances in response to the value of a CloudWatch metric. See PutAutoScalingPolicy. |
| bid_price                                        | core | string | If specified, indicates that the instance group uses Spot Instances. This is the maximum price you are willing to pay for Spot Instances. Specify OnDemandPrice to set the amount equal to the On-Demand price, or specify an amount in USD.                                                      |
| configurations                                   | core | json   | Amazon EMR releases 4.x or later. The list of configurations supplied for an Amazon EMR cluster instance group. You can specify a separate configuration for each instance group (master, core, and task).                                                                                        |
| configurations_version                           | core | int64  | The version number of the requested configuration specification for this instance group.                                                                                                                                                                                                          |
| custom_ami_id                                    | core | string | The custom AMI ID to use for the provisioned instance group.                                                                                                                                                                                                                                      |
| ebs_block_devices                                | core | json   | The EBS block devices that are mapped to this instance group.                                                                                                                                                                                                                                     |
| ebs_optimized                                    | core | bool   | If the instance group is EBS-optimized. An Amazon EBS-optimized instance uses an optimized configuration stack and provides additional, dedicated capacity for Amazon EBS I/O.                                                                                                                    |
| id                                               | core | string | The identifier of the instance group.                                                                                                                                                                                                                                                             |
| instance_group_type                              | core | string | The type of the instance group. Valid values are MASTER, CORE or TASK.                                                                                                                                                                                                                            |
| instance_type                                    | core | string | The Amazon EC2 instance type for all instances in the instance group.                                                                                                                                                                                                                             |
| last_successfully_applied_configurations         | core | json   | A list of configurations that were successfully applied for an instance group last time.                                                                                                                                                                                                          |
| last_successfully_applied_configurations_version | core | int64  | The version number of a configuration specification that was successfully applied for an instance group last time.                                                                                                                                                                                |
| market                                           | core | string | The marketplace to provision instances for this group. Valid values are ON_DEMAND or SPOT.                                                                                                                                                                                                        |
| name                                             | core | string | The name of the instance group.                                                                                                                                                                                                                                                                   |
| requested_instance_count                         | core | int64  | The target number of instances for the instance group.                                                                                                                                                                                                                                            |
| running_instance_count                           | core | int64  | The number of instances currently running in this instance group.                                                                                                                                                                                                                                 |
| shrink_policy                                    | core | json   | Policy for customizing shrink operations.                                                                                                                                                                                                                                                         |
| status                                           | core | json   | The current status of the instance group.                                                                                                                                                                                                                                                         |
| tags                                             | core | hstore |
