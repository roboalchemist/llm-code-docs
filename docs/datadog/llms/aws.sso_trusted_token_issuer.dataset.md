# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sso_trusted_token_issuer.dataset.md

---
title: Trusted Token Issuer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Trusted Token Issuer
---

# Trusted Token Issuer

Trusted Token Issuer in AWS SSO is a resource that represents an external identity provider trusted by AWS IAM Identity Center (formerly AWS SSO) to issue tokens for authentication. It allows integration with third-party identity providers so that users can access AWS accounts and applications using their existing credentials.

```
aws.sso_trusted_token_issuer
```

## Fields

| Title                              | ID   | Type       | Data Type                                                                       | Description |
| ---------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string     |
| account_id                         | core | string     |
| name                               | core | string     | The name of the trusted token issuer configuration.                             |
| tags                               | core | hstore_csv |
| trusted_token_issuer_arn           | core | string     | The ARN of the trusted token issuer configuration.                              |
| trusted_token_issuer_configuration | core | json       | A structure the describes the settings that apply of this trusted token issuer. |
| trusted_token_issuer_type          | core | string     | The type of the trusted token issuer.                                           |
