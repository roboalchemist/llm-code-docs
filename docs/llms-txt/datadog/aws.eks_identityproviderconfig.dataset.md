# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eks_identityproviderconfig.dataset.md

---
title: EKS Identity Provider Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EKS Identity Provider Config
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.eks_identityproviderconfig.dataset/index.html
---

# EKS Identity Provider Config

This table represents the EKS Identity Provider Config resource from Amazon Web Services.

```
aws.eks_identityproviderconfig
```

## Fields

| Title                         | ID   | Type   | Data Type                                                                                                                                                                                                                                                                                              | Description |
| ----------------------------- | ---- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                          | core | string |
| account_id                    | core | string |
| client_id                     | core | string | This is also known as <i>audience</i>. The ID of the client application that makes authentication requests to the OIDC identity provider.                                                                                                                                                              |
| cluster_name                  | core | string | The name of your cluster.                                                                                                                                                                                                                                                                              |
| groups_claim                  | core | string | The JSON web token (JWT) claim that the provider uses to return your groups.                                                                                                                                                                                                                           |
| groups_prefix                 | core | string | The prefix that is prepended to group claims to prevent clashes with existing names (such as <code>system:</code> groups). For example, the value<code> oidc:</code> creates group names like <code>oidc:engineering</code> and <code>oidc:infra</code>. The prefix can't contain <code>system:</code> |
| identity_provider_config_arn  | core | string | The ARN of the configuration.                                                                                                                                                                                                                                                                          |
| identity_provider_config_name | core | string | The name of the configuration.                                                                                                                                                                                                                                                                         |
| issuer_url                    | core | string | The URL of the OIDC identity provider that allows the API server to discover public signing keys for verifying tokens.                                                                                                                                                                                 |
| required_claims               | core | hstore | The key-value pairs that describe required claims in the identity token. If set, each claim is verified to be present in the token with a matching value.                                                                                                                                              |
| status                        | core | string | The status of the OIDC identity provider.                                                                                                                                                                                                                                                              |
| tags                          | core | hstore |
| username_claim                | core | string | The JSON Web token (JWT) claim that is used as the username.                                                                                                                                                                                                                                           |
| username_prefix               | core | string | The prefix that is prepended to username claims to prevent clashes with existing names. The prefix can't contain <code>system:</code>                                                                                                                                                                  |
