# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_ipv6pool_ec2.dataset.md

---
title: EC2 IPv6 Pool EC2
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 IPv6 Pool EC2
---

# EC2 IPv6 Pool EC2

This table represents the EC2 IPv6 Pool EC2 resource from Amazon Web Services.

```
aws.ec2_ipv6pool_ec2
```

## Fields

| Title            | ID   | Type       | Data Type                             | Description |
| ---------------- | ---- | ---------- | ------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| description      | core | string     | The description for the address pool. |
| pool_cidr_blocks | core | json       | The CIDR blocks for the address pool. |
| pool_id          | core | string     | The ID of the address pool.           |
| tags             | core | hstore_csv |
