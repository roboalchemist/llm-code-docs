# Source: https://docs.datadoghq.com/events/triage_inbox.md

---
title: Event Management Triage Inbox
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Event Management > Event Management Triage Inbox
---

# Event Management Triage Inbox

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Datadog Event Management [Triage Inbox](https://app.datadoghq.com/event/correlation) simplifies incident response by consolidating related events from any source into actionable cases. This centralized view reduces noise and helps teams triage, investigate, and collaborate more effectively. With customizable saved views, you can stay focused on high-priority cases and review correlated alerts, related changes, and telemetry, all in one place.

## Triaging and investigating cases{% #triaging-and-investigating-cases %}

Case triage and investigation begins in the Triage Inbox, where you can sort, filter, and manage incoming cases. Collaborate with teammates, both within and outside of Datadog, to coordinate responses. From there, you can prioritize, assign, investigate, and escalate cases as needed to drive faster resolution.

{% video
   url="https://datadog-docs.imgix.net/images//service_management/events/triage_inbox/event_mgmt_inbox.mp4" /%}

## Getting Started{% #getting-started %}

1. Navigate to [**Event Management** > **Triage Inbox**](https://app.datadoghq.com/event/correlation).
1. Select a project from the left-hand panel to display out-of-the-box status views such as **Open**, **In Progress**, **Closed**, and **Archived**.
1. Use the display settings icon to choose between **split view** (for detailed case investigation) or **table view** (for bulk case review and column configuration). Customize your inbox ranking with the **Sort By** dropdown-options include **Priority**, **Created at**, or **Last Updated**. Click **Save** to re-use your customized inbox for future use.
1. Update the status, priority, and assignment directly on case cards during triage.
1. Maximize screen space by collapsing the left-hand case project panel and the Datadog navigation bar.
1. Hover over the case card **alert** count to preview correlated alerts.

## Next Steps{% #next-steps %}

Now that you've learned how to triage and investigate cases, use these tools to collaborate with your team, take action on root causes, and streamline response efforts.

## Collaborate and Integrate{% #collaborate-and-integrate %}

On the right hand split-view side panel, you can perform the following:

- **Tag and comment**: Collaborate with teammates in the case timeline by tagging users and adding notes.

- **Send notifications**: Alert stakeholders with Slack, Microsoft Teams, email, or webhooks.

- **Escalate issues**: Trigger an incident or page an on-call responder using [Incident Management](https://docs.datadoghq.com/incident_response/incident_management/), [On-Call](https://docs.datadoghq.com/incident_response/on-call/), [Workflow Automation](https://docs.datadoghq.com/actions/workflows/), or third-party tools.

- **Sync with external tools**: Keep Jira and ServiceNow records in sync to ensure external stakeholders stay up to date.

  {% image
     source="https://datadog-docs.imgix.net/images/service_management/events/triage_inbox/event_mgmt_inbox_right_hand_panel.b5ae1c2de9fd9b93dd90a5966bace2ba.png?auto=format"
     alt="Event Management Inbox right hand panel, highlighting Escalate drop down" /%}

## Take Action{% #take-action %}

- **Mark root cause**: Identify and mark a related event, such as a faulty change, as the root cause.
- **Run workflows**: Execute remediation runbooks manually or trigger them conditionally with [Case Automation Rules](https://docs.datadoghq.com/incident_response/case_management/automation_rules/).
- **Merge cases**: Combine related cases to streamline investigations.
- **Split cases**: Separate alerts that require individual investigation.

**Note**: When all alerts in a case are resolved, the system automatically closes the case. You can also manually mark a case as resolved.

## Further Reading{% #further-reading %}

- [Send events to Datadog](https://docs.datadoghq.com/events/ingest/)
- [Learn more about event correlation](https://docs.datadoghq.com/events/correlation/)
- [Aggregate, correlate, and act on alerts faster with AIOps-powered Event Management](https://www.datadoghq.com/blog/datadog-event-management/)
