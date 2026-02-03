# Source: https://docs.datadoghq.com/account_management/org_settings/oauth_apps.md

---
title: OAuth Apps
description: >-
  Manage and monitor OAuth applications in your organization, including
  permissions, user access, and application status controls.
breadcrumbs: Docs > Account Management > OAuth Apps
---

# OAuth Apps

## Overview{% #overview %}

Use the **OAuth Apps** management page under [Organization Settings](https://app.datadoghq.com/organization-settings/) to manage and gain visibility into your organization's OAuth applications, such as the scopes and permissions granted to an application and the users that have authorized access for it.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/oauth_apps/org-management-page.f310df7c5cf76906ef251e477ccf5697.png?auto=format"
   alt="OAuth Apps management page in Datadog" /%}

## Setup{% #setup %}

### Permissions{% #permissions %}

By default, users with the [Datadog Admin role](https://docs.datadoghq.com/account_management/rbac/permissions/#general-permissions) can access the OAuth Apps management page. If your organization has [custom roles](https://docs.datadoghq.com/account_management/rbac/?tab=datadogapplication#custom-role) defined, add your user to any custom role with the `org_management` permission.

Only users with the Datadog Admin role or the `org_management` permission can manage OAuth applications on this page, such as disabling applications or revoking OAuth access for a user.

### Enable{% #enable %}

Enabled OAuth applications allow users with necessary permissions to authorize access on their behalf. OAuth applications include the Datadog Mobile App.

### Disable{% #disable %}

Disabling OAuth access for an application revokes access to this application for all users in your organization. While the application remains installed, users are no longer able to use the application and are prompted with an error if they attempt to authorize it.

There are two ways to disable an application from the OAuth Apps management page:

1. Hover over your application in the apps table to reveal the **Disable** button on the right side of the row.

   {% image
      source="https://datadog-docs.imgix.net/images/account_management/oauth_apps/disable-app-table.234fa16d0ea4d026d7040c1e6da50e58.png?auto=format"
      alt="Disable button in apps table" /%}



1. Click on your application to open the detailed view of the application and click the **Disable Application** button.

   {% image
      source="https://datadog-docs.imgix.net/images/account_management/oauth_apps/disable-app-detailed.e3824b606f27cd2d35c0ca8a86be6e14.png?auto=format"
      alt="Disable button in app's detailed view" /%}

**Note**: When re-enabled, users that previously authorized the application are required to re-authorize the application to regain access.

### Revoke access{% #revoke-access %}

Revoking a user's OAuth access to an application removes all access to that application. If the user has the required permissions to authorize the application, they can regain access by re-authorizing it.

{% image
   source="https://datadog-docs.imgix.net/images/account_management/oauth_apps/revoke-user.518089b8df98fe76d0736df4841c3f78.png?auto=format"
   alt="Disable button in apps detailed view" /%}



## Further Reading{% #further-reading %}

- [Learn more about organization settings](https://docs.datadoghq.com/account_management/org_settings/)
