# Source: https://docs.datadoghq.com/error_tracking/guides/enable_infra.md

---
title: Enable Infrastructure Monitoring
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Error Tracking > Error Tracking Guides > Enable Infrastructure
  Monitoring
---

# Enable Infrastructure Monitoring

[Infrastructure monitoring](https://docs.datadoghq.com/infrastructure) includes core Datadog features that visualize, monitor, and measure the performance of your hosts, containers, and processes. This guide explains how to update the Datadog Agent configuration to enable infrastructure monitoring and leverage its features on top of standalone backend error tracking.

{% tab title="Linux host or VM" %}
If your agent is deployed on a Linux host, the configuration update depends on the method you used to install the agent.

{% collapsible-section %}
##### Single Step Instrumentation

For a Datadog agent installed using the one-line installation command:

1. Open the [datadog.yaml configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files).

1. Remove the `enable_payloads` top-level attribute:

   ```diff
   - enable_payloads:
   -   series: false
   -   events: false
   -   service_checks: false
   -   sketches: false
   
     apm_config:
       enabled: true
       error_tracking_standalone:
         enabled: true
   ```

1. [Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent).

{% /collapsible-section %}

{% collapsible-section %}
##### Using Datadog tracing libraries

For a Datadog agent configured manually for Backend Error Tracking:

1. Open the [datadog.yaml configuration file](https://docs.datadoghq.com/agent/configuration/agent-configuration-files).

1. Remove the `core_agent` top-level attribute:

   ```diff
   - core_agent:
   -   enabled: false
     apm_config:
       error_tracking_standalone:
         enabled: true
   ```

1. [Restart the Agent](https://docs.datadoghq.com/agent/configuration/agent-commands/#restart-the-agent).

{% /collapsible-section %}

{% /tab %}

{% tab title="Kubernetes" %}
If your agent is deployed in Kubernetes, you need to update its configuration in Datadog Operator or Helm depending on the method you used to install the agent.

{% collapsible-section %}
##### Helm

For a Datadog agent installed with Helm:

1. Update your `datadog-values.yaml` file, replacing the `site` and `env` values appropriately:

   ```diff
     agents:
       containers:
         agent:
           env:
             [...]
   -         - name: DD_CORE_AGENT_ENABLED
   -           value: "false"
     datadog:
   -   processAgent:
   -     enabled: false
   -     containerCollection: false
     apiKeyExistingSecret: datadog-secret
     site: <DATADOG_SITE>
     tags:
       - env:<AGENT_ENV>
     apm:
       errorTrackingStandalone:
         enabled: true
       # Required to enable Single-Step Instrumentation
       instrumentation:
         enabled: true
         libVersions:
           java: "1"
           dotnet: "3"
           python: "2"
           js: "5"
           php: "1"
   ```

1. After making your changes, upgrade your Datadog Helm chart:

   ```shell
   helm upgrade -f datadog-values.yaml datadog-agent datadog/datadog
   ```

{% /collapsible-section %}

{% collapsible-section %}
##### Datadog Operator

For a Datadog agent installed with the Datadog Operator:

1. Update your `datadog-agent.yaml` file, replacing the `site` and `env` values appropriately:
   ```diff
     apiVersion: datadoghq.com/v2alpha1
     kind: DatadogAgent
     metadata:
       name: datadog
     spec:
       global:
         site: <DATADOG_SITE>
         tags:
           - env:<AGENT_ENV>
         credentials:
           apiSecret:
             secretName: datadog-secret
             keyName: api-key
         env:
   -       - name: DD_CORE_AGENT_ENABLED
   -         value: "false"
       features:
         apm:
           errorTrackingStandalone:
             enabled: true
           instrumentation:
             enabled: true
             libVersions:
               java: "1"
               dotnet: "3"
               python: "2"
               js: "5"
               php: "1"
   ```
1. Deploy the Datadog Agent with the updated configuration file:
   ```shell
   kubectl apply -f path/to/your/datadog-agent.yaml
   ```

{% /collapsible-section %}

{% /tab %}
