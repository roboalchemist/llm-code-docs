# Source: https://docs.helicone.ai/gateway/integrations/dpsy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# DSPy

> Integrate Helicone AI Gateway with DSPy to access 100+ LLM providers with unified observability and optimization.

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

[DSPy](https://dspy.ai) is a declarative framework for building modular AI software with structured code instead of brittle prompts, offering algorithms that compile AI programs into effective prompts and weights for language models across classifiers, RAG pipelines, and agent loops.

## Integration Steps

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title={strings.setApiKey}>
    Create a `.env` file in your project.

    ```env  theme={null}
    HELICONE_API_KEY=sk-helicone-...
    ```
  </Step>

  <Step title={strings.installSDK("DSPy")}>
    <p>
      {strings.installRequiredDependencies}
    </p>

    ```bash Python theme={null}
    pip install dspy
    ```
  </Step>

  <Step title={strings.startUsing("DSPy")}>
    <p>
      {strings.viewRequestsInDashboard}
    </p>

    ```python Python theme={null}
    import dspy
    import os
    from dotenv import load_dotenv

    load_dotenv()

    # Configure DSPy to use Helicone AI Gateway
    lm = dspy.LM(
      'gpt-4o-mini',  # or any other model from the Helicone model registry
      api_key=os.getenv('HELICONE_API_KEY'),
      api_base='https://ai-gateway.helicone.ai/'
    )

    dspy.configure(lm=lm)

    print(lm("Hello, world!"))
    ```

    <div dangerouslySetInnerHTML={{ __html: strings.modelRegistryDescription }} />
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("DSPy") }} />

    <Tip>
      While you're here, why not <a href="https://github.com/helicone/helicone" target="_blank" rel="noreferrer">give us a star on GitHub</a>? It helps us a lot!
    </Tip>
  </Step>
</Steps>

## Complete Working Examples

### Basic Chain of Thought

```python Python theme={null}
import dspy
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Helicone AI Gateway
lm = dspy.LM(
    'gpt-4o-mini',
    api_key=os.getenv('HELICONE_API_KEY'),
    api_base='https://ai-gateway.helicone.ai/v1'
)
dspy.configure(lm=lm)

# Define a module
qa = dspy.ChainOfThought('question -> answer')

# Run inference
response = qa(question="How many floors are in the castle David Gregory inherited?")

print('Answer:', response.answer)
print('Reasoning:', response.reasoning)
```

### Custom Generation Configuration

Configure temperature, max\_tokens, and other parameters:

```python Python theme={null}
import dspy
import os
from dotenv import load_dotenv

load_dotenv()

# Configure with custom generation parameters
lm = dspy.LM(
    'gpt-4o-mini',
    api_key=os.getenv('HELICONE_API_KEY'),
    api_base='https://ai-gateway.helicone.ai/v1',
    temperature=0.9,
    max_tokens=2000
)
dspy.configure(lm=lm)

# Use with any DSPy module
predict = dspy.Predict("question -> creative_answer")
response = predict(question="Write a creative story about AI")
print(response.creative_answer)
```

### Tracking with Custom Properties

Add custom properties to track and filter your requests in the Helicone dashboard:

```python Python theme={null}
import dspy
import os
from dotenv import load_dotenv

load_dotenv()

# Configure with custom Helicone headers
lm = dspy.LM(
    'gpt-4o-mini',
    api_key=os.getenv('HELICONE_API_KEY'),
    api_base='https://ai-gateway.helicone.ai/v1',
    extra_headers={
        # Session tracking
        'Helicone-Session-Id': 'dspy-example-session',
        'Helicone-Session-Name': 'Question Answering',

        # User tracking
        'Helicone-User-Id': 'user-123',

        # Custom properties for filtering
        'Helicone-Property-Environment': 'production',
        'Helicone-Property-Module': 'chain-of-thought',
        'Helicone-Property-Version': '1.0.0'
    }
)
dspy.configure(lm=lm)

# Use normally
qa = dspy.ChainOfThought('question -> answer')
response = qa(question="What is DSPy?")
print(response.answer)
```

## Helicone Prompts Integration

Use Helicone Prompts for centralized prompt management with DSPy signatures:

```python Python theme={null}
import dspy
import os
from dotenv import load_dotenv

load_dotenv()

# Configure with prompt parameters
lm = dspy.LM(
    'gpt-4o-mini',
    api_key=os.getenv('HELICONE_API_KEY'),
    api_base='https://ai-gateway.helicone.ai/v1',
    extra_body={
        'prompt_id': 'customer-support-prompt-id',
        'version_id': 'version-uuid',
        'environment': 'production',
        'inputs': {
            'customer_name': 'Sarah',
            'issue_type': 'technical'
        }
    }
)
dspy.configure(lm=lm)
```

<Note>
  Learn more about [Prompts with AI Gateway](/gateway/concepts/prompt-caching).
</Note>

## Advanced Features

### Rate Limiting

Configure rate limits for your DSPy applications:

```python Python theme={null}
lm = dspy.LM(
    'gpt-4o-mini',
    api_key=os.getenv('HELICONE_API_KEY'),
    api_base='https://ai-gateway.helicone.ai/v1',
    extra_headers={
        'Helicone-Rate-Limit-Policy': 'basic-100'
    }
)
```

### Caching

Enable intelligent caching to reduce costs:

```python Python theme={null}
lm = dspy.LM(
    'gpt-4o-mini',
    api_key=os.getenv('HELICONE_API_KEY'),
    api_base='https://ai-gateway.helicone.ai/v1',
    cache=True  # DSPy's built-in caching works with Helicone
)
```

### Session Tracking for Multi-Turn Conversations

Track entire conversation flows in DSPy programs:

```python Python theme={null}
import uuid

session_id = str(uuid.uuid4())

lm = dspy.LM(
    'gpt-4o-mini',
    api_key=os.getenv('HELICONE_API_KEY'),
    api_base='https://ai-gateway.helicone.ai/v1',
    extra_headers={
        'Helicone-Session-Id': session_id,
        'Helicone-Session-Name': 'Customer Support',
        'Helicone-Session-Path': '/support/chat'
    }
)
dspy.configure(lm=lm)

# All calls in this session will be grouped together
qa = dspy.ChainOfThought('question -> answer')

# Multiple turns
response1 = qa(question="What is your return policy?")
response2 = qa(question="How long does shipping take?")
response3 = qa(question="Do you ship internationally?")

# View the full conversation in Helicone Sessions
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
