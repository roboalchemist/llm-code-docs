# Source: https://python.useinstructor.com/integrations/index.md

# LLM Provider Integration Tutorials

Learn how to integrate Instructor with various AI model providers. These comprehensive tutorials cover everything from cloud-based services like OpenAI and Anthropic to local open-source models, helping you extract structured outputs from any LLM.

- **Major Cloud Providers**

  Leading AI providers with comprehensive features

  [OpenAI](https://python.useinstructor.com/integrations/openai/index.md) Â· [OpenAI Responses](https://python.useinstructor.com/integrations/openai-responses/index.md) Â· [Azure](https://python.useinstructor.com/integrations/azure/index.md) Â· [Anthropic](https://python.useinstructor.com/integrations/anthropic/index.md) Â· [Google.GenerativeAI](https://python.useinstructor.com/integrations/google/index.md) Â· [Vertex AI](https://python.useinstructor.com/integrations/vertex/index.md) Â· [AWS Bedrock](https://python.useinstructor.com/integrations/bedrock/index.md) Â· [Google.GenAI](https://python.useinstructor.com/integrations/genai/index.md) Â· [xAI](https://python.useinstructor.com/integrations/xai/index.md)

- **Additional Cloud Providers**

  Other commercial AI providers with specialized offerings

  [Cohere](https://python.useinstructor.com/integrations/cohere/index.md) Â· [Mistral](https://python.useinstructor.com/integrations/mistral/index.md) Â· [DeepSeek](https://python.useinstructor.com/integrations/deepseek/index.md) Â· [Together AI](https://python.useinstructor.com/integrations/together/index.md) Â· [Groq](https://python.useinstructor.com/integrations/groq/index.md) Â· [Fireworks](https://python.useinstructor.com/integrations/fireworks/index.md) Â· [Cerebras](https://python.useinstructor.com/integrations/cerebras/index.md) Â· [Writer](https://python.useinstructor.com/integrations/writer/index.md) Â· [Perplexity](https://python.useinstructor.com/integrations/perplexity/index.md) [SambaNova](https://python.useinstructor.com/integrations/sambanova/index.md)

- **Open Source**

  Run open-source models locally or in the cloud

  [Ollama](https://python.useinstructor.com/integrations/ollama/index.md) Â· [llama-cpp-python](https://python.useinstructor.com/integrations/llama-cpp-python/index.md)

- **Routing**

  Unified interfaces for multiple providers

  [LiteLLM](https://python.useinstructor.com/integrations/litellm/index.md) [OpenRouter](https://python.useinstructor.com/integrations/openrouter/index.md)

## Common Features

All integrations support these core features:

| Feature             | Description                                                  | Documentation                                                                                                                                  |
| ------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Model Patching**  | Enhance provider clients with structured output capabilities | [Patching](https://python.useinstructor.com/concepts/patching/index.md)                                                                        |
| **Response Models** | Define expected response schema with Pydantic                | [Models](https://python.useinstructor.com/concepts/models/index.md)                                                                            |
| **Validation**      | Ensure responses match your schema definition                | [Validation](https://python.useinstructor.com/concepts/validation/index.md)                                                                    |
| **Streaming**       | Stream partial or iterative responses                        | [Partial](https://python.useinstructor.com/concepts/partial/index.md), [Iterable](https://python.useinstructor.com/concepts/iterable/index.md) |
| **Hooks**           | Add callbacks for monitoring and debugging                   | [Hooks](https://python.useinstructor.com/concepts/hooks/index.md)                                                                              |

However, each provider has different capabilities and limitations. Refer to the specific provider documentation for details.

## Provider Modes

Providers support different methods for generating structured outputs:

| Mode             | Description                              | Providers                     |
| ---------------- | ---------------------------------------- | ----------------------------- |
| `TOOLS`          | Uses OpenAI-style tools/function calling | OpenAI, Anthropic, Mistral    |
| `PARALLEL_TOOLS` | Multiple simultaneous tool calls         | OpenAI                        |
| `JSON`           | Direct JSON response generation          | OpenAI, Gemini, Cohere, GenAI |
| `MD_JSON`        | JSON embedded in markdown                | Most providers                |

See the [Modes Comparison](https://python.useinstructor.com/modes-comparison/index.md) guide for details.

## Getting Started

There are two ways to use providers with Instructor:

### 1. Using Provider Initialization (Recommended)

The simplest way to get started is using the provider initialization:

```python
import instructor
from pydantic import BaseModel

class UserInfo(BaseModel):
    name: str
    age: int

# Initialize any provider with a simple string
client = instructor.from_provider("openai/gpt-4")
# Or use async client
async_client = instructor.from_provider("anthropic/claude-3-sonnet", async_client=True)

# Use the same interface for all providers
response = client.create(
    response_model=UserInfo,
    messages=[{"role": "user", "content": "Your prompt"}]
)
```

Supported provider strings:

- `openai/model-name`: OpenAI models
- `anthropic/model-name`: Anthropic models
- `google/model-name`: Google models
- `mistral/model-name`: Mistral models
- `cohere/model-name`: Cohere models
- `perplexity/model-name`: Perplexity models
- `groq/model-name`: Groq models
- `writer/model-name`: Writer models
- `bedrock/model-name`: AWS Bedrock models
- `cerebras/model-name`: Cerebras models
- `fireworks/model-name`: Fireworks models
- `vertexai/model-name`: Vertex AI models
- `genai/model-name`: Google GenAI models
- `ollama/model-name`: Ollama models

### Provider Checklist

Use these example strings with `from_provider` to quickly get started:

- `instructor.from_provider("openai/gpt-5-nano")`
- `instructor.from_provider("anthropic/claude-3-sonnet")`
- `instructor.from_provider("google/gemini-2.5-flash")`
- `instructor.from_provider("mistral/mistral-large-latest")`
- `instructor.from_provider("cohere/command-r")`
- `instructor.from_provider("perplexity/sonar-small")`
- `instructor.from_provider("groq/llama3-8b-8192")`
- `instructor.from_provider("writer/palmyra-x-004")`
- `instructor.from_provider("bedrock/anthropic.claude-3-sonnet-20240229-v1:0")`
- `instructor.from_provider("cerebras/llama3.1-70b")`
- `instructor.from_provider("fireworks/llama-v3-70b-instruct")`
- `instructor.from_provider("vertexai/gemini-3-flash")`
- `instructor.from_provider("genai/gemini-3-flash")`
- `instructor.from_provider("ollama/llama3")`

### 2. Manual Client Setup

Alternatively, you can manually set up the client:

1. Install the required dependencies:

   ```bash
   pip install "instructor[provider]"  # e.g., instructor[anthropic]
   ```

1. Import the provider client and patch it with Instructor:

   ```python
   import instructor
   from provider_package import Client

   client = instructor.from_provider(Client())
   ```

1. Use the patched client with your Pydantic model:

   ```python
   response = client.create(
       response_model=YourModel,
       messages=[{"role": "user", "content": "Your prompt"}]
   )
   ```

For provider-specific setup and examples, visit each provider's documentation page.

## Need Help?

If you need assistance with a specific integration:

1. Check the provider-specific documentation
1. Browse the [examples](https://python.useinstructor.com/examples/index.md) and [cookbooks](https://python.useinstructor.com/examples/index.md)
1. Search existing [GitHub issues](https://github.com/jxnl/instructor/issues)
1. Join our [Discord community](https://discord.gg/bD9YE9JArw)
