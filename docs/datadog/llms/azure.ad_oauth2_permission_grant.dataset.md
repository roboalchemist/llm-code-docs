# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.ad_oauth2_permission_grant.dataset.md

---
title: Active Directory OAuth2 Permission Grant
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Active Directory OAuth2 Permission
  Grant
---

# Active Directory OAuth2 Permission Grant

This table represents the Active Directory OAuth2 Permission Grant resource from Microsoft Azure.

```
azure.ad_oauth2_permission_grant
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| ----------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| client_id         | core | string     | The object id (not appId) of the client service principal for the application that's authorized to act on behalf of a signed-in user when accessing an API. Required. Supports $filter (eq only).                                                                                                                                                                                                                                                                                  |
| consent_type      | core | string     | Indicates if authorization is granted for the client application to impersonate all users or only a specific user. AllPrincipals indicates authorization to impersonate all users. Principal indicates authorization to impersonate a specific user. Consent on behalf of all users can be granted by an administrator. Nonadmin users might be authorized to consent on behalf of themselves in some cases, for some delegated permissions. Required. Supports $filter (eq only). |
| id                | core | string     | The unique identifier for an entity. Read-only.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| location          | core | string     |
| name              | core | string     |
| principal_id      | core | string     | The id of the user on behalf of whom the client is authorized to access the resource, when consentType is Principal. If consentType is AllPrincipals this value is null. Required when consentType is Principal. Supports $filter (eq only).                                                                                                                                                                                                                                       |
| resource_group    | core | string     |
| resource_id       | core | string     | The id of the resource service principal to which access is authorized. This identifies the API that the client is authorized to attempt to call on behalf of a signed-in user. Supports $filter (eq only).                                                                                                                                                                                                                                                                        |
| scope             | core | string     | A space-separated list of the claim values for delegated permissions that should be included in access tokens for the resource application (the API). For example, openid User.Read GroupMember.Read.All. Each claim value should match the value field of one of the delegated permissions defined by the API, listed in the oauth2PermissionScopes property of the resource service principal. Must not exceed 3,850 characters in length.                                       |
| subscription_id   | core | string     |
| subscription_name | core | string     |
| tags              | core | hstore_csv |
