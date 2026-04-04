# Source: https://braintrust.dev/docs/integrations/agent-frameworks/pydantic-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pydantic AI

[Pydantic AI](https://ai.pydantic.dev) is a Python agent framework built on Pydantic. Braintrust provides native integration to trace Pydantic AI agents, capturing inputs, outputs, tool calls, and performance metrics.

## Setup

Install the Braintrust SDK and Pydantic AI:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
pip install braintrust pydantic-ai
```

## Trace Pydantic AI agents

Use `setup_pydantic_ai()` to automatically instrument all Pydantic AI agents and direct API calls:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust.wrappers.pydantic_ai import setup_pydantic_ai
from pydantic_ai import Agent

# Initialize Braintrust tracing for Pydantic AI
setup_pydantic_ai(project_name="my-pydantic-project")

# Use agents as normal - they're automatically traced
agent = Agent("openai:gpt-4o", system_prompt="You are a helpful assistant.")
result = await agent.run("What is the capital of France?")
```

This automatically traces:

* **Agent runs**: `agent.run()`, `agent.run_sync()`, `agent.run_stream()`, and `agent.run_stream_sync()`
* **Direct API calls**: `model_request()`, `model_request_sync()`, and streaming variants
* **Model interactions**: Individual LLM calls made by agents
* **Tool calls**: Any tools defined on your agents

### Example with tools and streaming

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust.wrappers.pydantic_ai import setup_pydantic_ai
from pydantic_ai import Agent, ModelSettings

setup_pydantic_ai(project_name="my-pydantic-project")

agent = Agent(
    "openai:gpt-4o",
    model_settings=ModelSettings(max_tokens=500),
)

@agent.tool_plain
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    return f"22°C and sunny in {city}"

# Streaming is fully traced, including time-to-first-token
async with agent.run_stream("What's the weather in Paris?") as result:
    async for text in result.stream_text(delta=True):
        print(text, end="", flush=True)
```

### Using with existing spans

If you already have a Braintrust span context (e.g., from `@traced` or `start_span`), Pydantic AI traces will nest under it:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust import traced
from braintrust.wrappers.pydantic_ai import setup_pydantic_ai
from pydantic_ai import Agent

setup_pydantic_ai(project_name="my-pydantic-project")

agent = Agent("openai:gpt-4o")

@traced
async def my_workflow(question: str):
    # Agent traces appear as children of this span
    result = await agent.run(question)
    return result.output
```

## Alternative: OpenTelemetry integration

You can also use Braintrust's [OpenTelemetry support](/integrations/sdk-integrations/opentelemetry) with Pydantic AI's built-in instrumentation:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust.otel import BraintrustSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from pydantic_ai import Agent

provider = TracerProvider()
trace.set_tracer_provider(provider)
provider.add_span_processor(BraintrustSpanProcessor())

Agent.instrument_all()
```

This requires `pip install "braintrust[otel]"`. See the [OpenTelemetry guide](/integrations/sdk-integrations/opentelemetry) for more details.

## Resources

* [Pydantic AI documentation](https://ai.pydantic.dev)
* [Braintrust tracing guide](/guides/tracing)
