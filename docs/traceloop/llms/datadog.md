# Source: https://www.traceloop.com/docs/openllmetry/integrations/datadog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with Datadog and OpenLLMetry

With datadog, there are 2 options - you can either export directly to a Datadog Agent in your cluster, or through an OpenTelemetry Collector (which requires that you deploy one in your cluster).

See also [Datadog documentation](https://docs.datadoghq.com/opentelemetry/).

Exporting directly to an agent is easiest.
To do that, first enable the OTLP HTTP collector in your agent configuration.
This depends on how you deployed your Datadog agent. For example, if you've used a Helm chart,
you can add the following to your `values.yaml`
(see [this](https://docs.datadoghq.com/opentelemetry/otlp_ingest_in_the_agent/?tab=kuberneteshelmvaluesyaml#enabling-otlp-ingestion-on-the-datadog-agent) for other options):

```yaml  theme={null}
otlp:
  receiver:
    protocols:
      http:
        enabled: true
```

Then, set this env var, and you're done!

```bash  theme={null}
TRACELOOP_BASE_URL=http://<datadog-agent-hostname>:4318
```
