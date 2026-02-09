# Source: https://braintrust.dev/docs/integrations/ai-providers/google.md

# Source: https://braintrust.dev/docs/integrations/agent-frameworks/google.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Google ADK (Agent Development Kit)

[Google ADK (Agent Development Kit)](https://github.com/google/adk-python) is Google's framework for building AI agents powered by Gemini models. Braintrust automatically traces ADK agent executions, capturing agent invocations, tool calls, parallel flows, and multi-step reasoning.

## Setup

Install the Braintrust ADK integration:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install braintrust-adk
  ```
</CodeGroup>

## Trace with Google ADK

Call `setup_adk()` to enable automatic tracing for all ADK agent interactions:

```python title="trace-adk-braintrust.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import asyncio

from braintrust_adk import setup_adk
from google.adk import Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.genai import types

setup_adk(
    project_name="my-adk-project",
)

# Create your ADK agent as normal
def get_weather(city: str) -> dict:
    """Get weather for a city."""
    return {"temperature": 72, "condition": "sunny", "city": city}

def get_current_time() -> str:
    """Get the current time."""
    from datetime import datetime

    return datetime.now().strftime("%I:%M %p")

async def main():
    # Create the agent
    agent = LlmAgent(
        name="weather_time_assistant",
        tools=[get_weather, get_current_time],
        model="gemini-2.5-flash",
        instruction="You are a helpful assistant that can check weather and time.",
    )
    # Create a session service and a runner
    session_service = InMemorySessionService()
    runner = Runner(app_name="weather_app", agent=agent, session_service=session_service)
    # Create a fake session
    user_id = "user123"
    session_id = "session123"
    await session_service.create_session(app_name="weather_app", user_id=user_id, session_id=session_id)
    # Create the message to send
    new_message = types.Content(
        parts=[types.Part(text="What's the weather like in New York?")],
        role="user",
    )
    # Run the agent with the query
    events = runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=new_message,
    )
    # Process the events and print the agent's response
    for event in events:
        print(event)

if __name__ == "__main__":
    asyncio.run(main())
```

<img src="https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/adk.png?fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=7e888caf295dd2fc1e4dd263c63a29b6" alt="Example of automatic Google ADK tracing and logs sent to Braintrust" data-og-width="1571" width="1571" data-og-height="1293" height="1293" data-path="images/integrations/adk.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/adk.png?w=280&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=6368cc82026761691f0f0f1b0b1de0d4 280w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/adk.png?w=560&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=5f524445f3d7af3ff8b0e152655658bb 560w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/adk.png?w=840&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=1e3bac859a6a74b39b1bbeba631790d6 840w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/adk.png?w=1100&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=5cf565c2a90256ac3017ced3a12074ff 1100w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/adk.png?w=1650&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=869ac44c7a4d184bb7fe5ca3533e46a5 1650w, https://mintcdn.com/braintrust/p0aIuwUs6uEDT4tr/images/integrations/adk.png?w=2500&fit=max&auto=format&n=p0aIuwUs6uEDT4tr&q=85&s=8fa295b9495dad1e1487bd895eb6dcc2 2500w" />

## Resources

* [Google ADK documentation](https://github.com/google/adk-python)
* [Google Gemini models](https://ai.google.dev/)
