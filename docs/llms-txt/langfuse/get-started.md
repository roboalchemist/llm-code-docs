# Source: https://langfuse.com/docs/prompt-management/get-started.md

# Source: https://langfuse.com/docs/observability/get-started.md

# Source: https://langfuse.com/docs/prompt-management/get-started.md

# Source: https://langfuse.com/docs/observability/get-started.md

# Source: https://langfuse.com/docs/prompt-management/get-started.md

# Source: https://langfuse.com/docs/observability/get-started.md

---
description: Get started with LLM observability with Langfuse in minutes before diving into all platform features.
---

# Get Started with Tracing

This quickstart helps you to ingest your first trace in Langfuse.

<Steps>

## Get API keys

1.  [Create Langfuse account](https://cloud.langfuse.com/auth/sign-up) or [self-host Langfuse](/self-hosting).
2.  Create new API credentials in the project settings.

## Ingest your first trace

import { CopyAgentOnboardingPrompt } from "@/components/agentic-onboarding/CopyAgentOnboardingPrompt";








import { BookOpen, Code } from "lucide-react";

<LangTabs items={["OpenAI SDK (Python)", "OpenAI SDK (JS/TS)", "LangChain (Python)", "LangChain (JS/TS)", "Python SDK", "JS/TS SDK", "✨ Auto Install", "More integrations"]}>

<Tab>
{/* PYTHON - OPENAI*/}

Use the drop-in replacement for the OpenAI Python SDK to get full observability.




```bash
pip install langfuse
```

Add you Langfuse credentials as environment variables.


```bash filename=".env"
LANGFUSE_SECRET_KEY = "sk-lf-..."
LANGFUSE_PUBLIC_KEY = "pk-lf-..."
LANGFUSE_BASE_URL = "https://cloud.langfuse.com" # 🇪🇺 EU region
# LANGFUSE_BASE_URL = "https://us.cloud.langfuse.com" # 🇺🇸 US region
```



Change the import to use the OpenAI drop-in replacement.

```python
from langfuse.openai import openai
```

Use the OpenAI SDK as usual.

```python
completion = openai.chat.completions.create(
  name="test-chat",
  model="gpt-4o",
  messages=[
      {"role": "system", "content": "You are a very accurate calculator. You output only the result of the calculation."},
      {"role": "user", "content": "1 + 1 = "}],
  metadata={"someMetadataKey": "someValue"},
)
```


<Cards num={2}>
  <Card
    icon={<BookOpen />}
    title="Documentation"
    href="/integrations/model-providers/openai-py"
    arrow
  />
  <Card
    icon={
      <div className="w-6 h-6 dark:bg-white rounded-sm p-0.5 flex items-center justify-center">
        <img
          src="/images/integrations/colab_icon.png"
          className="w-full h-full object-contain"
        />
      </div>
    }
    title="Notebook"
    href="https://colab.research.google.com/github/langfuse/langfuse-docs/blob/main/cookbook/integration_openai_sdk.ipynb"
    arrow
  />
</Cards>

</Tab>

<Tab>
{/* JS/TS - OpenAI */}

Use the Langfuse wrapper function around the OpenAI JS/TS SDK for full observability.


**Install package**
```sh
npm install @langfuse/openai
```

**Add credentials**

Add your Langfuse credentials to your environment variables. Make sure that you have a `.env` file in your project root and a package like `dotenv` to load the variables.




```bash filename=".env"
LANGFUSE_SECRET_KEY = "sk-lf-..."
LANGFUSE_PUBLIC_KEY = "pk-lf-..."
LANGFUSE_BASE_URL = "https://cloud.langfuse.com" # 🇪🇺 EU region
# LANGFUSE_BASE_URL = "https://us.cloud.langfuse.com" # 🇺🇸 US region
```



**Initialize OpenTelemetry**


Install the OpenTelemetry Node SDK package:

```bash
npm install @opentelemetry/sdk-node
```

Create a `instrumentation.ts` file that initializes the OpenTelemetry `NodeSDK` and registers the `LangfuseSpanProcessor`.

```ts filename="instrumentation.ts" /LangfuseSpanProcessor/
import { NodeSDK } from "@opentelemetry/sdk-node";
import { LangfuseSpanProcessor } from "@langfuse/otel";

const sdk = new NodeSDK({
  spanProcessors: [new LangfuseSpanProcessor()],
});

sdk.start();
```

Import the `instrumentation.ts` file at the top of your application.

```ts filename="index.ts"
import "./instrumentation"; // Must be the first import
```



With your environment configured and OpenTelemetry initialized, call OpenAI SDK methods as usual from the wrapped client.

**Wrap OpenAI client**
```ts
import OpenAI from "openai";
import { observeOpenAI } from "@langfuse/openai";

const openai = observeOpenAI(new OpenAI());

const res = await openai.chat.completions.create({
    messages: [{ role: "system", content: "Tell me a story about a dog." }],
    model: "gpt-4o",
    max_tokens: 300,
});
```



<Cards num={2}>
  <Card
    icon={<BookOpen />}
    title="Documentation"
    href="/integrations/model-providers/openai-js"
    arrow
  />
  <Card
    icon={<Code />}
    title="Notebook"
    href="/guides/cookbook/js_integration_openai"
    arrow
  />
</Cards>

</Tab>

<Tab>
{/* LANGCHAIN */}

Use the Langfuse CallbackHandler to get full observability of the LangChain Python SDK.




```bash
pip install langfuse langchain-openai
```

Add your Langfuse credentials as environment variables.


```bash filename=".env"
LANGFUSE_SECRET_KEY = "sk-lf-..."
LANGFUSE_PUBLIC_KEY = "pk-lf-..."
LANGFUSE_BASE_URL = "https://cloud.langfuse.com" # 🇪🇺 EU region
# LANGFUSE_BASE_URL = "https://us.cloud.langfuse.com" # 🇺🇸 US region
```



Initialize the Langfuse callback handler.

```python
from langfuse.langchain import CallbackHandler

langfuse_handler = CallbackHandler()
```

Add the Langfuse callback handler to your chain.

```python {10}
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
 
llm = ChatOpenAI(model_name="gpt-4o")
prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
chain = prompt | llm
 
response = chain.invoke(
    {"topic": "cats"}, 
    config={"callbacks": [langfuse_handler]})
```


<Cards num={2}>
  <Card
    icon={<BookOpen />}
    title="Documentation"
    href="/integrations/frameworks/langchain"
    arrow
  />
  <Card
    icon={
      <div className="w-6 h-6 dark:bg-white rounded-sm p-0.5 flex items-center justify-center">
        <img
          src="/images/integrations/colab_icon.png"
          className="w-full h-full object-contain"
        />
      </div>
    }
    title="Notebook"
    href="https://colab.research.google.com/github/langfuse/langfuse-docs/blob/main/cookbook/integration_langchain.ipynb"
    arrow
  />
</Cards>

</Tab>

<Tab>
{/* LANGCHAIN (JS/TS) */}

Use the Langfuse CallbackHandler to get full observability of the LangChain JS/TS SDK.


```bash
npm install @langfuse/core @langfuse/langchain
```


Add your Langfuse credentials to your environment variables. Make sure that you have a `.env` file in your project root and a package like `dotenv` to load the variables.


```bash filename=".env"
LANGFUSE_SECRET_KEY = "sk-lf-..."
LANGFUSE_PUBLIC_KEY = "pk-lf-..."
LANGFUSE_BASE_URL = "https://cloud.langfuse.com" # 🇪🇺 EU region
# LANGFUSE_BASE_URL = "https://us.cloud.langfuse.com" # 🇺🇸 US region
```



With the environment variables set, we can now initialize the `langfuseSpanProcessor` which is passed to the main OpenTelemetry SDK that orchestrates tracing.

```ts
import { NodeSDK } from "@opentelemetry/sdk-node";
import { LangfuseSpanProcessor } from "@langfuse/otel";
 
const sdk = new NodeSDK({
  spanProcessors: [new LangfuseSpanProcessor()],
});
 
sdk.start();
```

Finally, initialize the Langfuse `CallbackHandler` and add it to your chain.

```typescript
import { CallbackHandler } from "@langfuse/langchain";
 
// Initialize the Langfuse CallbackHandler
const langfuseHandler = new CallbackHandler();
```

```typescript /{ callbacks: [langfuseHandler] }/
import { createAgent, tool } from "@langchain/core/agents";
import * as z from "zod";

const getWeather = tool(
  (input) => `It's always sunny in ${input.city}!`,
  {
    name: "get_weather",
    description: "Get the weather for a given city",
    schema: z.object({
      city: z.string().describe("The city to get the weather for"),
    }),
  }
);

