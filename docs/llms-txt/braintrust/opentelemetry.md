# Source: https://braintrust.dev/docs/integrations/sdk-integrations/opentelemetry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenTelemetry (OTel)

export const feature_0 = "OTel compatibility mode"

To set up Braintrust as an [OpenTelemetry](https://opentelemetry.io/docs/)
backend, you'll need to route the traces to Braintrust's OpenTelemetry endpoint,
set your API key, and specify a parent project or experiment.

Braintrust supports configuring OTel with our SDK, as well as libraries like [OpenLLMetry](https://github.com/traceloop/openllmetry) and the [Vercel AI SDK](https://sdk.vercel.ai/). You can also use OTel's built-in exporters to send traces to Braintrust if you don't want to install additional libraries or write code. OpenLLMetry supports a range of languages including Python, TypeScript, Java, and Go, so you can start logging to Braintrust from many different environments.

## Python SDK configuration

Install the Braintrust Python SDK with OpenTelemetry support:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install "braintrust[otel]"
  ```
</CodeGroup>

Configure these environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=your-api-key
BRAINTRUST_PARENT=project_name:my-otel-project

# If you are self-hosting Braintrust, set the URL of your hosted dataplane. You can omit this otherwise.
# BRAINTRUST_API_URL=https://api.braintrust.dev
```

For Python applications, use the `BraintrustSpanProcessor` for simplified configuration:

```python title="opentelemetry-braintrust.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os

from braintrust.otel import BraintrustSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

# Configure the global OTel tracer provider
provider = TracerProvider()
trace.set_tracer_provider(provider)

# Send spans to Braintrust.
provider.add_span_processor(BraintrustSpanProcessor())
```

For more advanced configuration, you can pass in the following arguments to `BraintrustSpanProcessor`:

* `api_key`: The API key to use for Braintrust. Defaults to the `BRAINTRUST_API_KEY` environment variable.
* `api_url`: The URL of the Braintrust API. Defaults to the `BRAINTRUST_API_URL` environment variable or `https://api.braintrust.dev` if not set.
* `parent`: The parent project or experiment to use for Braintrust. Defaults to the `BRAINTRUST_PARENT` environment variable.
* `filter_ai_spans`: Defaults to `False`. If `True`, only AI-related spans will be sent to Braintrust.
* `custom_filter`: A function that gives you fine-grained control over which spans are sent to Braintrust. It takes a span and returns a boolean. If `True`, the span will be sent to Braintrust. If `False`, the span will be dropped. If `None`, don't influence the sampling decision.

## TypeScript SDK configuration

<Note>
  Starting with v1.0, OpenTelemetry functionality has been moved to the separate `@braintrust/otel` [npm package](https://www.npmjs.com/package/@braintrust/otel). This solves ESM build issues in Next.js (edge), Cloudflare Workers, Bun, and TanStack applications, and adds support for both OpenTelemetry v1 and v2.

  If you're upgrading from v0.x, see the [upgrade guide](/reference/sdks/typescript-upgrade-guide) for migration instructions.
</Note>

Install the [Braintrust TypeScript SDK](/reference/sdks/typescript) with the following OpenTelemetry dependencies:

<CodeGroup>
  ```bash Typescript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  # pnpm
  pnpm add braintrust @braintrust/otel @opentelemetry/api @opentelemetry/sdk-node @opentelemetry/sdk-trace-base
  # npm
  npm install braintrust @braintrust/otel @opentelemetry/api @opentelemetry/sdk-node @opentelemetry/sdk-trace-base
  ```
</CodeGroup>

For TypeScript/JavaScript applications, use the `BraintrustSpanProcessor` with NodeSDK:

```typescript title="opentelemetry-braintrust.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { NodeSDK } from "@opentelemetry/sdk-node";
import { BraintrustSpanProcessor } from "@braintrust/otel";

const sdk = new NodeSDK({
  serviceName: "my-service",
  spanProcessor: new BraintrustSpanProcessor({
    parent: "project_name:your-project-name",
  }),
});

sdk.start();
```

Or configure it manually with a custom tracer provider:

```typescript title="opentelemetry-braintrust.ts" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { BasicTracerProvider } from "@opentelemetry/sdk-trace-base";
import { trace } from "@opentelemetry/api";
import { BraintrustSpanProcessor } from "@braintrust/otel";

trace.setGlobalTracerProvider(
  new BasicTracerProvider({
    spanProcessors: [
      new BraintrustSpanProcessor({
        parent: "project_name:your-project-name",
      }),
    ],
  }),
);
```

For more advanced configuration, you can pass in the following arguments to `BraintrustSpanProcessor`:

* `apiKey`: The API key to use for Braintrust. Defaults to the `BRAINTRUST_API_KEY` environment variable.
* `apiUrl`: The URL of the Braintrust API. Defaults to the `BRAINTRUST_API_URL` environment variable or `https://api.braintrust.dev` if not set.
* `parent`: The parent project or experiment to use for Braintrust. Defaults to the `BRAINTRUST_PARENT` environment variable.
* `filterAISpans`: Defaults to `false`. If `true`, only AI-related spans will be sent to Braintrust.
* `customFilter`: A function that gives you fine-grained control over which spans are sent to Braintrust. It takes a span and returns a boolean. If `true`, the span will be sent to Braintrust. If `false`, the span will be dropped. If `null`, don't influence the sampling decision.

## OTel compatibility mode

<Warning>
  {feature_0} is a beta feature.
</Warning>

OpenTelemetry compatibility mode allows seamless tracing between Braintrust SDKs and OTel. It works by generating OTel compatible span IDs and storing the current active span in OTel's context. It is useful if you are running evals that wrap OpenTelemetry-instrumented code or doing distributed tracing between processes that use each mode of tracing.

<Note>
  OTel compatibility mode requires the following versions of the Braintrust SDKs:

  * Python SDK: `braintrust[otel] >= 0.3.1`
  * TypeScript SDK: `braintrust >= 1.0.0` with `@braintrust/otel >= 0.1.0`

  **Important:** OTel compatibility mode updates the format of `span.export()`. All machines that read exported spans (via the `x-bt-parent` header or distributed tracing) must use these minimum versions. Upgrade them before enabling compatibility mode.
</Note>

<Tabs>
  <Tab title="Python">
    Install the required version of the Braintrust SDK and set the required environment variables:

    ```python Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    import os

    # Enable OTel compatibility before imports
    os.environ["BRAINTRUST_OTEL_COMPAT"] = "true"
    os.environ["BRAINTRUST_API_KEY"] = "<your-api-key>"

    from braintrust import Eval
    from braintrust.otel import BraintrustSpanProcessor
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider

    # Set up OTel tracing
    provider = TracerProvider()
    provider.add_span_processor(BraintrustSpanProcessor(parent="project_name:my-project"))
    trace.set_tracer_provider(provider)

    def task(input):
        tracer = trace.get_tracer(__name__)

        # This OTel span will nest under the Braintrust eval span
        with tracer.start_as_current_span("otel.task") as span:
            span.set_attribute("input", input)
            result = f"Processed: {input}"
            span.set_attribute("output", result)
            return result

    Eval(
        "OTEL Integration Example",
        data=[
            {"input": "test1", "expected": "Processed: test1"},
            {"input": "test2", "expected": "Processed: test2"},
        ],
        task=task,
    )
    ```
  </Tab>

  <Tab title="TypeScript">
    Install the required version of the Braintrust SDK and do the following:

    * Call `setupOtelCompat()` before creating any loggers or spans to allow spans from OTel and Braintrust to be grouped together.
    * Use `AsyncLocalStorageContextManager` to properly nest spans under their parent evaluation spans.

    ```typescript TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    import { BasicTracerProvider } from "@opentelemetry/sdk-trace-base";
    import { trace, context } from "@opentelemetry/api";
    import { AsyncLocalStorageContextManager } from "@opentelemetry/context-async-hooks";
    import { setupOtelCompat, BraintrustSpanProcessor } from "@braintrust/otel";

    // Setup context manager to group span
    const contextManager = new AsyncLocalStorageContextManager();
    contextManager.enable();
    context.setGlobalContextManager(contextManager);

    const braintrustProcessor = new BraintrustSpanProcessor({
      parent: "project_name:my-braintrust-project",
      filterAISpans: true,
    });

    const provider = new BasicTracerProvider({
      spanProcessors: [braintrustProcessor]
    });
    trace.setGlobalTracerProvider(provider);

    // Call this first, before any logger or span creation
    setupOtelCompat();

    async function task(input: string): Promise<string> {
      const tracer = trace.getTracer("my-service");

      return await tracer.startActiveSpan("otel.task", async (span) => {
        span.setAttribute("input", input);
        const result = `Processed: ${input}`;
        span.setAttribute("output", result);
        span.end();
        return result;
      });
    }

    await Eval("OTEL Integration Example", {
      data: [
        { input: "test1", expected: "Processed: test1" },
        { input: "test2", expected: "Processed: test2" },
      ],
      task,
    });
    ```
  </Tab>
</Tabs>

## Distributed tracing

<Note>
  Distributed tracing requires the following minimum versions:

  * Python SDK: `braintrust[otel] >= v0.3.5`
  * TypeScript SDK: `braintrust >= v1.0.0` with `@braintrust/otel >= v0.1.0`
</Note>

You can do distributed tracing between services instrumented with the Braintrust SDK and OpenTelemetry, either to create OpenTelemetry spans as children of Braintrust spans or to create Braintrust spans as children of OpenTelemetry spans.

<Note>
  These examples use `fetch` and `requests` to make HTTP requests. The trace context can also be transmitted via message queue metadata, gRPC metadata, or any other inter-service communication mechanism that supports custom headers.
</Note>

### Create OpenTelemetry spans as children of Braintrust spans

Export the Braintrust span context and use it to create an OpenTelemetry context.

<CodeGroup dropdown>
  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import braintrust
  from braintrust.otel import context_from_span_export
  from opentelemetry import context as otel_context
  from opentelemetry import trace

  # Service A: Create Braintrust span and export context
  project = braintrust.init_logger(project="my-project")
  with project.start_span(name="service_a") as span:
      exported = span.export()
      # Send to Service B via HTTP
      import requests

      requests.post("https://service-b/api", headers={"x-braintrust-context": exported})

  # Service B: Receive request and create OTel span as child
  exported = request.headers.get("x-braintrust-context")
  ctx = context_from_span_export(exported)
  token = otel_context.attach(ctx)
  try:
      tracer = trace.get_tracer(__name__)
      with tracer.start_as_current_span("service_b") as span:
          # This span is now a child of the Braintrust span
          pass
  finally:
      otel_context.detach(token)
  ```

  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { initLogger } from "braintrust";
  import { contextFromSpanExport } from "@braintrust/otel";
  import * as api from "@opentelemetry/api";

  // Service A: Create Braintrust span and export context
  const logger = initLogger({ projectName: "my-project" });
  await logger.traced(async (span) => {
    const exported = await span.export();
    // Send to Service B via HTTP
    await fetch("https://service-b/api", {
      headers: { "x-braintrust-context": exported },
    });
  });

  // Service B: Receive request and create OTel span as child
  const exported = req.headers.get("x-braintrust-context");
  const ctx = contextFromSpanExport(exported);
  await api.context.with(ctx, async () => {
    const tracer = api.trace.getTracer("service-b");
    await tracer.startActiveSpan("service_b", async (span) => {
      // This span is now a child of the Braintrust span
      span.end();
    });
  });
  ```
</CodeGroup>

### Create Braintrust spans as children of OpenTelemetry spans

Propagate the OpenTelemetry context using W3C Trace Context headers.

<CodeGroup>
  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust.otel import add_span_parent_to_baggage, parent_from_headers
  from opentelemetry import trace
  from opentelemetry.propagate import inject

  # Service A: Create OTel span and export headers
  tracer = trace.get_tracer(__name__)
  with tracer.start_as_current_span("service_a") as span:
      # Add Braintrust parent to baggage for propagation
      add_span_parent_to_baggage(span)

      # Export W3C trace context headers and send to Service B
      headers = {}
      inject(headers)
      import requests

      requests.post("https://service-b/api", headers=headers)

  # Service B: Receive request and create Braintrust span as child
  parent = parent_from_headers(request.headers)
  with project.start_span(name="service_b", parent=parent) as span:
      # This span is now a child of the OTel span
      pass
  ```

  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { addSpanParentToBaggage, parentFromHeaders } from "@braintrust/otel";
  import * as api from "@opentelemetry/api";

  // Service A: Create OTel span and export headers
  const tracer = api.trace.getTracer("service-a");
  await tracer.startActiveSpan("service_a", async (span) => {
    // Add Braintrust parent to baggage for propagation
    const ctx = addSpanParentToBaggage(span);

    // Export W3C trace context headers and send to Service B
    const headers: Record<string, string> = {};
    api.propagation.inject(ctx, headers);
    await fetch("https://service-b/api", { headers });

    span.end();
  });

  // Service B: Receive request and create Braintrust span as child
  const parent = parentFromHeaders(req.headers);
  await logger.traced(
    async (span) => {
      // This span is now a child of the OTel span
    },
    { name: "service_b", parent },
  );
  ```
</CodeGroup>

## OTLP configuration

If you are using a different language or want to use pure OTel code, you can set up the OpenTelemetry Protocol Exporter (OTLP) to send traces to Braintrust.

Once you set up an [OTLP exporter](https://opentelemetry.io/docs/languages/js/exporters/) to send traces to Braintrust, we automatically
convert LLM calls into Braintrust `LLM` spans, which
can be saved as [prompts](/deploy/prompts)
and evaluated in the [playground](/evaluate/playgrounds).

For JavaScript/TypeScript applications, you can use the `BraintrustExporter` directly:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { BatchSpanProcessor } from "@opentelemetry/sdk-trace-base";
import { BraintrustExporter } from "@braintrust/otel";

const exporter = new BraintrustExporter({
  apiKey: "your-api-key",
  parent: "project_name:your-project",
  filterAISpans: true,
});

const processor = new BatchSpanProcessor(exporter);
```

For collectors that use the [OpenTelemetry SDK](https://opentelemetry.io/docs/languages/) to export traces, set the
following environment variables:

```
OTEL_EXPORTER_OTLP_ENDPOINT=https://api.braintrust.dev/otel
OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer <Your API Key>, x-bt-parent=project_id:<Your Project ID>"
```

<Note>
  The trace endpoint URL is `https://api.braintrust.dev/otel/v1/traces`. If your exporter
  uses signal-specific environment variables, you'll need to set the full path:
  `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://api.braintrust.dev/otel/v1/traces`
</Note>

<Note>
  If you're self-hosting Braintrust, substitute your stack's Universal API URL. For example:
  `OTEL_EXPORTER_OTLP_ENDPOINT=https://dfwhllz61x709.cloudfront.net/otel`
</Note>

The `x-bt-parent` header sets the trace's parent project or experiment. You can use
a prefix like `project_id:`, `project_name:`, or `experiment_id:` here, or pass in
a [span slug](/instrument/custom-tracing#distributed-tracing)
(`span.export()`) to nest the trace under a span within the parent object.

<Note>
  To find your project ID, navigate to your project's configuration page and find the **Copy Project ID** button at the bottom of the page.
</Note>

## Vercel AI SDK

The [Vercel AI SDK](https://sdk.vercel.ai) natively supports OpenTelemetry and works out of the box with Braintrust, either
via Next.js or Node.js.

### Next.js

If you are using Next.js, use the Braintrust exporter with `@vercel/otel`:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { registerOTel } from "@vercel/otel";
import { BraintrustExporter } from "@braintrust/otel";

// In your instrumentation.ts file
export function register() {
  registerOTel({
    serviceName: "my-braintrust-app",
    traceExporter: new BraintrustExporter({
      parent: "project_name:your-project-name",
      filterAISpans: true, // Only send AI-related spans
    }),
  });
}
```

Traced LLM calls will appear under the Braintrust project or experiment provided in the `parent` field.

When you call the AI SDK, make sure to set `experimental_telemetry`:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
const result = await generateText({
  model: openai("gpt-4o-mini"),
  prompt: "What is 2 + 2?",
  experimental_telemetry: {
    isEnabled: true,
    metadata: {
      query: "weather",
      location: "San Francisco",
    },
  },
});
```

<Note>
  The integration supports streaming functions like `streamText`. Each streamed call will produce `ai.streamText` spans in Braintrust.

  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { openai } from "@ai-sdk/openai";
  import { streamText } from "ai";

  export async function POST(req: Request) {
    const { prompt } = await req.json();

    const result = await streamText({
      model: openai("gpt-4o-mini"),
      prompt,
      experimental_telemetry: { isEnabled: true },
    });

    return result.toDataStreamResponse();
  }
  ```
</Note>

### Node.js

If you are using Node.js without a framework, you must configure the `NodeSDK` directly. Here, it's more straightforward
to use the `BraintrustSpanProcessor`.

First, install the necessary dependencies:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npm install ai @ai-sdk/openai braintrust @braintrust/otel @opentelemetry/sdk-node @opentelemetry/sdk-trace-base zod
```

Then, set up the OpenTelemetry SDK:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { NodeSDK } from "@opentelemetry/sdk-node";
import { generateText, tool } from "ai";
import { openai } from "@ai-sdk/openai";
import { z } from "zod";
import { BraintrustSpanProcessor } from "@braintrust/otel";

const sdk = new NodeSDK({
  spanProcessors: [
    new BraintrustSpanProcessor({
      parent: "project_name:your-project-name",
      filterAISpans: true,
    }),
  ],
});

sdk.start();

async function main() {
  const result = await generateText({
    model: openai("gpt-4o-mini"),
    messages: [
      {
        role: "user",
        content: "What are my orders and where are they? My user ID is 123",
      },
    ],
    tools: {
      listOrders: tool({
        description: "list all orders",
        parameters: z.object({ userId: z.string() }),
        execute: async ({ userId }) =>
          `User ${userId} has the following orders: 1`,
      }),
      viewTrackingInformation: tool({
        description: "view tracking information for a specific order",
        parameters: z.object({ orderId: z.string() }),
        execute: async ({ orderId }) =>
          `Here is the tracking information for ${orderId}`,
      }),
    },
    experimental_telemetry: {
      isEnabled: true,
      functionId: "my-awesome-function",
      metadata: {
        something: "custom",
        someOtherThing: "other-value",
      },
    },
    maxSteps: 10,
  });

  await sdk.shutdown();
}

main().catch(console.error);
```

## Manual tracing

If you want to log LLM calls directly to the OTel endpoint, you can set up a custom OpenTelemetry tracer and add the appropriate attributes to your spans. This gives you fine-grained control over what data gets logged.

Braintrust implements the [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/). When you send traces with these attributes, they are automatically mapped to Braintrust fields.

| Attribute                        | Braintrust Field            | Description                                                                                                                                                                                                                       |
| -------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gen_ai.input.messages`          | `input`                     | The chat history provided to the model as an input. Messages must be structured according to the [OpenTelemetry GenAI Input messages JSON schema](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-input-messages.json). |
| `gen_ai.prompt`                  | `input`                     | User message (string). If you have an array of messages, you'll need to use `gen_ai.prompt_json` (see below) or set flattened attributes like `gen_ai.prompt.0.role` or `gen_ai.prompt.0.content`.                                |
| `gen_ai.prompt_json`             | `input`                     | A JSON-serialized string containing an array of [OpenAI messages](https://platform.openai.com/docs/api-reference/chat/create).                                                                                                    |
| `gen_ai.output.messages`         | `output`                    | Messages returned by the model. Messages must be structured according to the [OpenTelemetry GenAI Output messages JSON schema](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-output-messages.json).                   |
| `gen_ai.completion`              | `output`                    | Assistant message (string). Note that if you have an array of messages, you'll need to use `gen_ai.completion_json` (see below) or set flattened attributes like `gen_ai.completion.0.role` or `gen_ai.completion.0.content`.     |
| `gen_ai.completion_json`         | `output`                    | A JSON-serialized string containing an array of [OpenAI messages](https://platform.openai.com/docs/api-reference/chat/create).                                                                                                    |
| `gen_ai.request`                 | `metadata.*`                | A JSON object or flattened attributes containing model parameters. The `model` parameter is cleaned of provider prefixes (e.g., "openai/gpt-4o" becomes "gpt-4o").                                                                |
| `gen_ai.request.model`           | `metadata.model`            | The model name (e.g. "gpt-4o"). Provider prefixes like "openai/", "anthropic/", "google/" are automatically removed.                                                                                                              |
| `gen_ai.request.max_tokens`      | `metadata.max_tokens`       | Maximum tokens to generate.                                                                                                                                                                                                       |
| `gen_ai.request.temperature`     | `metadata.temperature`      | Sampling temperature.                                                                                                                                                                                                             |
| `gen_ai.request.top_p`           | `metadata.top_p`            | Nucleus sampling parameter.                                                                                                                                                                                                       |
| `gen_ai.operation.name`          | `span_attributes.type`      | The operation type. Value "chat" maps to type "llm", "execute\_tool" maps to type "tool".                                                                                                                                         |
| `gen_ai.agent.tools`             | `metadata.tools`            | A JSON-serialized array of tool names available to the agent. Tool names are automatically converted into tool definition objects with `type: "function"` and basic schemas.                                                      |
| `gen_ai.tool.name`               | `metadata.tools`            | The name of the tool being executed. Automatically converted into a tool definition object. Also sets `span_attributes.type` to "tool".                                                                                           |
| `gen_ai.usage`                   | `metrics.*`                 | A JSON object containing token usage. Can include `prompt_tokens`, `completion_tokens`, `input_tokens`, `output_tokens`, and `total_tokens`.                                                                                      |
| `gen_ai.usage.prompt_tokens`     | `metrics.prompt_tokens`     | Input tokens (preferred field name).                                                                                                                                                                                              |
| `gen_ai.usage.completion_tokens` | `metrics.completion_tokens` | Output tokens (preferred field name).                                                                                                                                                                                             |
| `gen_ai.usage.input_tokens`      | `metrics.prompt_tokens`     | Input tokens (alternative field name, normalized to `prompt_tokens`).                                                                                                                                                             |
| `gen_ai.usage.output_tokens`     | `metrics.completion_tokens` | Output tokens (alternative field name, normalized to `completion_tokens`).                                                                                                                                                        |
| `gen_ai.usage.total_tokens`      | `metrics.tokens`            | Total tokens (normalized to `tokens`). If not provided, automatically calculated from `prompt_tokens` + `completion_tokens`.                                                                                                      |

You can also use the `braintrust` namespace to set fields in Braintrust directly:

| Attribute                    | Braintrust Field  | Notes                                                                                                                                                                                                                                                                             |
| ---------------------------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `braintrust.input`           | `input`           | Typically a single user message (string). If you have an array of messages, use `braintrust.input_json` instead (see below) or set flattened attributes like `braintrust.input.0.role` or `braintrust.input.0.content`.                                                           |
| `braintrust.input_json`      | `input`           | A JSON-serialized string containing an array of [OpenAI messages](https://platform.openai.com/docs/api-reference/chat/create).                                                                                                                                                    |
| `braintrust.output`          | `output`          | Typically a single assistant message (string). If you have an array of messages, use `braintrust.output_json` instead (see below) or set flattened attributes like `braintrust.output.0.role` or `braintrust.output.0.content`.                                                   |
| `braintrust.output_json`     | `output`          | A JSON-serialized string containing an array of [OpenAI messages](https://platform.openai.com/docs/api-reference/chat/create).                                                                                                                                                    |
| `braintrust.metadata`        | `metadata`        | A JSON-serialized dictionary with string keys. Alternatively, you can use flattened attribute names, like `braintrust.metadata.model` or `braintrust.metadata.temperature`. If you include `tools`, you must provide full tool definition objects.                                |
| `braintrust.metrics`         | `metrics`         | A JSON-serialized dictionary with string keys. Alternatively, you can use flattened attribute names, like `braintrust.metrics.prompt_tokens` or `braintrust.metrics.completion_tokens`.                                                                                           |
| `braintrust.scores`          | `scores`          | A JSON-serialized dictionary with string keys, where values are scores for the span. Alternatively, you can use flattened attribute names, like `braintrust.scores.accuracy` or `braintrust.scores.relevance`.                                                                    |
| `braintrust.expected`        | `expected`        | The expected output for the span. Can be any value (string, number, object, etc.).                                                                                                                                                                                                |
| `braintrust.expected_json`   | `expected`        | A JSON-serialized string containing the expected output. Use this when you need to pass complex objects or arrays as the expected value.                                                                                                                                          |
| `braintrust.tags`            | `tags`            | An array of strings that can be set on any span. Tags from all spans in a trace are aggregated together.                                                                                                                                                                          |
| `braintrust.span_attributes` | `span_attributes` | A JSON-serialized dictionary with string keys. Alternatively, you can use flattened attribute names, like `braintrust.span_attributes.type` or `braintrust.span_attributes.name`. The `type` field can be one of: `"llm"`, `"task"`, `"tool"`, `"eval"`, `"score"`, `"function"`. |

Fields mapped from `braintrust.*` attributes are deleted and translated into Braintrust's native format.

### GenAI Events

In addition to attributes, Braintrust also processes GenAI events on spans to extract input/output messages. These events follow the [OpenTelemetry GenAI semantic conventions for events](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/):

| Event Name                 | Field    | Description                                                                                                                    |
| -------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `gen_ai.user.message`      | `input`  | User message event. Content is extracted from the `content` attribute (supports both string and JSON array format).            |
| `gen_ai.system.message`    | `input`  | System message event. Content is extracted from the `content` attribute.                                                       |
| `gen_ai.choice`            | `output` | Model response event. Message is extracted from the `message` attribute and can include both text content and tool calls.      |
| `gen_ai.assistant.message` | `output` | Assistant message event. Content is extracted from the `content` attribute.                                                    |
| `gen_ai.tool.message`      | `input`  | Tool result event. Content is extracted from the `content` attribute and associated with the tool call via the `id` attribute. |

Events are processed in chronological order and combined with attribute-based messages to provide a complete view of the conversation flow.

Here's an example of how to set up manual tracing:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import json
import os

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

BRAINTRUST_API_URL = os.environ.get("BRAINTRUST_API_URL", "https://api.braintrust.dev")
BRAINTRUST_API_KEY = os.environ.get("BRAINTRUST_API_KEY", "<Your API Key>")
PROJECT_ID = "<Your Project ID>"

provider = TracerProvider()
processor = BatchSpanProcessor(
    OTLPSpanExporter(
        endpoint=f"{BRAINTRUST_API_URL}/otel/v1/traces",
        headers={"Authorization": f"Bearer {BRAINTRUST_API_KEY}", "x-bt-parent": f"project_id:{PROJECT_ID}"},
    )
)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Export a span with flattened attribute names.
with tracer.start_as_current_span("GenAI Attributes") as span:
    span.set_attribute("gen_ai.prompt.0.role", "system")
    span.set_attribute("gen_ai.prompt.0.content", "You are a helpful assistant.")
    span.set_attribute("gen_ai.prompt.1.role", "user")
    span.set_attribute("gen_ai.prompt.1.content", "What is the capital of France?")

    span.set_attribute("gen_ai.completion.0.role", "assistant")
    span.set_attribute("gen_ai.completion.0.content", "The capital of France is Paris.")

    span.set_attribute("gen_ai.request.model", "gpt-4o-mini")
    span.set_attribute("gen_ai.request.temperature", 0.5)
    span.set_attribute("gen_ai.usage.prompt_tokens", 10)
    span.set_attribute("gen_ai.usage.completion_tokens", 30)

# Export a span using JSON-serialized attributes.
with tracer.start_as_current_span("GenAI JSON-Serialized Attributes") as span:
    span.set_attribute(
        "gen_ai.prompt_json",
        json.dumps(
            [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is the capital of Italy?"},
            ]
        ),
    )
    span.set_attribute(
        "gen_ai.completion_json",
        json.dumps(
            [
                {"role": "assistant", "content": "The capital of Italy is Rome."},
            ]
        ),
    )

# Export a span using the `braintrust` namespace.
with tracer.start_as_current_span("Braintrust Attributes") as span:
    span.set_attribute("braintrust.input.0.role", "system")
    span.set_attribute("braintrust.input.0.content", "You are a helpful assistant.")
    span.set_attribute("braintrust.input.1.role", "user")
    span.set_attribute("braintrust.input.1.content", "What is the capital of Libya?")

    span.set_attribute("braintrust.output.0.role", "assistant")
    span.set_attribute("braintrust.output.0.content", "The capital of Libya is Tripoli.")

    span.set_attribute("braintrust.metadata.model", "gpt-4o-mini")
    span.set_attribute("braintrust.metadata.country", "Libya")
    span.set_attribute("braintrust.metrics.prompt_tokens", 10)
    span.set_attribute("braintrust.metrics.completion_tokens", 20)

# Export a span using JSON-serialized `braintrust` attributes.
with tracer.start_as_current_span("Braintrust JSON-Serialized Attributes") as span:
    span.set_attribute(
        "braintrust.input_json",
        json.dumps(
            [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is the capital of Argentina?"},
            ]
        ),
    )
    span.set_attribute(
        "braintrust.output_json",
        json.dumps(
            [
                {"role": "assistant", "content": "The capital of Argentina is Buenos Aires."},
            ]
        ),
    )
    span.set_attribute(
        "braintrust.metadata",
        json.dumps({"model": "gpt-4o-mini", "country": "Argentina"}),
    )
    span.set_attribute(
        "braintrust.metrics",
        json.dumps({"prompt_tokens": 15, "completion_tokens": 45}),
    )
    span.set_attribute(
        "braintrust.expected_json",
        json.dumps([{"role": "assistant", "content": "The capital of Argentina is Buenos Aires."}]),
    )
    span.set_attribute(
        "braintrust.scores",
        json.dumps({"accuracy": 1.0, "relevance": 0.95}),
    )
```

## Troubleshooting

### Why are my traces not showing up?

There are a few common reasons why your traces may not show up in Braintrust:

* Braintrust's logs table only shows traces that have a root span (i.e. `span_parents` is empty). If you only send children
  spans, they will not appear in the logs table. A common reason for this is only sending spans to Braintrust which have a
  `traceparent` header. To fix this, make sure to send a root span for every trace you want to appear in the UI.
* If you are self-hosting Braintrust, make sure you **do not** use `https://api.braintrust.dev` and instead use your custom
  API URL as the `OTLP_ENDPOINT`, for example `https://dfwhllz61x709.cloudfront.net/otel`.
* You must explicitly set up OpenTelemetry in your application. If you're using Next.js, then follow the [Next.js OpenTelemetry guide](https://nextjs.org/docs/app/guides/open-telemetry).
  If you are using Node.js without a framework, then follow [this example](https://github.com/vercel/ai/blob/main/examples/ai-core/src/telemetry/stream-text.ts) to set up a basic exporter.
