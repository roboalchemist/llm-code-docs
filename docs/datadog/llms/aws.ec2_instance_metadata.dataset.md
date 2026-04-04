# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_instance_metadata.dataset.md

---
title: Ec2 Instance Metadata
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ec2 Instance Metadata
---

# Ec2 Instance Metadata

This table represents the ec2_instance_metadata resource from Amazon Web Services.

```
aws.ec2_instance_metadata
```

## Fields

| Title             | ID   | Type       | Data Type                                                         | Description |
| ----------------- | ---- | ---------- | ----------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| availability_zone | core | string     | The Availability Zone or Local Zone of the instance.              |
| image_metadata    | core | json       | Information about the AMI used to launch the instance.            |
| instance_id       | core | string     | The ID of the instance.                                           |
| instance_type     | core | string     | The instance type.                                                |
| launch_time       | core | timestamp  | The time the instance was launched.                               |
| operator          | core | json       | The entity that manages the instance.                             |
| owner_id          | core | string     | The ID of the Amazon Web Services account that owns the instance. |
| state             | core | json       | The current state of the instance.                                |
| tags              | core | hstore_csv |
| zone_id           | core | string     | The ID of the Availability Zone or Local Zone of the instance.    |
