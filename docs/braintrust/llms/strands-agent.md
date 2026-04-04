# Source: https://braintrust.dev/docs/integrations/agent-frameworks/strands-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Strands Agent SDK

[Strands Agent SDK](https://strandsagents.com/) is a Python framework for building AI agents. Braintrust traces Strands agents using OpenTelemetry to capture agent invocations, tool calls, and multi-step interactions.

## Setup

This integration uses Braintrust's [Python SDK OpenTelemetry configuration](/integrations/sdk-integrations/opentelemetry#python-sdk-configuration).

Install the Strands Agent SDK with OpenTelemetry instrumentation:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install "braintrust[otel]" strands-agents-tools strands-agents[openai]
  ```
</CodeGroup>

Configure your environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY="<your Braintrust API key>"
BRAINTRUST_PARENT="project_name:<your Braintrust Project Name>"
OPENAI_API_KEY="<your OpenAI API key>"

# If you are self-hosting Braintrust, set the URL of your hosted dataplane. You can omit this otherwise.
# BRAINTRUST_API_URL=https://api.braintrust.dev
```

## Trace with Strands Agent SDK

Configure OpenTelemetry with Braintrust's span processor and Strands telemetry.

This example adapts the [Weather Forecaster Strands example](https://strandsagents.com/latest/documentation/docs/examples/python/weather_forecaster/):

```python title="trace-strands-agent.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Load packages to form the Strands agent using an OpenAI model
# Load packages to execute the agent
import asyncio
import os

from braintrust.otel import BraintrustSpanProcessor
from dotenv import load_dotenv

# Load OpenTelemetry assets and Braintrust span processor added to the project from the braintrust[otel] library
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from strands import Agent
from strands.models.openai import OpenAIModel
from strands.telemetry import StrandsTelemetry
from strands_tools import http_request

load_dotenv()

# Define a weather-focused system prompt
WEATHER_SYSTEM_PROMPT = """You are a weather assistant with HTTP capabilities. You can:

1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data
3. Provide weather information for locations in the United States

When retrieving weather information:
1. First get the coordinates or grid information using https://api.weather.gov/points/{latitude},{longitude} or https://api.weather.gov/points/{zipcode}
2. Then use the returned forecast URL to get the actual forecast

When displaying responses:
- Format weather data in a human-readable way
- Highlight important information like temperature, precipitation, and alerts
- Handle errors appropriately
- Convert technical terms to user-friendly language

Always explain the weather conditions clearly and provide context for the forecast.
"""

# Configure the global OTel tracer provider
provider = TracerProvider()
trace.set_tracer_provider(provider)

# Add the Braintrust span processor to the tracer provider and configure Strands telemetry
provider.add_span_processor(BraintrustSpanProcessor())
telemetry = StrandsTelemetry(provider)

# Configure the OpenAI model to be used by the Strands agent
model = OpenAIModel(
    client_args={
        "api_key": os.getenv("OPENAI_API_KEY"),
    },
    # **model_config
    model_id="gpt-4o-mini",
)

# Create an agent with HTTP tool call capabilities and the OpenAI model
weather_agent = Agent(
    system_prompt=WEATHER_SYSTEM_PROMPT,
    tools=[http_request],  # Explicitly enable http_request tool
    model=model,
)

# Create an async function to run the agent
async def main():
    result = await weather_agent.invoke_async(prompt="What is the weather in San Francisco?")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

<img src="https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/strands-agent.png?fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=d4804830976b112d73cf36ca30c6eb4f" alt="Example of automatic Strands agent tracing and logs sent to Braintrust" data-og-width="2540" width="2540" data-og-height="1580" height="1580" data-path="images/integrations/strands-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/strands-agent.png?w=280&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=6fdf3a87a3ccf285ec47e758a63bdfbf 280w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/strands-agent.png?w=560&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=ee40324da5aca7f004a8b971e2fa0587 560w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/strands-agent.png?w=840&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=3a26f8de51fecbd8f27c413f3dee6d47 840w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/strands-agent.png?w=1100&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=32c653bb8f3d0b8f5cf8cd9e0bbe2b94 1100w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/strands-agent.png?w=1650&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=247afab77615cbd68bfb3a4404d96202 1650w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/integrations/strands-agent.png?w=2500&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=4285277025ac439c1c8cfee50ea3a295 2500w" />

## Resources

* [Strands Agent SDK documentation](https://strandsagents.com/)
* [Braintrust OpenTelemetry guide](/integrations/sdk-integrations/opentelemetry)
