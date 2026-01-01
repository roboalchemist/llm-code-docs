# Source: https://braintrust.dev/docs/integrations/sdk-integrations/livekit-agents.md

# LiveKit Agents

[LiveKit Agents](https://livekit.io/) is a framework for building real-time voice and video AI applications. Braintrust traces LiveKit Agents applications using OpenTelemetry to capture voice interactions, agent sessions, and realtime model usage.

## Setup

This integration uses Braintrust's [Python SDK OpenTelemetry configuration](/integrations/sdk-integrations/opentelemetry#python-sdk-configuration).

Install LiveKit Agents with OpenTelemetry instrumentation:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install "braintrust[otel]" livekit-agents livekit-plugins-openai opentelemetry-sdk
  ```
</CodeGroup>

Configure your environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=your-api-key
BRAINTRUST_PARENT=project_name:livekit-demo
OPENAI_API_KEY=your-openai-api-key
```

## Trace with LiveKit Agents

Configure Braintrust's span processor and set it as LiveKit's tracer provider:

```python title="livekit_agent.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from braintrust.otel import BraintrustSpanProcessor
from livekit import agents
from livekit.agents import Agent, AgentSession, RoomInputOptions
from livekit.agents.telemetry import set_tracer_provider
from livekit.plugins import noise_cancellation, openai
from opentelemetry.sdk.trace import TracerProvider

def setup_braintrust_telemetry():
    """Setup Braintrust OTEL telemetry for agent monitoring"""
    trace_provider = TracerProvider()
    trace_provider.add_span_processor(BraintrustSpanProcessor())
    set_tracer_provider(trace_provider)

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a helpful voice AI assistant.")

async def entrypoint(ctx: agents.JobContext):
    # Setup telemetry
    setup_braintrust_telemetry()

    # Create agent session with OpenAI realtime model
    session = AgentSession(llm=openai.realtime.RealtimeModel(voice="coral"))

    # Start session with assistant agent
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

# Run script locally with `python livekit_agent.py console`
if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
```

## Resources

* [LiveKit Agents documentation](https://docs.livekit.io/agents/)
* [Braintrust OpenTelemetry guide](/integrations/sdk-integrations/opentelemetry)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt