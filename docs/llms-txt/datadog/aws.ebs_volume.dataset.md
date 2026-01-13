# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ebs_volume.dataset.md

---
title: EBS Volume
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EBS Volume
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ebs_volume.dataset/index.html
---

# EBS Volume

This table represents the EBS Volume resource from Amazon Web Services.

```
aws.ebs_volume
```

## Fields

| Title                | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                                                 | Description |
| -------------------- | ---- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string    |
| account_id           | core | string    |
| attachments          | core | json      | <note> This parameter is not returned by CreateVolume. </note> Information about the volume attachments.                                                                                                                                                                                                                                                  |
| availability_zone    | core | string    | The Availability Zone for the volume.                                                                                                                                                                                                                                                                                                                     |
| create_time          | core | timestamp | The time stamp when volume creation was initiated.                                                                                                                                                                                                                                                                                                        |
| encrypted            | core | bool      | Indicates whether the volume is encrypted.                                                                                                                                                                                                                                                                                                                |
| fast_restored        | core | bool      | <note> This parameter is not returned by CreateVolume. </note> Indicates whether the volume was created using fast snapshot restore.                                                                                                                                                                                                                      |
| iops                 | core | int64     | The number of I/O operations per second (IOPS). For <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes, this represents the number of IOPS that are provisioned for the volume. For <code>gp2</code> volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. |
| kms_key_id           | core | string    | The Amazon Resource Name (ARN) of the KMS key that was used to protect the volume encryption key for the volume.                                                                                                                                                                                                                                          |
| multi_attach_enabled | core | bool      | Indicates whether Amazon EBS Multi-Attach is enabled.                                                                                                                                                                                                                                                                                                     |
| operator             | core | json      | The service provider that manages the volume.                                                                                                                                                                                                                                                                                                             |
| outpost_arn          | core | string    | The Amazon Resource Name (ARN) of the Outpost.                                                                                                                                                                                                                                                                                                            |
| size                 | core | int64     | The size of the volume, in GiBs.                                                                                                                                                                                                                                                                                                                          |
| snapshot_id          | core | string    | The snapshot from which the volume was created, if applicable.                                                                                                                                                                                                                                                                                            |
| sse_type             | core | string    | <note> This parameter is not returned by CreateVolume. </note> Reserved for future use.                                                                                                                                                                                                                                                                   |
| state                | core | string    | The volume state.                                                                                                                                                                                                                                                                                                                                         |
| tags                 | core | hstore    |
| throughput           | core | int64     | The throughput that the volume supports, in MiB/s.                                                                                                                                                                                                                                                                                                        |
| volume_arn           | core | string    |
| volume_id            | core | string    | The ID of the volume.                                                                                                                                                                                                                                                                                                                                     |
| volume_type          | core | string    | The volume type.                                                                                                                                                                                                                                                                                                                                          |
