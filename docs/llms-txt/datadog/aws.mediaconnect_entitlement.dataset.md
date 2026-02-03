# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediaconnect_entitlement.dataset.md

---
title: Elemental MediaConnect Entitlement
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaConnect Entitlement
---

# Elemental MediaConnect Entitlement

Elemental MediaConnect Entitlement in AWS represents permission granted to another AWS account to access a MediaConnect flow. It allows secure sharing of live video streams between accounts without duplicating infrastructure. This resource defines the details of the entitlement, such as the subscriber account ID and status, enabling controlled distribution of live video content.

```
aws.mediaconnect_entitlement
```

## Fields

| Title                                | ID   | Type       | Data Type                                                                       | Description |
| ------------------------------------ | ---- | ---------- | ------------------------------------------------------------------------------- | ----------- |
| _key                                 | core | string     |
| account_id                           | core | string     |
| data_transfer_subscriber_fee_percent | core | int64      | Percentage from 0-100 of the data transfer cost to be billed to the subscriber. |
| entitlement_arn                      | core | string     | The ARN of the entitlement.                                                     |
| entitlement_name                     | core | string     | The name of the entitlement.                                                    |
| tags                                 | core | hstore_csv |
