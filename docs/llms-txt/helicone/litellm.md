# Source: https://docs.helicone.ai/getting-started/integration-method/litellm.md

# Source: https://docs.helicone.ai/gateway/integrations/litellm.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# LiteLLM Integration

> Use Helicone AI Gateway with LiteLLM to get top tier observability for your LLM requests.

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

[LiteLLM](https://www.litellm.ai/) is an self-hosted interface for calling LLM APIs.

## Integration Steps

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title={strings.setApiKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.setApiKeyInstructions }} />

    ```env  theme={null}
    HELICONE_API_KEY=sk-helicone-...
    ```
  </Step>

  <Step title={installSDK("LiteLLM")}>
    <p>
      {strings.installRequiredDependencies}
    </p>

    ```bash  theme={null}
    pip install litellm python-dotenv
    ```
  </Step>

  <Step title="Use LiteLLM with Helicone">
    Add the `helicone/` prefix to any model name to logg requests for Helicone:

    ```python  theme={null}
    import os
    from litellm import completion
    from dotenv import load_dotenv

    load_dotenv()

    # Route through Helicone by adding "helicone/" prefix
    response = completion(
        model="helicone/gpt-4o",
        messages=[{"role": "user", "content": "What is the capital of France?"}],
        api_key=os.getenv("HELICONE_API_KEY")
    )

    print(response.choices[0].message.content)
    ```

    <div dangerouslySetInnerHTML={{ __html: strings.modelRegistryDescription }} />
  </Step>

  <Step title={strings.viewRequestsInDashboard}>
    <div dangerouslySetInnerHTML={{ __html: strings.viewRequestsInDashboardDescription("LiteLLM") }} />

    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("any LiteLLM request") }} />

    <Tip>
      While you're here, why not <a href="https://github.com/helicone/helicone" target="_blank" rel="noreferrer">give us a star on GitHub</a>? It helps us a lot!
    </Tip>
  </Step>
</Steps>

## Complete Working Examples

### Basic Completion

```python  theme={null}
import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

# Simple completion
response = completion(
    model="helicone/gpt-4o-mini",
    messages=[{"role": "user", "content": "Tell me a fun fact about space"}],
    api_key=os.getenv("HELICONE_API_KEY")
)

print(response.choices[0].message.content)
```

### Streaming Responses

```python  theme={null}
import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

# Streaming example
response = completion(
    model="helicone/claude-4.5-sonnet",
    messages=[{"role": "user", "content": "Write a short story about a robot learning to paint"}],
    stream=True,
    api_key=os.getenv("HELICONE_API_KEY")
)

print("🤖 Assistant (streaming):")
for chunk in response:
    if hasattr(chunk.choices[0].delta, 'content') and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print("\n")
```

### Custom Properties and Session Tracking

Add metadata to track and filter your requests:

```python  theme={null}
import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

response = completion(
    model="helicone/gpt-4o-mini",
    messages=[{"role": "user", "content": "What's the weather like?"}],
    api_key=os.getenv("HELICONE_API_KEY"),
    metadata={
        "Helicone-Session-Id": "session-abc-123",
        "Helicone-Session-Name": "Weather Assistant",
        "Helicone-User-Id": "user-789",
        "Helicone-Property-Environment": "production",
        "Helicone-Property-App-Version": "2.1.0",
        "Helicone-Property-Feature": "weather-query"
    }
)

print(response.choices[0].message.content)
```

## Provider Selection and Fallback

Helicone's AI Gateway supports automatic failover between providers:

```python  theme={null}
import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

# Automatic routing (cheapest provider)
response = completion(
    model="helicone/gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}],
    api_key=os.getenv("HELICONE_API_KEY")
)

# Manual provider selection
response = completion(
    model="helicone/claude-4.5-sonnet/anthropic",
    messages=[{"role": "user", "content": "Hello!"}],
    api_key=os.getenv("HELICONE_API_KEY")
)

# Multiple provider fallback chain
# Try OpenAI first, then Anthropic if it fails
response = completion(
    model="helicone/gpt-4o/openai,claude-4.5-sonnet/anthropic",
    messages=[{"role": "user", "content": "Hello!"}],
    api_key=os.getenv("HELICONE_API_KEY")
)
```

## Advanced Features

### Caching

Enable caching to reduce costs and latency for repeated requests:

```python  theme={null}
import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

# Enable caching for this request
response = completion(
    model="helicone/gpt-4o",
    messages=[{"role": "user", "content": "What is 2+2?"}],
    api_key=os.getenv("HELICONE_API_KEY"),
    metadata={
        "Helicone-Cache-Enabled": "true"
    }
)

print(response.choices[0].message.content)

# Subsequent identical requests will be served from cache
response2 = completion(
    model="helicone/gpt-4o",
    messages=[{"role": "user", "content": "What is 2+2?"}],
    api_key=os.getenv("HELICONE_API_KEY"),
    metadata={
        "Helicone-Cache-Enabled": "true"
    }
)

print(response2.choices[0].message.content)
```

### Rate Limiting

Apply rate limiting policies to control request rates:

```python  theme={null}
import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

response = completion(
    model="helicone/gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
    api_key=os.getenv("HELICONE_API_KEY"),
    metadata={
        "Helicone-Rate-Limit-Policy": "basic-100"
    }
)

print(response.choices[0].message.content)
```

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

  <Card title="LiteLLM Documentation" icon="book" href="https://docs.litellm.ai">
    Official LiteLLM documentation
  </Card>
</CardGroup>
