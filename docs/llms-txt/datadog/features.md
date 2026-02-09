# Source: https://docs.datadoghq.com/continuous_delivery/features.md

# Source: https://docs.datadoghq.com/cloudprem/introduction/features.md

---
title: Supported Features
description: Learn which Datadog Log Explorer features are supported in CloudPrem
breadcrumbs: Docs > CloudPrem > Introduction to CloudPrem > Supported Features
---

# Supported Features

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### CloudPrem is in Preview

Join the CloudPrem Preview to access new self-hosted log management features.

[Request Access](https://www.datadoghq.com/product-preview/cloudprem/)
{% /callout %}

## Overview{% #overview %}

Datadog CloudPrem brings core Log Explorer capabilities to your self-hosted environment. This page outlines available features, notes any differences from the SaaS platform, and helps you plan your log workflows.

## Supported features{% #supported-features %}

The following log features are already supported:

- Full text search on any log attributes
- List, Timeseries, Top List, Table, Tree Map, Pie Chart, Scatter Plot visualizations
- Group by into Fields and Patterns (except the monthly timeshift)
- Dashboards
- Log monitors
- RBAC through [Log Restriction Queries](https://docs.datadoghq.com/api/latest/logs-restriction-queries/)
- Download CSV
- Correlation from a log to metrics sent to Datadog SaaS (the reverse is not yet supported)
- Correlation from a log to traces sent to Datadog SaaS (the reverse is not yet supported)

## Unsupported features{% #unsupported-features %}

Feature support is actively evolving. The following are not currently supported:

- Bits AI SRE
- Index management for multiple retention periods and segmentation needs
- Notebooks
- Federated search
- LiveTail
- Watchdogs