const agent = createAgent({
  model: "openai:gpt-5-mini",
  tools: [getWeather],
});

console.log(
    await agent.invoke(
        { messages: [{ role: "user", content: "What's the weather in San Francisco?" }] }, 
        { callbacks: [langfuseHandler] }
    )
);
```



<Cards num={2}>
  <Card
    icon={<BookOpen />}
    title="Documentation"
    href="/integrations/frameworks/langchain"
    arrow
  />
  <Card
    icon={<Code />}
    title="Notebook"
    href="/guides/cookbook/js_integration_langchain"
    arrow
  />
</Cards>

</Tab>

<Tab>
{/* PYTHON SDK */}

Use the Langfuse Python SDK to wrap any LLM or Agent

```bash
pip install langfuse
```


```bash filename=".env"
LANGFUSE_SECRET_KEY = "sk-lf-..."
LANGFUSE_PUBLIC_KEY = "pk-lf-..."
LANGFUSE_BASE_URL = "https://cloud.langfuse.com" # 🇪🇺 EU region
# LANGFUSE_BASE_URL = "https://us.cloud.langfuse.com" # 🇺🇸 US region
```



There are three main ways of creating traces with the Python SDK:


<Tabs items={["Observe Decorator", "Context Managers", "Manual Observations"]}>

<Tab>
The `@observe` decorator is the simplest way to instrument your application. It is a function decorator that can be applied to any function.

It sets the current span in the context for automatic nesting of child spans and automatically ends it when the function returns. It also automatically captures the function name, arguments, and return value.

```python
from langfuse import observe, get_client

