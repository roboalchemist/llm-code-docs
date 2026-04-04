# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_ingress_point.dataset.md

---
title: SES Ingress Point
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Ingress Point
---

# SES Ingress Point

This table represents the SES Ingress Point resource from Amazon Web Services.

```
aws.ses_ingress_point
```

## Fields

| Title                            | ID   | Type       | Data Type                                                                                                                                             | Description |
| -------------------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string     |
| a_record                         | core | string     | The DNS A Record that identifies your ingress endpoint. Configure your DNS Mail Exchange (MX) record with this value to route emails to Mail Manager. |
| account_id                       | core | string     |
| created_timestamp                | core | timestamp  | The timestamp of when the ingress endpoint was created.                                                                                               |
| ingress_point_arn                | core | string     | The Amazon Resource Name (ARN) of the ingress endpoint resource.                                                                                      |
| ingress_point_auth_configuration | core | json       | The authentication configuration of the ingress endpoint resource.                                                                                    |
| ingress_point_id                 | core | string     | The identifier of an ingress endpoint resource.                                                                                                       |
| ingress_point_name               | core | string     | A user friendly name for the ingress endpoint.                                                                                                        |
| last_updated_timestamp           | core | timestamp  | The timestamp of when the ingress endpoint was last updated.                                                                                          |
| rule_set_id                      | core | string     | The identifier of a rule set resource associated with the ingress endpoint.                                                                           |
| status                           | core | string     | The status of the ingress endpoint resource.                                                                                                          |
| tags                             | core | hstore_csv |
| traffic_policy_id                | core | string     | The identifier of the traffic policy resource associated with the ingress endpoint.                                                                   |
| type                             | core | string     | The type of ingress endpoint.                                                                                                                         |
