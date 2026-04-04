# Source: https://docs.helicone.ai/integrations/openai/responses.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpenAI Responses API

> Integrate OpenAI Responses API with Helicone to monitor and analyze your model's responses.

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

OpenAI Responses enable you to provide text or image inputs to generate text or JSON outputs by calling your own custom code or use built-in tools like web search or file search. By integrating them with Helicone, you can monitor performance, analyze interactions, and gain valuable insights into your responses.

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title={strings.setApiKey}>
    ```javascript  theme={null}
    HELICONE_API_KEY=<your-helicone-api-key>
    OPENAI_API_KEY=<your-openai-api-key>
    ```
  </Step>

  <Step title={strings.modifyBasePath}>
    ```javascript  theme={null}
    import OpenAI from "openai";

    const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
      baseURL: "https://oai.helicone.ai/v1",
      defaultHeaders: {
        "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY}`
      }
    });
    ```
  </Step>

  <Step title={strings.startUsing("OpenAI Responses API")}>
    <Note>
      Replace the response's model, input, and output with content relevant to your application.
    </Note>

    <CodeGroup>
      ```javascript text theme={null}
      const textInputResponse = await openai.responses.create({
          model: "gpt-4.1",
          input: "What is the meaning of life?"
      });

      console.log(textInputResponse);
      ```

      ```javascript image theme={null}
      const imageInputResponse = await openai.responses.create({
          model: "gpt-4.1",
          input: [
              {
                  role: "user",
                  content: [
                      { type: "input_text", text: "what is in this image?" },
                      {
                          type: "input_image",
                          image_url:
                              "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                      },
                  ],
              },
          ],
      });

      console.log(imageInputResponse);
      ```

      ```javascript json theme={null}
      const jsonInputResponse = await openai.responses.create({
        model: "gpt-4.1",
        input: { name: "John", age: 30 }
      });

      console.log(jsonInputResponse);
      ```

      ```javascript web-search theme={null}
      const webSearchResponse = await openai.responses.create({
        model: "gpt-4.1",
        tools: [{ type: "web_search_preview" }],
        input: "What was a positive news story from today?",
      });

      console.log(webSearchResponse);
      ```

      ```javascript file-search theme={null}
      const fileSearchResponse = await openai.responses.create({
        model: "gpt-4.1",
        tools: [{
          type: "file_search",
          vector_store_ids: ["vs_1234567890"],
          max_num_results: 20
        }],
        input: "What are the attributes of an ancient brown dragon?",
      });

      console.log(fileSearchResponse);
      ```

      ```javascript streaming theme={null}
      const streamingResponse = await openai.responses.create({
        model: "gpt-4.1",
        instructions: "You are a helpful assistant.",
        input: "Hello!",
        stream: true,
      });

      for await (const event of streamingResponse) {
        console.log(event);
      }
      ```

      ```javascript function-calling theme={null}
      const tools = [
        {
          type: "function" as const,
          name: "get_current_weather",
          description: "Get the current weather in a given location",
          parameters: {
            type: "object",
            properties: {
              location: {
                type: "string",
                description: "The city and state, e.g. San Francisco, CA"
              },
              unit: { type: "string", enum: ["celsius", "fahrenheit"] }
            },
            required: ["location", "unit"]
          },
          strict: true
        },
      ];

      const functionCallingResponse = await openai.responses.create({
        model: "gpt-4.1",
        tools: tools,
        input: "What is the weather like in Boston today?",
        tool_choice: "auto"
      });

      console.log(functionCallingResponse);
      ```

      ```javascript reasoning theme={null}
      const reasoningResponse = await openai.responses.create({
        model: "o3-mini",
        input: "How much wood would a woodchuck chuck?",
        reasoning: {
          effort: "high"
        }
      });

      console.log(reasoningResponse);
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("OpenAI Responses API") }} />
  </Step>
</Steps>

## {strings.relatedGuides}

<CardGroup cols={2}>
  <Card title="Building a chatbot with OpenAI structured outputs" icon="lightbulb" href="/guides/cookbooks/openai-structured-outputs" iconType="light" vertical>
    {strings.chatbotCookbookDescription}
  </Card>

  <Card title="Use Chain-of-Thought Prompting" icon="stairs" href="/guides/prompt-engineering/use-chain-of-thought-prompting" iconType="light" vertical>
    {strings.chainOfThoughtPromptingCookbookDescription}
  </Card>
</CardGroup>
