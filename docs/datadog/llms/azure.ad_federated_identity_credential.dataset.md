# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.ad_federated_identity_credential.dataset.md

---
title: Active Directory Federated Identity Credential
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Active Directory Federated Identity
  Credential
---

# Active Directory Federated Identity Credential

This table represents the Active Directory Federated Identity Credential resource from Microsoft Azure.

```
azure.ad_federated_identity_credential
```

## Fields

| Title             | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| ----------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string        |
| audiences         | core | array<string> | The audience that can appear in the external token. This field is mandatory and should be set to api://AzureADTokenExchange for Microsoft Entra ID. It says what Microsoft identity platform should accept in the aud claim in the incoming token. This value represents Microsoft Entra ID in your external identity provider and has no fixed value across identity providers - you might need to create a new application registration in your identity provider to serve as the audience of this token. This field can only accept a single value and has a limit of 600 characters. Required. |
| description       | core | string        | The unvalidated description of the federated identity credential, provided by the user. It has a limit of 600 characters. Optional.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| id                | core | string        | The unique identifier for an entity. Read-only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| issuer            | core | string        | The URL of the external identity provider, which must match the issuer claim of the external token being exchanged. The combination of the values of issuer and subject must be unique within the app. It has a limit of 600 characters. Required.                                                                                                                                                                                                                                                                                                                                                 |
| location          | core | string        |
| name              | core | string        | The unique identifier for the federated identity credential, which has a limit of 120 characters and must be URL friendly. The string is immutable after it's created. Alternate key. Required. Not nullable. Supports $filter (eq).                                                                                                                                                                                                                                                                                                                                                               |
| resource_group    | core | string        |
| subject           | core | string        | Required. The identifier of the external software workload within the external identity provider. Like the audience value, it has no fixed format; each identity provider uses their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes arbitrary strings. The value here must match the sub claim within the token presented to Microsoft Entra ID. The combination of issuer and subject must be unique within the app. It has a limit of 600 characters. Supports $filter (eq).                                                                                          |
| subscription_id   | core | string        |
| subscription_name | core | string        |
| tags              | core | hstore_csv    |
