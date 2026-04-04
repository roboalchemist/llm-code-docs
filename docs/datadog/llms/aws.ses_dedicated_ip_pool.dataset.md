# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_dedicated_ip_pool.dataset.md

---
title: SES Dedicated IP Pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Dedicated IP Pool
---

# SES Dedicated IP Pool

This table represents the SES Dedicated IP Pool resource from Amazon Web Services.

```
aws.ses_dedicated_ip_pool
```

## Fields

| Title        | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                        | Description |
| ------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key         | core | string     |
| account_id   | core | string     |
| pool_name    | core | string     | The name of the dedicated IP pool.                                                                                                                                                                                                                                                               |
| scaling_mode | core | string     | The type of the dedicated IP pool. <ul> <li> <code>STANDARD</code> â A dedicated IP pool where you can control which IPs are part of the pool. </li> <li> <code>MANAGED</code> â A dedicated IP pool where the reputation and number of IPs are automatically managed by Amazon SES. </li> </ul> |
| tags         | core | hstore_csv |
