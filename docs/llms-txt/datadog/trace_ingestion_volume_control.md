# Source: https://docs.datadoghq.com/tracing/guide/trace_ingestion_volume_control.md

---
title: Ingestion volume control with APM Distributed Tracing
description: >-
  Learn how to control span ingestion volume with APM tracing mechanisms to
  manage costs while maintaining observability.
breadcrumbs: >-
  Docs > APM > Tracing Guides > Ingestion volume control with APM Distributed
  Tracing
---

# Ingestion volume control with APM Distributed Tracing

## Overview{% #overview %}

The [Ingestion control page](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls) provides granular visibility into the ingestion configuration for all services, in the agent and in the tracing libraries. All [Ingestion Mechanisms](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/) are publicly documented and configurable.

With the ingestion control page, you have full visibility and complete control of your span volume. Consequently, you are be able to:

- Ingest the data that is most relevant to your business and your observability goals.
- Reduce network costs by avoiding sending unused trace data to the Datadog platform.
- Control and manage your overall costs.

## Effects of reducing trace ingestion volume{% #effects-of-reducing-trace-ingestion-volume %}

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/trace_ingestion_volume_control/sampling_25_percent.a32d9d011304ba65d1a848db771bbf47.png?auto=format"
   alt="APM ingestion sampling displaying 25 percent complete traces ingested" /%}

