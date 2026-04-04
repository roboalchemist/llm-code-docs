# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshift_hsm_configuration.dataset.md

---
title: Redshift HSM Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift HSM Configuration
---

# Redshift HSM Configuration

This table represents the Redshift HSM Configuration resource from Amazon Web Services.

```
aws.redshift_hsm_configuration
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                          | Description |
| ---------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| description                  | core | string     | A text description of the HSM configuration.                                                                       |
| hsm_configuration_identifier | core | string     | The name of the Amazon Redshift HSM configuration.                                                                 |
| hsm_ip_address               | core | string     | The IP address that the Amazon Redshift cluster must use to access the HSM.                                        |
| hsm_partition_name           | core | string     | The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys. |
| tags                         | core | hstore_csv |
