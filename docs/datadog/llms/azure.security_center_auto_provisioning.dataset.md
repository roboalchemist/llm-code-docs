# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.security_center_auto_provisioning.dataset.md

---
title: Security Center Auto Provisioning
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Security Center Auto Provisioning
---

# Security Center Auto Provisioning

This table represents the Security Center Auto Provisioning resource from Microsoft Azure.

```
azure.security_center_auto_provisioning
```

## Fields

| Title             | ID   | Type       | Data Type                                                         | Description |
| ----------------- | ---- | ---------- | ----------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| auto_provision    | core | string     | Describes what kind of security agent provisioning action to take |
| id                | core | string     | Resource Id                                                       |
| location          | core | string     |
| name              | core | string     | Resource name                                                     |
| resource_group    | core | string     |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
| type              | core | string     | Resource type                                                     |
