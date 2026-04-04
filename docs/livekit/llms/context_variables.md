# Source: https://docs.livekit.io/recipes/context_variables.md

LiveKit docs › Advanced LLM › Context Variables

---

# Context Variables

> Shows how to give an agent context about the user using simple variables.

This example shows how to personalize an agent's instructions with user-specific variables. The example injects name, age, and city into the prompt before the session starts.

## Prerequisites

- Add a `.env` in this directory with your LiveKit credentials:```
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret

```
- Install dependencies:```bash
pip install "livekit-agents[silero]" python-dotenv

```

## Load environment, logging, and define an AgentServer

Start by loading your environment variables and setting up logging. Define an `AgentServer` which wraps your application and handles the worker lifecycle.

```python
import logging
from dotenv import load_dotenv
from livekit.agents import JobContext, JobProcess, Agent, AgentSession, AgentServer, cli, inference
from livekit.plugins import silero

load_dotenv()

logger = logging.getLogger("context-variables")
logger.setLevel(logging.INFO)

server = AgentServer()

```

## Prewarm VAD for faster connections

Preload the VAD model once per process using the `setup_fnc`.

```python
def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()

server.setup_fnc = prewarm

```

## Create an agent that accepts context

Build a lightweight agent that formats its instructions with values from a dictionary. If context is passed, the prompt is customized before the agent starts.

```python
class ContextAgent(Agent):
    def __init__(self, context_vars=None) -> None:
        instructions = """
            You are a helpful agent. The user's name is {name}.
            They are {age} years old and live in {city}.
        """

        if context_vars:
            instructions = instructions.format(**context_vars)

        super().__init__(instructions=instructions)

    async def on_enter(self):
        self.session.generate_reply()

```

## Define the RTC session entrypoint

Create the context variables dictionary with user-specific data, then pass it to the agent when starting the session.

```python
@server.rtc_session()
async def entrypoint(ctx: JobContext):
    ctx.log_context_fields = {"room": ctx.room.name}

    context_variables = {
        "name": "Shayne",
        "age": 35,
        "city": "Toronto"
    }

    session = AgentSession(
        stt=inference.STT(model="deepgram/nova-3-general"),
        llm=inference.LLM(model="openai/gpt-4.1-mini"),
        tts=inference.TTS(model="cartesia/sonic-3", voice="9626c31c-bec5-4cca-baa8-f8ba9e84c8bc"),
        vad=ctx.proc.userdata["vad"],
        preemptive_generation=True,
    )

    await session.start(agent=ContextAgent(context_vars=context_variables), room=ctx.room)
    await ctx.connect()

```

## Run the server

```python
if __name__ == "__main__":
    cli.run_app(server)

```

## Run it

```bash
python context_variables.py console

```

## How it works

1. Load environment variables and set up logging.
2. Format the agent's instructions with user-specific context variables.
3. Generate an immediate greeting using the personalized prompt when the agent enters.

## Full example

```python
import logging
from dotenv import load_dotenv
from livekit.agents import JobContext, JobProcess, Agent, AgentSession, AgentServer, cli, inference
from livekit.plugins import silero

load_dotenv()

logger = logging.getLogger("context-variables")
logger.setLevel(logging.INFO)


class ContextAgent(Agent):
    def __init__(self, context_vars=None) -> None:
        instructions = """
            You are a helpful agent. The user's name is {name}.
            They are {age} years old and live in {city}.
        """

        if context_vars:
            instructions = instructions.format(**context_vars)

        super().__init__(instructions=instructions)

    async def on_enter(self):
        self.session.generate_reply()


server = AgentServer()


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


server.setup_fnc = prewarm


@server.rtc_session()
async def entrypoint(ctx: JobContext):
    ctx.log_context_fields = {"room": ctx.room.name}

    context_variables = {
        "name": "Shayne",
        "age": 35,
        "city": "Toronto"
    }

    session = AgentSession(
        stt=inference.STT(model="deepgram/nova-3-general"),
        llm=inference.LLM(model="openai/gpt-4.1-mini"),
        tts=inference.TTS(model="cartesia/sonic-3", voice="9626c31c-bec5-4cca-baa8-f8ba9e84c8bc"),
        vad=ctx.proc.userdata["vad"],
        preemptive_generation=True,
    )

    await session.start(agent=ContextAgent(context_vars=context_variables), room=ctx.room)
    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(server)

```

---

This document was rendered at 2026-02-03T03:25:29.784Z.
For the latest version of this document, see [https://docs.livekit.io/recipes/context_variables.md](https://docs.livekit.io/recipes/context_variables.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).