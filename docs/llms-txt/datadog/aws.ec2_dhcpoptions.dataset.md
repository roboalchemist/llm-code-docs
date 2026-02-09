# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_dhcpoptions.dataset.md

---
title: EC2 DHCP Options
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EC2 DHCP Options
---

# EC2 DHCP Options

This table represents the EC2 DHCP Options resource from Amazon Web Services.

```
aws.ec2_dhcpoptions
```

## Fields

| Title               | ID   | Type       | Data Type                                                                 | Description |
| ------------------- | ---- | ---------- | ------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| dhcp_configurations | core | json       | The DHCP options in the set.                                              |
| dhcp_options_id     | core | string     | The ID of the set of DHCP options.                                        |
| owner_id            | core | string     | The ID of the Amazon Web Services account that owns the DHCP options set. |
| tags                | core | hstore_csv |
