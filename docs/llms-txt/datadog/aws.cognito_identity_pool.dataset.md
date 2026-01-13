# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cognito_identity_pool.dataset.md

---
title: Cognito Identity Pools
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cognito Identity Pools
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.cognito_identity_pool.dataset/index.html
---

# Cognito Identity Pools

This table represents the Cognito Identity Pools resource from Amazon Web Services.

```
aws.cognito_identity_pool
```

## Fields

| Title                            | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                       | Description |
| -------------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string        |
| account_id                       | core | string        |
| allow_classic_flow               | core | bool          | Enables or disables the Basic (Classic) authentication flow. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html">Identity Pools (Federated Identities) Authentication Flow</a> in the <i>Amazon Cognito Developer Guide</i>. |
| allow_unauthenticated_identities | core | bool          | TRUE if the identity pool supports unauthenticated logins.                                                                                                                                                                                                                                      |
| cognito_identity_providers       | core | json          | A list representing an Amazon Cognito user pool and its client ID.                                                                                                                                                                                                                              |
| developer_provider_name          | core | string        | The "domain" by which Cognito will refer to your users.                                                                                                                                                                                                                                         |
| identity_pool_arn                | core | string        |
| identity_pool_id                 | core | string        | An identity pool ID in the format REGION:GUID.                                                                                                                                                                                                                                                  |
| identity_pool_name               | core | string        | A string that you provide.                                                                                                                                                                                                                                                                      |
| identity_pool_tags               | core | hstore        | The tags that are assigned to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.                                                                              |
| open_id_connect_provider_arns    | core | array<string> | The ARNs of the OpenID Connect providers.                                                                                                                                                                                                                                                       |
| role_mappings                    | core | string        | How users for a specific identity provider are to mapped to roles. This is a String-to-<a>RoleMapping</a> object map. The string identifies the identity provider, for example, "graph.facebook.com" or "cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id".                |
| roles                            | core | hstore        | The map of roles associated with this pool. Currently only authenticated and unauthenticated roles are supported.                                                                                                                                                                               |
| saml_provider_arns               | core | array<string> | An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.                                                                                                                                                                                                           |
| supported_login_providers        | core | hstore        | Optional key:value pairs mapping provider names to provider app IDs.                                                                                                                                                                                                                            |
| tags                             | core | hstore        |
