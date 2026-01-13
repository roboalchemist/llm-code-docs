# Source: https://docs.datadoghq.com/tracing/guide/agent_tracer_hostnames.md

---
title: Understand the Difference Between the Agent Host and the Tracer Host
description: >-
  Learn the difference between the Agent host and Tracer host in APM, and how
  hostname configuration affects infrastructure correlation.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Understand the Difference Between the Agent Host
  and the Tracer Host
source_url: https://docs.datadoghq.com/guide/agent_tracer_hostnames/index.html
---

# Understand the Difference Between the Agent Host and the Tracer Host

## Overview{% #overview %}

In Datadog APM, the `host` tag correlates spans and traces to infrastructure monitoring data, so host metrics are associated with hosts from spans and traces.

## Datadog Agent vs. Tracer hostname{% #datadog-agent-vs-tracer-hostname %}

The **Agent host** is the host on which the Datadog Agent is running. The **Tracer host** is the host on which the application instrumented with the tracing library is running.

The Agent host and the Tracer host may differ based on how you deploy the Datadog Agent on your infrastructure:

When the Agent is deployed on the same host as the application (for example, using a [DaemonSet](https://docs.datadoghq.com/containers/kubernetes/apm/?tab=daemonset)), the Agent host and the Tracer host are the same.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/agent_tracer_hostnames/agent_host.de4710f7d947349ee6fb9cefd76b732e.png?auto=format"
   alt="Agent deployed on the same host as the application" /%}

When the Agent is deployed on a remote host, the Agent host is different from the Tracer host.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/agent_tracer_hostnames/remote_host.8cc71c0c97448fe6be21d62dd364c583.png?auto=format"
   alt="Agent deployed on a remote host, different from the application" /%}

### When are the Tracer and Agent hosts set on spans?{% #when-are-the-tracer-and-agent-hosts-set-on-spans %}

- The Datadog Agent hostname is always set on spans.
- The Tracer hostname is set on spans if `DD_TRACE_REPORT_HOSTNAME` is `true` (default is `false`).

| Language | Config                          | Environment Variable       |
| -------- | ------------------------------- | -------------------------- |
| Ruby     | `tracing.report_hostname`       | `DD_TRACE_REPORT_HOSTNAME` |
| C++      | `dd.trace.report-hostname`      | `DD_TRACE_REPORT_HOSTNAME` |
| Node.js  | `reportHostname`                | `DD_TRACE_REPORT_HOSTNAME` |
| Go       | -                               | `DD_TRACE_REPORT_HOSTNAME` |
| Python   | -                               | `DD_TRACE_REPORT_HOSTNAME` |
| PHP      | `datadog.trace.report_hostname` | `DD_TRACE_REPORT_HOSTNAME` |
| Java     | `dd.trace.report-hostname`      | `DD_TRACE_REPORT_HOSTNAME` |

### When does APM use host information?{% #when-does-apm-use-host-information %}

APM uses host information when you create [retention filters](https://docs.datadoghq.com/tracing/trace_pipeline/trace_retention), generate [metrics from spans](https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics), or create [sensitive data scanner rules](https://docs.datadoghq.com/security/sensitive_data_scanner/) using host tag filters in queries. For example, host tag filters like `availability-zone` and `cluster-name` are enriched from the Datadog Agent host information.
