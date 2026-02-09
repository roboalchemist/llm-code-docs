# Source: https://www.traceloop.com/docs/openllmetry/integrations/oraclecloud.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with Oracle Cloud Infrastructure Application Performance Monitoring(APM) service

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/ociapm-traceexplorer.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=cf421f3f4b032ff07040a3c3abe33b03" data-og-width="1789" width="1789" data-og-height="822" height="822" data-path="img/integrations/ociapm-traceexplorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/ociapm-traceexplorer.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=e78e72ef46055f1d23b5d89fbfcd1835 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/ociapm-traceexplorer.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=09156e0ee7beb7af96b4ed360cdc3541 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/ociapm-traceexplorer.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=0d8cc9a0fdb8be19c5a7a0a77b75e0e9 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/ociapm-traceexplorer.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=a64de324ae064724f1a69d60d6999477 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/ociapm-traceexplorer.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=f1bc19b8361b8af8c486f87d3b7d4783 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/ociapm-traceexplorer.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=3c1d280f901c1b1dacc568f2219d7fd7 2500w" />
</Frame>

[Oracle Cloud Infrastructure Application Performance Monitoring(APM) service](https://docs.oracle.com/en-us/iaas/application-performance-monitoring/home.htm) natively supports and can ingest OpenTelemetry (OTLP) spans and metrics. Traceloop's OpenLLMetry library enables instrumenting LLM frameworks and applications in Open Telemetry format and can be routed to OCI Application Performance Monitoring for observability and evaluation of LLM applications.

## Initialize and export directly from application code

```python  theme={null}
APM_BASE_URL=“<OCI APM dataUploadEndpoint>/20200101/opentelemetry/private"
APM_DATA_KEY="dataKey <OCI APM Private Data Key>"
APM_SERVICE_NAME=“My LLM Service”
 
Traceloop.init(
    disable_batch=True,
    app_name=APM_SERVICE_NAME,
    api_endpoint=APM_BASE_URL,
    headers={
      "Authorization": APM_DATA_KEY
      }
)
```

## Initialize using environment variables

```bash  theme={null}
export TRACELOOP_BASE_URL=<OCI APM dataUploadEndpoint>/20200101/opentelemetry/private
export TRACELOOP_HEADERS="Authorization=dataKey <OCI APM Private Data Key>"
```

## Using an OpenTelemetry Collector

If you are using an OpenTelemetry Collector, you can route metrics and traces to OCI APM by simply adding an OTLP exporter to your collector configuration.

```yaml  theme={null}
receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4318
processors:
  batch:
exporters:
  otlphttp/apm:
    endpoint: "<OCI APM dataUploadEndpoint>/20200101/opentelemetry/private" 
    headers:
      "Authorization": "dataKey <OCI APM Private Data Key>"
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/apm]
```

For more information check out the [docs link](https://docs.oracle.com/en-us/iaas/application-performance-monitoring/doc/configure-open-source-tracing-systems.html#GUID-4D941163-F357-4839-8B06-688876D4C61F).
