# Source: https://docs.helicone.ai/gateway/integrations/vercel-ai-sdk.md

# Vercel AI SDK Integration

> Integrate Helicone AI Gateway with Vercel AI SDK to access 100+ LLM providers with full observability.

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
  modifyBasePath: "Modify the base URL path and set up authentication",
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
  whyUseSessions: "By including the session headers in each request, you have more granular control over session tracking. This approach is especially useful if you want to handle sessions dynamically or manage multiple sessions concurrently.",
  viewRequestsInDashboard: "View requests in the Helicone dashboard",
  viewRequestsInDashboardDescription: product => `All your ${product} requests are now visible in your <a href="https://us.helicone.ai/dashboard" target="_blank">Helicone dashboard</a>`,
  modelRegistryDescription: "You can find all 100+ supported models at <a href=\"https://helicone.ai/models\" target=\"_blank\">helicone.ai/models</a>."
};

## Introduction

[Vercel AI SDK](https://sdk.vercel.ai) is a TypeScript toolkit for building AI-powered applications with React, Next.js, Vue, and more.

<Note>
  The Helicone provider for Vercel AI SDK is available as a dedicated package: `@helicone/ai-sdk-provider`.
</Note>

## Integration Steps

<Steps>
  <Step title={strings.generateKey}>
    Sign up at [helicone.ai](https://www.helicone.ai) and generate an [API key](https://us.helicone.ai/settings/api-keys).

    <Note>
      You'll also need to configure your provider API keys (OpenAI, Anthropic, etc.) at [Helicone Providers](https://us.helicone.ai/providers) for BYOK (Bring Your Own Keys).
    </Note>
  </Step>

  <Step title={strings.setApiKey}>
    ```bash  theme={null}
    HELICONE_API_KEY=sk-helicone-...
    ```
  </Step>

  <Step title="Install the Helicone AI SDK provider">
    <CodeGroup>
      ```bash pnpm theme={null}
      pnpm add @helicone/ai-sdk-provider ai
      ```

      ```bash npm theme={null}
      npm install @helicone/ai-sdk-provider ai
      ```

      ```bash yarn theme={null}
      yarn add @helicone/ai-sdk-provider ai
      ```

      ```bash bun theme={null}
      bun add @helicone/ai-sdk-provider ai
      ```
    </CodeGroup>
  </Step>

  <Step title="Configure Vercel AI SDK with Helicone">
    ```typescript  theme={null}
    import { createHelicone } from '@helicone/ai-sdk-provider';
    import { generateText } from 'ai';

    // Initialize Helicone provider
    const helicone = createHelicone({
      apiKey: process.env.HELICONE_API_KEY
    });

    // Use any model from 100+ providers
    const result = await generateText({
      model: helicone('claude-4.5-haiku'),
      prompt: 'Write a haiku about artificial intelligence'
    });

    console.log(result.text);
    ```

    <Info>
      You can switch between [100+ models](https://helicone.ai/models) without changing your code. Just update the model name!
    </Info>
  </Step>
</Steps>

## Complete Working Examples

### Basic Text Generation

```typescript  theme={null}
import { createHelicone } from '@helicone/ai-sdk-provider';
import { generateText } from 'ai';

const helicone = createHelicone({
  apiKey: process.env.HELICONE_API_KEY
});

const { text } = await generateText({
  model: helicone('gemini-2.5-flash-lite'),
  prompt: 'What is Helicone?'
});

console.log(text);
```

### Streaming Text

```typescript  theme={null}
import { createHelicone } from '@helicone/ai-sdk-provider';
import { streamText } from 'ai';

const helicone = createHelicone({
  apiKey: process.env.HELICONE_API_KEY
});

const result = await streamText({
  model: helicone('deepseek-v3.1-terminus'),
  prompt: 'Write a short story about a robot learning to paint',
  maxTokens: 300
});

for await (const chunk of result.textStream) {
  process.stdout.write(chunk);
}

console.log('\n\nStream completed!');
```

### Provider Selection

By default, Helicone's AI gateway automatically routes to the cheapest provider. You can also manually select a specific provider:

```typescript  theme={null}
import { createHelicone } from '@helicone/ai-sdk-provider';
import { generateText } from 'ai';

const helicone = createHelicone({
  apiKey: process.env.HELICONE_API_KEY
});

// Automatic routing (cheapest provider)
const autoResult = await generateText({
  model: helicone('gpt-4o'),
  prompt: 'Hello!'
});

// Manual provider selection
const manualResult = await generateText({
  model: helicone('claude-4.5-sonnet/anthropic'),
  prompt: 'Hello!'
});

// Multiple provider selection: first model/provider is used, if it fails, the second model/provider is used, and so on.
const manualResult = await generateText({
  model: helicone('claude-4.5-sonnet/anthropic,gpt-4o/openai'),
  prompt: 'Hello!'
});
```

### With Custom Properties and Session Tracking

```typescript  theme={null}
import { createHelicone } from '@helicone/ai-sdk-provider';
import { generateText } from 'ai';

const helicone = createHelicone({
  apiKey: process.env.HELICONE_API_KEY
});

const result = await generateText({
  model: helicone('claude-4.5-haiku', {
    extraBody: {
      helicone: {
        sessionId: 'my-session',
        userId: 'user-123',
        properties: {
          environment: 'production',
          appVersion: '2.1.0',
          feature: 'quantum-explanation'
        }
      }
    }
  }),
  prompt: 'Explain quantum computing'
});
```

### Tool Calling

```typescript  theme={null}
import { createHelicone } from '@helicone/ai-sdk-provider';
import { generateText, tool } from 'ai';
import { z } from 'zod';

const helicone = createHelicone({
  apiKey: process.env.HELICONE_API_KEY
});

const result = await generateText({
  model: helicone('gpt-4o'),
  prompt: 'What is the weather like in San Francisco?',
  tools: {
    getWeather: tool({
      description: 'Get weather for a location',
      parameters: z.object({
        location: z.string().describe('The city name')
      }),
      execute: async (args) => {
        return `It's sunny in ${args.location}`;
      }
    })
  }
});