@observe
def my_function():
    return "Hello, world!" # Input/output and timings are automatically captured

my_function()

# Flush events in short-lived applications
langfuse = get_client()
langfuse.flush()
```

</Tab>

<Tab>
Context managers are the recommended way to instrument chunks of work in your application as they automatically handle the start and end of spans, and set the current span in the context for automatic nesting of child spans. They provide more control than the `@observe` decorator.

```python
from langfuse import get_client

langfuse = get_client()

# Create a span using a context manager
with langfuse.start_as_current_observation(as_type="span", name="process-request") as span:
    # Your processing logic here
    span.update(output="Processing complete")

    # Create a nested generation for an LLM call
    with langfuse.start_as_current_observation(as_type="generation", name="llm-response", model="gpt-3.5-turbo") as generation:
        # Your LLM call logic here
        generation.update(output="Generated response")

# All spans are automatically closed when exiting their context blocks


# Flush events in short-lived applications
langfuse.flush()
```

</Tab>

<Tab>
Manual observations give you control over when spans start and end and do not set the current span in the context for automatic nesting of child spans. You must explicitly call `.end()` when they're complete.

```python
from langfuse import get_client

langfuse = get_client()

# Create a span without a context manager
span = langfuse.start_span(name="user-request")

# Your processing logic here
span.update(output="Request processed")

# Child spans must be created using the parent span object
nested_span = span.start_span(name="nested-span")
nested_span.update(output="Nested span output")

