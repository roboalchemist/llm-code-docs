# Source: https://docs.datadoghq.com/incident_response/on-call.md

---
title: On-Call
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > On-Call
source_url: https://docs.datadoghq.com/on-call/index.html
---

# On-Call

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

Datadog On-Call integrates monitoring, paging, and incident response into one platform.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/oncall_overview.7cf5ebef4d88d615b086b22f2c600240.png?auto=format"
   alt="Overview of how Pages are routed. From a monitor, incident, security signal, or API call, the Page is sent to a Team (e.g. 'payments-team'), then to routing rules (e.g. based on priority) then to an escalation policy. There, it can be sent to a schedule or directly to a user." /%}

## Concepts{% #concepts %}

- **Pages** represent something to get alerted for, such as a monitor, incident, or security signal. A Page can have a status of `Triggered`, `Acknowledged`, or `Resolved`.
- **Teams** are groups configured within Datadog to handle specific types of Pages, based on expertise and operational roles.
- **Routing rules** allow Teams to finely adjust their reactions to specific types of incoming events. These rules can set a Page's urgency level and route Pages to different escalation policies depending on the event's metadata.
- **Escalation policies** determine how Pages are escalated within or across Teams.
- **Schedules** set timetables for when specific Team members are on-call to respond to Pages.

## How it works{% #how-it-works %}

**Teams** are the central organizational unit of Datadog On-Call. When a notification is triggered in Datadog, a **Page** is sent to the designated On-Call Team.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/notification_page.daa7e914865641789d565bd04bf92a24.png?auto=format"
   alt="Notification that mentions an On-Call Team." /%}

Each Team owns **escalation policies** and **schedules**. Escalation policies define how a Page is sent to various schedules, such as *Checkout Operations - Interrupt Handler*, *Primary*, and *Secondary* in the following screenshot. Each Team can also configure **routing rules** to route Pages to different escalation policies.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/escalation_policy.5d70f1584c132885a006cd06846f6822.png?auto=format"
   alt="A sample escalation policy." /%}

A schedule defines specific times when Team members are assigned to respond to Pages. Schedules organize and manage the availability of Team members across different time zones and shifts.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/schedule.6ff0867246f7a17b4d4deb7e3245ea07.png?auto=format"
   alt="A sample schedule, with multiple layers for JP, EU, and US business hours." /%}

## Granular access control{% #granular-access-control %}

Use [granular access controls](https://docs.datadoghq.com/account_management/rbac/granular_access/) to limit the [roles](https://docs.datadoghq.com/account_management/rbac/#role-based-access-control), teams, or users that can access On-Call resources. By default, access to On-Call schedules, escalation policies, and team routing rules is unrestricted.

Granular access controls are available for the following On-Call resources:

- **Schedules**: Control who can view, edit, and override schedules
- **Escalation policies**: Control who can view and edit escalation policies
- **Team routing rules**: Control who can view and edit team routing rules

### Supported resources and permissions{% #supported-resources-and-permissions %}

| On-Call resource        | Viewer                       | Overrider                              | Editor                                        |
| ----------------------- | ---------------------------- | -------------------------------------- | --------------------------------------------- |
| **Schedules**           | Can view schedules           | Can view schedules and override shifts | Can view, edit schedules, and override shifts |
| **Escalation policies** | Can view escalation policies | -                                      | Can view and edit escalation policies         |
| **Team routing rules**  | Can view team rules          | -                                      | Can view and edit team rules                  |

### Restrict access to On-Call resources{% #restrict-access-to-on-call-resources %}

To restrict access to an On-Call resource:

1. Navigate to the specific On-Call resource (schedule, escalation policy, or team routing rules).
1. Click **Manage**.
1. Select **Permissions** from the dropdown menu.
1. Click **Restrict Access**.
1. Select one or more roles, teams, or users from the dropdown menu.
1. Click **Add**.
1. Select the level of access you want to associate with each of them from the dropdown menu next to their name:
   - **Viewer**: Read-only access to view the resource
   - **Overrider** (schedules only): Can view and create schedule overrides
   - **Editor**: Full access to view and modify the resource
1. Click **Save**.

**Note**: To maintain your edit access to the resource, Datadog requires you to include at least one role that you are a member of before saving.

## Start using Datadog On-Call{% #start-using-datadog-on-call %}

{% alert level="danger" %}
To preserve incident history, Datadog On-Call does not support deletion of resources like Pages, escalation policies, or schedules. To test On-Call without affecting your production environment, create a trial organization as a sandbox.
{% /alert %}

To get started with On-Call, [onboard an On-Call Team](https://docs.datadoghq.com/incident_response/on-call/teams) and ensure that all Team members configure their [On-Call profile settings](https://docs.datadoghq.com/incident_response/on-call/profile_settings) to receive notifications.

- [Onboard a Team: Create a new On-Call Team, add an existing Datadog Team to On-Call, or import a team from PagerDuty.](https://docs.datadoghq.com/incident_response/on-call/teams)
- [Trigger a Page: Page a team through monitors, incidents, security signals, etc.; or manually send a Page through Datadog, Slack, Microsoft Teams, or the Datadog API.](https://docs.datadoghq.com/incident_response/on-call/triggering_pages)
- [Escalation Policies: Define steps for how a Page is sent to different schedules.](https://docs.datadoghq.com/incident_response/on-call/escalation_policies)
- [Schedules: Define timetables for Team members' on-call rotations.](https://docs.datadoghq.com/incident_response/on-call/schedules)
- [Profile Settings: Configure your contact methods and notification preferences to ensure you receive timely and effective Pages.](https://docs.datadoghq.com/incident_response/on-call/profile_settings)

## Billing{% #billing %}

On-Call is a seat-based SKU. To learn more about how On-Call is billed and how to manage seats within Datadog, visit our [pricing page](https://www.datadoghq.com/pricing/?product=incident-response#products) and the [Incident Response billing documentation](https://docs.datadoghq.com/account_management/billing/incident_response/).

## Further Reading{% #further-reading %}

- [Enrich your on-call experience by using Datadog On-Call](https://www.datadoghq.com/blog/datadog-on-call/)
- [How to create an effective paging strategy](https://www.datadoghq.com/blog/on-call-paging/)
- [Unify remediation and communication with Datadog Incident Response](https://www.datadoghq.com/blog/incidents-ai-workbench-status-page/)
