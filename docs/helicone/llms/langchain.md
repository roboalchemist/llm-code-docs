# Source: https://docs.helicone.ai/integrations/openai/langchain.md

# Source: https://docs.helicone.ai/integrations/azure/langchain.md

# Source: https://docs.helicone.ai/integrations/anthropic/langchain.md

# Source: https://docs.helicone.ai/gateway/integrations/langchain.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# LangChain Integration

> Integrate Helicone AI Gateway with LangChain to access 100+ LLM providers with unified observability.

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

[LangChain](https://www.langchain.com/) is a popular open-source framework for building applications with large language models across Python, TypeScript, and other languages. By integrating Helicone AI Gateway with LangChain, you can:

* **Route to different models & providers** with automatic failover through a single endpoint
* **Unified billing** with pass-through billing or bring your own keys
* **Monitor all requests** with automatic cost tracking in one dashboard
* **Stream responses** with full observability for real-time applications

<Note>
  This integration requires only **two changes** to your existing LangChain code - updating the base URL and API key.
</Note>

## Integration Steps

<Steps>
  <Step title="Create an account + Generate an API Key">
    Sign up at [helicone.ai](https://www.helicone.ai) and generate an [API key](https://us.helicone.ai/settings/api-keys).

    <Note>
      You'll also need to configure your provider API keys (OpenAI, Anthropic, etc.) at [Helicone Providers](https://us.helicone.ai/providers) for BYOK (Bring Your Own Keys).
    </Note>
  </Step>

  <Step title="Set environment variables">
    ```bash  theme={null}
    # Your Helicone API key
    export HELICONE_API_KEY=<your-helicone-api-key>
    ```

    Create a `.env` file in your project:

    ```env  theme={null}
    HELICONE_API_KEY=sk-helicone-...
    ```
  </Step>

  <Step title="Install LangChain packages">
    <CodeGroup>
      ```bash TypeScript theme={null}
      npm install @langchain/openai @langchain/core dotenv
      # or
      yarn add @langchain/openai @langchain/core dotenv
      ```

      ```bash Python theme={null}
      pip install langchain-openai langchain-core python-dotenv
      ```
    </CodeGroup>
  </Step>

  <Step title="Configure LangChain with Helicone AI Gateway">
    <CodeGroup>
      ```typescript TypeScript theme={null}
      import { ChatOpenAI } from "@langchain/openai";
      import { HumanMessage, SystemMessage } from "@langchain/core/messages";
      import dotenv from 'dotenv';

      dotenv.config();

      // Initialize ChatOpenAI with Helicone AI Gateway
      const chat = new ChatOpenAI({
          model: 'gpt-4.1-mini',  // 100+ models supported
          apiKey: process.env.HELICONE_API_KEY,
          configuration: {
              baseURL: "https://ai-gateway.helicone.ai/v1",
              defaultHeaders: {
                  // Optional: Add custom tracking headers
                  "Helicone-Session-Id": "my-session",
                  "Helicone-User-Id": "user-123",
                  "Helicone-Property-Environment": "production",
              },
          },
      });
      ```

      ```python Python theme={null}
      import os
      from langchain_openai import ChatOpenAI
      from langchain_core.messages import HumanMessage, SystemMessage
      from dotenv import load_dotenv

      load_dotenv()

      # Initialize ChatOpenAI with Helicone AI Gateway
      chat = ChatOpenAI(
          model='gpt-4.1-mini',  # 100+ models supported
          api_key=os.getenv('HELICONE_API_KEY'),
          base_url="https://ai-gateway.helicone.ai/v1",
          default_headers={
              # Optional: Add custom tracking headers
              'Helicone-Session-Id': 'my-session',
              'Helicone-User-Id': 'user-123',
              'Helicone-Property-Environment': 'production',
          },
      )
      ```
    </CodeGroup>

    <Info>
      The **only changes** from a standard LangChain setup are the `apiKey`, `baseURL` (or `base_url` in Python), and optional tracking headers. Everything else stays the same!
    </Info>

    <div dangerouslySetInnerHTML={{ __html: strings.modelRegistryDescription }} />
  </Step>

  <Step title="Use LangChain normally">
    Your existing LangChain code continues to work without any changes:

    <CodeGroup>
      ```typescript TypeScript theme={null}
      // Simple completion
      const response = await chat.invoke([
          new SystemMessage("You are a helpful assistant."),
          new HumanMessage("What is the capital of France?"),
      ]);

      console.log(response.content);
      ```

      ```python Python theme={null}
      # Simple completion
      messages = [
          SystemMessage(content="You are a helpful assistant."),
          HumanMessage(content="What is the capital of France?"),
      ]

      response = chat.invoke(messages)
      print(response.content)
      ```
    </CodeGroup>
  </Step>

  <Step title={strings.viewRequestsInDashboard}>
    <div dangerouslySetInnerHTML={{ __html: strings.viewRequestsInDashboardDescription("LangChain") }} />

    * Request/response bodies
    * Latency metrics
    * Token usage and costs
    * Model performance analytics
    * Error tracking
    * Session tracking

    <Tip>
      While you're here, why not <a href="https://github.com/helicone/helicone" target="_blank" rel="noreferrer">give us a star on GitHub</a>? It helps us a lot!
    </Tip>
  </Step>
</Steps>

## Migration Example

Here's what migrating an existing LangChain application looks like:

### Before (Direct OpenAI)

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { ChatOpenAI } from "@langchain/openai";

  const chat = new ChatOpenAI({
      model: 'gpt-4o-mini',
      apiKey: process.env.OPENAI_API_KEY,
  });
  ```

  ```python Python theme={null}
  from langchain_openai import ChatOpenAI

  chat = ChatOpenAI(
      model='gpt-4o-mini',
      api_key=os.getenv('OPENAI_API_KEY'),
  )
  ```
</CodeGroup>

### After (Helicone AI Gateway)

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { ChatOpenAI } from "@langchain/openai";

  const chat = new ChatOpenAI({
      model: 'gpt-4.1-mini',                      // 100+ models supported
      apiKey: process.env.HELICONE_API_KEY,      // Your Helicone API key
      configuration: {
          baseURL: "https://ai-gateway.helicone.ai/v1"  // Add this!
      },
  });
  ```

  ```python Python theme={null}
  from langchain_openai import ChatOpenAI

  chat = ChatOpenAI(
      model='gpt-4.1-mini',                      # 100+ models supported
      api_key=os.getenv('HELICONE_API_KEY'),    # Your Helicone API key
      base_url="https://ai-gateway.helicone.ai/v1"  # Add this!
  )
  ```
</CodeGroup>

That's it! Just two changes and you're routing through Helicone's AI Gateway.

## Complete Working Examples

### Basic Example

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { ChatOpenAI } from "@langchain/openai";
  import { HumanMessage, SystemMessage } from "@langchain/core/messages";
  import dotenv from 'dotenv';

  dotenv.config();

  const chat = new ChatOpenAI({
      model: 'gpt-4.1-mini',  // 100+ models supported
      apiKey: process.env.HELICONE_API_KEY,
      configuration: {
          baseURL: "https://ai-gateway.helicone.ai/v1",
          defaultHeaders: {
              "Helicone-Session-Id": "langchain-example",
              "Helicone-User-Id": "demo-user",
          },
      },
  });

  async function main() {
      console.log('🦜 Starting LangChain + Helicone AI Gateway example...\n');

      const response = await chat.invoke([
          new SystemMessage("You are a helpful assistant."),
          new HumanMessage("Tell me a joke about programming."),
      ]);

      console.log('🤖 Assistant response:');
      console.log(response.content);
      console.log('\n✅ Completed successfully!');
  }

  main().catch(console.error);
  ```

  ```python Python theme={null}
  import os
  from langchain_openai import ChatOpenAI
  from langchain_core.messages import HumanMessage, SystemMessage
  from dotenv import load_dotenv

  load_dotenv()

  chat = ChatOpenAI(
      model='gpt-4.1-mini',  # 100+ models supported
      api_key=os.getenv('HELICONE_API_KEY'),
      base_url="https://ai-gateway.helicone.ai/v1",
      default_headers={
          'Helicone-Session-Id': 'langchain-example',
          'Helicone-User-Id': 'demo-user',
      },
  )

  def main():
      print('🐍 Starting LangChain + Helicone AI Gateway example...\n')

      messages = [
          SystemMessage(content="You are a helpful assistant."),
          HumanMessage(content="Tell me a joke about Python programming."),
      ]

      response = chat.invoke(messages)

      print('🤖 Assistant response:')
      print(response.content)
      print('\n✅ Completed successfully!')

  if __name__ == "__main__":
      main()
  ```
</CodeGroup>

### Streaming Example

<CodeGroup>
  ```typescript TypeScript theme={null}
  async function streamingExample() {
      console.log('\n🌊 Streaming example...\n');

      const stream = await chat.stream([
          new SystemMessage("You are a helpful assistant."),
          new HumanMessage("Write a short story about a robot learning to code."),
      ]);

      console.log('🤖 Assistant (streaming):');
      for await (const chunk of stream) {
          process.stdout.write(chunk.content as string);
      }
      console.log('\n\n✅ Streaming completed!');
  }

  streamingExample().catch(console.error);
  ```

  ```python Python theme={null}
  def streaming_example():
      print('\n🌊 Streaming example...\n')

      messages = [
          SystemMessage(content="You are a helpful assistant."),
          HumanMessage(content="Write a short story about a robot learning to code."),
      ]

      print('🤖 Assistant (streaming):')
      for chunk in chat.stream(messages):
          print(chunk.content, end='', flush=True)

      print('\n\n✅ Streaming completed!')

  streaming_example()
  ```
</CodeGroup>

### Multiple Models Example

<CodeGroup>
  ```typescript TypeScript theme={null}
  async function testMultipleModels() {
      console.log('🚀 Testing multiple models through Helicone AI Gateway\n');

      const models = [
          { id: 'gpt-4.1-mini', name: 'OpenAI GPT-4.1 Mini' },
          { id: 'claude-opus-4-1', name: 'Anthropic Claude Opus 4.1' },
          { id: 'gemini-2.5-flash-lite', name: 'Google Gemini 2.5 Flash Lite' },
      ];

      for (const model of models) {
          try {
              const chat = new ChatOpenAI({
                  model: model.id,
                  apiKey: process.env.HELICONE_API_KEY,
                  configuration: {
                      baseURL: "https://ai-gateway.helicone.ai/v1",
                  },
              });

              console.log(`🤖 Testing ${model.name}... `);
              const response = await chat.invoke([
                  new HumanMessage("Say hello in one sentence."),
              ]);
              console.log(`   Response: ${response.content}\n`);
          } catch (error) {
              console.error(`   Error: ${error}\n`);
          }
      }

      console.log('✅ All models tested!');
      console.log('🔍 Check your dashboard: https://us.helicone.ai/dashboard');
  }

  testMultipleModels().catch(console.error);
  ```

  ```python Python theme={null}
  def test_multiple_models():
      print('🚀 Testing multiple models through Helicone AI Gateway\n')

      models = [
          {'id': 'gpt-4.1-mini', 'name': 'OpenAI GPT-4.1 Mini'},
          {'id': 'claude-opus-4-1', 'name': 'Anthropic Claude Opus 4.1'},
          {'id': 'gemini-2.5-flash-lite', 'name': 'Google Gemini 2.5 Flash Lite'},
      ]

      for model in models:
          try:
              chat = ChatOpenAI(
                  model=model['id'],
                  api_key=os.getenv('HELICONE_API_KEY'),
                  base_url="https://ai-gateway.helicone.ai/v1",
              )

              print(f"🤖 Testing {model['name']}... ")
              response = chat.invoke([
                  HumanMessage(content="Say hello in one sentence."),
              ])
              print(f"   Response: {response.content}\n")
          except Exception as error:
              print(f"   Error: {error}\n")

      print('✅ All models tested!')
      print('🔍 Check your dashboard: https://us.helicone.ai/dashboard')

  test_multiple_models()
  ```
</CodeGroup>

### Batch Processing Example (Python)

```python Python theme={null}
def batch_example():
    print('\n📦 Batch processing example...\n')

    message_batches = [
        [HumanMessage(content="What is Python?")],
        [HumanMessage(content="What is JavaScript?")],
        [HumanMessage(content="What is TypeScript?")],
    ]

    responses = chat.batch(message_batches)

    print('🤖 Batch responses:')
    for i, response in enumerate(responses, 1):
        print(f'\nResponse {i}: {response.content}')

    print('\n✅ Batch processing completed!')

batch_example()
```

## Helicone Prompts Integration

You can use Helicone Prompts for centralized prompt management and versioning by passing parameters through `modelKwargs`:

<CodeGroup>
  ```typescript TypeScript theme={null}
  const chat = new ChatOpenAI({
      model: 'gpt-4.1-mini',
      apiKey: process.env.HELICONE_API_KEY,
      modelKwargs: {
          prompt_id: 'customer-support-prompt',
          version_id: 'version-uuid',
          environment: 'production',
          inputs: { customer_name: 'John', issue_type: 'billing' },
      },
      configuration: {
          baseURL: "https://ai-gateway.helicone.ai/v1",
      },
  });
  ```

  ```python Python theme={null}
  chat = ChatOpenAI(
      model='gpt-4.1-mini',
      api_key=os.getenv('HELICONE_API_KEY'),
      base_url="https://ai-gateway.helicone.ai/v1",
      model_kwargs={
          'prompt_id': 'customer-support-prompt',
          'version_id': 'version-uuid',
          'environment': 'production',
          'inputs': {'customer_name': 'John', 'issue_type': 'billing'},
      },
  )
  ```
</CodeGroup>

<Note>
  All prompt parameters (`prompt_id`, `version_id`, `environment`, `inputs`) are optional. Learn more about [Prompts with AI Gateway](/gateway/concepts/prompt-caching).
</Note>

## Custom Headers and Properties

You can add custom properties to track and filter your requests:

<CodeGroup>
  ```typescript TypeScript theme={null}
  const chat = new ChatOpenAI({
      model: 'gpt-4.1-mini',
      apiKey: process.env.HELICONE_API_KEY,
      configuration: {
          baseURL: "https://ai-gateway.helicone.ai/v1",
          defaultHeaders: {
              // Session tracking
              "Helicone-Session-Id": "session-abc-123",
              "Helicone-Session-Name": "Customer Support Chat",
              "Helicone-Session-Path": "/support/chat/456",

              // User tracking
              "Helicone-User-Id": "user-789",

              // Custom properties for filtering
              "Helicone-Property-Environment": "production",
              "Helicone-Property-App-Version": "2.1.0",
              "Helicone-Property-Feature": "customer-support",

              // Rate limiting (optional)
              "Helicone-Rate-Limit-Policy": "basic-100",
          },
      },
  });
  ```

  ```python Python theme={null}
  chat = ChatOpenAI(
      model='gpt-4.1-mini',
      api_key=os.getenv('HELICONE_API_KEY'),
      base_url="https://ai-gateway.helicone.ai/v1",
      default_headers={
          # Session tracking
          'Helicone-Session-Id': 'session-abc-123',
          'Helicone-Session-Name': 'Customer Support Chat',
          'Helicone-Session-Path': '/support/chat/456',

          # User tracking
          'Helicone-User-Id': 'user-789',

          # Custom properties for filtering
          'Helicone-Property-Environment': 'production',
          'Helicone-Property-App-Version': '2.1.0',
          'Helicone-Property-Feature': 'customer-support',

          # Rate limiting (optional)
          'Helicone-Rate-Limit-Policy': 'basic-100',
      },
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
</CardGroup>
