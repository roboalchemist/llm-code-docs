# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_transitgatewaypolicytable.dataset.md

---
title: Ec2 Transitgatewaypolicytable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ec2 Transitgatewaypolicytable
---

# Ec2 Transitgatewaypolicytable

This table represents the ec2_transitgatewaypolicytable resource from Amazon Web Services.

```
aws.ec2_transitgatewaypolicytable
```

## Fields

| Title                           | ID   | Type       | Data Type                                                        | Description |
| ------------------------------- | ---- | ---------- | ---------------------------------------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| creation_time                   | core | timestamp  | The timestamp when the transit gateway policy table was created. |
| state                           | core | string     | The state of the transit gateway policy table                    |
| tags                            | core | hstore_csv |
| transit_gateway_id              | core | string     | The ID of the transit gateway.                                   |
| transit_gateway_policy_table_id | core | string     | The ID of the transit gateway policy table.                      |
