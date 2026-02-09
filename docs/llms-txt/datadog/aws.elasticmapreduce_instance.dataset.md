# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.elasticmapreduce_instance.dataset.md

---
title: Elasticmapreduce Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elasticmapreduce Instance
---

# Elasticmapreduce Instance

This table represents the elasticmapreduce_instance resource from Amazon Web Services.

```
aws.elasticmapreduce_instance
```

## Fields

| Title              | ID   | Type       | Data Type | Description |
| ------------------ | ---- | ---------- | --------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| ebs_volumes        | core | json       |
| ec2_instance_id    | core | string     |
| id                 | core | string     |
| instance_fleet_id  | core | string     |
| instance_group_id  | core | string     |
| instance_type      | core | string     |
| market             | core | string     |
| private_dns_name   | core | string     |
| private_ip_address | core | string     |
| public_dns_name    | core | string     |
| public_ip_address  | core | string     |
| status             | core | json       |
| tags               | core | hstore_csv |
