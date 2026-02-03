# Source: https://docs.datadoghq.com/getting_started/devsecops.md

---
title: Getting Started with Infrastructure DevSecOps
description: >-
  Introduction to Infrastructure DevSecOps bundles combining monitoring with
  Cloud Security for Pro and Enterprise tiers.
breadcrumbs: Docs > Getting Started > Getting Started with Infrastructure DevSecOps
---

# Getting Started with Infrastructure DevSecOps

This guide introduces the Infrastructure Monitoring DevSecOps bundles, with links to setup instructions to help you install and configure them.

## Infrastructure DevSecOps{% #infrastructure-devsecops %}

The Infrastructure DevSecOps bundles combine infrastructure monitoring with the security capabilities of [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/).

{% tab title="Infrastructure DevSecOps Pro" %}
Infrastructure DevSecOps Pro includes [Containers](https://docs.datadoghq.com/containers/), [Serverless](https://docs.datadoghq.com/serverless/), and [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/setup/). It also includes more than 1,000 [out-of-the-box integrations](https://docs.datadoghq.com/integrations/).

### Setup{% #setup %}

To get started with Infrastructure DevSecOps Pro, [install and configure the Datadog Agent](https://docs.datadoghq.com/agent/) for Containers and Serverless. You should also set up the integrations for your services. For detailed instructions, see the following docs:

- [Containers](https://docs.datadoghq.com/containers/)
- [Serverless](https://docs.datadoghq.com/serverless/)
- [Integrations](https://docs.datadoghq.com/integrations/)

After you install the Agent, configure Cloud Security for your environment.

- [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/setup/)

### Next steps{% #next-steps %}

Learn more about the features included with Infrastructure DevSecOps Pro:

- [Infrastructure List](https://docs.datadoghq.com/infrastructure/list/): View activity on your hosts
- [Metrics](https://docs.datadoghq.com/metrics/): Explore and understand your metrics
- [Host and Container Maps](https://docs.datadoghq.com/infrastructure/hostmap/): Visualize your hosts and containers
- [Live Containers](https://docs.datadoghq.com/infrastructure/containers/): Gain real-time visibility into all containers across your environment
- [Serverless](https://docs.datadoghq.com/serverless/): Gain full visibility into all of the managed services that power your serverless applications
- [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/): Real-time threat detection and continuous configuration audits across your entire cloud infrastructure

{% /tab %}

{% tab title="Infrastructure DevSecOps Enterprise" %}
Infrastructure DevSecOps Enterprise includes [Containers](https://docs.datadoghq.com/containers/), [Serverless](https://docs.datadoghq.com/serverless/), [Live Processes](https://docs.datadoghq.com/infrastructure/process/), and [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/setup/). It also includes more than 1,000 [out-of-the-box integrations](https://docs.datadoghq.com/integrations/).

### Setup{% #setup %}

To get started with Infrastructure DevSecOps Enterprise, [install and configure the Datadog Agent](https://docs.datadoghq.com/agent/) for Containers, Serverless, and Live Processes. You should also set up the integrations for your services. For detailed instructions, see the following docs:

- [Containers](https://docs.datadoghq.com/containers/)
- [Serverless](https://docs.datadoghq.com/serverless/)
- [Live Processes](https://docs.datadoghq.com/infrastructure/process/?tab=linuxwindows#installation)
- [Integrations](https://docs.datadoghq.com/integrations/)

After you install the Agent, configure Cloud Security for your environment.

- [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/setup/)

### Next steps{% #next-steps %}

Learn more about the features included with Infrastructure DevSecOps Enterprise:

- [Infrastructure List](https://docs.datadoghq.com/infrastructure/list/): View activity on your hosts
- [Metrics](https://docs.datadoghq.com/metrics/): Explore and understand your metrics
- [Metric Correlations](https://docs.datadoghq.com/dashboards/correlations/): Find potential root causes for an issue by searching for other metrics that exhibit irregular behavior
- [Host and Container Maps](https://docs.datadoghq.com/infrastructure/hostmap/): Visualize your hosts and containers
- [Live Containers](https://docs.datadoghq.com/infrastructure/containers/): Gain real-time visibility into all containers across your environment
- [Live Processes](https://docs.datadoghq.com/infrastructure/process/): Gain real-time visibility into the process running on your infrastructure
- [Serverless](https://docs.datadoghq.com/serverless/): Gain full visibility into all of the managed services that power your serverless
- [Watchdog](https://docs.datadoghq.com/watchdog/): Automatically detect potential application and infrastructure issues
- [Cloud Security](https://docs.datadoghq.com/security/cloud_security_management/): Real-time threat detection and continuous configuration audits across your entire cloud infrastructure

{% /tab %}