console.log(result.text);
```

### Helicone Prompts Integration

Use prompts created in your Helicone dashboard instead of hardcoding messages in your application:

```typescript  theme={null}
import { createHelicone } from '@helicone/ai-sdk-provider';
import type { WithHeliconePrompt } from '@helicone/ai-sdk-provider';
import { generateText } from 'ai';

const helicone = createHelicone({
  apiKey: process.env.HELICONE_API_KEY
});

const result = await generateText({
  model: helicone('gpt-4o', {
    promptId: 'sg45wqc',
    inputs: {
      customer_name: 'Sarah Johnson',
      issue_type: 'billing',
      account_type: 'premium'
    },
    environment: 'production',
    extraBody: {
      helicone: {
        sessionId: 'support-session-123',
        properties: {
          department: 'customer-support'
        }
      }
    }
  }),
  messages: [{ role: 'user', content: 'placeholder' }]
} as WithHeliconePrompt);
```

<Note>
  When using `promptId`, you must still pass a placeholder `messages` array to satisfy the Vercel AI SDK's validation. The actual prompt content will be fetched from your Helicone dashboard, and the placeholder messages will be ignored.
</Note>

**Benefits of using Helicone prompts:**

* 🎯 **Centralized Management**: Update prompts without code changes
* 👩🏻‍💻 **Perfect for non-technical users**: Create prompts using the Helicone dashboard
* 🚀 **Lower Latency**: Single API call, no message construction overhead
* 🔧 **A/B Testing**: Test different prompt versions with environments
* 📊 **Better Analytics**: Track prompt performance across versions

### Additional Examples

For more comprehensive examples, check out the [GitHub repository](https://github.com/Helicone/ai-sdk-provider/tree/main/examples):

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

  <Card title="Caching" icon="bolt" href="/features/advanced-usage/caching">
    Reduce costs and latency with intelligent caching
  </Card>
</CardGroup>

## Additional Resources

* [Vercel AI SDK Documentation](https://sdk.vercel.ai)
* [Helicone AI SDK Provider GitHub](https://github.com/Helicone/ai-sdk-provider)
* [Helicone AI SDK Provider on Vercel](https://ai-sdk.dev/providers/community-providers/helicone)
