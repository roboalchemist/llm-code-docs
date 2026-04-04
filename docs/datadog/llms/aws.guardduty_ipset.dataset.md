# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.guardduty_ipset.dataset.md

---
title: GuardDuty IPSet
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GuardDuty IPSet
---

# GuardDuty IPSet

GuardDuty IPSet in AWS is a custom list of trusted or malicious IP addresses that you can upload and use with Amazon GuardDuty. It allows you to define known safe or suspicious IP ranges so GuardDuty can better detect and filter findings based on your security context.

```
aws.guardduty_ipset
```

## Fields

| Title      | ID   | Type       | Data Type                                       | Description |
| ---------- | ---- | ---------- | ----------------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| format     | core | string     | The format of the file that contains the IPSet. |
| location   | core | string     | The URI of the file that contains the IPSet.    |
| name       | core | string     | The user-friendly name for the IPSet.           |
| status     | core | string     | The status of IPSet file that was uploaded.     |
| tags       | core | hstore_csv |
