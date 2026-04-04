# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.verifiedpermissions_identity_source.dataset.md

---
title: Verified Permissions Identity Source Item
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Verified Permissions Identity Source
  Item
---

# Verified Permissions Identity Source Item

Represents an identity source used in AWS Verified Permissions. It defines the connection between Verified Permissions and an external identity provider, such as Amazon Cognito or AWS IAM Identity Center, allowing policies to evaluate user attributes and group memberships for access decisions.

```
aws.verifiedpermissions_identity_source
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                           | Description |
| --------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| configuration         | core | json       | Contains configuration information about an identity source.                                        |
| created_date          | core | timestamp  | The date and time the identity source was originally created.                                       |
| details               | core | json       | A structure that contains the details of the associated identity provider (IdP).                    |
| identity_source_id    | core | string     | The unique identifier of the identity source.                                                       |
| last_updated_date     | core | timestamp  | The date and time the identity source was most recently updated.                                    |
| policy_store_id       | core | string     | The identifier of the policy store that contains the identity source.                               |
| principal_entity_type | core | string     | The Cedar entity type of the principals returned from the IdP associated with this identity source. |
| tags                  | core | hstore_csv |
