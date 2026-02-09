# Source: https://docs.lunary.ai/docs/integrations/javascript/vercel-ai-sdk.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Vercel AI SDK

> Send Vercel AI SDK telemetry to Lunary via OpenTelemetry.

Lunary accepts OpenTelemetry traces, so you can forward the spans that the Vercel AI SDK
emits to Lunary without writing a custom logger. This guide walks through the minimal
changes required for a Next.js or Node.js app that already uses the AI SDK.

## Prerequisites

* A Lunary project with its public key copied from **Settings → API Keys**.
* A Vercel AI SDK app running on Node.js 18+ with access to modify instrumentation files.
* Optional (Next.js ≤14): `experimental.instrumentationHook` enabled in `next.config.mjs`.

## 1. Enable Vercel's OpenTelemetry instrumentation

Install the instrumentation helper if it is not already included in your project:

```bash  theme={null}
npm install @vercel/otel @opentelemetry/api
```

For Next.js, ensure `instrumentation.ts` exists at the project root (or inside `src/` if
you use that folder) and register OpenTelemetry:

```ts  theme={null}
// instrumentation.ts
import { registerOTel } from "@vercel/otel";

export function register() {
  registerOTel({ serviceName: "vercel-ai-with-lunary" });
}
```

If you target Next.js 14 or earlier, add the instrumentation hook in `next.config.mjs`:

```js  theme={null}
export default {
  experimental: {
    instrumentationHook: true,
  },
};
```

Vercel's helper wires the AI SDK to OpenTelemetry so spans are created whenever you call
`generateText`, `streamText`, or other AI SDK functions.citeturn5search1turn5search0

## 2. Point OpenTelemetry to Lunary

Configure the OTLP exporter to send traces to Lunary's managed collector. Using
environment variables keeps local and hosted deployments aligned:

```bash  theme={null}
# .env (or Vercel/Vault environment variables)
OTEL_EXPORTER_OTLP_ENDPOINT=https://api.lunary.ai
OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer ${LUNARY_PUBLIC_KEY}"
OTEL_RESOURCE_ATTRIBUTES="service.name=vercel-ai-app,deployment.environment=production"
```

If you prefer explicit code, supply Lunary's endpoint and headers when registering
OpenTelemetry:

```ts  theme={null}
// instrumentation.ts
import { registerOTel, OTLPHttpJsonTraceExporter } from "@vercel/otel";

export function register() {
  registerOTel({
    serviceName: "vercel-ai-with-lunary",
    traceExporter: new OTLPHttpJsonTraceExporter({
      url: "https://api.lunary.ai/v1/traces",
      headers: {
        Authorization: `Bearer ${process.env.LUNARY_PUBLIC_KEY}`,
      },
    }),
  });
}
```

Either approach sends OTLP/HTTP traces to Lunary using your project public key for
authentication. Resource attributes travel with every span and help Lunary group data by
service and environment.citeturn4search1turn5search1turn3search3

## 3. Emit AI spans with Lunary metadata

Telemetry remains an opt-in experimental flag in the AI SDK. Wrap the calls you want to
observe with `experimental_telemetry` and include metadata that Lunary can use for
filtering and trace grouping:

```ts  theme={null}
import { generateText } from "ai";
import { openai } from "@ai-sdk/openai";

export async function summarize(content: string, userId: string) {
  const result = await generateText({
    model: openai("gpt-5"),
    prompt: `Summarize:\n${content}`,
    experimental_telemetry: {
      isEnabled: true,
      functionId: "summarizer",
      metadata: {
        lunary_user_id: userId,
        thread_id: `thread-${userId}`,
      },
    },
  });

  return result.text;
}
```

Every traced invocation appears in Lunary with the function ID, custom metadata, tokens,
latency, and errors captured by the AI SDK spans.

## 4. Validate traces inside Lunary

Deploy or start your app locally and trigger the instrumented route. Open the Lunary
dashboard and visit **Observability → Traces** to confirm new spans tagged with your
`service.name` and metadata. From there you can drill into token usage, latency, and
prompt/response payloads per trace.