# Important: Manually end the span
nested_span.end()

# Important: Manually end the parent span
span.end()

# Flush events in short-lived applications
langfuse.flush()
```

</Tab>
</Tabs>


<Cards num={1}>
  <Card
    icon={<BookOpen />}
    title="Documentation"
    href="/docs/sdk/python/sdk-v3"
    arrow
  />
</Cards>

</Tab>

<Tab>
{/* JS/TS SDK */}

Use the Langfuse JS/TS SDK to wrap any LLM or Agent


**Install package**
```sh
npm install @langfuse/tracing
```

**Add credentials**

Add your Langfuse credentials to your environment variables. Make sure that you have a `.env` file in your project root and a package like `dotenv` to load the variables.




```bash filename=".env"
LANGFUSE_SECRET_KEY = "sk-lf-..."
LANGFUSE_PUBLIC_KEY = "pk-lf-..."
LANGFUSE_BASE_URL = "https://cloud.langfuse.com" # 🇪🇺 EU region
# LANGFUSE_BASE_URL = "https://us.cloud.langfuse.com" # 🇺🇸 US region
```



**Initialize OpenTelemetry**


Install the OpenTelemetry Node SDK package:

```bash
npm install @opentelemetry/sdk-node
```

Create a `instrumentation.ts` file that initializes the OpenTelemetry `NodeSDK` and registers the `LangfuseSpanProcessor`.

```ts filename="instrumentation.ts" /LangfuseSpanProcessor/
import { NodeSDK } from "@opentelemetry/sdk-node";
import { LangfuseSpanProcessor } from "@langfuse/otel";

const sdk = new NodeSDK({
  spanProcessors: [new LangfuseSpanProcessor()],
});

sdk.start();
```

Import the `instrumentation.ts` file at the top of your application.

```ts filename="index.ts"
import "./instrumentation"; // Must be the first import
```



**Instrument application**

```ts filename="server.ts"
import { startActiveObservation, startObservation } from "@langfuse/tracing";

await startActiveObservation("user-request", async (span) => {
  span.update({
    input: { query: "What is the capital of France?" },
  });

  // This generation will automatically be a child of "user-request"
  const generation = startObservation(
    "llm-call",
    {
      model: "gpt-4",
      input: [{ role: "user", content: "What is the capital of France?" }],
    },
    { asType: "generation" },
  );

  // ... LLM call logic ...

  generation
    .update({
      output: { content: "The capital of France is Paris." },
    })
    .end();

  span.update({ output: "Successfully answered." });
});
```



<Cards num={2}>
  <Card
    icon={<BookOpen />}
    title="Documentation"
    href="/docs/sdk/typescript/guide"
    arrow
  />
  <Card
    icon={<Code />}
    title="Notebook"
    href="/docs/sdk/typescript/example-notebook"
    arrow
  />
</Cards>

</Tab>

<Tab>
{/* AUTO INSTALL */}

Use the agent mode of your editor to integrate Langfuse into your existing codebase.

<Callout type="warning" emoji="🤖">
  This might or might not work very well (depending on your code base). Please
  share any feedback or issues on [GitHub](/issues).
</Callout>

**1. Install the Langfuse Docs MCP Server (optional)**

The agent will use the Langfuse `searchLangfuseDocs` tool ([docs](/docs/docs-mcp)) to find the correct documentation for the integration you are looking for. This is optional, alternatively the agent can use its native websearch capabilities.


import { Button } from "@/components/ui/button";
import Link from "next/link";

<Tabs items={["Cursor", "Copilot (in VSCode)", "Claude Code", "Windsurf", "Other MCP Clients"]}>

<Tab>

Add Langfuse Docs MCP to Cursor via the one-click install:

<div className="flex gap-2 mt-3 mb-6">
  <Button asChild>
    <Link
      href="https://cursor.com/en/install-mcp?name=langfuse-docs&config=eyJ1cmwiOiJodHRwczovL2xhbmdmdXNlLmNvbS9hcGkvbWNwIn0%3D"
      target="_blank"
      rel="noopener noreferrer"
    >
      Install MCP Server in Cursor
    </Link>
  </Button>
</div>

<details>
<summary>Manual configuration</summary>

Add the following to your `mcp.json`:

```json
{
  "mcpServers": {
    "langfuse-docs": {
      "url": "https://langfuse.com/api/mcp"
    }
  }
}
```

</details>

</Tab>

<Tab>

Add Langfuse Docs MCP to Copilot in VSCode via the one-click install:

<div className="flex gap-2 mt-3 mb-6">
  <Button asChild>
    <Link
      href="vscode:mcp/install?%7B%22name%22%3A%22langfuse-docs%22%2C%22url%22%3A%22https%3A%2F%2Flangfuse.com%2Fapi%2Fmcp%22%7D"
      target="_blank"
      rel="noopener noreferrer"
    >
      Install MCP Server in VS Code
    </Link>
  </Button>
</div>

<details>
<summary>Manual configuration</summary>

Add Langfuse Docs MCP to Copilot in VSCode via the following steps:

1. Open Command Palette (⌘+Shift+P)
2. Open "MCP: Add Server..."
3. Select `HTTP`
4. Paste `https://langfuse.com/api/mcp`
5. Select name (e.g. `langfuse-docs`) and whether to save in user or workspace settings
6. You're all set! The MCP server is now available in Agent mode

