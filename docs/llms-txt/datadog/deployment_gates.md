# Source: https://docs.datadoghq.com/deployment_gates.md

---
title: Deployment Gates
description: >-
  Reduce deployment incidents by automatically evaluating monitors and APM
  anomalies to halt releases when performance regressions are detected.
breadcrumbs: Docs > Deployment Gates
source_url: https://docs.datadoghq.com/index.html
---

# Deployment Gates

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
Deployment Gates are not available for the selected site ().
{% /alert %}


{% /callout %}

{% callout %}
##### Join the Preview!

Deployment Gates are in Preview. If you're interested in this feature, complete the form to request access.

[Request Access](http://datadoghq.com/product-preview/deployment-gates)
{% /callout %}

Deployment Gates allow you to reduce the likelihood and impact of incidents caused by deployments.

When performing a production rollout, you can use Deployment Gates to evaluate the impact of the new changes by using [monitors](https://docs.datadoghq.com/monitors/) and APM anomalies. When anomalies or performance regressions are detected, you can automatically halt the release, preventing unstable code from reaching a wider user base. Additionally, you can then use Deployment Gates as the entry-point to investigate the problem.

For setup instructions, see [Set up Deployment Gates](https://docs.datadoghq.com/deployment_gates/setup). After the setup is completed, you can track and analyze gate evaluations through the [Deployment Gates Evaluations](https://docs.datadoghq.com/deployment_gates/explore) page:

{% image
   source="https://datadog-docs.imgix.net/images/deployment_gates/explore/deployment_gates_explorer.5ba87fde3a5435208268b2a1d360f435.png?auto=format"
   alt="" /%}

## Further reading{% #further-reading %}

- [Set up Deployment Gates](https://docs.datadoghq.com/deployment_gates/setup)
- [Learn about the Deployment Gates explorer](https://docs.datadoghq.com/deployment_gates/explore)
- [Learn about Continuous Delivery Visibility](https://docs.datadoghq.com/continuous_delivery)
- [Learn how to set up CD Visibility](https://docs.datadoghq.com/continuous_delivery/deployments)
