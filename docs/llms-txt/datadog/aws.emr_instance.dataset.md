# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.emr_instance.dataset.md

---
title: EMR Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EMR Instance
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.emr_instance.dataset/index.html
---

# EMR Instance

An EMR Instance in AWS is a compute resource that runs as part of an Amazon EMR cluster. It provides the processing power needed to run big data frameworks like Apache Spark, Hadoop, and Hive. Instances can be configured as master, core, or task nodes, each serving different roles in managing cluster operations, storing data, or executing distributed processing tasks.

```
aws.emr_instance
```

## Fields

| Title              | ID   | Type   | Data Type                                                                            | Description |
| ------------------ | ---- | ------ | ------------------------------------------------------------------------------------ | ----------- |
| _key               | core | string |
| account_id         | core | string |
| ebs_volumes        | core | json   | The list of Amazon EBS volumes that are attached to this instance.                   |
| ec2_instance_id    | core | string | The unique identifier of the instance in Amazon EC2.                                 |
| id                 | core | string | The unique identifier for the instance in Amazon EMR.                                |
| instance_fleet_id  | core | string | The unique identifier of the instance fleet to which an Amazon EC2 instance belongs. |
| instance_group_id  | core | string | The identifier of the instance group to which this instance belongs.                 |
| instance_type      | core | string | The Amazon EC2 instance type, for example m3.xlarge.                                 |
| market             | core | string | The instance purchasing option. Valid values are ON_DEMAND or SPOT.                  |
| private_dns_name   | core | string | The private DNS name of the instance.                                                |
| private_ip_address | core | string | The private IP address of the instance.                                              |
| public_dns_name    | core | string | The public DNS name of the instance.                                                 |
| public_ip_address  | core | string | The public IP address of the instance.                                               |
| status             | core | json   | The current status of the instance.                                                  |
| tags               | core | hstore |
