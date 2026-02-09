# Source: https://docs.datadoghq.com/bits_ai/chat_with_bits_ai.md

---
title: Chat with Bits AI
description: >-
  Chat with Bits AI in Datadog and Slack to query observability data using
  natural language and get insights about your services.
breadcrumbs: Docs > Bits AI > Chat with Bits AI
---

# Chat with Bits AI

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

Chat with Bits AI is in preview. Please reach out to your account manager if you have questions.
{% /callout %}

## Chat in Datadog{% #chat-in-datadog %}

Bits AI supports natural language querying for logs, APM traces, infrastructure data, cloud cost, and RUM. You can also ask Bits AI about the health and ownership of your services, and retrieve Datadog resources related to those services.

You can ask Bits AI questions such as:

- `Who is on call for example-service?`
- `Find me the example-service dashboard.`
- `What is going on with example-service?`
- `Are there any issues with example-service's dependencies?`

When relevant to your query, Bits AI surfaces faulty deployments, Watchdog anomalies, incidents, alerts, and more. It also expands on issues with upstream and downstream dependencies. This feature works best if your APM services are tagged by **team** and **service**.

### In the chat panel{% #in-the-chat-panel %}

To open the chat panel in the app, click **Bits AI** at the bottom-left corner of the navigation menu, or use `Cmd + /` to show or hide the chat panel.

Some responses from Bits AI include a **suggestions** button. Clicking it displays additional queries that apply to the conversation's context.

{% image
   source="https://datadog-docs.imgix.net/images/bits_ai/getting_started/chat_panel_star_service.fdaa99c17b51cc20b50d4b15a26e335a.png?auto=format"
   alt="Bits AI chat panel with example question of 'How do I star a service' and Bits AI's answer" /%}

### On the mobile app{% #on-the-mobile-app %}

{% image
   source="https://datadog-docs.imgix.net/images/bits_ai/getting_started/bitsai_mobile_app.9f1538361d9bd8f3c271bdc3a443abbb.PNG?auto=format"
   alt="View of the Mobile App Home dashboard with Bits AI" /%}

Click Bits AI on the mobile app to access the same querying features available on the browser.

## Querying in Slack{% #querying-in-slack %}

1. [Connect your Datadog account to your Slack workspace](https://docs.datadoghq.com/integrations/slack/?tab=applicationforslack).
1. In Slack, use the `/dd connect` command to display a list of accounts to connect to.
1. Choose the name of your Datadog account in the dropdown.
1. Authorize additional permissions needed by Bits AI.

After setup is completed, you can send queries to `@Datadog` in natural language: `@Datadog Are there any issues with example-service's dependencies?`

{% image
   source="https://datadog-docs.imgix.net/images/bits_ai/getting_started/example-slack-query.2325c54273ed695c8e22e1e972cdda0f.png?auto=format"
   alt="Output of an example service-dependency query in Slack" /%}

## Further reading{% #further-reading %}

- [Bits AI Overview](https://docs.datadoghq.com/bits_ai/)
- [Coordinate incidents with Incident AI](https://docs.datadoghq.com/incident_response/incident_management/incident_ai)
