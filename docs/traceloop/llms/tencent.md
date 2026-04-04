# Source: https://www.traceloop.com/docs/openllmetry/integrations/tencent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with Tencent APM and OpenLLMetry

[Tencent APM](https://console.tencentcloud.com/apm), also known as `TAPM`, is a monitoring and observability platform that provides a comprehensive view of your application's performance and behavior.

Tencent APM natively supports OpenTelemetry, so you can use OpenLLMetry to trace your applications.

<Frame>
  <img src="https://mintcdn.com/enrolla/GnqeYuB5cchQKSek/img/integrations/tencent.png?fit=max&auto=format&n=GnqeYuB5cchQKSek&q=85&s=bce312dcae554692a83799b54ef5bace" data-og-width="3454" width="3454" data-og-height="1986" height="1986" data-path="img/integrations/tencent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/GnqeYuB5cchQKSek/img/integrations/tencent.png?w=280&fit=max&auto=format&n=GnqeYuB5cchQKSek&q=85&s=b4bcb1e54a5a7e479d45823016af3dd0 280w, https://mintcdn.com/enrolla/GnqeYuB5cchQKSek/img/integrations/tencent.png?w=560&fit=max&auto=format&n=GnqeYuB5cchQKSek&q=85&s=73e8010dde2ce1e45d1e5fa604333c0f 560w, https://mintcdn.com/enrolla/GnqeYuB5cchQKSek/img/integrations/tencent.png?w=840&fit=max&auto=format&n=GnqeYuB5cchQKSek&q=85&s=1862b0b428e3d4e3d9e2497c4172b652 840w, https://mintcdn.com/enrolla/GnqeYuB5cchQKSek/img/integrations/tencent.png?w=1100&fit=max&auto=format&n=GnqeYuB5cchQKSek&q=85&s=08bb634502fa0ecd244beab2a5d145cd 1100w, https://mintcdn.com/enrolla/GnqeYuB5cchQKSek/img/integrations/tencent.png?w=1650&fit=max&auto=format&n=GnqeYuB5cchQKSek&q=85&s=5bc962374dbdecf82afdc5249375741e 1650w, https://mintcdn.com/enrolla/GnqeYuB5cchQKSek/img/integrations/tencent.png?w=2500&fit=max&auto=format&n=GnqeYuB5cchQKSek&q=85&s=55bfdb3a8467121c8f051fc17881db0e 2500w" />
</Frame>

To integrate OpenLLMetry with Tencent APM, you'll need to configure your tracing endpoint and authentication:

```bash  theme={null}
TRACELOOP_BASE_URL="<TAPM_ENDPOINT>" # Use port `55681` rather than `4317` as the default port.
TRACELOOP_HEADERS="Authorization=Bearer%20<TAPM_TOKEN>" # header values in env variables must be URL‑encoded.
```

Tencent APM defaults to using port `4317` for the gRPC exporter, and we recommend using port `55681` instead here, which is the HTTP exporter port.
