# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.appflow_connectorprofile.dataset.md

---
title: Appflow Connectorprofile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Appflow Connectorprofile
---

# Appflow Connectorprofile

This table represents the appflow_connectorprofile resource from Amazon Web Services.

```
aws.appflow_connectorprofile
```

## Fields

| Title                                 | ID   | Type       | Data Type                                                                                                                        | Description |
| ------------------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                  | core | string     |
| account_id                            | core | string     |
| connection_mode                       | core | string     | Indicates the connection mode and if it is public or private.                                                                    |
| connector_label                       | core | string     | The label for the connector profile being created.                                                                               |
| connector_profile_arn                 | core | string     | The Amazon Resource Name (ARN) of the connector profile.                                                                         |
| connector_profile_name                | core | string     | The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in the Amazon Web Services account. |
| connector_profile_properties          | core | json       | The connector-specific properties of the profile configuration.                                                                  |
| connector_type                        | core | string     | The type of connector, such as Salesforce, Amplitude, and so on.                                                                 |
| created_at                            | core | timestamp  | Specifies when the connector profile was created.                                                                                |
| credentials_arn                       | core | string     | The Amazon Resource Name (ARN) of the connector profile credentials.                                                             |
| last_updated_at                       | core | timestamp  | Specifies when the connector profile was last updated.                                                                           |
| private_connection_provisioning_state | core | json       | Specifies the private connection provisioning state.                                                                             |
| tags                                  | core | hstore_csv |
