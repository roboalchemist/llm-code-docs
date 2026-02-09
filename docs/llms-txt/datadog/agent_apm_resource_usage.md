# Source: https://docs.datadoghq.com/tracing/troubleshooting/agent_apm_resource_usage.md

---
title: Agent Resource Usage by APM
description: >-
  Monitor and optimize Datadog Agent CPU and memory usage for APM workloads to
  prevent resource exhaustion.
breadcrumbs: Docs > APM > APM Troubleshooting > Agent Resource Usage by APM
---

# Agent Resource Usage by APM

The Agent is CPU-bound and its CPU usage is correlated with the number of spans received per second.

The Agent buffers unprocessed payloads in memory, so throttling the Agent process because of an insufficient CPU limit can lead to an out-of-memory issue.

## Detect out-of-CPU{% #detect-out-of-cpu %}

To monitor CPU usage and detect oncoming out-of-CPU issues, compare the [maximum CPU percentage](https://docs.datadoghq.com/tracing/troubleshooting/agent_rate_limits/#maximum-cpu-percentage) configured for the Agent to the `datadog.trace_agent.cpu_percent` metric. The `datadog.trace_agent.cpu_percent` metric is CPU usage in terms of percentage of a core. For example, a value of `50` is half a core, or `200` is two cores.

See the full list of [Agent APM metrics](https://docs.datadoghq.com/tracing/send_traces/agent-apm-metrics/).

## Resource requirements{% #resource-requirements %}

A good indicator to calculate adequate resource limits for the Agent is the number of spans received per second, reported in the `datadog.trace_agent.receiver.spans_received` metric. Based on that metric's value, follow the table below to choose adequate CPU and memory limits:

| Spans per second | CPU (core) | Memory (MB) |
| ---------------- | ---------- | ----------- |
| 2000             | 0.05       | 35          |
| 11 000           | 0.2        | 40          |
| 32 000           | 0.6        | 60          |
| 58 000           | 1          | 70          |
| 130 000          | 2          | 130         |

**Notes:**

- The values are based on Agent `7.39.0` benchmarks.
- The benchmarks were performed on an AWS `c5.2xlarge` instance (8 VCPU/ 16GiB RAM)
