# Source: https://www.traceloop.com/docs/openllmetry/integrations/traceloop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# LLM Observability with Traceloop

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=2733424bcb797188846417e2516e50fe" data-og-width="3014" width="3014" data-og-height="1798" height="1798" data-path="img/trace/trace-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=c024b621caac98fb924006c3e2fdf3e2 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=ab9ba8134ba04bdfefb6a56c44f03256 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=637f82f9dd748f77b39a80591f34ab9d 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=b47f4145aad5d3ac1f78646d6b000b05 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=176db5b65b57b786248777ac9660de8f 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-light.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=fac61fd5dc7f341881afe09c4a25cc67 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=740795f397c532c9080a91ea521a3a7e" data-og-width="3024" width="3024" data-og-height="1806" height="1806" data-path="img/trace/trace-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=280&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=2146004180f5dce3c59c73da4e4445f1 280w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=560&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=277eb56b1e83c16a15de79612b490935 560w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=840&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=d64bec8d366115d0070c6ac5fdf34855 840w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=1100&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=c892fe1ad02e8b04c94171ebf5b7fbad 1100w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=1650&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=8625ee39f6877740038d00c9ca5d97a4 1650w, https://mintcdn.com/enrolla/UIxmLWs2sJDl37WW/img/trace/trace-dark.png?w=2500&fit=max&auto=format&n=UIxmLWs2sJDl37WW&q=85&s=966a935d28281d3b9e1944e97e8ea6c6 2500w" />
</Frame>

[Traceloop](https://app.traceloop.com) is a platform for observability and evaluation of LLM outputs.
It allows you to deploy changes to prompts and model configurations with confidence, without breaking existing functionality.

## Connecting OpenLLMetry to Traceloop directly

<Note>
  You need an API key to send traces to Traceloop. API keys are scoped to a specific **project** and **environment**.

  **To generate an API key:**

  1. Go to [Settings → Organization](https://app.traceloop.com/settings/api-keys)
  2. Click on your project (or create a new one)
  3. Select an environment (Development, Staging, Production, or custom)
  4. Click **Generate API key**
  5. **Copy the key immediately** - it won't be shown again after you close or reload the page

  [Detailed instructions →](/settings/managing-api-keys)
</Note>

Set the API key as an environment variable named `TRACELOOP_API_KEY`:

```bash  theme={null}
export TRACELOOP_API_KEY=your_api_key_here
```

Done! You'll get instant visibility into everything that's happening with your LLM.
If you're calling a vector DB, or any other external service or database, you'll also see it in the Traceloop dashboard.

<Tip>
  **Want to organize your data?** Learn about [Projects and Environments](/settings/projects-and-environments)
  to separate traces for different applications and deployment stages.
</Tip>

## Using an OpenTelemetry Collector

If you are using an [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/), you can route metrics and traces to Traceloop by simply adding an OTLP exporter to your collector configuration.

```yaml  theme={null}
receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4318
processors:
  batch:
exporters:
  otlphttp/traceloop:
    endpoint: "https://api.traceloop.com" # US instance
    headers:
      "Authorization": "Bearer <YOUR_API_KEY>"
service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/traceloop]
```

You can route OpenLLMetry to your collector by following the [OpenTelemetry Collector](/openllmetry/integrations/otel-collector) integration instructions.
