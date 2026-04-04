# Source: https://docs.datadoghq.com/watchdog/faulty_cloud_saas_api_detection.md

---
title: Automatic Faulty Cloud & SaaS API Detection
description: >-
  Detect third-party provider issues within minutes using Watchdog's monitoring
  of external APIs like AWS, Stripe, OpenAI, and other cloud services.
breadcrumbs: Docs > Datadog Watchdogâ¢ > Automatic Faulty Cloud & SaaS API Detection
---

# Automatic Faulty Cloud & SaaS API Detection

{% callout %}
# Important note for users on the following Datadog sites: us3.datadoghq.com, us5.datadoghq.com, app.datadoghq.eu, ap1.datadoghq.com, ap2.datadoghq.com, app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Automatic Faulty Cloud & SaaS API Detection detects third-party providers (payment gateways, cloud providers, and so on) having issues within minutes, reducing mean time to detection (MTTD). Watchdog uses APM telemetry to continuously monitor for elevated error rates in requests to external providersâsuch as AWS, OpenAI, Slack, Stripe, and moreâto detect service degradation as soon as it occurs. This proactive detection gives you a head start in identifying and mitigating issues before they escalate, significantly reducing time spent on root cause analysis and improving response times.

When Watchdog identifies that an external provider you are using is faulty, it flags the services impacted by the problem and the extent of the disruption. This allows you to differentiate between external and internal issues. Datadog also provides direct links to the provider's status page and support channels, so you can reach out to them as needed.

{% image
   source="https://datadog-docs.imgix.net/images/watchdog/external_provider_outage.16efbb27d367b475607b7a0517350ddd.png?auto=format"
   alt="Faulty SaaS API vendor detection" /%}

Whenever Watchdog detects a provider degradation, it creates an event in the [Event Explorer](https://app.datadoghq.com/event/explorer). You can set up a monitor to get automatically notified on such events:

1. Go to the [New Monitor](https://app.datadoghq.com/monitors/create) page.
1. Choose **Watchdog**.
1. Select `Third Party` in the alert category.

## Supported providers{% #supported-providers %}

Watchdog monitors the status of the external providers' APIs listed in the [External Provider Status documentation](https://docs.datadoghq.com/internal_developer_portal/external_provider_status).

## Further Reading{% #further-reading %}

- [Stay ahead of service disruptions with Watchdog Cloud and API Outage Detection](https://www.datadoghq.com/blog/watchdog-outage-detection/)
- [Learn about Watchdog Faulty Service Deployment Detections](https://docs.datadoghq.com/watchdog/faulty_deployment_detection/)
