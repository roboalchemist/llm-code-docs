# Source: https://braintrust.dev/docs/cookbook/recipes/OTEL-logging.md

# Using OpenTelemetry for LLM observability

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/OTEL-logging/OTEL-logging.mdx) by [Ornella Altunyan](https://twitter.com/ornelladotcom) on 2024-10-31</div>

[OpenTelemetry](https://opentelemetry.io/docs/) (OTel) is an open-source observability framework designed to help developers collect, process, and export telemetry data from their applications for performance monitoring and debugging. It’s used by popular libraries like the [Vercel AI SDK](https://sdk.vercel.ai/), [LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/observability/), and [Traceloop OpenLLMetry](https://www.traceloop.com/docs) for observability in AI applications. OTel support extends to many programming languages including Python, TypeScript, Java, and Go.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/otel.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=521682a208916c54ffecc973c633f691" alt="Popular AI SDKs -> OTel -> traces" data-og-width="2400" width="2400" data-og-height="1261" height="1261" data-path="cookbook/assets/OTEL-logging/otel.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/otel.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=50cade7305388cf8dcccfd819a2dc6aa 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/otel.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=7cc3e120e4b179911a4514d0137f4e5f 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/otel.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1d611018dd693d7c3d85046fb42939c1 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/otel.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=0d00a62f22c2738f7a7d8995130d0311 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/otel.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=8c3812707fb0122500b17014ec51f0e0 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/otel.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=6f4df202a885972f5a642c9086b5b551 2500w" />

In Braintrust, we enable observability in AI applications through [**logging**](/core/logs). Logs are the recorded data and metadata from an AI routine — we record the inputs and outputs of your LLM calls to help you understand and debug your application. We want to make it simple for you to log to Braintrust from many different environments, so we defined a way to set up Braintrust as an OpenTelemetry backend. This guide will walk you through how to log to Braintrust from a sample project built with the Vercel AI SDK.

## Getting started

We’ll use the [Automatic Multiple Tool Steps Preview](https://github.com/vercel-labs/ai-sdk-preview-roundtrips) sample app from Vercel to demonstrate how simple it is to log to Braintrust, even if you have multiple steps and tool calls in your application.

To get started, you’ll need Braintrust and OpenAI accounts, along with their corresponding API keys, and the [npm](https://docs.npmjs.com/cli/init) and [create-next-app](https://github.com/vercel/next.js/tree/canary/packages/create-next-app) libraries installed locally.

First, bootstrap the example:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npx create-next-app --example https://github.com/vercel-labs/ai-sdk-preview-roundtrips ai-sdk-preview-roundtrips-example
```

Then, we’ll need to create a `.env` file to set the required environment variables. Start by adding your OpenAI API key:

```
OPENAI_API_KEY=<your-api-key>
```

<Note>
  You can also use the OpenAI API by adding your Braintrust API key and using
  the Braintrust [AI Proxy](/guides/proxy).
</Note>

## Setting up OTel

To set up Braintrust as an [**OpenTelemetry**](https://opentelemetry.io/docs/) backend, you'll use the `BraintrustSpanProcessor` which handles all the configuration automatically. First, install the required dependencies:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
npm install braintrust @braintrust/otel @opentelemetry/sdk-node
```

Then add your Braintrust configuration to your `.env` file:

```
BRAINTRUST_API_KEY=<Your API Key>
BRAINTRUST_PARENT=project_name:<Your Project Name>
```

Replace `<Your API Key>` with your Braintrust API key, and `<Your Project Name>` with the name of the project in Braintrust where you'd like to store your logs.

<Note>
  The `BRAINTRUST_PARENT` environment variable sets the trace's parent project
  or experiment. You can use a prefix like `project_id:`, `project_name:`, or
  `experiment_id:` here, or pass in a [**span
  slug**](/guides/traces#distributed-tracing) (`span.export()`) to nest the
  trace under a span within the parent object.
</Note>

Create a new file called `instrumentation.ts` to set up the Braintrust span processor:

```tsx  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import { NodeSDK } from "@opentelemetry/sdk-node";
import { BraintrustSpanProcessor } from "@braintrust/otel";

const sdk = new NodeSDK({
  serviceName: "multi-step-tool-calls-demo",
  spanProcessors: [
    new BraintrustSpanProcessor({
      // The processor will automatically use BRAINTRUST_API_KEY and BRAINTRUST_PARENT
      // environment variables if not specified here
      filterAISpans: true, // Optional: filter to only AI-related spans
    }),
  ],
});

export function register() {
  sdk.start();
}
```

Then, configure Next.js telemetry by adding the following to your `next.config.mjs` file:

```
nextConfig.experimental = {
  instrumentationHook: true,
};
```

You can then use the `experimental_telemetry` option to enable telemetry on supported AI SDK function calls. In your `route.ts` file, add the `experimental_telemetry` parameter to your LLM call:

```tsx  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
export async function POST(request: Request) {
  const { messages } = await request.json();

  const stream = await streamText({
    model: openai("gpt-4o"),
    system: `\
      - you are a friendly package tracking assistant
      - your responses are concise
      - you do not ever use lists, tables, or bullet points; instead, you provide a single response
    `,
    messages: convertToCoreMessages(messages),
    maxSteps: 5,
    tools: {
      listOrders: {
        description: "list all orders",
        parameters: z.object({}),
        execute: async function ({}) {
          const orders = getOrders();
          return orders;
        },
      },
      viewTrackingInformation: {
        description: "view tracking information for a specific order",
        parameters: z.object({
          orderId: z.string(),
        }),
        execute: async function ({ orderId }) {
          const trackingInformation = getTrackingInformation({ orderId });
          await new Promise((resolve) => setTimeout(resolve, 500));
          return trackingInformation;
        },
      },
    },
    experimental_telemetry: {
      isEnabled: true,
      functionId: "multi-step-tool-calls-demo",
      metadata: { foo: "bar" },
    },
  });

  return stream.toDataStreamResponse();
}
```

You can also add additional metadata here to make your LLM calls easier to track, and they'll end up as metadata in the Braintrust span.

## Logging LLM requests in Braintrust

Run `npm install` to install the required dependencies, then `npm run dev` to launch the development server. Your app should be served on [`localhost:3000`](http://localhost:3000) or another available port.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/app-start.png?fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=1e0ef580f2c70972fec55dff613477b1" alt="App running" data-og-width="2722" width="2722" data-og-height="1882" height="1882" data-path="cookbook/assets/OTEL-logging/app-start.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/app-start.png?w=280&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=d1534a35e79c51846583873389cb1c25 280w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/app-start.png?w=560&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=0d00df181cbebbf0969463ed3c8d3f63 560w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/app-start.png?w=840&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=22b6c7bc799da1ad7c78cade5a900543 840w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/app-start.png?w=1100&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=c35abe907218c0f39c2b8b85e38a531c 1100w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/app-start.png?w=1650&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=08ebb31719333de013faa95e77fe0682 1650w, https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/app-start.png?w=2500&fit=max&auto=format&n=rJl2RwVgGaZvMrWa&q=85&s=60be64fa8a114a0ffd02db89df291c44 2500w" />

Open your Braintrust project to the **Logs** page, and select **What orders have shipped?** in your applications. You should be able to watch the logs filter in as your application makes HTTP requests and LLM calls.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/otel-demo.gif?s=777f592d047db8e02807297400180516" alt="LLM calls and logs side by side" data-og-width="3384" width="3384" data-og-height="1882" height="1882" data-path="cookbook/assets/OTEL-logging/otel-demo.gif" data-optimize="true" data-opv="3" />

Because this application is using multi-step streaming and tool calls, the logs are especially interesting. In Braintrust, logs consist of [traces](/guides/traces), which roughly correspond to a single request or interaction in your application. Traces consist of one or more spans, each of which corresponds to a unit of work in your application. In this example, each step and tool call is logged inside of its own span. This level of granularity makes it easier to debug issues, track user behavior, and collect data into datasets.

### Filtering your logs

Run a couple more queries in the app and notice the logs that are generated. Our app is logging both `GET` and `POST` requests, but we’re most interested in the `POST` requests since they contain our LLM calls. We can apply a filter using the [BTQL](/reference/btql) query `Name LIKE 'POST%'` so that we only see the traces we care about:

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/add-post-filter.gif?s=55acb2d27093d1952b7535113f20599b" alt="Filter using BTQL" data-og-width="2680" width="2680" data-og-height="1838" height="1838" data-path="cookbook/assets/OTEL-logging/add-post-filter.gif" data-optimize="true" data-opv="3" />

You should now have a list of traces for all the `POST` requests your app has made. Each contains the inputs and outputs of each LLM call in a span called `ai.streamText`. If you go further into the trace, you’ll also notice a span for each tool call.

<img src="https://mintcdn.com/braintrust/rJl2RwVgGaZvMrWa/cookbook/assets/OTEL-logging/spans.gif?s=82d66fb8ea73a9984271d0cc26f81b6e" alt="Expanding tool call and stream spans" data-og-width="1768" width="1768" data-og-height="1454" height="1454" data-path="cookbook/assets/OTEL-logging/spans.gif" data-optimize="true" data-opv="3" />

This is valuable data that can be used to evaluate the quality of accuracy of your application in Braintrust.

## Next steps

Now that you’re able to log your application in Braintrust, you can explore other workflows like:

* Adding your [tools](/core/functions/tools) to your library and using them in [experiments](/core/experiments) and the [playground](/core/playground)
* Creating [custom scorers](/core/functions/scorers) to assess the quality of your LLM calls
* Adding your logs to a [dataset](/core/datasets) and running evaluations comparing models and prompts


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt