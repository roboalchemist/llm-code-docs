# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.emr_security_configuration.dataset.md

---
title: EMR Security Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EMR Security Configuration
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.emr_security_configuration.dataset/index.html
---

# EMR Security Configuration

EMR Security Configuration in AWS defines the security settings applied to an Amazon EMR cluster. It allows you to specify encryption options for data at rest and in transit, Kerberos authentication, and other security-related controls. This configuration ensures that sensitive data processed by EMR is protected according to compliance and organizational requirements.

```
aws.emr_security_configuration
```

## Fields

| Title                  | ID   | Type      | Data Type                                                | Description |
| ---------------------- | ---- | --------- | -------------------------------------------------------- | ----------- |
| _key                   | core | string    |
| account_id             | core | string    |
| creation_date_time     | core | timestamp | The date and time the security configuration was created |
| name                   | core | string    | The name of the security configuration.                  |
| security_configuration | core | string    | The security configuration details in JSON format.       |
| tags                   | core | hstore    |
