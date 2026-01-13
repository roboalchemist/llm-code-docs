# Source: https://docs.datadoghq.com/incident_response/case_management/create_case.md

---
title: Create a Case
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Case Management > Create a Case
source_url: https://docs.datadoghq.com/case_management/create_case/index.html
---

# Create a Case

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Cases can be created manually, automatically from across Datadog, or programmatically with the API. There are two types of cases: standard and security. Cases created from security signals and Sensitive Data Scanner are automatically made security cases. The security case type has all the features of the standard case type, along with a mandatory field for specifying the reason for closing a case (testing, false positive, or one time exception).

## Manual case creation{% #manual-case-creation %}

1. Navigate to the [Case Management page](https://app.datadoghq.com/cases).
1. Select a project to create the case in. **Note**: A case can only belong to a single project.
1. Click **New Case**.
1. Fill in a title for the case.
1. Select a case type.
1. Add a title.
1. (Optional) Add a description.
1. Click **Create Case** to complete.

You can also create cases manually from the following products:

| Product                       | Instructions                                                                                                                                                                                                                                                                                  |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Monitors                      | - On a [monitor status page](https://docs.datadoghq.com/monitors/status/), optionally scope the monitor to a time frame and specific monitor group(s). Then, click the **Actions** dropdown menu and select **Create a case**.- In Slack, click **Create case** under a monitor notification. |
| Security signals              | Click into a Security Signal to open up the side panel. Click **Escalate Investigation** and select **Create a case**.                                                                                                                                                                        |
| Error Tracking                | Click into an Error Tracking issue to open the side panel. Then, click **Actions** and select **Create a case**.                                                                                                                                                                              |
| Watchdog                      | Click into an alert to open its side panel. Click the **Actions** dropdown menu and select **Create a case**.                                                                                                                                                                                 |
| Event Management (raw events) | Click into an event to open its side panel. Click the **Actions** dropdown menu and select **Create a case**.                                                                                                                                                                                 |
| Cloud Cost Management         | Click into a cost recommendation to open its side panel. Then, click **Create case**.                                                                                                                                                                                                         |
| Sensitive Data Scanner        | Click **Create case** next to a Sensitive Data Scanner issue.                                                                                                                                                                                                                                 |
| Slack                         | Click the **Create Case** button under a monitor notification in Slack.                                                                                                                                                                                                                       |

## Automatic case creation{% #automatic-case-creation %}

Configure the following products to automatically create cases:

| Product                         | Instructions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Monitors                        | Navigate to the [Project Settings page](https://app.datadoghq.com/cases/settings), click **Integrations** > **Datadog Monitors**, and click on the toggle to get your @case-<project_handle>.When creating a monitor, include `@case-{project_handle}` in the **Configure notifications and automations** section. Cases are automatically created when the monitor transitions to a different status. To only create cases for certain monitor transitions, use [conditional variables](https://docs.datadoghq.com/monitors/notify/variables/?tab=is_alert#conditional-variables). As an example, to create cases only when a monitor triggers, wrap the `@case` mention with `{{#is_alert}}` and `{{/is_alert}}`.Toggle on **Auto-close cases when the monitor group resolves** to reduce manual cleanup. |
| Event Management (Correlations) | In Event Management, correlations configured to aggregate events from Datadog and third-party sources automatically create cases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Workflow Automation             | 1. In a new or existing workflow, add a step in the Workflow builder and search for "Case Management."2. Select the **Create Case** action.3. If the workflow is configured to run based on a monitor or security signal trigger, add the relevant workflow triggers and ensure that you've added the workflow handle to the desired resources. For more information, see [Trigger a workflow](https://docs.datadoghq.com/service_management/workflows/trigger/).                                                                                                                                                                                                                                                                                                                                           |
| Error Tracking                  | In Error Tracking, cases are automatically created when an issue is commented on or assigned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Case types{% #case-types %}

Add case types when you are creating a case. Not all case types are available for configuration between manual and automativ creation. For example, only `Standard`, `Security` and `Change Request`, `Event Management` types are available when creating cases manually.

To add and enable custom case types, see [Case Customization](https://docs.datadoghq.com/incident_response/case_management/customization).

| Case Type        | Description                                                                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard         | A general-purpose case for operational tasks, investigations, and more.                                                                             |
| Change Request   | Used in change management workflows to track planned or approved changes.                                                                           |
| Event Management | Integrated with the Event Management product to house correlated events.                                                                            |
| Security         | Used by security teams and products to manage investigations or alerts.                                                                             |
| Error Tracking   | Linked to the Error Tracking product to track and remediate application issues.                                                                     |
| Custom Type      | Add a custom case type. For more information, see [Case Customization](https://docs.datadoghq.com/incident_response/case_management/customization). |

## API{% #api %}

Create a case through the [API endpoint](https://docs.datadoghq.com/api/latest/case-management/#create-a-case).

**Note**: This endpoint requires the `cases_write` authorization scope.

## Further Reading{% #further-reading %}

- [View and Manage Cases](https://docs.datadoghq.com/incident_response/case_management/view_and_manage)
- [Case Customization](https://docs.datadoghq.com/incident_response/case_management/customization)
