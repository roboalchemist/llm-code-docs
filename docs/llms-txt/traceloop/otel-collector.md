# Source: https://www.traceloop.com/docs/openllmetry/integrations/otel-collector.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM observability with OpenTelemetry Collector

Since Traceloop is emitting standard OTLP HTTP (standard OpenTelemetry protocol), you can use any OpenTelemetry Collector, which gives you the flexibility
to then connect to any backend you want.
First, [deploy an OpenTelemetry Collector](https://opentelemetry.io/docs/kubernetes/operator/automatic/#create-an-opentelemetry-collector-optional)
in your cluster.
Then, point the output of the Traceloop SDK to the collector by setting:

```bash  theme={null}
TRACELOOP_BASE_URL=https://<opentelemetry-collector-hostname>:4318
```

You can connect your collector to Traceloop by following the instructions in the [Traceloop integration section](/openllmetry/integrations/traceloop#using-an-opentelemetry-collector).
