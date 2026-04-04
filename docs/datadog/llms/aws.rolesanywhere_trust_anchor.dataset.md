# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rolesanywhere_trust_anchor.dataset.md

---
title: Rolesanywhere Trust Anchor
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Rolesanywhere Trust Anchor
---

# Rolesanywhere Trust Anchor

This table represents the rolesanywhere_trust_anchor resource from Amazon Web Services.

```
aws.rolesanywhere_trust_anchor
```

## Fields

| Title                 | ID   | Type       | Data Type                                                             | Description |
| --------------------- | ---- | ---------- | --------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| created_at            | core | timestamp  | The ISO-8601 timestamp when the trust anchor was created.             |
| enabled               | core | bool       | Indicates whether the trust anchor is enabled.                        |
| name                  | core | string     | The name of the trust anchor.                                         |
| notification_settings | core | json       | A list of notification settings to be associated to the trust anchor. |
| tags                  | core | hstore_csv |
| trust_anchor_arn      | core | string     | The ARN of the trust anchor.                                          |
| trust_anchor_id       | core | string     | The unique identifier of the trust anchor.                            |
| updated_at            | core | timestamp  | The ISO-8601 timestamp when the trust anchor was last updated.        |
