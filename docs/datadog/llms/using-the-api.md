# Source: https://docs.datadoghq.com/api/latest/using-the-api.md

---
title: Using the API
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > API Reference > Using the API
---

## Using the API{% #using-the-api %}

Use the Datadog HTTP API to access the Datadog platform programmatically. You can use the API to send data to Datadog, build data visualizations, and manage your account.

## Send data to Datadog{% #send-data-to-datadog %}

Use the API to begin to send integrations data to Datadog. With some additional setup of the Agent, you can also use the API to send Synthetic test data, Logs, and Traces to Datadog.

**Integrations endpoints**

Available integrations endpoints:

- [AWS Integration](https://docs.datadoghq.com/api/v1/aws-integration/)
- [AWS Logs Integration](https://docs.datadoghq.com/api/v1/aws-logs-integration/)
- [Azure Integration](https://docs.datadoghq.com/api/v1/azure-integration/)
- [Cloudflare Integration](https://docs.datadoghq.com/api/latest/cloudflare-integration/)
- [Fastly Integration](https://docs.datadoghq.com/api/latest/fastly-integration/)
- [Google Cloud Integration](https://docs.datadoghq.com/api/v1/gcp-integration/)
- [Jira Integration](https://docs.datadoghq.com/api/latest/jira-integration/)
- [Microsoft Teams Integration](https://docs.datadoghq.com/api/latest/microsoft-teams-integration/)
- [Okta Integration](https://docs.datadoghq.com/api/latest/okta-integration/)
- [Opsgenie Integration](https://docs.datadoghq.com/api/latest/opsgenie-integration/)
- [PagerDuty Integration](https://docs.datadoghq.com/api/v1/pagerduty-integration/)
- [Slack Integration](https://docs.datadoghq.com/api/v1/slack-integration/)
- [Webhooks Integration](https://docs.datadoghq.com/api/v1/webhooks-integration/)

**Platform endpoints**

Use these endpoints to post and fetch data to and from other parts of the Datadog platform:

- The [metrics](https://docs.datadoghq.com/api/v1/metrics/) endpoints allow you to post [metrics](https://docs.datadoghq.com/metrics/introduction/) data so it can be graphed on Datadog's dashboards and query metrics from any time period.
- The [events](https://docs.datadoghq.com/api/v1/events/) endpoints allow you to post and fetch events to and from the [Datadog event explorer](https://docs.datadoghq.com/events/).
- Use the [Synthetic Monitoring](https://docs.datadoghq.com/api/v1/synthetics/) endpoints to create, start, stop, and see [Synthetic tests](https://docs.datadoghq.com/synthetics/) results.
- Use the [Tracing Agent API](https://docs.datadoghq.com/tracing/guide/send_traces_to_agent_by_api/) to send traces to your Datadog Agent, which then forwards them to Datadog.
- Use the [LLM Observability Export API](https://docs.datadoghq.com/llm_observability/evaluations/export_api) to access your LLM Observability data for running external evaluations and exporting spans for offline storage.

## Visualize your data{% #visualize-your-data %}

Once you are sending data to Datadog, you can use the API to build data visualizations programmatically:

- Build [Dashboards](https://docs.datadoghq.com/api/v1/dashboards/) and view [Dashboard Lists](https://docs.datadoghq.com/api/v1/dashboard-lists/)
- Manage [host tags](https://docs.datadoghq.com/api/v1/hosts/)
- Create [Embeddable Graphs](https://docs.datadoghq.com/api/v1/embeddable-graphs/)
- Take a [graph snapshot](https://docs.datadoghq.com/api/v1/snapshots/)
- [Service Dependencies](https://docs.datadoghq.com/api/v1/service-dependencies/) - see a list of your APM services and their dependencies
- Create [Monitors](https://docs.datadoghq.com/api/v1/monitors/)
- [Service Checks](https://docs.datadoghq.com/api/v1/service-checks/) - post check statuses for use with monitors
- Create and manage [Logs](https://docs.datadoghq.com/api/v1/logs/), [Logs Indexes](https://docs.datadoghq.com/api/v1/logs-indexes/), and [Logs Pipelines](https://docs.datadoghq.com/api/v1/logs-pipelines/)
- Get [Host](https://docs.datadoghq.com/api/v1/hosts/) information for your organization
- Create and manage [Service Level Objectives](https://docs.datadoghq.com/api/v1/service-level-objectives/)
- Generate [Security Monitoring](https://docs.datadoghq.com/api/v2/security-monitoring/) signals

## Manage your account{% #manage-your-account %}

You can also use the Datadog API to manage your account programmatically:

- Manage [Users](https://docs.datadoghq.com/api/v1/users/)
- Manage [Roles](https://docs.datadoghq.com/api/v1/roles/)
- Manage your [Organization](https://docs.datadoghq.com/api/v1/organizations/)
- Verify API and app keys with the [Authentication](https://docs.datadoghq.com/api/v1/authentication/) endpoint
- Grant specific logs access with the [Logs Restriction Queries](https://docs.datadoghq.com/api/v2/logs-restriction-queries/)
- Manage existing keys with [Key Management](https://docs.datadoghq.com/api/v1/key-management/)
- Get hourly, daily, and monthly usage across multiple facets of Datadog with the [Usage Metering](https://docs.datadoghq.com/api/v1/usage-metering/) endpoints
- See the list of IP prefixes belonging to Datadog with [IP Ranges](https://docs.datadoghq.com/api/v1/ip-ranges/)
