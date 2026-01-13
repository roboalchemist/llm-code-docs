# Source: https://docs.datadoghq.com/tracing/troubleshooting/agent_apm_metrics.md

---
title: APM metrics sent by the Datadog Agent
description: >-
  Reference list of all APM metrics sent by the Datadog Agent for monitoring
  trace processing and Agent performance.
breadcrumbs: Docs > APM > APM Troubleshooting > APM metrics sent by the Datadog Agent
source_url: https://docs.datadoghq.com/troubleshooting/agent_apm_metrics/index.html
---

# APM metrics sent by the Datadog Agent

Find below the list of out-of-the-box tracing metrics sent by the Datadog Agent when [APM is enabled](https://docs.datadoghq.com/tracing/setup/). Import the [APM monitoring dashboard](https://docs.datadoghq.com/resources/json/APM_monitoring_dashboard.json) in your Datadog account in order to get an out-of-the-box dashboard exploiting most of those metrics.

{% dl %}

{% dt %}
`datadog.trace_agent.cpu_percent`
{% /dt %}

{% dd %}
**Type**: GaugeCPU usage in terms of percentage of a core. For example, a value of `50` is half a core, or `200` is two cores.
{% /dd %}

{% dt %}
`datadog.trace_agent.events.max_eps.current_rate`
{% /dt %}

{% dd %}
**Type**: GaugeCount of APM Events per second received by the Agent
{% /dd %}

{% dt %}
`datadog.trace_agent.events.max_eps.max_rate`
{% /dt %}

{% dd %}
**Type**: GaugeSame as the Agent config's max_events_per_second parameter.
{% /dd %}

{% dt %}
`datadog.trace_agent.events.max_eps.reached_max`
{% /dt %}

{% dd %}
**Type**: GaugeIs set to `1` every time max_events_per_second is reached, otherwise it's `0`.
{% /dd %}

{% dt %}
`datadog.trace_agent.events.max_eps.sample_rate`
{% /dt %}

{% dd %}
**Type**: GaugeSample rate applied by the Agent to Events it received
{% /dd %}

{% dt %}
`datadog.trace_agent.heap_alloc`
{% /dt %}

{% dd %}
**Type**: GaugeHeap allocations as reported by the Go runtime.
{% /dd %}

{% dt %}
`datadog.trace_agent.heartbeat`
{% /dt %}

{% dd %}
**Type**: GaugeIncrement by one every 10 seconds.
{% /dd %}

{% dt %}
`datadog.trace_agent.normalizer.spans_malformed`
{% /dt %}

{% dd %}
**Type**: CountNumber of spans having malformed fields that had to be altered in order for the system to accept them
{% /dd %}

{% dt %}
`datadog.trace_agent.obfuscation.sql_cache.hits`
{% /dt %}

{% dd %}
**Type**: CountNumber of GET calls where a value was found for the corresponding key.
{% /dd %}

{% dt %}
`datadog.trace_agent.obfuscation.sql_cache.misses`
{% /dt %}

{% dd %}
**Type**: CountNumber of GET calls where a value was not found for the corresponding key.
{% /dd %}

{% dt %}
`datadog.trace_agent.panic`
{% /dt %}

{% dd %}
**Type**: GaugeIncrement by one on every code panic.
{% /dd %}

{% dt %}
`datadog.trace_agent.profile`
{% /dt %}

{% dd %}
**Type**: CountIncrement by one every time a reverse proxy of profile endpoints is created.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.error`
{% /dt %}

{% dd %}
**Type**: CountNumber of times that the API rejected a payload due to an error in either decoding, formatting or other.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.events_extracted`
{% /dt %}

{% dd %}
**Type**: CountTotal APM events sampled.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.events_sampled`
{% /dt %}

{% dd %}
**Type**: CountTotal APM events sampled by the `max_events_per_second` parameter sampler.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.oom_kill`
{% /dt %}

{% dd %}
**Type**: CountNumber of times the Agent killed itself due to excessive memory use (150% of max_memory).
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.out_chan_fill`
{% /dt %}

{% dd %}
**Type**: GaugeInternal metric. Percentage of fill on the receiver's output channel.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.payload_accepted`
{% /dt %}

{% dd %}
**Type**: CountNumber of payloads accepted by the Agent.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.payload_refused`
{% /dt %}

{% dd %}
**Type**: CountNumber of payloads rejected by the receiver because of the sampling.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.spans_dropped`
{% /dt %}

{% dd %}
**Type**: CountNumber of spans dropped by the Agent.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.spans_filtered`
{% /dt %}

{% dd %}
**Type**: CountNumber of spans filtered by the Agent.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.spans_received`
{% /dt %}

{% dd %}
**Type**: CountTotal number of spans received by the Agent.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.tcp_connections`
{% /dt %}

{% dd %}
**Type**: CountNumber of TCP connections coming in to the agent.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.trace`
{% /dt %}

{% dd %}
**Type**: CountNumber of traces received and accepted.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.traces_bytes`
{% /dt %}

{% dd %}
**Type**: CountTotal bytes of payloads accepted by the Agent.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.traces_filtered`
{% /dt %}

{% dd %}
**Type**: CountTraces filtered by ignored resources (as defined in `datadog.yaml` file).
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.traces_priority`
{% /dt %}

{% dd %}
**Type**: CountTraces processed by priority sampler that have the priority tag.
{% /dd %}

{% dt %}
`datadog.trace_agent.receiver.traces_received`
{% /dt %}

{% dd %}
**Type**: CountNumber of traces received and accepted.
{% /dd %}

{% dt %}
`datadog.trace_agent.started`
{% /dt %}

{% dd %}
**Type**: CountIncrement by one every time the Agent starts.
{% /dd %}

{% dt %}
`datadog.trace_agent.stats_writer.bytes`
{% /dt %}

{% dd %}
**Type**: CountNumber of bytes sent (calculated after Gzip).
{% /dd %}

{% dt %}
`datadog.trace_agent.stats_writer.connection_fill`
{% /dt %}

{% dd %}
**Type**: HistogramPercentage of outgoing connections used.
{% /dd %}

{% dt %}
`datadog.trace_agent.stats_writer.dropped`
{% /dt %}

{% dd %}
**Type**: CountNumber of payloads dropped due to non retriable HTTP errors.
{% /dd %}

{% dt %}
`datadog.trace_agent.stats_writer.dropped_bytes`
{% /dt %}

{% dd %}
**Type**: CountNumber of bytes dropped due to non retriable HTTP errors.
{% /dd %}

{% dt %}
`datadog.trace_agent.stats_writer.encode_ms`
{% /dt %}

{% dd %}
**Type**: HistogramTime it took to encode a stats payload.
{% /dd %}

{% dt %}
`datadog.trace_agent.stats_writer.errors`
{% /dt %}

{% dd %}
**Type**: CountErrors that could not be retried.
{% /dd %}

{% dt %}
`datadog.trace_agent.stats_writer.queue_fill`
{% /dt %}

{% dd %}
**Type**: HistogramPercentage of queue filled.
{% /dd %}

{% dt %}
`datadog.trace_agent.stats_writer.retries`
{% /dt %}

{% dd %}
**Type**: CountNumber of retries on failures to the Datadog API
{% /dd %}

{% dt %}
`datadog.trace_agent.stats_writer.splits`
{% /dt %}

{% dd %}
**Type**: CountNumber of times a payload was split into multiple ones.
{% /dd %}

{% dt %}
`datadog.trace_agent.stats_writer.stats_buckets`
{% /dt %}

{% dd %}
**Type**: CountNumber of stats buckets flushed.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.bytes`
{% /dt %}

{% dd %}
**Type**: CountNumber of bytes sent (calculated after Gzip).
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.bytes_uncompressed`
{% /dt %}

{% dd %}
**Type**: CountNumber of bytes sent (calculated before Gzip).
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.compress_ms`
{% /dt %}

{% dd %}
**Type**: GaugeNumber of milliseconds it took to compress an encoded trace payload.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.connection_fill`
{% /dt %}

{% dd %}
**Type**: HistogramPercentage of outgoing connections used by the trace writer.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.dropped`
{% /dt %}

{% dd %}
**Type**: CountNumber of dropped payloads due to non retriable HTTP errors.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.dropped_bytes`
{% /dt %}

{% dd %}
**Type**: CountNumber of dropped bytes due to non retriable HTTP errors.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.encode_ms`
{% /dt %}

{% dd %}
**Type**: GaugeNumber of milliseconds it took to encode a trace payload.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.errors`
{% /dt %}

{% dd %}
**Type**: CountErrors that could not be retried.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.events`
{% /dt %}

{% dd %}
**Type**: CountNumber of events processed.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.flush_duration`
{% /dt %}

{% dd %}
**Type**: GaugeTime it took to flush a payload to the Datadog API.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.payloads`
{% /dt %}

{% dd %}
**Type**: CountNumber of payloads sent.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.queue_fill`
{% /dt %}

{% dd %}
**Type**: HistogramPercentage of outgoing payload queue fill.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.retries`
{% /dt %}

{% dd %}
**Type**: CountNumber of retries on failures to the Datadog API.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.spans`
{% /dt %}

{% dd %}
**Type**: CountNumber of spans processed.
{% /dd %}

{% dt %}
`datadog.trace_agent.trace_writer.traces`
{% /dt %}

{% dd %}
**Type**: CountNumber of traces processed.
{% /dd %}

{% /dl %}
