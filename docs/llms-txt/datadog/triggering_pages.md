# Source: https://docs.datadoghq.com/incident_response/on-call/triggering_pages.md

---
title: Trigger a Page
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Incident Response > On-Call > Trigger a Page
---

# Trigger a Page

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

A Page is sent to a Team and subsequently routed through that Team's escalation policies and schedules. After your Team is [onboarded to Datadog On-Call](https://docs.datadoghq.com/incident_response/on-call/teams), you can start paging it.

### Page from notifications{% #page-from-notifications %}

You can send a Page by mentioning a Team's handle with `oncall-` prepended. For example: to send a Page to the Checkout Operations team (`@checkout-operations`), mention `@oncall-checkout-operations`.

{% image
   source="https://datadog-docs.imgix.net/images/service_management/oncall/notification_page.daa7e914865641789d565bd04bf92a24.png?auto=format"
   alt="Notification that mentions an On-Call Team." /%}

You can send Pages to On-Call Teams wherever @-handles are supported, including monitors, Incident Management, security detection rules, Event Management, and more.

#### Resolving pages automatically{% #resolving-pages-automatically %}

When a monitor recovers, any Page it triggered is automatically set to `Resolved` if the recovery notification includes the On-Call team mention (for example, `@oncall-payments`). If the mention appears only in the alert template (such as within `{{#is_alert}} ... {{/is_alert}}`) and not in the recovery message, the Page does not auto-resolve.

#### Monitors and dynamic urgencies{% #monitors-and-dynamic-urgencies %}

If you send a Page through a monitor alert, and your Team's routing rule uses dynamic urgencies:

- If the WARN threshold is crossed, the Page urgency is set to `low`.
- If the ALERT threshold is crossed, the Page urgency is set to `high`.

### Trigger Pages through emails{% #trigger-pages-through-emails %}

You can generate a unique email address that is used to trigger a Page directly to the team's on-call responders. When an email is sent to this address, it initiates the paging process using your configured routing and escalation policies. For added clarity and ease of use, some customers choose to embed this paging address within a more human-readable distribution list (for example, [page-network@company.com](mailto:page-network@company.com)), which can make life easier in case the email is destined to be used by humans. To page a team through email:

1. Navigate to the on-call team's page and scroll down to "Custom Triggering Sources".
1. Click "Generate" under the email trigger section. This generates a unique email address that can be used to trigger a Page directly to the team's on-call responders.

### Trigger Pages through incidents{% #trigger-pages-through-incidents %}

You can trigger a Page directly from an active incident. This allows you to escalate and bring in responders without leaving the incident workflow. See [Trigger a Page from an incident](https://docs.datadoghq.com/incident_response/incident_management/notification/#trigger-a-page-from-an-incident) for detailed instructions.

### Trigger Pages through calls{% #trigger-pages-through-calls %}

You can trigger a Page through live call routing, which lets users initiate a Page by calling a dedicated phone number. This provides an additional channel for urgent situations. For setup instructions, see [Live Call Routing](https://docs.datadoghq.com/incident_response/on-call/triggering_pages/live_call_routing).

### Page manually{% #page-manually %}

You can manually send a Page directly in the Datadog platform, or through a tool like Slack or Microsoft Teams. This lets you alert a Datadog team or an individual directly (even if they aren't On-Call).

### Reroute Pages{% #reroute-pages %}

You can reroute an active Page to a different user or team if it is still open. You can only reroute Pages that are Triggered or Acknowledged; you cannot reroute Pages that are Resolved.

To reroute a Page:

1. Open the active Page.
1. Click **Reassign**.
1. Choose the user or team you want to send it to.
1. (Optional) Add a short message explaining the handoff.
1. Confirm the reroute.

The new recipient is notified immediately, and the Page continues from its current state.

#### Through Datadog{% #through-datadog %}

1. Go to [**On-Call** > **Teams**](https://app.datadoghq.com/on-call/teams).
1. Find the Team you want to page. Select **Page**.
   {% image
      source="https://datadog-docs.imgix.net/images/service_management/oncall/manual_page.af92d0e564847090f38d22be6bfd35a1.png?auto=format"
      alt="The list of On-Call Teams, showing the Checkout Operations Team. Three buttons are displayed: Schedules, Escalation Policies, Page." /%}
1. Enter a **Page title**. You can also select **Tags** and add more context in the **Description** field. Select **Page**.

Manually paging a Team through Datadog always results in a `high` urgency Page.

#### Through Slack{% #through-slack %}

1. Install the Datadog app
1. Enter `/datadog page` or `/dd page`.
1. Select a Team to send a Page to.

Manually paging a Team from Slack always results in a `high` urgency Page.

To send Pages to Slack, see [Routing Rules](https://docs.datadoghq.com/incident_response/on-call/routing_rules/#send-pages-to-slack-or-microsoft-teams).

## Further Reading{% #further-reading %}

- [Datadog On-Call](https://docs.datadoghq.com/incident_response/on-call/)
