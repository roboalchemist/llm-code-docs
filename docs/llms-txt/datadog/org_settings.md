# Source: https://docs.datadoghq.com/account_management/org_settings.md

---
title: Organization Settings
description: >-
  Manage users, teams, authentication, API keys, roles, and security settings
  for your Datadog organization from the Organization Settings section.
breadcrumbs: Docs > Account Management > Organization Settings
source_url: https://docs.datadoghq.com/org_settings/index.html
---

# Organization Settings

## Overview{% #overview %}

The Organization Settings section is available to [Administrators](https://docs.datadoghq.com/account_management/users/default_roles/) by clicking **Organization Settings** from the account menu in the bottom of the left side navigation or by selecting **Organization Settings** from the header dropdown at the top of the Personal Settings page.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/org_settings/nav.7cc83024673d821b5ff61bd4df489267.png?auto=format"
   alt="Navigate to your Organization Settings in Datadog" /%}

Organization Settings allow you to manage users, groups, RBAC, keys, and tokens. This page outlines every section and where in the documentation you can learn about specific tasks in **Organization Settings**.

## Identity & Accounts{% #identity--accounts %}

### Users{% #users %}

Read the [user management](https://docs.datadoghq.com/account_management/users/) documentation to add, edit, and disable users.

### Teams{% #teams %}

Read the [Teams](https://docs.datadoghq.com/account_management/teams/?s=login%20methods) documentation to manage teams for organizing your assets within Datadog.

### Service accounts{% #service-accounts %}

[Service accounts](https://docs.datadoghq.com/account_management/org_settings/service_accounts) are non-interactive accounts that you can use to own application keys and other resources that are shared across your teams. Service account application keys can only be viewed once by the individual who created the key. You can use service accounts to access Datadog APIs without associating your application or script with a particular person.

## Authentication{% #authentication %}

### Login methods{% #login-methods %}

The **Login Methods** tab shows password, Google, and SAML authentication settings. You can toggle each with the **Enabled by Default** dropdowns. In order to be "SAML Strict" or strict for any other type of login, disable the other login method types. You can allow per-user overrides in the User Management tab to allow users to login with another login method if needed.

Read the [Configuring Login Methods](https://docs.datadoghq.com/account_management/login_methods/) documentation to authenticate users to log into your Datadog organization.

#### SAML settings{% #saml-settings %}

To learn how to configure SAML, read the [Single sign on with SAML documentation](https://docs.datadoghq.com/account_management/saml/).

### SAML group mappings{% #saml-group-mappings %}

When enabled, users logging in with SAML to your Datadog account are permanently stripped of their current roles and reassigned to new roles. The SAML assertion passed on from the Identity Provider and the mappings you create determine each user's new roles.

Users who log in with SAML and do not have values that map to a Datadog role are permanently stripped of all roles. That user may no longer log in. To learn how to create and set mappings, read the [Mapping SAML attributes documentation](https://docs.datadoghq.com/account_management/saml/mapping).

## Access{% #access %}

### API keys{% #api-keys %}

This section allows you to view, copy, and revoke any API key in the list. Your API keys are unique to your organization. An API key is required by the Datadog Agent to submit metrics and events to Datadog. Read the [API keys documentation](https://docs.datadoghq.com/account_management/api-app-keys/) for more information on creating, editing, and revoking keys.

### Application keys{% #application-keys %}

You can filter application keys by name, ID, or owner, or click the **Only My Keys** toggle to only view application keys you own. Read the [Application keys documentation](https://docs.datadoghq.com/account_management/api-app-keys/) for more information on adding and removing keys.

### Roles{% #roles %}

To learn about default and custom roles in Datadog, read the [Role Based Access Control documentation](https://docs.datadoghq.com/account_management/rbac/).

### Remote Configuration{% #remote-configuration %}

To learn how to remotely configure the behavior or Datadog components deployed in your infrastructure, read [How Remote Configuration Works](https://docs.datadoghq.com/remote_configuration#how-it-works).

### Client tokens{% #client-tokens %}

Client tokens are used to send events and logs from your user's web and mobile applications. They are unique to your organization. Deleting a client token that is linked to a RUM Application causes your RUM Application to stop reporting. The [process to create client tokens](https://docs.datadoghq.com/account_management/api-app-keys/#client-tokens) is similar to that for API and application keys.

### Events API emails{% #events-api-emails %}

If your application does not have an existing Datadog integration, and you don't want to create a custom Agent check, you can send events with email. To learn how to set up events API emails, read the [Events with email guide](https://docs.datadoghq.com/events/guides/email/).

### Synthetic tests{% #synthetic-tests %}

Learn how to access and control [Synthetic Monitoring Settings](https://docs.datadoghq.com/synthetics/settings/?tab=specifyvalue#overview).

## Security{% #security %}

### Safety Center{% #safety-center %}

The [**Safety Center**](https://docs.datadoghq.com/account_management/safety_center) page contains security alerts, warnings, and recommendations to review in your organization.

### Public sharing{% #public-sharing %}

The **Public Sharing** tab includes org-wide settings for sharing, along with lists of shared dashboards and graphs. You can enable sharing features granularly and configure additional security options, such as setting a maximum invite duration.

To apply sharing settings across all your orgs, reach out to [Datadog Support](https://docs.datadoghq.com/help/).

**Note**: OrgAdmin permission is required to view and manage sharing settings and resources.

### OAuth Apps{% #oauth-apps %}

The [**OAuth Apps**](https://docs.datadoghq.com/account_management/org_settings/oauth_apps) page allows you to view or manage OAuth applications in your organization.

## Compliance{% #compliance %}

### Audit trail{% #audit-trail %}

The **Audit Trail** tab in the Organization Settings page opens a new tab to the Audit Events Explorer.

### Audit trail settings{% #audit-trail-settings %}

The **Audit Trail Settings** tab allows you to set the retention period of audit trails and enable archiving to other cloud storage services.

## General{% #general %}

### Preferences{% #preferences %}

#### Organization name{% #organization-name %}

To rename your organization, click the **Edit** button in the **Preferences** tab of **Organization Settings**, enter the new name, then click the **Save** button.

**Note**: Your organization name must not exceed 32 characters.

#### Datadog homepage{% #datadog-homepage %}

You can choose to set your organization homepage to a Dashboard List or an individual dashboard.

#### Out-of-contract retention periods for log indexes{% #out-of-contract-retention-periods-for-log-indexes %}

Users with `Org Management` permission can enable the out-of-contract retention periods feature for log indexes. This feature is enabled on a per-org basis. This means that if a user enables the feature on a parent org, the feature is not automatically enabled for all child orgs.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/out-of-contract-retention.fd17b6c318e5d8e135082e22c5f085cc.png?auto=format"
   alt="The out-of-contract retention periods for log indexes setting showing enabled." /%}

When enabled, users with `Modify Index` permission can choose any of the 3-, 7-, 15-, 30-, 45-, and 60-day retention periods, even if it is not in the contract. This can be useful when troubleshooting a potential long standing issue or meeting compliance requirements for which customers need a higher retention period that is not part of the current contract.

**Note**: Using out-of-contract retention periods incur on-demand charges. If an out-of-contract retention period is often used, Datadog recommends that customers contact their account manager to have it added to their contract.

#### Max session duration configuration{% #max-session-duration-configuration %}

Users with the `Org Management` permission can set a maximum session duration for their organization. The duration applies to all new web sessions created after you change it, for all users, regardless of their role in the organization. It doesn't apply to Datadog mobile application sessions.

The session duration can be configured within the following limits:

- **Minimum duration:** 1 hour
- **Maximum duration:**

{% image
   source="https://datadog-docs.imgix.net/images/account_management/org_settings/max_session_duration.a9c220a750dab62f23cecf3bb6f255fb.png?auto=format"
   alt="Max Session Duration Setting" /%}

#### Idle time session duration configuration{% #idle-time-session-duration-configuration %}

{% alert level="info" %}
This feature is available in preview.
{% /alert %}

Users with the `Org Management` permission can enable or disable the idle time session timeout for their organization. When enabled, users are automatically signed out after 30 minutes of inactivity. The setting applies to all new web sessions created after you change it, and for all users, regardless of their role in the organization. It doesn't apply to Datadog mobile application sessions.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/org_settings/idle_session_timeout.2372b892ae5d1abf9a55916f392f25b8.png?auto=format"
   alt="Idle Session Timeout Setting" /%}

## Further reading{% #further-reading %}

- [API and application keys](https://docs.datadoghq.com/account_management/api-app-keys/)
- [User management](https://docs.datadoghq.com/account_management/users/)