</details>

</Tab>

<Tab>

Add Langfuse Docs MCP to Claude Code via the CLI:

```bash
claude mcp add \
  --transport http \
  langfuse-docs \
  https://langfuse.com/api/mcp \
  --scope user
```

<details>
<summary>Manual configuration</summary>

Alternatively, add the following to your settings file:

- **User scope**: `~/.claude/settings.json`
- **Project scope**: `your-repo/.claude/settings.json`
- **Local scope**: `your-repo/.claude/settings.local.json`

```json
{
  "mcpServers": {
    "langfuse-docs": {
      "transportType": "http",
      "url": "https://langfuse.com/api/mcp",
      "verifySsl": true
    }
  }
}
```

**One-liner JSON import**

```bash
claude mcp add-json langfuse-docs \
  '{"type":"http","url":"https://langfuse.com/api/mcp"}'
```

Once added, start a Claude Code session (`claude`) and type `/mcp` to confirm the connection.

</details>

</Tab>

<Tab>

Add Langfuse Docs MCP to Windsurf via the following steps:

1. Open Command Palette (⌘+Shift+P)
2. Open "MCP Configuration Panel"
3. Select `Add custom server`
4. Add the following configuration:

   ```json
   {
     "mcpServers": {
       "langfuse-docs": {
         "command": "npx",
         "args": ["mcp-remote", "https://langfuse.com/api/mcp"]
       }
     }
   }
   ```

</Tab>

<Tab>

Langfuse uses the `streamableHttp` protocol to communicate with the MCP server. This is supported by most clients.

```json
{
  "mcpServers": {
    "langfuse-docs": {
      "url": "https://langfuse.com/api/mcp"
    }
  }
}
```

If you use a client that does not support `streamableHttp` (e.g. Windsurf), you can use the `mcp-remote` command as a local proxy.

```json
{
  "mcpServers": {
    "langfuse-docs": {
      "command": "npx",
      "args": ["mcp-remote", "https://langfuse.com/api/mcp"]
    }
  }
}
```

</Tab>

</Tabs>



**2. Run Agent**

Copy and execute the following prompt in the agent mode of your editor:

<CopyAgentOnboardingPrompt />

</Tab>

<Tab>
{/* MORE INTEGRATIONS */}

Explore all integrations and frameworks that Langfuse supports.

