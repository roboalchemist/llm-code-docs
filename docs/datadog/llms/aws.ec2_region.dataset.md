# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_region.dataset.md

---
title: EC2 Region
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 Region
---

# EC2 Region

An EC2 Region in AWS represents a distinct geographical area where Amazon EC2 resources are hosted. Each region consists of multiple isolated Availability Zones, providing redundancy and high availability. Users can choose regions based on proximity to their customers, compliance requirements, or cost considerations. Regions help ensure data locality and fault tolerance.

```
aws.ec2_region
```

## Fields

| Title         | ID   | Type       | Data Type                                                                                          | Description |
| ------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| endpoint      | core | string     | The Region service endpoint.                                                                       |
| opt_in_status | core | string     | The Region opt-in status. The possible values are opt-in-not-required, opted-in, and not-opted-in. |
| region_name   | core | string     | The name of the Region.                                                                            |
| tags          | core | hstore_csv |
