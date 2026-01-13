# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_saml_provider.dataset.md

---
title: IAM SAML Provider
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM SAML Provider
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iam_saml_provider.dataset/index.html
---

# IAM SAML Provider

IAM SAML Provider in AWS is a resource that stores information about a Security Assertion Markup Language (SAML) identity provider. It allows federated users from external identity systems to access AWS resources without creating individual IAM users. This enables single sign-on (SSO) by trusting assertions from the external provider.

```
aws.iam_saml_provider
```

## Fields

| Title                     | ID   | Type      | Data Type                                                                       | Description |
| ------------------------- | ---- | --------- | ------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string    |
| account_id                | core | string    |
| assertion_encryption_mode | core | string    | Specifies the encryption setting for the SAML provider.                         |
| create_date               | core | timestamp | The date and time when the SAML provider was created.                           |
| private_key_list          | core | json      | The private key metadata for the SAML provider.                                 |
| saml_metadata_document    | core | string    | The XML metadata document that includes information about an identity provider. |
| saml_provider_uuid        | core | string    | The unique identifier assigned to the SAML provider.                            |
| tags                      | core | hstore    |
| valid_until               | core | timestamp | The expiration date and time for the SAML provider.                             |
