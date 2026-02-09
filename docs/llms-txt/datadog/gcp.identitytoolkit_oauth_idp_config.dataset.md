# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.identitytoolkit_oauth_idp_config.dataset.md

---
title: Identity Platform OAuth IdP Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Identity Platform OAuth IdP Config
---

# Identity Platform OAuth IdP Config

Identity Platform OAuth IdP Config in Google Cloud is a configuration resource that defines how an external OAuth identity provider integrates with Identity Platform. It specifies details such as client IDs, client secrets, and authorization endpoints, enabling users to sign in using third-party providers like Google, Facebook, or GitHub. This resource helps manage authentication flows and user identity federation securely.

```gdscript3
gcp.identitytoolkit_oauth_idp_config
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                            | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| client_id            | core | string        | The client id of an OAuth client.                                                                                                                                                                                                    |
| client_secret        | core | string        | The client secret of the OAuth client, to enable OIDC code flow.                                                                                                                                                                     |
| datadog_display_name | core | string        |
| enabled              | core | bool          | True if allows the user to sign in with the provider.                                                                                                                                                                                |
| gcp_display_name     | core | string        | The config's display name set by developers.                                                                                                                                                                                         |
| issuer               | core | string        | For OIDC Idps, the issuer identifier.                                                                                                                                                                                                |
| labels               | core | array<string> |
| name                 | core | string        | The name of the OAuthIdpConfig resource, for example: 'projects/my-awesome-project/oauthIdpConfigs/oauth-config-id'. Ignored during create requests.                                                                                 |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| response_type        | core | json          | The response type to request for in the OAuth authorization flow. You can set either `id_token` or `code` to true, but not both. Setting both types to be simultaneously true (`{code: true, id_token: true}`) is not yet supported. |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
