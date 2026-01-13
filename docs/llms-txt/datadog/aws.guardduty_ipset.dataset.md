# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.guardduty_ipset.dataset.md

---
title: GuardDuty Ipset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > GuardDuty Ipset
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.guardduty_ipset.dataset/index.html
---

# GuardDuty Ipset

This table represents the GuardDuty Ipset resource from Amazon Web Services.

```
aws.guardduty_ipset
```

## Fields

| Title      | ID   | Type   | Data Type                                       | Description |
| ---------- | ---- | ------ | ----------------------------------------------- | ----------- |
| _key       | core | string |
| account_id | core | string |
| format     | core | string | The format of the file that contains the IPSet. |
| location   | core | string | The URI of the file that contains the IPSet.    |
| name       | core | string | The user-friendly name for the IPSet.           |
| status     | core | string | The status of IPSet file that was uploaded.     |
| tags       | core | hstore |
