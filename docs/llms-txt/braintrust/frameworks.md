# Source: https://braintrust.dev/docs/instrument/frameworks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrate frameworks

> Use existing framework integrations for automatic tracing

If you're using a popular AI framework or agent platform, Braintrust provides native integrations that automatically capture traces from your application. Braintrust supports both [agent frameworks](/integrations#agent-frameworks) like LangGraph, CrewAI, and Pydantic AI, as well as [SDK integrations](/integrations#sdk-integrations) like LangChain, OpenTelemetry, and Vercel AI SDK.

## When to use frameworks

Use framework integrations when:

* You're already using a supported framework or agent platform
* You want automatic tracing without wrapping individual clients
* Your application uses complex chains, agents, or multi-step workflows

Use [AI provider wrappers](/instrument/wrap-providers) when:

* You're making direct API calls without a framework
* You want simpler, more lightweight instrumentation

## LangChain

[LangChain](https://www.langchain.com/) is a framework for building applications with language models. Braintrust integrates using callback handlers to automatically trace chains, agents, and LLM calls. See the [LangChain integration guide](/integrations/sdk-integrations/langchain) for complete documentation.

<Steps>
  <Step title="Install packages">
    <CodeGroup>
      ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # pnpm
      pnpm add braintrust @braintrust/langchain-js @langchain/core
      # npm
      npm install braintrust @braintrust/langchain-js @langchain/core
      ```

      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pip install braintrust braintrust-langchain langchain-core
      ```
    </CodeGroup>
  </Step>

  <Step title="Add callback handler">
    Add the Braintrust callback handler to your LangChain application:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { BraintrustCallbackHandler } from "@braintrust/langchain-js";
      import { ChatOpenAI } from "@langchain/openai";
      import { initLogger } from "braintrust";

      initLogger({ projectName: "My Project" });

      const handler = new BraintrustCallbackHandler();

      async function main() {
        const model = new ChatOpenAI({ modelName: "gpt-4o" });

        // Pass the handler to capture traces
        await model.invoke("What is the capital of France?", {
          callbacks: [handler],
        });
      }

      main();
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from braintrust import init_logger
      from braintrust_langchain import BraintrustCallbackHandler, set_global_handler
      from langchain_openai import ChatOpenAI

      init_logger(project="My Project")

      handler = BraintrustCallbackHandler()
      set_global_handler(handler)  # Apply to all LangChain calls

      # Initialize your LangChain components
      model = ChatOpenAI()

      # Use LangChain as normal - all calls are automatically logged
      response = model.invoke("What is the capital of France?")
      ```
    </CodeGroup>

    The callback handler captures chains, agents, retrievers, and individual LLM calls automatically.
  </Step>
</Steps>

## OpenTelemetry

[OpenTelemetry](https://opentelemetry.io/) is an open standard for distributed tracing. Braintrust acts as an OpenTelemetry backend, accepting spans from any OTel-instrumented application. See the [OpenTelemetry integration guide](/integrations/sdk-integrations/opentelemetry) for complete documentation.

<Steps>
  <Step title="Install packages">
    <CodeGroup>
      ```bash TypeScript theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # pnpm
      pnpm add braintrust @braintrust/otel @opentelemetry/api @opentelemetry/sdk-node
      # npm
      npm install braintrust @braintrust/otel @opentelemetry/api @opentelemetry/sdk-node
      ```

      ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      pip install "braintrust[otel]"
      ```
    </CodeGroup>
  </Step>

  <Step title="Configure span processor">
    Route OpenTelemetry spans to Braintrust:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
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

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from braintrust.otel import BraintrustSpanProcessor
      from opentelemetry import trace
      from opentelemetry.sdk.trace import TracerProvider

      provider = TracerProvider()
      trace.set_tracer_provider(provider)

      # Send spans to Braintrust
      provider.add_span_processor(BraintrustSpanProcessor())
      ```
    </CodeGroup>
  </Step>

  <Step title="Set environment variables">
    Set these environment variables:

    ```bash .env theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
    BRAINTRUST_API_KEY=your-api-key
    BRAINTRUST_PARENT=project_name:my-project
    ```
  </Step>
</Steps>

## Other frameworks

Braintrust provides integrations for many popular frameworks:

<CardGroup cols={2}>
  <Card title="LangGraph" href="/integrations/agent-frameworks/langgraph" icon="git-graph">
    Build stateful, multi-agent applications
  </Card>

  <Card title="Vercel AI SDK" href="/integrations/sdk-integrations/vercel" icon="triangle">
    Stream AI responses in web applications
  </Card>

  <Card title="LlamaIndex" href="/integrations/sdk-integrations/llamaindex" icon="database">
    RAG and data-aware applications
  </Card>

  <Card title="DSPy" href="/integrations/sdk-integrations/dspy" icon="wand-sparkles">
    Programming with foundation models
  </Card>

  <Card title="Pydantic AI" href="/integrations/agent-frameworks/pydantic-ai" icon="shield-check">
    Type-safe agent framework
  </Card>

  <Card title="Instructor" href="/integrations/sdk-integrations/instructor" icon="graduation-cap">
    Structured outputs from LLMs
  </Card>

  <Card title="CrewAI" href="/integrations/agent-frameworks/crew-ai" icon="users">
    Multi-agent orchestration
  </Card>

  <Card title="Autogen" href="/integrations/agent-frameworks/autogen" icon="robot">
    Multi-agent conversation framework
  </Card>
</CardGroup>

See the [integrations overview](/integrations) for all supported frameworks.

## Next steps

* [Add custom tracing](/instrument/custom-tracing) for application logic beyond frameworks
* [Capture user feedback](/instrument/user-feedback) like thumbs up/down
* [View your logs](/observe/view-logs) in the Braintrust dashboard
