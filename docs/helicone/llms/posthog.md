# Source: https://docs.helicone.ai/getting-started/integration-method/posthog.md

# Source: https://docs.helicone.ai/gateway/integrations/posthog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# PostHog Integration

> Integrate Helicone AI Gateway with PostHog to automatically export LLM request events to your PostHog analytics platform for unified product analytics.

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

[PostHog](https://www.posthog.com/) is a comprehensive product analytics platform that helps you understand user behavior and product performance.

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
    <p>Sign up at <a href="https://www.helicone.ai" target="_blank">helicone.ai</a> and generate an <a href="https://us.helicone.ai/settings/api-keys" target="_blank">API key</a>.</p>
    <p>Create a <a href="https://posthog.com" target="_blank">Posthog account</a> if you don't have one. Get your Project API Key from your <a href="https://us.posthog.com/settings/project" target="_blank">PostHog project settings</a>.</p>

    ```env  theme={null}
    HELICONE_API_KEY=sk-helicone-...
    POSTHOG_PROJECT_API_KEY=phc_...

    # Optional: PostHog host (defaults to https://app.posthog.com)
    # Only needed if using self-hosted PostHog
    # POSTHOG_CLIENT_API_HOST=https://app.posthog.com
    ```
  </Step>

  <Step title={strings.installSDK('OpenAI')}>
    <CodeGroup>
      ```bash TypeScript theme={null}
      npm install openai
      # or
      yarn add openai
      ```

      ```bash Python theme={null}
      pip install openai
      ```
    </CodeGroup>
  </Step>

  <Step title="Configure OpenAI client with Helicone AI Gateway">
    <CodeGroup>
      ```typescript TypeScript theme={null}
      import { OpenAI } from "openai";
      import dotenv from "dotenv";

      dotenv.config();

      const client = new OpenAI({
        baseURL: "https://ai-gateway.helicone.ai",
        apiKey: process.env.HELICONE_API_KEY,
        defaultHeaders: {
          "Helicone-Posthog-Key": POSTHOG_PROJECT_API_KEY,
          "Helicone-Posthog-Host": POSTHOG_CLIENT_API_HOST
        },
      });
      ```

      ```python Python theme={null}
      import os
      from openai import OpenAI
      from dotenv import load_dotenv

      load_dotenv()

      client = OpenAI(
          base_url="https://ai-gateway.helicone.ai",
          api_key=os.getenv("HELICONE_API_KEY"),
          default_headers={
              "Helicone-Posthog-Key": os.getenv("POSTHOG_PROJECT_API_KEY"),
              "Helicone-Posthog-Host": os.getenv("POSTHOG_CLIENT_API_HOST")
          },
      )
      ```
    </CodeGroup>

    <div dangerouslySetInnerHTML={{ __html: strings.modelRegistryDescription }} />
  </Step>

  <Step title={strings.useTheSDK('OpenAI')}>
    Your existing OpenAI code continues to work without any changes. Events will automatically be exported to PostHog.

    <CodeGroup>
      ```typescript TypeScript theme={null}
        const response = await client.chat.completions.create({
          model: "gpt-4o-mini",
          messages: [{ role: "user", content: "Hello, world!" }],
          temperature: 0.7,
        });

        console.log(response.choices[0]?.message?.content);
      ```

      ```python Python theme={null}
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Hello, world!"}],
            temperature=0.7,
        )

        print("Completion:", response.choices[0].message.content)
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("Posthog") }} />

    1. Go to your <a href="https://us.posthog.com/events" target="_blank">PostHog Events</a> page
    2. Look for events with the <code>helicone\_request</code> event name
    3. Each event contains metadata about the LLM request including:
       * Model used
       * Token counts
       * Latency
       * Cost
       * Request/response data
  </Step>
</Steps>

<Tip>
  While you're here, why not <a href="https://github.com/helicone/helicone" target="_blank" rel="noreferrer">give us a star on GitHub</a>? It helps us a lot!
</Tip>

<Note title="Request a Helicone Integration" type="info">
  Looking for a framework or tool not listed here? [Request it here!](https://forms.gle/E9GYKWevh6NGDdDj7)
</Note>

## Related Documentation

<CardGroup cols={2}>
  <Card title="AI Gateway Overview" icon="arrow-progress" href="/gateway/overview">
    Learn about Helicone's AI Gateway features and capabilities
  </Card>

  <Card title="Custom Properties" icon="tags" href="/features/advanced-usage/custom-properties">
    Add metadata to track and filter your requests
  </Card>

  <Card title="Sessions" icon="link" href="/features/sessions">
    Track multi-turn conversations and user sessions
  </Card>

  <Card title="Model Registry" icon="database" href="https://helicone.ai/models">
    Browse all available models and providers
  </Card>
</CardGroup>
