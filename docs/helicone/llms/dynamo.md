# Source: https://docs.helicone.ai/integrations/nvidia/dynamo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Nvidia Dynamo Integration

> Use Nvidia Dynamo with Helicone for comprehensive logging and monitoring.

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

<Warning>
  This integration method is maintained but no longer actively developed. For the best experience and latest features, use our new [AI Gateway](/gateway/overview) with unified API access to 100+ models.
</Warning>

Use Nvidia Dynamo or other OpenAI-compatible Nvidia inference providers with Helicone by routing through our gateway with custom headers.

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title={strings.setApiKey}>
    ```bash  theme={null}
    HELICONE_API_KEY=<your-helicone-api-key>
    NVIDIA_API_KEY=<your-nvidia-api-key>
    ```
  </Step>

  <Step title={strings.modifyBasePath}>
    <CodeGroup>
      ```bash cURL theme={null}
      curl -X POST https://gateway.helicone.ai/v1/chat/completions \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $NVIDIA_API_KEY" \
        -H "Helicone-Auth: Bearer $HELICONE_API_KEY" \
        -H "Helicone-Target-Url: https://your-dynamo-endpoint.com" \
        -d '{
          "model": "your-model-name",
          "messages": [
            {
              "role": "user",
              "content": "Hello, how are you?"
            }
          ],
          "max_tokens": 1024,
          "temperature": 0.7
        }'
      ```

      ```javascript JavaScript theme={null}
      import OpenAI from "openai";

      const openai = new OpenAI({
        apiKey: process.env.NVIDIA_API_KEY,
        baseURL: "https://gateway.helicone.ai/v1",
        defaultHeaders: {
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
          "Helicone-Target-Url": "https://your-dynamo-endpoint.com"
        }
      });

      const response = await openai.chat.completions.create({
        model: "your-model-name",
        messages: [{ role: "user", content: "Hello, how are you?" }],
        max_tokens: 1024,
        temperature: 0.7
      });

      console.log(response);
      ```

      ```python Python theme={null}
      from openai import OpenAI
      import os

      client = OpenAI(
        api_key=os.getenv("NVIDIA_API_KEY"),
        base_url="https://gateway.helicone.ai/v1",
        default_headers={
          "Helicone-Auth": f"Bearer {os.getenv('HELICONE_API_KEY')}",
          "Helicone-Target-Url": "https://your-dynamo-endpoint.com"
        }
      )

      chat_completion = client.chat.completions.create(
        model="your-model-name",
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        max_tokens=1024,
        temperature=0.7
      )

      print(chat_completion)
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("Dynamo") }} />
  </Step>
</Steps>
