# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.identitytoolkit_tenant.dataset.md

---
title: Identity Platform Tenant
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Identity Platform Tenant
---

# Identity Platform Tenant

Identity Platform Tenant in Google Cloud is an isolated identity and authentication environment that allows you to manage users, authentication methods, and security settings separately from other tenants. It is useful for multi-tenant applications where each customer or organization requires its own identity store and configuration.

```gdscript3
gcp.identitytoolkit_tenant
```

## Fields

| Title                      | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                          | Description |
| -------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                       | core | string        |
| allow_password_signup      | core | bool          | Whether to allow email/password user authentication.                                                                                                                                                                                                                                                                                                               |
| ancestors                  | core | array<string> |
| autodelete_anonymous_users | core | bool          | Whether anonymous users will be auto-deleted after a period of 30 days.                                                                                                                                                                                                                                                                                            |
| client                     | core | json          | Options related to how clients making requests on behalf of a project should be configured.                                                                                                                                                                                                                                                                        |
| datadog_display_name       | core | string        |
| disable_auth               | core | bool          | Whether authentication is disabled for the tenant. If true, the users under the disabled tenant are not allowed to sign-in. Admins of the disabled tenant are not able to manage its users.                                                                                                                                                                        |
| email_privacy_config       | core | json          | Configuration for settings related to email privacy and public visibility.                                                                                                                                                                                                                                                                                         |
| enable_anonymous_user      | core | bool          | Whether to enable anonymous user authentication.                                                                                                                                                                                                                                                                                                                   |
| enable_email_link_signin   | core | bool          | Whether to enable email link user authentication.                                                                                                                                                                                                                                                                                                                  |
| gcp_display_name           | core | string        | Display name of the tenant.                                                                                                                                                                                                                                                                                                                                        |
| hash_config                | core | json          | Output only. Hash config information of a tenant for display on Pantheon. This can only be displayed on Pantheon to avoid the sensitive information to get accidentally leaked. Only returned in GetTenant response to restrict reading of this information. Requires firebaseauth.configs.getHashConfig permission on the agent project for returning this field. |
| inheritance                | core | json          | Specify the settings that the tenant could inherit.                                                                                                                                                                                                                                                                                                                |
| labels                     | core | array<string> |
| mfa_config                 | core | json          | The tenant-level configuration of MFA options.                                                                                                                                                                                                                                                                                                                     |
| mobile_links_config        | core | json          | Optional. Deprecated. Never launched. Configuration for settings related to univeral links (iOS) and app links (Android).                                                                                                                                                                                                                                          |
| monitoring                 | core | json          | Configuration related to monitoring project activity.                                                                                                                                                                                                                                                                                                              |
| name                       | core | string        | Output only. Resource name of a tenant. For example: "projects/{project-id}/tenants/{tenant-id}"                                                                                                                                                                                                                                                                   |
| organization_id            | core | string        |
| parent                     | core | string        |
| password_policy_config     | core | json          | The tenant-level password policy config                                                                                                                                                                                                                                                                                                                            |
| project_id                 | core | string        |
| project_number             | core | string        |
| recaptcha_config           | core | json          | The tenant-level reCAPTCHA config.                                                                                                                                                                                                                                                                                                                                 |
| region_id                  | core | string        |
| resource_name              | core | string        |
| sms_region_config          | core | json          | Configures which regions are enabled for SMS verification code sending.                                                                                                                                                                                                                                                                                            |
| tags                       | core | hstore_csv    |
| zone_id                    | core | string        |
