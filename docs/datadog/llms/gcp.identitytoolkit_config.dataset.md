# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.identitytoolkit_config.dataset.md

---
title: Identity Platform Config
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Identity Platform Config
---

# Identity Platform Config

Identity Platform Config in Google Cloud is a configuration resource that manages authentication settings for applications using Identity Platform. It defines how users sign in, which identity providers are supported, and how authentication flows are handled. This resource helps control user management, security policies, and integration with external identity systems.

```gdscript3
gcp.identitytoolkit_config
```

## Fields

| Title                      | ID   | Type          | Data Type                                                                                                                                       | Description |
| -------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string        |
| ancestors                  | core | array<string> |
| authorized_domains         | core | array<string> | List of domains authorized for OAuth redirects                                                                                                  |
| autodelete_anonymous_users | core | bool          | Whether anonymous users will be auto-deleted after a period of 30 days.                                                                         |
| blocking_functions         | core | json          | Configuration related to blocking functions.                                                                                                    |
| client                     | core | json          | Options related to how clients making requests on behalf of a project should be configured.                                                     |
| datadog_display_name       | core | string        |
| default_hosting_site       | core | string        | Output only. Default Firebase hosting site name                                                                                                 |
| email_privacy_config       | core | json          | Configuration for settings related to email privacy and public visibility.                                                                      |
| labels                     | core | array<string> |
| mfa                        | core | json          | Configuration for this project's multi-factor authentication, including whether it is active and what factors can be used for the second factor |
| mobile_links_config        | core | json          | Configuration for settings related to univeral links (iOS) and app links (Android).                                                             |
| monitoring                 | core | json          | Configuration related to monitoring project activity.                                                                                           |
| multi_tenant               | core | json          | Configuration related to multi-tenant functionality.                                                                                            |
| name                       | core | string        | Output only. The name of the Config resource. Example: "projects/my-awesome-project/config"                                                     |
| notification               | core | json          | Configuration related to sending notifications to users.                                                                                        |
| organization_id            | core | string        |
| parent                     | core | string        |
| password_policy_config     | core | json          | The project level password policy configuration.                                                                                                |
| project_id                 | core | string        |
| project_number             | core | string        |
| quota                      | core | json          | Configuration related to quotas.                                                                                                                |
| recaptcha_config           | core | json          | The project-level reCAPTCHA config.                                                                                                             |
| region_id                  | core | string        |
| resource_name              | core | string        |
| sign_in                    | core | json          | Configuration related to local sign in methods.                                                                                                 |
| sms_region_config          | core | json          | Configures which regions are enabled for SMS verification code sending.                                                                         |
| subtype                    | core | string        | Output only. The subtype of this config.                                                                                                        |
| tags                       | core | hstore_csv    |
| zone_id                    | core | string        |
