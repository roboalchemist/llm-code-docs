# Source: https://docs.helicone.ai/gateway/integrations/claude-agent-sdk.md

# Claude Agent SDK Integration

> Use Helicone AI Gateway with the Claude Agent SDK for building AI agents with automatic observability

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

The [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/typescript) allows you to build powerful AI agents that can use tools and make decisions autonomously.

<Note>
  This integration uses [Helicone's Model Context Protocol (MCP)](https://github.com/Helicone/helicone/tree/main/helicone-mcp) to provide seamless AI Gateway access to your Claude agents.
</Note>

## Integration Steps

<Steps>
  <Step title={strings.generateKey}>
    Sign up at [helicone.ai](https://www.helicone.ai) and generate an [API key](https://us.helicone.ai/settings/api-keys).

    Make sure to have some [credits](https://us.helicone.ai/credits) available in your Helicone account to make requests (or BYOK).
  </Step>

  <Step title="Install the Helicone MCP Package">
    <CodeGroup>
      ```bash npm theme={null}
      npm install @helicone/mcp
      ```

      ```bash yarn theme={null}
      yarn add @helicone/mcp
      ```

      ```bash pnpm theme={null}
      pnpm add @helicone/mcp
      ```
    </CodeGroup>
  </Step>

  <Step title="Configure MCP Server in Your Application">
    <Tabs>
      <Tab title="Claude Desktop (Development)">
        Add to your Claude Desktop configuration:

        * **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
        * **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

        ```json  theme={null}
        {
          "mcpServers": {
            "helicone": {
              "command": "npx",
              "args": ["@helicone/mcp@latest"],
              "env": {
                "HELICONE_API_KEY": "sk-helicone-xxxxxxx-xxxxxxx-xxxxxxx-xxxxxxx"
              }
            }
          }
        }
        ```

        The Helicone MCP tools will be automatically available in Claude Desktop.
      </Tab>

      <Tab title="Claude Agent SDK">
        ```typescript  theme={null}
        import { query } from '@anthropic-ai/claude-agent-sdk';

        // Make a query with Helicone MCP
        const result = await query({
          prompt: 'Use the use_ai_gateway tool to ask GPT-4o: "What is Helicone?"',
          options: {
            mcpServers: {
              helicone: {
                command: 'npx',
                args: ['@helicone/mcp'],
                env: {
                  HELICONE_API_KEY: process.env.HELICONE_API_KEY
                }
              }
            },
            // Explicitly allow Helicone MCP tools (recommended for production)
            allowedTools: [
              'mcp__helicone__use_ai_gateway',
              'mcp__helicone__query_requests',
              'mcp__helicone__query_sessions'
            ]
          }
        });

        // Extract the response
        for await (const message of result.sdkMessages) {
          if (message.type === 'result' && message.result) {
            console.log('Response:', message.result);
          }
        }
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Test the Integration">
    ```typescript  theme={null}
    import { query } from '@anthropic-ai/claude-agent-sdk';

    const result = await query({
      prompt: 'Use the use_ai_gateway tool to generate a creative story about AI using gpt-4o with temperature 0.8',
      options: {
        mcpServers: {
          helicone: {
            command: 'npx',
            args: ['@helicone/mcp'],
            env: {
              HELICONE_API_KEY: process.env.HELICONE_API_KEY
            }
          }
        },
        allowedTools: ['mcp__helicone__use_ai_gateway']
      }
    });

    // Get the response
    for await (const message of result.sdkMessages) {
      if (message.type === 'result' && message.result) {
        console.log(message.result);
      }
    }
    ```

    The agent will automatically use the `use_ai_gateway` tool to make the request through Helicone AI Gateway.
  </Step>
</Steps>

## Available MCP Tools

### `use_ai_gateway`

Make requests to any LLM provider through Helicone AI Gateway with automatic observability.

**Parameters:**

* `model` (required): Model name (e.g., `gpt-4o`, `claude-sonnet-4`, `gemini-2.0-flash` - see [Supported Models](https://helicone.ai/models) for more)
* `messages` (required): Array of conversation messages
* `max_tokens` (optional): Maximum tokens to generate
* `temperature` (optional): Response randomness (0-2)
* `sessionId` (optional): Session ID for request grouping
* `sessionName` (optional): Human-readable session name
* `userId` (optional): User identifier for tracking
* `customProperties` (optional): Custom metadata for filtering

### `query_requests`

Query historical requests for debugging and analysis with filters, pagination, and sorting.

### `query_sessions`

Query conversation sessions with filtering, search, and time range capabilities.

## Complete Working Examples

### Basic Agent with Session Tracking

```typescript  theme={null}
import { query } from '@anthropic-ai/claude-agent-sdk';

// Configure MCP server
const mcpConfig = {
  helicone: {
    command: 'npx',
    args: ['@helicone/mcp'],
    env: {
      HELICONE_API_KEY: process.env.HELICONE_API_KEY
    }
  }
};

// Make a request with session tracking
const sessionId = `chat-${Date.now()}`;
const result = await query({
  prompt: `Use the use_ai_gateway tool to ask Claude Sonnet: "Plan a 3-day trip to Japan"

Use these settings:
- sessionId: "${sessionId}"
- sessionName: "travel-planning"
- customProperties: {"topic": "travel", "destination": "japan"}`,
  options: {
    mcpServers: mcpConfig,
    allowedTools: ['mcp__helicone__use_ai_gateway']
  }
});

// Extract response
for await (const message of result.sdkMessages) {
  if (message.type === 'result' && message.result) {
    console.log('Travel Plan:', message.result);
  }
}
```

### Multi-Model Comparison

```typescript  theme={null}
import { query } from '@anthropic-ai/claude-agent-sdk';

const sessionId = `comparison-${Date.now()}`;
const result = await query({
  prompt: `Compare responses from multiple models on: "Explain quantum computing in simple terms"

1. Use GPT-4o-mini (fast, cost-effective)
2. Use Claude Sonnet (high quality)
3. Use GPT-4o (balanced)

Use sessionId: "${sessionId}" for all requests so I can compare them later.`,
  options: {
    mcpServers: {
      helicone: {
        command: 'npx',
        args: ['@helicone/mcp'],
        env: {
          HELICONE_API_KEY: process.env.HELICONE_API_KEY
        }
      }
    },
    allowedTools: ['mcp__helicone__use_ai_gateway']
  }
});

// Get comparison results
for await (const message of result.sdkMessages) {
  if (message.type === 'result') {
    console.log('Comparison:', message.result);
  }
}
```

### Self-Analyzing Agent

```typescript  theme={null}
import { query } from '@anthropic-ai/claude-agent-sdk';

const result = await query({
  prompt: `Perform a task and then analyze your own performance:

1. Use the use_ai_gateway tool to generate a haiku about AI
2. Then use query_requests to check how much the request cost
3. Use query_sessions to see your recent activity
4. Provide a summary of your performance and costs`,
  options: {
    mcpServers: {
      helicone: {
        command: 'npx',
        args: ['@helicone/mcp'],
        env: {
          HELICONE_API_KEY: process.env.HELICONE_API_KEY
        }
      }
    },
    allowedTools: [
      'mcp__helicone__use_ai_gateway',
      'mcp__helicone__query_requests',
      'mcp__helicone__query_sessions'
    ]
  }
});

// Get self-analysis
for await (const message of result.sdkMessages) {
  if (message.type === 'result') {
    console.log('Self-Analysis:', message.result);
  }
}
```

## Next Steps

<CardGroup cols={2}>
  <Card title="Model Registry" icon="list" href="https://helicone.ai/models">
    Browse all supported models and providers
  </Card>

  <Card title="Dashboard" icon="chart-line" href="https://us.helicone.ai">
    View your agent's requests and analytics
  </Card>

  <Card title="Provider Routing" icon="route" href="/gateway/provider-routing">
    Set up automatic failovers and routing
  </Card>

  <Card title="Custom Properties" icon="tag" href="/features/advanced-usage/custom-properties">
    Learn about advanced filtering and analytics
  </Card>
</CardGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.helicone.ai/llms.txt