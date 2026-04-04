# Source: https://docs.datadoghq.com/datadog_cloudcraft/overlays/observability.md

---
title: Observability
description: >-
  Use the Observability overlay in Cloudcraft to see where the Datadog Agent is
  installed and which features are enabled per host.
breadcrumbs: Docs > Cloudcraft in Datadog > Overlays > Observability
---

# Observability

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Overview{% #overview %}

The Observability overlay shows where the Datadog Agent is installed and what features are enabled per host, such as Application Performance Monitoring (APM), Cloud Network Monitoring (CNM), Log Management, and more. This helps you to assess visibility gaps across your environment.

## Take action on resources{% #take-action-on-resources %}

On the Observability overlay, you can take action on individual resources or groups of resources:

- Click a single host to open a side panel with direct links to Fleet Automation, where you can deploy configurations or upgrade the Agent.
- Click a resource group, such as a subnet or VPC, to open a side panel that allows you to apply bulk updates across all the hosts in that resource group.
- To select multiple (but not all) hosts, hold down the `Command` key on Mac or the `Control` key on Windows while clicking on each host.

{% video
   url="https://datadog-docs.imgix.net/images/datadog_cloudcraft/observability_overlay_with_fleet_2.mp4" /%}

## View Datadog coverage{% #view-datadog-coverage %}

In the bottom left legend, the **View Datadog coverage by** dropdown allows you to inspect the installation status for specific features. Each row shows:

- Feature name (for example, APM, Logs, CNM)
- Numerical coverage: X / Y (for example, 16/35), where:
  - X is the number of resources with that feature enabled
  - Y is the total number of relevant resources in the current view or filter

### Legend{% #legend %}

| Pin Color | Description                                                    |
| --------- | -------------------------------------------------------------- |
| Green     | Agent and feature are both enabled                             |
| Gray      | Feature is not enabled                                         |
| Yellow    | Agent is installed but needs an upgrade to enable all features |

### Tracked features{% #tracked-features %}

The observability overlay tracks coverage for the following products:

| Feature           | Description                                                |
| ----------------- | ---------------------------------------------------------- |
| Agent version     | Verifies if the Datadog Agent is installed and its version |
| APM               | Application Performance Monitoring (traces collected)      |
| CNM               | Cloud Network Monitoring coverage                          |
| Logs              | Log Management collection status                           |
| CWS               | Cloud Workload Protection coverage                         |
| CSPM              | Cloud Security Misconfigurations coverage                  |
| Process           | Process monitoring enabled                                 |
| CSM VM Hosts      | Coverage of Cloud Security Vulnerabilities on hosts        |
| CSM VM Containers | Coverage of Cloud Security Vulnerabilities on containers   |
| USM               | Coverage of Universal Service Monitoring                   |

## Further reading{% #further-reading %}

- [Infrastructure overlay](https://docs.datadoghq.com/datadog_cloudcraft/overlays/infrastructure/)
- [Security overlay](https://docs.datadoghq.com/datadog_cloudcraft/overlays/security/)
- [Cloud Cost Management overlay](https://docs.datadoghq.com/datadog_cloudcraft/overlays/ccm/)
- [Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/)
