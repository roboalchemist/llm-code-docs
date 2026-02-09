# Source: https://docs.datadoghq.com/tracing/troubleshooting/correlated-logs-not-showing-up-in-the-trace-id-panel.md

---
title: Correlated Logs Are Not Showing Up In The Trace ID Panel
description: >-
  Troubleshoot missing correlated logs in the trace panel by checking log
  correlation setup and attribute mapping.
breadcrumbs: >-
  Docs > APM > APM Troubleshooting > Correlated Logs Are Not Showing Up In The
  Trace ID Panel
---

# Correlated Logs Are Not Showing Up In The Trace ID Panel

## Overview{% #overview %}

The [trace](https://docs.datadoghq.com/tracing/glossary/#trace) panel contains information about the trace, host, and correlated logs.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/troubleshooting/tracing_no_logs_in_trace.b2630cc410655ba9a565eb7b091cc84e.png?auto=format"
   alt="A trace page showing an empty log section" /%}

There are four types of logs that appear in a [trace](https://docs.datadoghq.com/tracing/glossary/#trace):

- `trace_id`: Display logs that have the corresponding trace ID.
- `host`: Display logs from the trace's host within the trace's timeframe.
- `container_id`: Display logs from the trace's container within the trace's timeframe.
- `pod_name`: Display logs from the trace's pod within the trace's timeframe.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/troubleshooting/tracing_logs_display_option.68b116ed0e1f5720030284d95c8a0f57.png?auto=format"
   alt="A trace's log dropdown menu showing the trace ID and host options" /%}

In some cases, the **Logs** section in the trace panel may appear empty. This guide walks you through how to fix this issue.

## Infrastructure options{% #infrastructure-options %}

If the **Log** section is empty for the `host`, `container_id`, or `pod_name` options, navigate to the [Log Explorer](https://app.datadoghq.com/logs) and ensure the following conditions:

1. Logs are being sent from the host/container/pod that emitted the trace.
1. There are logs for that host within the trace's timeframe.
1. The logs' timestamp is properly set. For more information, see [Logs Not Showing Expected Timestamp](https://docs.datadoghq.com/logs/guide/logs-not-showing-expected-timestamp/).

## Trace ID option{% #trace-id-option %}

If the **Log** section is empty for the `trace_id` option, ensure you have a standard `trace_id` attribute in your logs. If your logs do not contain `trace_id`, [correlate your traces and logs](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/) in order to do the following:

1. Extract the trace ID in a log attribute.

1. Remap this attribute to the reserved `trace_id` attribute.

   {% tab title="JSON logs" %}
For JSON logs, Step 1 and 2 are automatic. The tracer injects the [trace](https://docs.datadoghq.com/tracing/glossary/#trace) and [span](https://docs.datadoghq.com/tracing/glossary/#spans) IDs into the logs, which are automatically remapped by the [reserved attribute remappers](https://docs.datadoghq.com/logs/log_configuration/processors/#remapper).

If this process is not working as expected, ensure the logs attribute's name containing the trace ID is `dd.trace_id` and verify that the attribute is correctly set in the [reserved attributes'](https://app.datadoghq.com/logs/pipelines/remapping) Trace ID section.

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/troubleshooting/trace_id_reserved_attribute_mapping.bf8ead6e5722342da25c5315aec7bb68.png?auto=format"
      alt="The preprocessing for JSON logs page with the Trace Id section highlighted" /%}

      {% /tab %}

   {% tab title="With Log integration" %}
For raw logs (where you are collecting the logs using a [log integration](https://docs.datadoghq.com/logs/log_collection/?tab=application#setup) for a specific language), set the `source` attribute to the language, such as `java`, `python`, `ruby`, and more. The integration automatically correlates traces and logs.

This example demonstrates the Java integration pipeline:

   {% image
      source="https://datadog-docs.imgix.net/images/tracing/troubleshooting/tracing_java_traceid_remapping.9aea4d2194cba4e077d724709744026d.png?auto=format"
      alt="The Java log pipeline with the Trace Id remapper highlighted" /%}

It is possible that the log format is not recognized by the integration pipeline. In this case, clone the pipeline and follow the [parsing troubleshooting guide](https://docs.datadoghq.com/logs/faq/how-to-investigate-a-log-parsing-issue/) to make sure the pipeline accepts the log format.
   {% /tab %}

   {% tab title="Custom" %}
For raw logs where you aren't using an integration to collect the logs:

   1. Make sure that the custom parsing rule extracts the [trace](https://docs.datadoghq.com/tracing/glossary/#trace) and [span](https://docs.datadoghq.com/tracing/glossary/#spans) IDs as a string, like in the following example:

      {% image
         source="https://datadog-docs.imgix.net/images/tracing/troubleshooting/tracing_custom_parsing.f94340f25bb28374d9f46f7aaffbd491.png?auto=format"
         alt="A custom parser with the trace Id highlighted in the sample log, parsing rule, and extraction sections" /%}

   1. Then define a [Trace remapper](https://docs.datadoghq.com/logs/log_configuration/processors/#trace-remapper) on the extracted attribute to remap it to the official trace ID of the logs.

      {% /tab %}

Once the IDs are properly injected and remapped to your logs, you can see the logs correlated to the trace in the trace panel.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/troubleshooting/trace_id_injection.32c00c69e59d6c50e6c89efc16b27af3.png?auto=format"
   alt="A trace page showing the logs section with correlated logs" /%}

**Note**: Trace IDs and span IDs are not displayed in your logs or log attributes in the UI.

## Further Reading{% #further-reading %}

- [Correlate Traces and Logs](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/)
- [Ease troubleshooting with cross product correlation](https://docs.datadoghq.com/logs/guide/ease-troubleshooting-with-cross-product-correlation/)
