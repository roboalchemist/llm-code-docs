# Source: https://docs.datadoghq.com/datadog_cloudcraft/overlays.md

---
title: Overlays
description: >-
  Use Cloudcraft overlays to view your infrastructure from different
  perspectives including observability, security, cost management, and
  infrastructure.
breadcrumbs: Docs > Cloudcraft in Datadog > Overlays
---

# Overlays

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

Cloudcraft supports overlays that integrate data from multiple sources, enriching your diagrams with real-time insights. These views let you group and filter resources by key attributes, helping you focus on different parts of your architecture for troubleshooting, cost optimization, or security analysis. Each overlay is designed to address a specific operational goal, making it easy to adapt the diagram to your needs.

## Available overlays{% #available-overlays %}

Cloudcraft provides the following built-in overlays:

- [Infrastructure](https://docs.datadoghq.com/datadog_cloudcraft/overlays/infrastructure/): View resources grouped by Account, Region, and VPC for architecture diagrams and troubleshooting.
- [Observability](https://docs.datadoghq.com/datadog_cloudcraft/overlays/observability/): See where the Datadog Agent is installed and which features are enabled per host.
- [Security](https://docs.datadoghq.com/datadog_cloudcraft/overlays/security/): Identify security exposures, misconfigurations, and vulnerabilities in your architecture.
- [Cloud Cost Management (CCM)](https://docs.datadoghq.com/datadog_cloudcraft/overlays/ccm/): Discover savings opportunities with cost recommendations shown directly on resources.

## Further reading{% #further-reading %}

- [Plan new architectures and track your cloud footprint with Cloudcraft (Standalone)](https://www.datadoghq.com/blog/cloud-architecture-diagrams-cost-compliance-cloudcraft-datadog/)
- [Visually identify observability gaps with Cloudcraft in Datadog](https://www.datadoghq.com/blog/cloudcraft-observability-overlay/)
