# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_open_id_connect_provider.dataset.md

---
title: IAM OpenID Connect Identity Provider
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM OpenID Connect Identity Provider
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iam_open_id_connect_provider.dataset/index.html
---

# IAM OpenID Connect Identity Provider

IAM OpenID Connect Identity Provider in AWS is a resource that lets you establish trust between your AWS account and an external identity provider that supports OpenID Connect. This allows users from the external provider to assume IAM roles in your AWS account without needing separate AWS credentials, enabling secure federated authentication for workloads and applications.

```
aws.iam_open_id_connect_provider
```

## Fields

| Title           | ID   | Type          | Data Type                                                                                                                                                                       | Description |
| --------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key            | core | string        |
| account_id      | core | string        |
| client_id_list  | core | array<string> | A list of client IDs (also known as audiences) that are associated with the specified IAM OIDC provider resource object. For more information, see CreateOpenIDConnectProvider. |
| create_date     | core | timestamp     | The date and time when the IAM OIDC provider resource object was created in the Amazon Web Services account.                                                                    |
| tags            | core | hstore        |
| thumbprint_list | core | array<string> | A list of certificate thumbprints that are associated with the specified IAM OIDC provider resource object. For more information, see CreateOpenIDConnectProvider.              |
| url             | core | string        | The URL that the IAM OIDC provider resource object is associated with. For more information, see CreateOpenIDConnectProvider.                                                   |
