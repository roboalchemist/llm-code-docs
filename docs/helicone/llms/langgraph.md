# Source: https://docs.helicone.ai/other-integrations/langgraph.md

# Source: https://docs.helicone.ai/gateway/integrations/langgraph.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# LangGraph Integration

> Integrate Helicone AI Gateway with LangGraph to build multi-agent workflows with access to 100+ LLM providers.

export const strings = {
  additionalHeadersForSessions: "Helicone provides additional headers to help you manage and analyze your sessions.",
  azureOpenAIDocs: `To learn more about the differences between OpenAI and AzureOpenAI, review the <a href="https://learn.microsoft.com/en-us/azure/ai-services/openai/overview">documentation here</a>.`,
  chainOfThoughtPromptingCookbookDescription: "Craft effective prompts, ideal for complex responses requiring multi-step problem solving.",
  chatbotCookbookDescription: "This step-by-step guide covers function calling, response formatting and monitoring with Helicone.",
  createHeliconeManualLogger: "Create a new HeliconeManualLogger instance",
  configureWebSocketConnection: "Configure WebSocket connection",
  environmentTrackingCookbookDescription: "Effortlessly track and manage your environments with Helicone across different deployment contexts.",
  exportBaseUrl: tool => `Export your ${tool} base URL`,
  getStartedWithPackage: "To get started, install the @helicone/helpers package",
  generateKey: "Create an account and generate an API key",
  generateKeyInstructions: `Log into <a href="https://www.helicone.ai" target="_blank">Helicone</a> or create an account. Once you have an account, you can generate an <a href="https://helicone.ai/developer" target="_blank">API key here</a>.`,
  generateSessionId: "Generate the unique session ID that will be used to track the session.",
  gettingUserRequestsCookbookDescription: "Retrieve user-specific requests to monitor, debug, and track costs for individual users.",
  githubActionsCookbookDescription: "Automate the monitoring and caching of your LLM calls in your CI pipelines for better deployment processes.",
  groupingCallsWithSessions: "Grouping Calls with Helicone Sessions",
  handleWebSocketEvents: "Handle WebSocket events",
  heliconeLoggerAPIReference: `To learn more about the <code>HeliconeManualLogger</code> API, see the <a href="/getting-started/integration-method/custom" target="_blank">API Reference here</a>.`,
  howToIntegrate: "How to Integrate",
  howToPromptThinkingModelsCookbookDescription: "Best practices to to effectively prompt thinking models like Deepseek and OpenAI o1-o3 for optimal results.",
  howToUseSessions: "To group related API calls and analyze them collectively, you can use Helicone's session tracking features. This is useful for grouping all interactions within a single conversation or user session.",
  includeHeadersInRequests: "Include headers in your requests",
  includeSessionHeaders: "Include the session headers when you make API requests. This way, the session information is attached to each request, allowing Helicone to group and analyze them together.",
  installRequiredDependencies: "Install required dependencies",
  installSDK: tool => `Install ${tool}`,
  logYourRequest: "Log your request",
  modelRegistryDescription: "You can find all 100+ supported models at <a href=\"https://helicone.ai/models\" target=\"_blank\">helicone.ai/models</a>.",
  modifyBasePath: "Modify the base URL path",
  optional: "Optional",
  relatedGuides: "Related Guides",
  replayLlmSessionsCookbookDescription: "Learn how to replay and modify LLM sessions using Helicone to optimize your AI agents and improve their performance.",
  sessionManagement: "Session Management",
  setApiKey: "Set up your Helicone API key in your .env file",
  setUpToolBaseUrl: tool => `Set up your ${tool} base URL`,
  setUpToolApiKey: tool => `Set up your ${tool} API key as an environment variable`,
  startUsing: tool => `Start using ${tool} with Helicone`,
  useTheSDK: tool => `Use the ${tool} SDK`,
  verifyInHelicone: "Verify your requests in Helicone",
  verifyInHeliconeDesciption: tool => `With the above setup, any calls to ${tool} will automatically be logged and monitored by Helicone. Review them in your <a href="https://www.helicone.ai/dashboard" target="_blank">Helicone dashboard</a>.`,
  viewRequestsInDashboard: "View requests in the Helicone dashboard",
  viewRequestsInDashboardDescription: product => `All your ${product} requests are now visible in your <a href="https://us.helicone.ai/dashboard" target="_blank">Helicone dashboard</a>.`,
  whyUseSessions: "By including the session headers in each request, you have more granular control over session tracking. This approach is especially useful if you want to handle sessions dynamically or manage multiple sessions concurrently."
};

## Introduction

