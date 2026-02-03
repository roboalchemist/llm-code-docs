# Source: https://docs.helicone.ai/gateway/integrations/openai-agents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Agents Integration

> Integrate Helicone AI Gateway with OpenAI Agents SDK to build AI agents with tools and full observability.

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

[OpenAI Agents SDK](https://github.com/openai/agents) is a framework for building AI agents with tool calling, multi-step reasoning, and structured outputs.

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
    {strings.generateKeyInstructions}

    ```js  theme={null}
    HELICONE_API_KEY=sk-helicone-...
    ```
  </Step>

  <Step title={strings.installSDK('OpenAI Agents SDK')}>
    ```bash  theme={null}
    npm install @openai/agents openai
    # or
    pip install openai-agents
    ```
  </Step>

  <Step title="Configure OpenAI Agents with Helicone AI Gateway">
    <CodeGroup>
      ```typescript TypeScript theme={null}
      import { Agent, setDefaultOpenAIClient } from "@openai/agents";
      import OpenAI from "openai";
      import dotenv from "dotenv";

      dotenv.config();

      const client = new OpenAI({
        baseURL: "https://ai-gateway.helicone.ai/v1",
        apiKey: process.env.HELICONE_API_KEY
      });

      // Set the client globally for all agents
      setDefaultOpenAIClient(client);
      ```

      ```python Python theme={null}
      import os
      from agents import set_default_openai_client
      from openai import OpenAI

      client = OpenAI(
          base_url="https://ai-gateway.helicone.ai/v1",
          api_key=os.getenv("HELICONE_API_KEY")
      )

      # Set the client globally for all agents
      set_default_openai_client(client)
      ```
    </CodeGroup>

    <div dangerouslySetInnerHTML={{ __html: strings.modelRegistryDescription }} />
  </Step>

  <Step title="Use OpenAI Agents normally">
    Your existing OpenAI Agents code continues to work without any changes:

    <CodeGroup>
      ```typescript TypeScript theme={null}
      import { Agent, run, tool } from "@openai/agents";
      import { z } from "zod";

      // Define tools
      const calculator = tool({
        name: "calculator",
        description: "Perform basic arithmetic operations",
        parameters: z.object({
          operation: z.enum(["add", "subtract", "multiply", "divide"]),
          a: z.number(),
          b: z.number()
        }),
        async execute({ operation, a, b }) {
          switch (operation) {
            case "add":
              return a + b;
            case "subtract":
              return a - b;
            case "multiply":
              return a * b;
            case "divide":
              if (b === 0) return "Error: Division by zero";
              return a / b;
          }
        }
      });

      // Create an agent with tools
      const agent = new Agent({
        name: "Assistant",
        instructions: "You are a helpful assistant.",
        tools: [calculator],
        model: "gpt-4o-mini",
      });

      // Run the agent
      const result = await run(agent, "Multiply 2 by 2");
      console.log(result.finalOutput);
      ```

      ```python Python theme={null}
      from agents import Agent, Runner, tool
      from typing import Literal

      # Define tools
      @tool
      def calculator(operation: Literal["add", "subtract", "multiply", "divide"], a: float, b: float) -> float | str:
          """Perform basic arithmetic operations."""
          if operation == "add":
              return a + b
          elif operation == "subtract":
              return a - b
          elif operation == "multiply":
              return a * b
          elif operation == "divide":
              if b == 0:
                  return "Error: Division by zero"
              return a / b

      # Create an agent with tools
      agent = Agent(
          name="Assistant",
          instructions="You are a helpful assistant.",
          tools=[calculator],
          model="gpt-4o-mini"
      )

      # Run the agent
      result = Runner.run_sync(agent, "Multiply 2 by 2")
      print(result.final_output)
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.viewRequestsInDashboard}>
    <div dangerouslySetInnerHTML={{ __html: strings.viewRequestsInDashboardDescription("OpenAI Agents") }} />

    * Request/response bodies
    * Latency metrics
    * Token usage and costs
    * Model performance analytics
    * Tool usage tracking
    * Agent reasoning steps
    * Error tracking
    * Session tracking

    <Tip>
      While you're here, why not <a href="https://github.com/helicone/helicone" target="_blank" rel="noreferrer">give us a star on GitHub</a>? It helps us a lot!
    </Tip>
  </Step>
</Steps>

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

  <Card title="Prompt Management" icon="code" href="/gateway/concepts/prompt-caching">
    Version and manage prompts with Helicone Prompts
  </Card>

  <Card title="Custom Properties" icon="tags" href="/features/advanced-usage/custom-properties">
    Add metadata to track and filter your requests
  </Card>

  <Card title="Sessions" icon="link" href="/features/sessions">
    Track multi-turn conversations and user sessions
  </Card>

  <Card title="Rate Limiting" icon="gauge" href="/features/advanced-usage/custom-rate-limits">
    Configure rate limits for your applications
  </Card>

  <Card title="Tool Usage Tracking" icon="wrench" href="/features/tool-usage">
    Monitor tool calls and function usage in your agents
  </Card>
</CardGroup>
