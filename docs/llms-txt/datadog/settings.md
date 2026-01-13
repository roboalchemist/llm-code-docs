# Source: https://docs.datadoghq.com/incident_response/case_management/settings.md

---
title: Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Case Management > Settings
source_url: https://docs.datadoghq.com/case_management/settings/index.html
---

# Settings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

In Project Settings, you can manage access control, configure automatic status transitions, set up third-party integrations like Jira and ServiceNow, and more.

## Granular Access Control{% #granular-access-control %}

By default, access to projects and cases is unrestricted. [Granular Access Control](https://docs.datadoghq.com/account_management/rbac/granular_access) can be used to manage the permissions of users, teams, roles, or your full organization at the project level. There are four sets of permissions that can be used:

- **Manager**: Users can create and edit cases, views, settings, and permissions of the project, and can delete the project.
- **Contributor**: Users can create, comment on, and edit cases. They can't change settings, permissions, or the project.
- **Viewer**: Users can view and watch all cases, views, and settings of the project. They can't create, edit, or comment on cases.
- **No Access**: Users can't view any cases, views, or settings of the project.

**Note:** Other Datadog products that integrate with Case Management, such as Monitors, are able to automatically create cases within a project regardless of the project's access settings.

## Status transitions{% #status-transitions %}

To reduce noise, configure cases to automatically close after 7, 14, 30, 90, or 180 days of inactivity from the status transitions page of project settings. Inactivity is defined as the absence of human-initiated action, such as updating an attribute or writing a comment. Once a day, Datadog checks for cases that are inactive for at least the selected period and closes them out.

## Set up integrations{% #set-up-integrations %}

Case Management offers a range of native and third-party integrations, so you can incorporate Datadog solutions into your existing workflows and processes. With the Jira and ServiceNow integrations, you can solve the case with full-stack telemetry in Datadog, while maintaining a record of the investigation in those third-party systems.

### Monitors{% #monitors %}

Navigate to the [Project Settings page](https://app.datadoghq.com/cases/settings), click **Integrations** > **Datadog Monitors**, and click on the toggle to get your @case-<project_handle>.

Project handles can be used in monitors to automatically create cases. In the monitor message body, include `@case-<project_handle>`. Datadog suggests a handle based on the project's name. You can accept or modify it as you wish.

### Third party integrations{% #third-party-integrations %}

To configure third party integrations, navigate to [Create notifications and tickets ](https://docs.datadoghq.com/incident_response/case_management/create_notifications_and_third_party_tickets).

## Custom case types and attributes{% #custom-case-types-and-attributes %}

Add custom case types and attributes to projects so that you can tailor your cases to fit your organizational needs. For more information, see [Case Customization](https://docs.datadoghq.com/incident_response/case_management/customization).

## Further Reading{% #further-reading %}

- [Troubleshooting third-party integrations](https://docs.datadoghq.com/incident_response/case_management/troubleshooting)
- [Case Customization](https://docs.datadoghq.com/incident_response/case_management/customization)
