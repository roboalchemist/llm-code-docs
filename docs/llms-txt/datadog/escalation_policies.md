# Source: https://docs.datadoghq.com/incident_response/on-call/escalation_policies.md

---
title: Escalation Policies
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Incident Response > On-Call > Escalation Policies
---

# Escalation Policies

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

In Datadog On-Call, escalation policies ensure that Pages are promptly addressed. Pages are escalated through predefined steps, unless acknowledged within set timeframes.

Datadog creates a default escalation policy when you [onboard a Team to On-Call](https://docs.datadoghq.com/incident_response/on-call/teams).

## Create a new escalation policy{% #create-a-new-escalation-policy %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/escalation_policy_2.caea299acaa29891e653a43b7d5e4eee.png?auto=format"
   alt="A sample escalation policy." /%}

1. Go to [**On-Call** > **Escalation Policies**](https://app.datadoghq.com/on-call/escalation-policies).
1. Select [**+ New Escalation Policy**](https://app.datadoghq.com/on-call/escalation-policies/create).
1. Enter a **Name** for your escalation policy. For example, *Payment's Escalation Policy*.
1. Select the **Teams** that own this escalation policy.
1. For each escalation step: 1. Decide who should be notified. You can specify individual users, teams, or whoever is on-call in a schedule. 1. Select one of the following notification methods: `Notify All`, `Round Robin`. See Escalation policy notification types for details. 1. Specify how many minutes the recipient has to acknowledge the page before it is escalated to the next tier. For example, the following will notify the current on-call user when a page is triggered. It will escalate to Jane Doe if John does not acknowledge the page within 5 minutes.
   {% image
      source="https://datadog-docs.imgix.net/images/service_management/oncall/escalation_policy_2_steps_v2.4e0c35c3e12501492c381c4b0dc055a4.png?auto=format"
      alt="An escalation policy configured to notify the scheduled on-call user and escalate to Jane Doe if the page is not acknowledged after 5 minutes." /%}
1. Set how many times to repeat the steps if no one acknowledges the page.
1. Select whether Datadog should automatically update the page status to **Resolved** after executing all rules and repeats.

## Escalation policy step notification types{% #escalation-policy-step-notification-types %}

In each step of an escalation policy, you can keep the standard `Notify All` behavior or opt-in for `Round Robin`.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/escalation_policy_notification_type.a299dfba43666d3ca538ed39526ed587.png?auto=format"
   alt="Notification type selector in Escalation Policy creation" /%}



### Notify all (default){% #notify-all-default %}

Notify all targets of the step at the same time.

For example, if a step includes an individual user, a team with three members, and a schedule, then five people will be notified: the individual user, each of the three team members, and the on-call user from the schedule.

### Round robin{% #round-robin %}

Automatically distribute pages across multiple targets (users, schedules, teams) in a rotating order to ensure fair load balancing.

For example, if you have a 50-person support team, you can break up the team into five 10-person schedules and set up the following policy to evenly distribute load:

- Page A â Support Schedule Group 1
- Page B â Support Schedule Group 2
- Page C â Support Schedule Group 3
- Page D â Support Schedule Group 4
- Page E â Support Schedule Group 5
- Page F â Support Schedule Group 1
- Page G â Support Schedule Group 2

#### Escalation behavior{% #escalation-behavior %}

In round robin mode, if a page isn't acknowledged in time, it doesn't move to the next person in the round robin rotation. Instead, it escalates to the next step in the policy.

If you want the page to go to the next target in the round robin, use only one round robin step in your escalation policy and configure it to repeat at least as many times as there are targets.

## Escalation policy step targets{% #escalation-policy-step-targets %}

In each step of an escalation policy, you can notify individual users, entire teams, or whoever is on-call in a schedule.

### Schedules{% #schedules %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/escalation_policy_notify_schedule.2963629d053a4188d10c37f7520f5b42.png?auto=format"
   alt="A sample escalation policy step that notifies a schedule." /%}

Escalation policies can notify whoever is on-call according to a predefined schedule. The system checks the schedule and notifies the person or group that is actively on-call during the incident. Using schedules is beneficial for:

- Routing alerts to on-call responders across different time zones for 24/7 coverage.
- Handling tiered support, where different shifts handle different levels of urgency.
- Dynamic notifications for teams with rotating on-call responsibilities, ensuring the right person is always paged.

If no one is on-call for a given schedule, the escalation step gracefully skips and the process moves forward without delays or interruptions. The UI indicates a skipped escalation.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/escalation_policy_schedule_skipped.e75a96bccf81b6c28a8eaa2d3f30a677.png?auto=format"
   alt="A sample escalation policy indicating a skipped escalation due to no one being on call." /%}

### Users{% #users %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/escalation_policy_notify_user.a4c9f2e185fb3c905a0bea2a0f8fa238.png?auto=format"
   alt="A sample escalation policy that specifies a user in the escalation policy." /%}

You can include specific users in an escalation policy to ensure key individuals are always notified in the event of a Page. Common use cases for directly paging a user are:

- Notifying a senior engineer for high-severity incidents requiring specialized knowledge.
- Alerting a product manager or director in case of customer-facing incidents.
- Routing alerts to a backup responder if the primary contact is unavailable.

### Teams{% #teams %}

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/escalation_policy_notify_team.7fb2687cf9019723a67c053b4ff77692.png?auto=format"
   alt="A sample escalation policy that notifies an entire Team." /%}

Common use cases for paging an entire Team are:

- Incidents affecting multiple systems where various team members may contribute to the solution.
- Escalating to a DevOps team for infrastructure-related incidents.
- Ensuring that all relevant members of an engineering or security team are alerted for critical outages.

## Limitations{% #limitations %}

- Maximum escalation steps: 10
- Maximum number of notify targets (individuals, teams, or schedules) per escalation step: 10
- Minimum time before escalation to the next step: one minute
