# Source: https://docs.datadoghq.com/developers/custom_checks.md

---
title: Custom Checks
description: Setting up a custom check with Datadog
breadcrumbs: Docs > Developers > Custom Checks
---

# Custom Checks

## Overview{% #overview %}

Custom checks, also known as custom Agent checks, enable you to collect metrics and other data from your custom systems or applications and send them to Datadog. By creating and configuring a new check file in your `conf.d` directory, you can configure the Datadog Agent to collect data emitted from your application. Custom checks are considered low effort compared to writing a Datadog integration. They impact your billing because Metrics emitted through custom checks are considered custom metrics, which have a cost associated depending on your subscription plan.

**Note**: A custom check is different from a service check. Service checks monitor the up or down status of a service. For more information, see [Service checks](https://docs.datadoghq.com/developers/service_checks/).

### Should you write a custom Agent check or an integration?{% #should-you-write-a-custom-agent-check-or-an-integration %}

Use custom checks to collect metrics from custom applications or unique systems. However, if you are trying to gather metrics from a generally available application, public service, or open source project, Datadog recommends that you [create a full-fledged Agent integration](https://docs.datadoghq.com/developers/integrations/agent_integration/). For more information about deciding how to send your data, see [Developers](https://docs.datadoghq.com/developers/). To learn how to write an integration, see [Creating New Integrations](https://docs.datadoghq.com/developers/integrations/agent_integration/).

## Getting started{% #getting-started %}

- [To quickly get started, see the Writing an Agent Check docs.](https://docs.datadoghq.com/developers/custom_checks/write_agent_check/)
- [If you have more advanced needs than the generic check (for example, metrics preprocessing), see the writing a custom Open Metrics check docs.](https://docs.datadoghq.com/developers/custom_checks/prometheus/)
