# Source: https://docs.helicone.ai/gateway/integrations/langfuse.md

# Langfuse Integration

> Integrate Helicone AI Gateway with Langfuse to access 100+ LLM providers with observability and LLM tracing.

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

[Langfuse](https://langfuse.com/) is an open-source LLM observability and analytics platform that provides tracing, monitoring, and analytics for LLM applications.

<Note>
  This integration requires only **two changes** to your existing Langfuse code - updating the base URL and API key.
</Note>

## Integration Steps

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />

    Create a `.env` file in your project:

    ```env  theme={null}
    HELICONE_API_KEY=sk-helicone-...
    ```
  </Step>

  <Step title="Install Langfuse packages">
    ```bash  theme={null}
    pip install langfuse python-dotenv
    ```
  </Step>

  <Step title="Create a Langfuse OpenAI client using Helicone">
    Use Langfuse's OpenAI client wrapper with Helicone's base URL:

    ```python  theme={null}
    import os
    from dotenv import load_dotenv
    from langfuse.openai import openai

    # Load environment variables
    load_dotenv()

    # Create an OpenAI client with Helicone's base URL
    client = openai.OpenAI(
        api_key=os.getenv("HELICONE_API_KEY"),
        base_url="https://ai-gateway.helicone.ai/"
    )
    ```
  </Step>

  <Step title="Make requests with Langfuse tracing">
    Your existing Langfuse code continues to work without any changes:

    ```python  theme={null}
    # Make a chat completion request
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a fun fact about space."}
        ],
        name="fun-fact-request"  # Optional: Name of the generation in Langfuse
    )

    # Print the assistant's reply
    print(response.choices[0].message.content)
    ```

    <div dangerouslySetInnerHTML={{ __html: strings.modelRegistryDescription }} />
  </Step>

  <Step title={strings.viewRequestsInDashboard}>
    <div dangerouslySetInnerHTML={{ __html: strings.viewRequestsInDashboardDescription("Langfuse") }} />

    * Request/response bodies
    * Latency metrics
    * Token usage and costs
    * Model performance analytics
    * Error tracking
    * LLM traces and spans in Langfuse
    * Session tracking

    <Tip>
      While you're here, why not <a href="https://github.com/helicone/helicone" target="_blank" rel="noreferrer">give us a star on GitHub</a>? It helps us a lot!
    </Tip>
  </Step>
</Steps>

## Complete Working Example

```python  theme={null}
#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from langfuse.openai import openai

# Load environment variables
load_dotenv()

# Create an OpenAI client with Helicone's base URL
client = openai.OpenAI(
    api_key=os.getenv("HELICONE_API_KEY"),
    base_url="https://ai-gateway.helicone.ai/"
)

# Make a chat completion request
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a fun fact about space."}
    ],
    name="fun-fact-request"  # Optional: Name of the generation in Langfuse
)

# Print the assistant's reply
print(response.choices[0].message.content)
```

### Streaming Responses

Langfuse supports streaming responses with full observability:

```python  theme={null}
# Streaming example
stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Write a short story about a robot learning to code."}
    ],
    stream=True,
    name="streaming-story"
)

print("🤖 Assistant (streaming):")
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)
print("\n")
```

### Nested Example

```python  theme={null}
import os
from dotenv import load_dotenv
from langfuse import observe
from langfuse.openai import openai

load_dotenv()

client = openai.OpenAI(
    base_url="https://ai-gateway.helicone.ai/",
    api_key=os.getenv("HELICONE_API_KEY"),
)

@observe()  # This decorator enables tracing of the function
def analyze_text(text: str):
    # First LLM call: Summarize the text
    summary_response = summarize_text(text)
    summary = summary_response.choices[0].message.content

    # Second LLM call: Analyze the sentiment of the summary
    sentiment_response = analyze_sentiment(summary)
    sentiment = sentiment_response.choices[0].message.content

    return {
        "summary": summary,
        "sentiment": sentiment
    }

@observe()  # Nested function to be traced
def summarize_text(text: str):
    return client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You summarize texts in a concise manner."},
            {"role": "user", "content": f"Summarize the following text:\n{text}"}
        ],
        name="summarize-text"
    )

@observe()  # Nested function to be traced
def analyze_sentiment(summary: str):
    return client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You analyze the sentiment of texts."},
            {"role": "user", "content": f"Analyze the sentiment of the following summary:\n{summary}"}
        ],
        name="analyze-sentiment"
    )

# Example usage
text_to_analyze = "OpenAI's GPT-4 model has significantly advanced the field of AI, setting new standards for language generation."
analyze_text(text_to_analyze)
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
</CardGroup>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.helicone.ai/llms.txt