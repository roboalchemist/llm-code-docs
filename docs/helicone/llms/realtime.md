# Source: https://docs.helicone.ai/integrations/openai/realtime.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Realtime API

> Integrate OpenAI's Realtime API with Helicone to monitor and analyze your real-time conversations.

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

OpenAI's Realtime API enables low-latency, multi-modal conversational experiences with support for text and audio as both input and output.

By integrating with Helicone, you can monitor performance, analyze interactions, and gain valuable insights into your real-time conversations.

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title={strings.setApiKey}>
    ```javascript  theme={null}
     // For OpenAI
     OPENAI_API_KEY=<your-openai-api-key>
     HELICONE_API_KEY=<your-helicone-api-key>

     // For Azure
     AZURE_API_KEY=<your-azure-api-key>
     AZURE_RESOURCE=<your-azure-resource>
     AZURE_DEPLOYMENT=<your-azure-deployment>
     HELICONE_API_KEY=<your-helicone-api-key>
    ```
  </Step>

  <Step title={strings.configureWebSocketConnection}>
    You can connect to the Realtime API through Helicone using either OpenAI or Azure as your provider.

    <CodeGroup>
      ```typescript OpenAI theme={null}
      import WebSocket from "ws";
      import { config } from "dotenv";

      config();

      const url = "wss://api.helicone.ai/v1/gateway/oai/realtime?model=[MODEL_NAME]"; // gpt-4o-realtime-preview-2024-12-17

      const ws = new WebSocket(url, {
        headers: {
          "Authorization": `Bearer ${process.env.OPENAI_API_KEY}`,
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
          // Optional Helicone properties
          "Helicone-Session-Id": `session_${Date.now()}`,
          "Helicone-User-Id": "user_123"
        },
      });

      ws.on("open", function open() {
        console.log("Connected to server");

        ws.send(JSON.stringify({
          type: "session.update",
          session: {
            modalities: ["text", "audio"],
            instructions: "You are a helpful AI assistant...",
            voice: "alloy",
            input_audio_format: "pcm16",
            output_audio_format: "pcm16",
          }
        }));
      });
      ```

      ```typescript Azure theme={null}
      import WebSocket from "ws";
      import { config } from "dotenv";

      config();

      const url = `wss://api.helicone.ai/v1/gateway/oai/realtime?resource=${process.env.AZURE_RESOURCE}&deployment=${process.env.AZURE_DEPLOYMENT}`;

      const ws = new WebSocket(url, {
        headers: {
          "Authorization": `Bearer ${process.env.AZURE_API_KEY}`,
          "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`,
          // Optional Helicone properties
          "Helicone-Session-Id": `session_${Date.now()}`,
          "Helicone-User-Id": "user_123",
        },
      });

      ws.on("open", function open() {
        console.log("Connected to server");
        // Initialize session with desired configuration
        ws.send(JSON.stringify({
          type: "session.update",
          session: {
            modalities: ["text", "audio"],
            instructions: "You are a helpful AI assistant...",
            voice: "alloy",
            input_audio_format: "pcm16",
            output_audio_format: "pcm16",
          }
        }));
      });
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.handleWebSocketEvents}>
    ```javascript  theme={null}
    ws.on("message", function incoming(message) {
      try {
        const response = JSON.parse(message.toString());
        console.log("Received:", response);

        // Handle specific event types
        switch (response.type) {
          case "input_audio_buffer.speech_started":
            console.log("Speech detected!");
            break;
          case "input_audio_buffer.speech_stopped":
            console.log("Speech ended. Processing...");
            break;
          case "conversation.item.input_audio_transcription.completed":
            console.log("Transcription:", response.transcript);
            break;
          case "error":
            console.error("Error:", response.error.message);
            break;
        }
      } catch (error) {
        console.error("Error parsing message:", error);
      }
    });

    ws.on("error", function error(err) {
      console.error("WebSocket error:", err);
    });

    // Handle cleanup
    process.on("SIGINT", () => {
      console.log("\nClosing connection...");
      ws.close();
      process.exit(0);
    });
    ```
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("OpenAI Realtime API") }} />
  </Step>
</Steps>

## {strings.relatedGuides}

<CardGroup cols={2}>
  <Card title="Building a chatbot with OpenAI structured outputs" icon="lightbulb" href="/guides/cookbooks/openai-structured-outputs" iconType="light" vertical>
    {strings.chatbotCookbookDescription}
  </Card>

  <Card title="Trace, replay, and debug LLM sessions" icon="arrows-rotate" href="/guides/cookbooks/replay-llm-sessions" iconType="light" vertical>
    {strings.replayLlmSessionsCookbookDescription}
  </Card>
</CardGroup>
