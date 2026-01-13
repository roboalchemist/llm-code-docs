# Source: https://docs.datadoghq.com/account_management/safety_center.md

---
title: Safety Center
description: >-
  Review security alerts, configuration warnings, and user management best
  practices from Datadog's centralized Safety Center.
breadcrumbs: Docs > Account Management > Safety Center
source_url: https://docs.datadoghq.com/safety_center/index.html
---

# Safety Center

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Datadog's Safety Center in **Organization Settings** is a centralized location for security alerts and best practices. [Administrators](https://docs.datadoghq.com/account_management/rbac/#datadog-default-roles) of an organization can open this page to review recommendations and take action on high priority security warnings and alerts.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/safety_center/overview.148bca341b38b90418571f5ab6908e68.png?auto=format"
   alt="Safety Center Overview page" /%}

## Security Alerts{% #security-alerts %}

If your organization has a high priority security alert, it appears in the **Security Alerts** section of **Safety Center**. Safety Center supports two types of alerts: leaked [application keys](https://docs.datadoghq.com/account_management/api-app-keys/#application-keys) and leaked [API keys](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys).

A leaked key alert means that one or more private keys (application or API) have been compromised or publicly exposed on the internet. Exposed keys have to be [revoked](https://docs.datadoghq.com/account_management/api-app-keys/#what-to-do-if-an-api-or-application-key-was-exposed) as soon as possible to minimize security risks to your organization. Removing the file containing the key from a public site such as GitHub **does not** guarantee it was not already accessed by another party.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/safety_center/revoke-leaked-api-key.66cfc440ffdd6c6e18d365cae52a8bbc.png?auto=format"
   alt="Revoking leaked API key" /%}

## Configuration{% #configuration %}

The **Configuration** tab in **Safety Center** allows setting **Security Contacts** - primary and secondary email addresses to receive security notifications for your Datadog organization. Upon detecting security issues, like publicly exposed Datadog keys needing [rotation](https://docs.datadoghq.com/account_management/api-app-keys/#what-to-do-if-an-api-or-application-key-was-exposed), your assigned **Security Contacts** gets notified.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/safety_center/set-security-contacts.e9f40d0c651621a91612afaafac38f0f.png?auto=format"
   alt="Setting Security Contacts" /%}

It is important to keep **Security Contacts** up to date to ensure that potential security risks are promptly addressed and mitigated. The **Safety Center** page reminds you to review assigned **Security Contacts** every 6 months.

## Access & Sharing{% #access--sharing %}

The **Access & Sharing** section in **Safety Center** lists entities that allow external access to your Datadog organization. It highlights:

- [**OAuth applications**](https://docs.datadoghq.com/account_management/org_settings/oauth_apps) that have been inactive for 60+ days or have write access and have been inactive for 30+ days.
- [**API keys**](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys) that have been unused for 30+ days.

### OAuth Apps{% #oauth-apps %}

Inactive **OAuth applications** can pose a potential security risk to your organization if compromised. They should be reviewed regularly and those applications that are no longer in use should be disabled.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/safety_center/disable-unused-oauth-app.c4194b8633f17a55c7ca68cede78fc50.png?auto=format"
   alt="Disabling unused OAuth app" /%}

### API Keys{% #api-keys %}

Unused **API keys** can facilitate unauthorized access to your organization if they become exposed on the internet. Unused keys need to be reviewed and revoked if your organization's infrastructure does not rely on them.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/safety_center/revoke-unused-api-key.2ef66e1b0a80a6edf9970a8517d91e54.png?auto=format"
   alt="Revoking unused API key" /%}

## Users{% #users %}

In order to keep your organization safe it is important to follow best practices for user management. The **Users** page in **Safety Center** surfaces user-related security recommendations:

- [User invites](https://docs.datadoghq.com/account_management/users/#add-new-members-and-manage-invites) that have not been accepted for 30+ days.
- [Admin users](https://docs.datadoghq.com/account_management/rbac/#datadog-default-roles) in the event their number exceeds 10% of all users within an organization.

### Pending Invites{% #pending-invites %}

Having inactive user accounts or **stale pending user invites** increases the surface for a potential account takeover attack. That can be especially dangerous if inactive user accounts have high-privilege access. To keep the number of inactive users to a minimum consider either resending **old pending invites** or deleting them if those users do not need access to the Datadog platform.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/safety_center/resend-pending-invite.324ea3f1b26cd2544917eadc488c2a8d.png?auto=format"
   alt="Resending pending invite" /%}

{% image
   source="https://datadog-docs.imgix.net/images/account_management/safety_center/delete-pending-invite.2b500deb88d80eb6747e08f057bf5a2f.png?auto=format"
   alt="Deleting pending invite" /%}

### Admins{% #admins %}

Giving **admin access** to users without careful consideration increases potential security risks in the event where a user account with elevated privileges gets compromised. To keep the number of users with **admin access** low, review your admin users regularly and revoke admin privileges if users do not require them.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/safety_center/edit-admin-user.6cd7a00ce551ea499df09b0cad5f8890.png?auto=format"
   alt="Editing admin user" /%}

## Further reading{% #further-reading %}

- [API and application keys](https://docs.datadoghq.com/account_management/api-app-keys/)
- [User management](https://docs.datadoghq.com/account_management/users/)
- [OAuth Apps](https://docs.datadoghq.com/account_management/org_settings/oauth_apps)
