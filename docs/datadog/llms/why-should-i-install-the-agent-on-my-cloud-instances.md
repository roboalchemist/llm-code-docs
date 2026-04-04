# Source: https://docs.datadoghq.com/agent/guide/why-should-i-install-the-agent-on-my-cloud-instances.md

---
title: Why should I install the Datadog Agent on my cloud instances?
description: >-
  Explains the benefits of installing the Datadog Agent on cloud instances,
  including better resolution, more metrics, integrations, and custom monitoring
  capabilities.
breadcrumbs: >-
  Docs > Agent > Agent Guides > Why should I install the Datadog Agent on my
  cloud instances?
---

# Why should I install the Datadog Agent on my cloud instances?

The Datadog Agent is software that runs on your hosts. It collects events and metrics from hosts and sends them to Datadog, where you can analyze your monitoring and performance data. The Datadog Agent is open source and its source code is available on GitHub at [DataDog/datadog-agent](https://github.com/DataDog/datadog-agent).

If you use AWS, Azure, Google Cloud, or another cloud-based metrics provider, installing the Datadog Agent on your instances gives you several benefits, for example:

- **Better resolution** - Cloud providers monitor your hosts externally by sampling them every 5-25 minutes. Additionally, AWS provides metrics on a per-minute basis through their API. As Datadog stores all metrics at a 1-second resolution, AWS metrics are averaged over 60 seconds during post-processing. To provide more granular insight into host performance, the Datadog Agent collects performance statistics every 15 seconds, offering a more detailed view of what's happening inside your hosts.

  {% image
     source="https://datadog-docs.imgix.net/images/agent/guide/Agent_VS_AWSA.1f7ad44c5fd6003ce0ea40336125df23.jpg?auto=format"
     alt="Agent vs AWS CloudWatch" /%}

- **Exposed metrics** - Datadog has over 50 metrics enabled by default. More metrics can be added with Datadog's application-specific [integrations](https://docs.datadoghq.com/integrations/).

- **Integrations** - Over [1,000 integrations](https://docs.datadoghq.com/integrations/) extend the functionality of the Datadog Agent beyond the native metrics.

- **Tagging consistency across services**: Tags applied at the Agent level are added to all metrics, logs, and traces reported by the Agent.

- **Custom metrics with DogStatsD** - With the Datadog Agent, use the built-in [StatsD client](https://docs.datadoghq.com/tracing/) to send custom metrics from your application, allowing you to correlate what's happening with your application, your users, and your system.

- **Custom Agent checks** - For even deeper customization, implement [custom Agent checks](https://docs.datadoghq.com/developers/custom_checks/) to collect metrics and other data from your custom systems or applications and send them to Datadog.

- **Application logs**: The Datadog Agent [collects and forwards application logs that are created locally](https://docs.datadoghq.com/agent/logs/?tab=tailfiles) on your cloud VMs or containers, so they don't need to be forwarded through the cloud provider integration. These logs also have Agent-level tags applied.

- **Application Performance Monitoring (APM)** - [Traces collected through the Agent](https://docs.datadoghq.com/tracing/) give a comprehensive look into your applications, helping you understand end-to-end service performance and identify potential bottlenecks.

## Further Reading{% #further-reading %}

- [Cloud Metric Delay](https://docs.datadoghq.com/integrations/guide/cloud-metric-delay/)
