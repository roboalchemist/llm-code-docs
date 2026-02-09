# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.storagegateway_volume.dataset.md

---
title: Storage Gateway Volume
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Storage Gateway Volume
---

# Storage Gateway Volume

Storage Gateway Volume in AWS represents a virtual storage volume managed through the AWS Storage Gateway service. It allows on-premises applications to use cloud-backed storage as if it were local, supporting block-based workloads. Data written to the volume is stored in AWS and can be asynchronously backed up as Amazon EBS snapshots, providing durability and scalability while integrating with existing on-premises environments.

```
aws.storagegateway_volume
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                                                                                                                                                                  | Description |
| ------------------------ | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| gateway_arn              | core | string     | The Amazon Resource Name (ARN) of the gateway. Use the ListGateways operation to return a list of gateways for your account and Amazon Web Services Region.                                                                                                                |
| gateway_id               | core | string     | The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations. Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).           |
| tags                     | core | hstore_csv |
| volume_arn               | core | string     | The Amazon Resource Name (ARN) for the storage volume. For example, the following is a valid ARN: arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-). |
| volume_attachment_status | core | string     | One of the VolumeStatus values that indicates the state of the storage volume.                                                                                                                                                                                             |
| volume_id                | core | string     | The unique identifier assigned to the volume. This ID becomes part of the volume Amazon Resource Name (ARN), which you use as input for other operations. Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).                                |
| volume_size_in_bytes     | core | int64      | The size of the volume in bytes. Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).                                                                                                                                                         |
| volume_type              | core | string     | One of the VolumeType enumeration values describing the type of the volume.                                                                                                                                                                                                |
