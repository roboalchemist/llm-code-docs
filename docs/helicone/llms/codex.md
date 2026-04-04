# Source: https://docs.helicone.ai/gateway/integrations/codex.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Codex

> Use OpenAI Codex CLI and SDK with Helicone AI Gateway to log your coding agent interactions.

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

<Info>
  This integration uses the [AI Gateway](/gateway/overview), which provides a unified API for multiple LLM providers. The AI Gateway is currently in beta.
</Info>

## CLI Integration

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title="Configure Codex config file">
    Update your `$CODEX_HOME/.codex/config.toml` file to include the Helicone provider configuration:

    <Note>
      `$CODEX_HOME` is typically `~/.codex` on Mac or Linux.
    </Note>

    ```toml config.toml theme={null}
    model_provider = "helicone"

    [model_providers.helicone]
    name = "Helicone"
    base_url = "https://ai-gateway.helicone.ai/v1"
    env_key = "HELICONE_API_KEY"
    wire_api = "chat"
    ```
  </Step>

  <Step title="Set your Helicone API key">
    Set the `HELICONE_API_KEY` environment variable:

    ```bash  theme={null}
    export HELICONE_API_KEY=<your-helicone-api-key>
    ```
  </Step>

  <Step title="Run Codex with Helicone">
    Use Codex as normal. Your requests will automatically be logged to Helicone:

    ```bash  theme={null}
    # If you set model_provider in config.toml
    codex "What files are in the current directory?"

    # Or specify the provider explicitly
    codex -c model_provider="helicone" "What files are in the current directory?"
    ```
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("Codex CLI") }} />

    <Tip>
      While you're here, why not <a href="https://github.com/helicone/helicone" target="_blank" rel="noreferrer">give us a star on GitHub</a>? It helps us a lot!
    </Tip>
  </Step>
</Steps>

## SDK Integration

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title="Install the Codex SDK">
    ```bash  theme={null}
    npm install @openai/codex-sdk
    ```
  </Step>

  <Step title="Configure the SDK with Helicone">
    Initialize the Codex SDK with the AI Gateway base URL:

    ```typescript  theme={null}
    import { Codex } from "@openai/codex-sdk";

    const codex = new Codex({
      baseUrl: "https://ai-gateway.helicone.ai/v1",
      apiKey: process.env.HELICONE_API_KEY,
    });

    const thread = codex.startThread({
      model: "gpt-5" // 100+ models supported
    });
    const turn = await thread.run("What files are in the current directory?");

    console.log(turn.finalResponse);
    console.log(turn.items);
    ```

    <Note>
      The Codex SDK doesn't currently support specifying the wire API, so it will use the Responses API by default. This works with the AI Gateway with limited model and provider support. See the [Responses API documentation](/gateway/concepts/responses-api) for more details.
    </Note>
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("Codex SDK") }} />
  </Step>
</Steps>

## Additional Features

Once integrated with Helicone AI Gateway, you can take advantage of:

* **Unified Observability**: Monitor all your Codex usage alongside other LLM providers
* **Cost Tracking**: Track costs across different models and providers
* **Custom Properties**: Add metadata to your requests for better organization
* **Rate Limiting**: Control usage and prevent abuse

<Note title="Request a Helicone Integration" type="info">
  Looking for a framework or tool not listed here? [Request it here!](https://forms.gle/E9GYKWevh6NGDdDj7)
</Note>

## {strings.relatedGuides}

<CardGroup cols={2}>
  <Card title="AI Gateway Overview" icon="book-open" href="/gateway/overview" iconType="light" vertical>
    Learn more about Helicone's AI Gateway and its features
  </Card>

  <Card title="Responses API Support" icon="code" href="/gateway/concepts/responses-api" iconType="light" vertical>
    Use the OpenAI Responses API format through Helicone AI Gateway
  </Card>

  <Card title="Provider Routing" icon="route" href="/gateway/provider-routing" iconType="light" vertical>
    Configure automatic routing and fallbacks for reliability
  </Card>

  <Card title="Custom Properties" icon="tag" href="/features/advanced-usage/custom-properties" iconType="light" vertical>
    Add metadata to your requests for better tracking and organization
  </Card>
</CardGroup>
