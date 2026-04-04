# Source: https://www.traceloop.com/docs/openllmetry/integrations/splunk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with Splunk and OpenLLMetry

<Frame>
  <img src="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/splunk.png?fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=fd0d199e9157682c6f47e23e81bdee87" data-og-width="3416" width="3416" data-og-height="1516" height="1516" data-path="img/integrations/splunk.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/splunk.png?w=280&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=287442db9bbb6268873324a3e9073c0c 280w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/splunk.png?w=560&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=c94ebddccc4f482deb5ab90fadd3df28 560w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/splunk.png?w=840&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=d91f2a068a8dc46e427a3b037a2a93d3 840w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/splunk.png?w=1100&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=667b6debc31f4f8ce54495c9798fcbb8 1100w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/splunk.png?w=1650&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=64d8e3f4c2d8ca976fa30ec4dae70723 1650w, https://mintcdn.com/enrolla/-xQ9K52hAYrcQGvz/img/integrations/splunk.png?w=2500&fit=max&auto=format&n=-xQ9K52hAYrcQGvz&q=85&s=29d2acf8ab6da8f94b475891fbd9584f 2500w" />
</Frame>

Collecting and analyzing LLM traces in [Splunk Observability Cloud](https://www.splunk.com/en_us/products/observability.html) can be achieved by configuring the **TRACELOOP\_BASE\_URL** environment variable to point to the [Splunk OpenTelemetry Collector](https://github.com/signalfx/splunk-otel-collector/releases) OTLP endpoint.

Have the Collector run in agent or gateway mode and ensure the OTLP receiver is configured, see [Get data into Splunk Observability Cloud](https://docs.splunk.com/observability/en/gdi/get-data-in/get-data-in.html).

```yaml  theme={null}
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: "0.0.0.0:4317"
      http:
        endpoint: "0.0.0.0:4318"
```

Secondly, ensure the OTLP exporter is configured to send to Splunk Observability Cloud:

```yaml  theme={null}
exporters:
  # Traces
  sapm:
    access_token: "${SPLUNK_ACCESS_TOKEN}"
    endpoint: "https://ingest.${SPLUNK_REALM}.signalfx.com/v2/trace"
    sending_queue:
      num_consumers: 32
```

Thirdly, make sure `otlp` is defined in the traces pipeline:

```yaml  theme={null}
  pipelines:
    traces:
      receivers: [jaeger, otlp, sapm, zipkin]
      processors:
      - memory_limiter
      - batch
      #- resource/add_environment
      exporters: [sapm]
```

Finally, define the `TRACELOOP_BASE_URL` environment variable to point to the Splunk OpenTelemetry Collector OTLP endpoint:

```bash  theme={null}
TRACELOOP_BASE_URL=http://<splunk-otel-collector>:4318
```