[LangGraph](https://www.langchain.com/langgraph) is a framework for building stateful, multi-agent applications with LLMs. The integration with Helicone AI Gateway is nearly identical to the [LangChain integration](/gateway/integrations/langchain), with the addition of agent-specific features.

<Note>
  This integration requires only **two changes** to your existing LangGraph code - updating the base URL and API key. See the [LangChain AI Gateway docs](/gateway/integrations/langchain) for full feature details.
</Note>

## Quick Start

Follow the same setup as [LangChain AI Gateway integration](/gateway/integrations/langchain), then create your agent:

<CodeGroup>
  ```typescript TypeScript - OpenAI theme={null}
  import { ChatOpenAI } from "@langchain/openai";
  import { createReactAgent } from "@langchain/langgraph/prebuilt";
  import { MemorySaver } from "@langchain/langgraph";

  const model = new ChatOpenAI({
      model: 'gpt-4.1-mini',
      apiKey: process.env.HELICONE_API_KEY,
      configuration: {
          baseURL: "https://ai-gateway.helicone.ai/v1",
      },
  });

  const agent = createReactAgent({
      llm: model,
      tools: yourTools,
      checkpointer: new MemorySaver(),
  });
  ```

  ```python Python - OpenAI theme={null}
  from langchain_openai import ChatOpenAI
  from langgraph.prebuilt import create_react_agent
  from langgraph.checkpoint.memory import MemorySaver

  model = ChatOpenAI(
      model='gpt-4.1-mini',
      api_key=os.getenv('HELICONE_API_KEY'),
      base_url="https://ai-gateway.helicone.ai/v1",
  )

  agent = create_react_agent(
      model,
      tools=your_tools,
      checkpointer=MemorySaver(),
  )
  ```
</CodeGroup>

<Tip>
  While you're here, why not <a href="https://github.com/helicone/helicone" target="_blank" rel="noreferrer">give us a star on GitHub</a>? It helps us a lot!
</Tip>

## Migration Example

### Before (Direct Provider)

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { ChatOpenAI } from "@langchain/openai";
  import { createReactAgent } from "@langchain/langgraph/prebuilt";

  const model = new ChatOpenAI({
      model: 'gpt-4o-mini',
      apiKey: process.env.OPENAI_API_KEY,
  });

  const agent = createReactAgent({
      llm: model,
      tools: myTools,
  });
  ```

  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langgraph.prebuilt import create_react_agent

  model = ChatOpenAI(
      model='gpt-4o-mini',
      api_key=os.getenv('OPENAI_API_KEY'),
  )

  agent = create_react_agent(model, tools=my_tools)
  ```
</CodeGroup>

### After (Helicone AI Gateway)

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { ChatOpenAI } from "@langchain/openai";
  import { createReactAgent } from "@langchain/langgraph/prebuilt";

  const model = new ChatOpenAI({
      model: 'gpt-4.1-mini',                      // 100+ models supported
      apiKey: process.env.HELICONE_API_KEY,      // Your Helicone API key
      configuration: {
          baseURL: "https://ai-gateway.helicone.ai/v1"  // Add this!
      },
  });

  const agent = createReactAgent({
      llm: model,
      tools: myTools,
  });
  ```

  ```python Python theme={null}
  from langchain_openai import ChatOpenAI
  from langgraph.prebuilt import create_react_agent

  model = ChatOpenAI(
      model='gpt-4.1-mini',                      # 100+ models supported
      api_key=os.getenv('HELICONE_API_KEY'),    # Your Helicone API key
      base_url="https://ai-gateway.helicone.ai/v1"  # Add this!
  )

  agent = create_react_agent(model, tools=my_tools)
  ```
</CodeGroup>

## Adding Custom Headers to Agent Invocations

You can add custom properties when calling your agent with `invoke()`:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { HumanMessage } from "@langchain/core/messages";
  import { v4 as uuidv4 } from 'uuid';

  const result = await agent.invoke(
      { messages: [new HumanMessage("What is the weather in San Francisco?")] },
      {
          options: {
              headers: {
                  "Helicone-Session-Id": uuidv4(),
                  "Helicone-Session-Path": "/weather/query",
                  "Helicone-Property-Query-Type": "weather",
              },
          },
      }
  );
  ```

  ```python Python theme={null}
  from langchain_core.messages import HumanMessage
  import uuid

  result = agent.invoke(
      {"messages": [HumanMessage(content="What is the weather in San Francisco?")]},
      {
          "configurable": {
              "headers": {
                  "Helicone-Session-Id": str(uuid.uuid4()),
                  "Helicone-Session-Path": "/weather/query",
                  "Helicone-Property-Query-Type": "weather",
              }
          }
      }
  )
  ```
</CodeGroup>

<Note title="Request a Helicone Integration" type="info">
  Looking for a framework or tool not listed here? [Request it here!](https://forms.gle/E9GYKWevh6NGDdDj7)
</Note>

## Related Documentation

<CardGroup cols={2}>
  <Card title="AI Gateway Overview" icon="arrow-progress" href="/gateway/overview">
    Learn about Helicone's AI Gateway features and capabilities
  </Card>

  <Card title="Provider Routing" icon="route" href="/gateway/provider-routing">
    Configure intelligent routing and automatic failover
  </Card>

  <Card title="Model Registry" icon="database" href="https://helicone.ai/models">
    Browse all available models and providers
  </Card>

  <Card title="LangChain Integration" icon="link" href="/gateway/integrations/langchain">
    Full AI Gateway feature documentation
  </Card>

  <Card title="Sessions" icon="chart-network" href="/features/sessions">
    Track multi-turn conversations and agent workflows
  </Card>

  <Card title="Custom Properties" icon="tags" href="/features/advanced-usage/custom-properties">
    Add metadata to track and filter your requests
  </Card>
</CardGroup>
