# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_traffic_policy.dataset.md

---
title: SES Traffic Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Traffic Policy
---

# SES Traffic Policy

This table represents the SES Traffic Policy resource from Amazon Web Services.

```
aws.ses_traffic_policy
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                              | Description |
| ---------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| created_timestamp      | core | timestamp  | The timestamp of when the traffic policy was created.                                                                  |
| default_action         | core | string     | The default action of the traffic policy.                                                                              |
| last_updated_timestamp | core | timestamp  | The timestamp of when the traffic policy was last updated.                                                             |
| max_message_size_bytes | core | int64      | The maximum message size in bytes of email which is allowed in by this traffic policyâanything larger will be blocked. |
| policy_statements      | core | json       | The list of conditions which are in the traffic policy resource.                                                       |
| tags                   | core | hstore_csv |
| traffic_policy_arn     | core | string     | The Amazon Resource Name (ARN) of the traffic policy resource.                                                         |
| traffic_policy_id      | core | string     | The identifier of the traffic policy resource.                                                                         |
| traffic_policy_name    | core | string     | A user-friendly name for the traffic policy resource.                                                                  |
