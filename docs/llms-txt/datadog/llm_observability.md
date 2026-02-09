# Source: https://docs.datadoghq.com/llm_observability.md

---
title: LLM Observability
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > LLM Observability
---

# LLM Observability

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Try Getting Started with LLM Observability in the Learning Center

Learn how to monitor your LLM application's performance, costs, traces, token usage, and errors to identify and resolve issues.

[ENROLL NOW](https://learn.datadoghq.com/courses/llm-obs-getting-started)
{% /callout %}

## Overview{% #overview %}

With LLM Observability, you can monitor, troubleshoot, and evaluate your LLM-powered applications, such as chatbots. You can investigate the root cause of issues, monitor operational performance, and evaluate the quality, privacy, and safety of your LLM applications.

Each request fulfilled by your application is represented as a trace on the [**LLM Observability** page](https://app.datadoghq.com/llm/traces) in Datadog.

{% image
   source="https://datadog-docs.imgix.net/images/llm_observability/traces.03f0666d1900ffe55652104872112023.png?auto=format"
   alt="A list of prompt-response pair traces on the LLM Observability page" /%}

A trace can represent:

- An individual LLM inference, including tokens, error information, and latency
- A predetermined LLM workflow, which is a grouping of LLM calls and their contextual operations, such as tool calls or preprocessing steps
- A dynamic LLM workflow executed by an LLM agent

Each trace contains spans representing each choice made by an agent or each step of a given workflow. A given trace can also include input and output, latency, privacy issues, errors, and more. For more information, see [Terms and Concepts](https://docs.datadoghq.com/llm_observability/terms).

## Troubleshoot with end-to-end tracing{% #troubleshoot-with-end-to-end-tracing %}

View every step of your LLM application chains and calls to pinpoint problematic requests and identify the root cause of errors.

{% image
   source="https://datadog-docs.imgix.net/images/llm_observability/errors.f7f6a86f8ea4da499fde4a9d410a56ed.png?auto=format"
   alt="Errors that occurred in a trace on the Errors tab in a trace side panel" /%}

## Monitor operational metrics and optimize cost{% #monitor-operational-metrics-and-optimize-cost %}

Monitor the cost, latency, performance, and usage trends for all your LLM applications with [out-of-the-box dashboards](https://app.datadoghq.com/dash/integration/llm_operational_insights).

{% image
   source="https://datadog-docs.imgix.net/images/llm_observability/dashboard_1.03b09c80d39dcf44341e6418dc7acd13.png?auto=format"
   alt="The out-of-the-box LLM Observability Operational Insights dashboard in Datadog" /%}

## Evaluate the quality and effectiveness of your LLM applications{% #evaluate-the-quality-and-effectiveness-of-your-llm-applications %}

Identify problematic clusters and monitor the quality of responses over time with topical clustering and checks like sentiment, failure to answer, and so on.

{% image
   source="https://datadog-docs.imgix.net/images/llm_observability/cluster_map/box.a7324289906d76156dcbb60ad124fa10.png?auto=format"
   alt="The box packing layout displays clusters of traces represented by colored circles, and includes a panel listing clusters with topics, trace counts, and failure rates." /%}

## Safeguard sensitive data and identify malicious users{% #safeguard-sensitive-data-and-identify-malicious-users %}

Automatically scan and redact any sensitive data in your AI applications and identify prompt injections, among other evaluations.

{% image
   source="https://datadog-docs.imgix.net/images/llm_observability/prompt_injection.f4560358ad3e0f4c563c50aee3483b7e.png?auto=format"
   alt="An example of a prompt-injection attempt detected by LLM Observability" /%}

## See anomalies highlighted as insights{% #see-anomalies-highlighted-as-insights %}

LLM Observability Insights provides a monitoring experience that helps users identify anomalies in their operational metricsâsuch as duration and error rateâand their [out-of-the-box (OOTB) evaluations](https://docs.datadoghq.com/llm_observability/evaluations/managed_evaluations).

Outlier detection is performed across key dimensions:

- Span name
- Workflow type
- [Cluster input/output topics](https://docs.datadoghq.com/llm_observability/monitoring/cluster_map)

These outliers are analyzed over the past week and automatically surfaced in the corresponding time window selected by the user. This enables teams to proactively detect regressions, performance drifts, or unexpected behavior in their LLM applications.

{% image
   source="https://datadog-docs.imgix.net/images/llm_observability/llm-insights.b7bcf97351b6495bac81ddea70cd057b.png?auto=format"
   alt="An 'Insights' banner across the top of the LLM Observability Monitor page. The banner displays 10 insights and has a View Insights button that leads to a side panel with further details." /%}

## Use integrations with LLM Observability{% #use-integrations-with-llm-observability %}

The [LLM Observability SDK for Python](https://docs.datadoghq.com/llm_observability/setup/sdk) integrates with frameworks such as OpenAI, LangChain, AWS Bedrock, and Anthropic. It automatically traces and annotate LLM calls, capturing latency, errors, and token usage metricsâwithout code changes.

{% alert level="info" %}
Datadog offers a variety of artificial intelligence (AI) and machine learning (ML) capabilities. The [AI/ML integrations on the Integrations page and the Datadog Marketplace](https://docs.datadoghq.com/integrations/#cat-aiml) are platform-wide Datadog functionalities.For example, APM offers a native integration with OpenAI for monitoring your OpenAI usage, while Infrastructure Monitoring offers an integration with NVIDIA DCGM Exporter for monitoring compute-intensive AI workloads. These integrations are different from the LLM Observability offering.
{% /alert %}

For more information, see the [Auto Instrumentation documentation](https://docs.datadoghq.com/llm_observability/setup/auto_instrumentation).

## Ready to start?{% #ready-to-start %}

See the [Setup documentation](https://docs.datadoghq.com/llm_observability/setup) for instructions on instrumenting your LLM application or follow the [Trace an LLM Application guide](https://docs.datadoghq.com/llm_observability/quickstart) to generate a trace using the [LLM Observability SDK for Python](https://docs.datadoghq.com/llm_observability/setup/sdk).

## Further Reading{% #further-reading %}

- [Building reliable dashboard agents with Datadog LLM Observability](https://www.datadoghq.com/blog/llm-observability-at-datadog-dashboards)
- [Driving AI ROI: How Datadog connects cost, performance, and infrastructure so you can scale responsibly](https://www.datadoghq.com/blog/manage-ai-cost-and-performance-with-datadog/)
- [Datadog LLM Observability natively supports OpenTelemetry GenAI Semantic Conventions](https://www.datadoghq.com/blog/llm-otel-semantic-convention)
- [Gain visibility into Strands Agents workflows with Datadog LLM Observability](https://www.datadoghq.com/blog/llm-aws-strands)
- [Monitor your Anthropic applications with Datadog LLM Observability](https://www.datadoghq.com/blog/anthropic-integration-datadog-llm-observability/)
- [Best practices for monitoring LLM prompt injection attacks to protect sensitive data](https://www.datadoghq.com/blog/monitor-llm-prompt-injection-attacks/)
- [Optimize LLM application performance with Datadog's vLLM integration](https://www.datadoghq.com/blog/vllm-integration/)
- [Optimize and troubleshoot AI infrastructure with Datadog GPU Monitoring](https://www.datadoghq.com/blog/datadog-gpu-monitoring/)
- [Monitor agents built on Amazon Bedrock with Datadog LLM Observability](https://www.datadoghq.com/blog/llm-observability-bedrock-agents/)
- [Identify common security risks in MCP servers](https://www.datadoghq.com/blog/monitor-mcp-servers/)
- [Abusing AI infrastructure: How mismanaged credentials and resources expose LLM applications](https://www.datadoghq.com/blog/detect-abuse-ai-infrastructure/)