<Cards num={2}>
  <Card
    icon={
      <div className="w-6 h-6 dark:bg-white rounded-sm p-0.5 flex items-center justify-center">
        <img
          src="/images/integrations/vercel_ai_sdk_icon.png"
          className="w-full h-full object-contain"
        />
      </div>
    }
    title="Vercel AI SDK"
    href="/integrations/frameworks/vercel-ai-sdk"
    arrow
  />
  <Card
    icon={
      <div className="w-6 h-6 dark:bg-white rounded-sm p-0.5 flex items-center justify-center">
        <img
          src="/images/integrations/llamaindex_icon.png"
          className="w-full h-full object-contain"
        />
      </div>
    }
    title="Llamaindex"
    href="/integrations/frameworks/llamaindex"
    arrow
  />
  <Card
    icon={
      <div className="w-6 h-6 dark:bg-white rounded-sm p-0.5 flex items-center justify-center">
        <img
          src="/images/integrations/crewai_icon.svg"
          className="w-full h-full object-contain"
        />
      </div>
    }
    title="CrewAI"
    href="/integrations/frameworks/crewai"
    arrow
  />
  <Card
    icon={
      <div className="w-6 h-6 dark:bg-white rounded-sm p-0.5 flex items-center justify-center">
        <img
          src="/images/integrations/ollama_icon.svg"
          className="w-full h-full object-contain"
        />
      </div>
    }
    title="Ollama"
    href="/integrations/model-providers/ollama"
    arrow
  />
  <Card
    icon={
      <div className="w-6 h-6 dark:bg-white rounded-sm p-0.5 flex items-center justify-center">
        <img
          src="/images/integrations/litellm_icon.png"
          className="w-full h-full object-contain"
        />
      </div>
    }
    title="LiteLLM"
    href="/integrations/gateways/litellm"
    arrow
  />
  <Card
    icon={
      <div className="w-6 h-6 dark:bg-white rounded-sm p-0.5 flex items-center justify-center">
        <img
          src="/images/integrations/autogen_icon.svg"
          className="w-full h-full object-contain"
        />
      </div>
    }
    title="AutoGen"
    href="/integrations/frameworks/autogen"
    arrow
  />
  <Card
    icon={
      <div className="w-6 h-6 dark:bg-white rounded-sm p-0.5 flex items-center justify-center">
        <img
          src="/images/integrations/google_adk_icon.png"
          className="w-full h-full object-contain"
        />
      </div>
    }
    title="Google ADK"
    href="/integrations/frameworks/google-adk"
    arrow
  />
  <Card title="All integrations" href="/integrations" arrow />
</Cards>

</Tab>

</LangTabs>

## See your trace in Langfuse

After running your application, visit the Langfuse interface to view the trace you just created. _[(Example LangGraph trace in Langfuse)](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/7d5f970573b8214d1ca891251e42282c)_

<Video
  src="https://static.langfuse.com/docs-videos/trace-new-ui.mp4"
  aspectRatio={16 / 9}
  gifStyle
/>

</Steps>

## Core Features



import {
  Users,
  Tag,
  MessagesSquare,
  Images,
  Braces,
  GitGraph,
  Globe,
  Database,
  FileDigit,
  GitCompare,
  MapPin,
  BarChart3,
  Filter,
  BadgeDollarSign,
  EyeOff,
  MessageCircle,
} from "lucide-react";

<Cards num={2}>
  <Card
    title="Sessions"
    href="/docs/tracing-features/sessions"
    icon={<MessagesSquare />}
    arrow
  />
  <Card
    title="Users"
    href="/docs/tracing-features/users"
    icon={<Users />}
    arrow
  />
  <Card
    title="Environments"
    href="/docs/tracing-features/environments"
    icon={<MapPin />}
    arrow
  />
  <Card title="Tags" href="/docs/tracing-features/tags" icon={<Tag />} arrow />
  <Card
    title="Metadata"
    href="/docs/tracing-features/metadata"
    icon={<Braces />}
    arrow
  />
  <Card
    title="Trace IDs"
    href="/docs/tracing-features/trace-ids"
    icon={<FileDigit />}
    arrow
  />
</Cards>

