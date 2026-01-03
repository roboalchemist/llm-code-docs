# Source: https://braintrust.dev/docs/integrations/sdk-integrations/pydantic-ai.md

# Pydantic AI

[Pydantic AI](https://ai.pydantic.dev) is a Python agent framework built on Pydantic. Braintrust traces Pydantic AI applications using OpenTelemetry to capture agent interactions, tool calls, and performance metrics.

## Setup

Install the [Braintrust Python SDK with OpenTelemetry support](/integrations/sdk-integrations/opentelemetry#python-sdk-configuration) and the Braintrust Pydantic AI integration:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install "braintrust[otel]" pydantic-ai
  ```
</CodeGroup>

Configure your environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=your-api-key
BRAINTRUST_PARENT=project_name:my-otel-project

# If you are self-hosting Braintrust, set the URL of your hosted dataplane. You can omit this otherwise.
# BRAINTRUST_API_URL=https://api.braintrust.dev
```

## Trace with Pydantic AI

Configure OpenTelemetry with Braintrust's span processor and enable instrumentation on your agents:

```python title="pydantic-ai-braintrust.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust.otel import BraintrustSpanProcessor
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from pydantic_ai.agent import Agent

# Configure the global OTel tracer provider
provider = TracerProvider()
trace.set_tracer_provider(provider)

# Send spans to Braintrust
provider.add_span_processor(BraintrustSpanProcessor())

# Enable instrumentation on all agents
Agent.instrument_all()

agent = Agent(...)
```

This automatically sends all agent interactions, tool calls, and performance metrics to Braintrust.

## Resources

* [Pydantic AI documentation](https://ai.pydantic.dev)
* [Braintrust OpenTelemetry guide](/integrations/sdk-integrations/opentelemetry)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt