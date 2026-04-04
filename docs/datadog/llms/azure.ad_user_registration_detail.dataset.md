# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.ad_user_registration_detail.dataset.md

---
title: Active Directory User Registration Detail
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Active Directory User Registration
  Detail
---

# Active Directory User Registration Detail

This table represents the Active Directory User Registration Detail resource from Microsoft Azure.

```
azure.ad_user_registration_detail
```

## Fields

| Title                                              | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                      | Description |
| -------------------------------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                                               | core | string        |
| id                                                 | core | string        | The unique identifier for an entity. Read-only.                                                                                                                                                                                                                                                                                                                |
| is_admin                                           | core | bool          | Indicates whether the user has an admin role in the tenant. This value can be used to check the authentication methods that privileged accounts are registered for and capable of.                                                                                                                                                                             |
| is_mfa_capable                                     | core | bool          | Indicates whether the user has registered a strong authentication method for multifactor authentication. The method must be allowed by the authentication methods policy. Supports $filter (eq).                                                                                                                                                               |
| is_mfa_registered                                  | core | bool          | Indicates whether the user has registered a strong authentication method for multifactor authentication. The method may not necessarily be allowed by the authentication methods policy. Supports $filter (eq).                                                                                                                                                |
| is_passwordless_capable                            | core | bool          | Indicates whether the user has registered a passwordless strong authentication method (including FIDO2, Windows Hello for Business, and Microsoft Authenticator (Passwordless)) that is allowed by the authentication methods policy. Supports $filter (eq).                                                                                                   |
| is_sspr_capable                                    | core | bool          | Indicates whether the user has registered the required number of authentication methods for self-service password reset and the user is allowed to perform self-service password reset by policy. Supports $filter (eq).                                                                                                                                       |
| is_sspr_enabled                                    | core | bool          | Indicates whether the user is allowed to perform self-service password reset by policy. The user may not necessarily have registered the required number of authentication methods for self-service password reset. Supports $filter (eq).                                                                                                                     |
| is_sspr_registered                                 | core | bool          | Indicates whether the user has registered the required number of authentication methods for self-service password reset. The user may not necessarily be allowed to perform self-service password reset by policy. Supports $filter (eq).                                                                                                                      |
| is_system_preferred_authentication_method_enabled  | core | bool          | Indicates whether system preferred authentication method is enabled. If enabled, the system dynamically determines the most secure authentication method among the methods registered by the user. Supports $filter (eq).                                                                                                                                      |
| last_updated_date_time                             | core | string        | The date and time (UTC) when the report was last updated. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.                                                                                                                      |
| location                                           | core | string        |
| methods_registered                                 | core | array<string> | Collection of authentication methods registered, such as mobilePhone, email, passKeyDeviceBound. Supports $filter (any with eq).                                                                                                                                                                                                                               |
| name                                               | core | string        |
| resource_group                                     | core | string        |
| subscription_id                                    | core | string        |
| subscription_name                                  | core | string        |
| system_preferred_authentication_methods            | core | array<string> | Collection of authentication methods that the system determined to be the most secure authentication methods among the registered methods for second factor authentication. Possible values are: push, oath, voiceMobile, voiceAlternateMobile, voiceOffice, sms, none, unknownFutureValue. Supports $filter (any with eq).                                    |
| tags                                               | core | hstore_csv    |
| user_display_name                                  | core | string        | The user display name, such as Adele Vance. Supports $filter (eq, startsWith) and $orderby.                                                                                                                                                                                                                                                                    |
| user_preferred_method_for_secondary_authentication | core | string        | The method the user selected as the default second-factor for performing multifactor authentication. Possible values are: push, oath, voiceMobile, voiceAlternateMobile, voiceOffice, sms, none, unknownFutureValue. This property is used as preferred MFA method when isSystemPreferredAuthenticationMethodEnabled is false. Supports $filter (any with eq). |
| user_principal_name                                | core | string        | The user principal name, such as AdeleV@contoso.com. Supports $filter (eq, startsWith) and $orderby.                                                                                                                                                                                                                                                           |
| user_type                                          | core | string        | Identifies whether the user is a member or guest in the tenant. The possible values are: member, guest, unknownFutureValue.                                                                                                                                                                                                                                    |
