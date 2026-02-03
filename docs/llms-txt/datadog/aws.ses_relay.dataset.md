# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_relay.dataset.md

---
title: SES Relay
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Relay
---

# SES Relay

This table represents the SES Relay resource from Amazon Web Services.

```
aws.ses_relay
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                    | Description |
| ----------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| authentication          | core | json       | The authentication attributeâcontains the secret ARN where the customer relay server credentials are stored. |
| created_timestamp       | core | timestamp  | The timestamp of when the relay was created.                                                                 |
| last_modified_timestamp | core | timestamp  | The timestamp of when relay was last updated.                                                                |
| relay_arn               | core | string     | The Amazon Resource Name (ARN) of the relay.                                                                 |
| relay_id                | core | string     | The unique relay identifier.                                                                                 |
| relay_name              | core | string     | The unique name of the relay.                                                                                |
| server_name             | core | string     | The destination relay server address.                                                                        |
| server_port             | core | int64      | The destination relay server port.                                                                           |
| tags                    | core | hstore_csv |