If you decide to reduce the ingestion volume for certain services, the **request, error, and latency [metrics](https://docs.datadoghq.com/tracing/metrics/metrics_namespace/)** (known as RED metrics, for Requests, Errors, and Duration) remain 100% accurate, as they are being calculated based on 100% of the application's traffic, regardless of any sampling configuration. These metrics are included when purchasing Datadog APM. In order to make sure you have full visibility into your application's traffic, you can use these metrics to spot potential errors on a service or a resource, by creating dashboards, monitors, and SLOs.

**Note**: If your applications and services are instrumented with OpenTelemetry libraries and you set up sampling at the SDK level and/or at the collector level, APM metrics are based on the **sampled** set of data by default. See [Ingestion Sampling with OpenTelemetry](https://docs.datadoghq.com/opentelemetry/guide/ingestion_sampling_with_opentelemetry/) for more information.

{% alert level="info" %}
Alternatively, use the [Datadog Connector](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/connector/datadogconnector) to calculate APM metrics on unsampled data. Read [Switch from Datadog Processor to Datadog Connector for OpenTelemetry APM Metrics](https://docs.datadoghq.com/opentelemetry/guide/switch_from_processor_to_connector) for more information.
{% /alert %}

Trace data is very repetitive, which means trace samples to investigate any issues are still available with ingestion sampling. For high throughput services, there's usually no need for you to collect every single request - an important enough problem should always show symptoms in multiple traces. Ingestion controls helps you to have the visibility that you need to troubleshoot problems while remaining within budget.

#### Metrics from spans{% #metrics-from-spans %}

[Metrics from spans](https://docs.datadoghq.com/tracing/trace_pipeline/generate_metrics/) are based on ingested spans.

Reducing ingestion sampling rates will impact any **count** type metric. **Distribution** type metrics, for instance `duration` measures, are not impacted as the sampling is mostly uniform, the distribution of latencies remains representative of the traffic.

#### Monitors{% #monitors %}

Any **metric** monitor using metrics from spans is impacted by ingestion volume reduction. Metric monitors based on **trace.\_\_** metrics will remain accurate, because these metrics are calculated based on 100% of the traffic.

Count-based [**Trace analytics**](https://docs.datadoghq.com/monitors/types/apm/?tab=analytics) monitors are impacted as well. Check if you have trace analytics monitors created by looking for `type:trace-analytics` monitors in the manage monitors page.

## Assess your services' ingestion configuration{% #assess-your-services-ingestion-configuration %}

To assess the current state of applications' instrumentation, leverage the [Trace Ingestion Control page](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls) that provides detailed information on agent and tracing library configuration.

### Understanding if you are within your monthly ingestion allocation{% #understanding-if-you-are-within-your-monthly-ingestion-allocation %}

Use the ingestion monthly usage KPI to get an estimation of your usage compared to the monthly allocation of 150 GB of ingested spans per APM host (summed across all APM hosts).

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/trace_ingestion_volume_control/ingestion_overage.b1db6c704216a7d9d1d3230f8932b2fb.png?auto=format"
   alt="Ingestion Overage KPI displaying 170 percent estimated monthly usage of 23.3 monthly available TB across all infrastructure" /%}

### Advanced APM usage investigation{% #advanced-apm-usage-investigation %}

The ingestion configuration can be investigated for each service. Click on a service row to see the Service Ingestion Summary, which surfaces:

- **Ingestion reason breakdown**: which [ingestion mechanism](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/) is responsible for the ingestion volume
- **Top sampling decision makers**: which upstream services are taking sampling decisions for the spans ingested in regards to the [default ingestion mechanism](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#head-based-sampling)

An [out-of-the-box dashboard](https://docs.datadoghq.com/tracing/trace_pipeline/metrics/) is also available to get more insights on historical trends related to your ingestion usage and volume. Clone this dashboard to be able to edit widgets and perform further analysis.

## Reduce your ingestion volume{% #reduce-your-ingestion-volume %}

### Identify services responsible for most of the ingestion volume{% #identify-services-responsible-for-most-of-the-ingestion-volume %}

To identify which services are responsible for most of the ingestion volume, sort the table by **Downstream Bytes/s**. This column allows you to spot which services take most of the sampling decisions, which also impact downstream services.

If the service is starting the trace, **Downstream Bytes/s** also encompasses the volume of spans coming from downstream services for which the service took the sampling decision.

The **Traffic Breakdown** column gives a good indication of the service's sampling configuration.

If the service has a high Downstream Bytes/s rate and a high sampling rate (displayed as the blue filled section of the traffic breakdown column), reducing the sampling rate for this service is expected to have a high impact on the ingestion volume.

{% image
   source="https://datadog-docs.imgix.net/images/tracing/guide/trace_ingestion_volume_control/sampling_99_percent.bf929d1677e824b76a911118a57386fb.png?auto=format"
   alt="APM ingestion sampling displaying 99 percent complete traces ingested, meaning no sampling" /%}

### Globally configure the ingestion sampling rate at the Agent level{% #globally-configure-the-ingestion-sampling-rate-at-the-agent-level %}

The **Configuration** column tells you whether or not your services are configured with sampling rules. If the top services are labelled with `AUTOMATIC` configuration, changing the **Agent configuration** will reduce the volume globally across services.

To reduce the ingestion volume at the Agent level, configure `DD_APM_MAX_TPS` (set to `10` by default) to reduce the share of head-based sampling volume. Read more about the [default sampling mechanism](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#head-based-sampling).

**Note**: This configuration option only goes into effect when using **Datadog tracing libraries**. If the OTLP Ingest in the Agent collects data from applications instrumented with OpenTelemetry, modifying `DD_APM_MAX_TPS` does not change sampling rates that are applied in tracing libraries.

Additionally, to reduce the volume of [error](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#error-traces) and [rare](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/#rare-traces) traces:

- Configure `DD_APM_ERROR_TPS` to reduce the share of error sampling.
- Set `DD_APM_DISABLE_RARE_SAMPLER` to true to stop sampling rare traces.

### Independently configure the ingestion sampling rate for services at the library level{% #independently-configure-the-ingestion-sampling-rate-for-services-at-the-library-level %}

By configuring sampling rates for a few high-throughput services, most of the "exceeding" ingestion volume can be lowered.

Click on a service to view the **Service Ingestion Summary**. Look at the **Ingestion reasons breakdown** in the side panel, which gives an overview of the share of ingestion volume attributed to each mechanism.

If the main reason for most of the ingestion volume is head-based sampling (`auto` or `rule`), the volume can be configured by setting a sampling rule at the tracing library level.

Click the **Manage Ingestion Rate** button to configure a sampling rate for the service. Select the service language and the ingestion sampling rate you want to apply.

**Note:** The application needs to be redeployed in order to apply the configuration changes. Datadog recommends applying the changes by setting [environment variables](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/?tab=environmentvariables#in-tracing-libraries-user-defined-rules).

### Trace sampling with OpenTelemetry{% #trace-sampling-with-opentelemetry %}

If your applications and services are instrumented with OpenTelemetry libraries and you're using the OpenTelemetry collector, you can use the following OpenTelemetry sampling capabilities:

- [TraceIdRatioBased](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/sdk.md#traceidratiobased) and [ParentBased](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/sdk.md#parentbased) are 2 built-in samplers that allow you to implement deterministic head-based sampling based on the trace_id at the **SDK** level.
- The [Tail Sampling Processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/tailsamplingprocessor/README.md) and [Probabilistic Sampling Processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/probabilisticsamplerprocessor/README.md) allow you to sample traces based on a set of rules at the **collector** level.

Using either of the two options results in sampled APM Metrics.

## Ingestion reasons glossary{% #ingestion-reasons-glossary %}

*Know which ingestion mechanisms are responsible for most of the ingestion volume*

The default mechanism to sample traces is head-based sampling. The decision whether to sample a trace or not is taken at the beginning of its lifecycle, and propagated downstream in the context of the requests in order to ensure that you can always view and analyze complete traces.

Head-based sampling is configurable in the tracing libraries or from the Datadog Agent:

| ingestion reason | Where             | Ingestion Mechanism Description                                    | Default                        |
| ---------------- | ----------------- | ------------------------------------------------------------------ | ------------------------------ |
| `auto`           | Agent             | The Datadog Agent distributes sampling rates to tracing libraries. | 10 traces per second per Agent |
| `rule`           | Tracing Libraries | The libraries' defined sampling percentage for specific services.  | null                           |

Several other ingestion reasons are surfaced in the Ingestion Control page and as a tag on the `datadog.estimated_usage.apm.ingested_bytes` metric. These ingestion reasons may be responsible for your ingestion volume:

| ingestion reason | Where                       | Ingestion Mechanism Description                                                                                                             | Default                                                     |
| ---------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `error`          | Agent                       | Sampling of errors uncaught by the head-based sampling.                                                                                     | 10 traces per second per Agent (null, if rules are defined) |
| `rare`           | Agent                       | Sampling of rare traces (catching all combinations of a set of span tags).                                                                  | 5 traces per second per Agent (null, if rules are defined)  |
| `manual`         | In-code                     | In-code decision override to keep/drop a span and its children.                                                                             | null                                                        |
| `analytics`      | Agent and Tracing Libraries | [Deprecated ingestion mechanism](https://docs.datadoghq.com/tracing/legacy_app_analytics) that samples single spans without the full trace. | null                                                        |

Additionally, other products can be responsible for sampled span volume:

- `synthetics` and `synthetics-browser`: API and browser tests are connected to the trace generated by the test.
- `rum`: Requests from web and mobile applications are linked to the corresponding backend traces.
- `lambda` and `xray`: Traces generated from AWS lambda functions instrumented with X-Ray or Datadog libraries.

Read more about ingestion reasons in the [Ingestion Mechanisms documentation](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_mechanisms/).

## Further Reading{% #further-reading %}

- [Ingestion Control Page](https://docs.datadoghq.com/tracing/trace_pipeline/ingestion_controls/)
