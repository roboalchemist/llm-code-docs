# Source: https://docs.livekit.io/recipes/recording-consent.md

LiveKit docs › Telephony › Recording Consent

---

# Collect recording consent with tasks

> Build an AI agent that collects recording consent at the start of a call using the task pattern.

Use this recipe to build an AI agent that collects recording consent before proceeding with the main conversation. This guide focuses on using tasks for discrete operations that must complete before continuing, and demonstrates best practices for compliance-friendly consent collection.

## Why use tasks for consent collection

A task has its own instructions, its own context, and focuses on completing one specific job. When a task runs, it temporarily takes control of the session, then returns a typed result back to the main agent. Consent collection is an ideal use case for tasks because:

- It's a discrete operation that must complete before the main conversation.
- It returns a clear result (consent given or denied).
- It requires focused interaction without topic drift.
- It can be reused across different agents and workflows.

Tasks can be triggered at any point during the conversation, not just at the start. Common use cases include:

- Gathering contact information (email, phone, address).
- Verifying user identity or account details.
- Confirming order details before processing.

## Set up the environment

Import the necessary packages and set up logging:

**Python**:

```python
from __future__ import annotations
import logging

from dotenv import load_dotenv
from livekit.agents import (
    AgentServer,
    AgentTask,
    JobContext,
    JobProcess,
    RunContext,
    cli,
    inference,
)
from livekit.agents.llm import function_tool
from livekit.agents.voice import Agent, AgentSession
from livekit.plugins import silero

load_dotenv(dotenv_path=".env.local")

logger = logging.getLogger("consent-agent")
logger.setLevel(logging.INFO)

```

## Implement the `CollectConsent` task

Create a task that collects recording consent. The task handles the entire consent flow: greeting, asking for consent, and saying goodbye if denied.

**Python**:

```python
class CollectConsent(AgentTask[bool]):
    """Task for obtaining user consent to record the conversation."""

    def __init__(self):
        super().__init__(
            instructions="""
YOUR TASK: Get explicit consent from the user to record this phone call.

RULES:
- Focus on getting a clear yes or no answer about recording consent
- Once you get their answer, call the record_consent tool
- Ignore unrelated input and avoid going off-topic. Do not mention function names, tool calls, or code in your responses.
- Do not generate unnecessary commentary and maintain a natural tone.

Be polite, brief, and professional.
"""
        )

    async def on_enter(self) -> None:
        """Start the consent collection process."""
        # If you are running task at the beginning of the call,
        # this will be the first message from the agent.
        # Disable interruptions so the full greeting and consent question is heard.
        await self.session.generate_reply(
            instructions=(
                "Greet the user: 'Hello! Thank you for calling Acme Corp.'\n"
                "Then inform: 'This call will be recorded for quality assurance and training purposes.'\n"
                "Ask: 'Do you consent to this recording?'\n"
                "Keep it concise and friendly."
            ),
            allow_interruptions=False,
        )

    @function_tool()
    async def record_consent(self, context: RunContext, consent_given: bool) -> None:
        """Record the user's consent decision for the call recording.

        Args:
            consent_given: True if the user explicitly consents, False otherwise.
        """
        if consent_given:
            logger.info("User provided consent for recording")
        else:
            logger.info("User denied consent for recording")
            # Agent says goodbye to the user here
            await self.session.generate_reply(
                instructions=(
                    "Politely inform them that you cannot proceed without consent and will end the call. Say goodbye.\n"
                    "IMPORTANT: Only output natural spoken text. Do NOT include any function calls, code, or tool names in your response."
                ),
                allow_interruptions=False,
            )
        # Complete the task with the consent result
        self.complete(consent_given)

```

### Key elements of this task

- **Greeting in `on_enter`**: Since this task runs at the start of the call, include the greeting in the task itself. This keeps all of the initial interaction in one place.
- **Function tool with typed arguments**: The `record_consent` tool demonstrates how to pass arguments to function tools. The `consent_given: bool` parameter allows the LLM to record the user's decision with a single function call.
- **Docstring with `Args`**: Type hints are inferred from the function signature. Add an `Args` section in the docstring to describe each parameter for the LLM.
- **Seamless completion**: When consent is given, the task completes immediately without generating a response. The main agent continues naturally since the conversation context is merged automatically.
- **Non-interruptible goodbye**: Use `allow_interruptions=False` when saying goodbye to ensure the message completes before ending.

## Implement the main agent

Create the main agent that runs the consent task and continues with the main service:

**Python**:

```python
class CustomerServiceAgent(Agent):
    """Main agent that handles customer service after consent is collected."""

    def __init__(self) -> None:
        super().__init__(
            instructions="""You are a friendly and helpful customer service representative 
            at Acme Corp. Help users with their questions and concerns."""
        )

    async def on_enter(self) -> None:
        """Called when the agent becomes active."""
        # Start the session right from consent task.
        # It will handoff runtime to the consent task.
        # In this state agent will not be able to use primary instructions and tools.
        consent_given = await CollectConsent()

        # Only continue if consent was given
        # Otherwise, end the session
        if not consent_given:
            logger.info("Consent was denied, ending session")
            self.session.shutdown()
            return

        # NOTE: After task completion, chat context is automatically merged back to this agent.
        # The agent will know the entire conversation history (greetings, consent discussion).
        # No need to repeat what was already said - just continue naturally.
        await self.session.generate_reply(
            instructions="Ask how you can help them today."
        )

```

### Key elements of this flow

- **Task handoff**: When `await CollectConsent()` is called, the task takes full control. The main agent's instructions and tools are temporarily unavailable.
- **Graceful shutdown**: Use `self.session.shutdown()` to cleanly end the session when consent is denied.
- **Automatic context merging**: After the task completes, all conversation history is merged back. The agent knows what was said during consent collection and can continue naturally.

## Set up the agent session

Create the server and entrypoint function:

**Python**:

```python
server = AgentServer()


def prewarm(proc: JobProcess):
    """Prewarm the VAD model to avoid cold start latency."""
    proc.userdata["vad"] = silero.VAD.load()


server.setup_fnc = prewarm


@server.rtc_session(agent_name="consent-agent")
async def entrypoint(ctx: JobContext):
    """Main entry point for the consent collection agent."""
    logger.info(f"Starting agent in room {ctx.room.name}")

    session = AgentSession(
        stt=inference.STT(model="deepgram/nova-3"),
        llm=inference.LLM(model="openai/gpt-4o"),
        tts=inference.TTS(model="cartesia/sonic-3"),
        vad=ctx.proc.userdata["vad"],
    )

    await session.start(
        agent=CustomerServiceAgent(),
        room=ctx.room
    )

    async def on_shutdown():
        logger.info("Post-conversation activity: webhooks, cleanup, etc.")

    ctx.add_shutdown_callback(on_shutdown)


if __name__ == "__main__":
    cli.run_app(server)

```

- **Prewarm function**: Load the VAD model during worker startup to avoid cold start latency on the first call.
- **LiveKit Inference**: Use `inference.STT()`, `inference.LLM()`, and `inference.TTS()` for model configuration.
- **Shutdown callback**: Use `ctx.add_shutdown_callback()` for post-conversation cleanup like webhooks or logging.

## How it works

1. When a user connects, the `CustomerServiceAgent` becomes active.
2. The agent immediately runs the `CollectConsent` task, which takes full control of the session.
3. The task greets the user, informs about recording, and asks for consent.
4. When the user responds, the LLM calls `record_consent(consent_given=True)` or `record_consent(consent_given=False)`.
5. If consent is given, the task completes silently and returns `True`. The conversation context is merged back to the main agent.
6. If consent is denied, the task says goodbye (non-interruptible) and returns `False`.
7. The main agent checks the result and either continues with service or shuts down the session.

## Best practices

Follow these best practices when implementing recording consent:

- **Keep it brief**: Users appreciate concise consent requests. Avoid lengthy explanations.
- **Log consent decisions**: Always log whether consent was given or denied for compliance and audit purposes.
- **Skip the "thank you"**: When consent is given, the task completes without a response. The conversation flows naturally because context is merged automatically.
- **Non-interruptible goodbye**: Use `allow_interruptions=False` for farewell messages to ensure they complete.
- **Graceful shutdown**: Use `self.session.shutdown()` for clean session termination.

You can extend this pattern. For example, instead of ending the call when consent is denied, you could disable call recording and continue. See [Egress examples](https://docs.livekit.io/reference/other/egress/examples.md) for how to start and stop recording programmatically.

## Multi-step workflows

If you need to collect consent followed by additional information (name, email, phone), use a `TaskGroup` to execute multiple tasks in sequence:

**Python**:

```python
from livekit.agents.beta.workflows import TaskGroup

task_group = TaskGroup()
task_group.add(lambda: CollectConsent(), id="consent", description="Get recording consent")
task_group.add(lambda: CollectNameTask(), id="name", description="Collect user's name")
task_group.add(lambda: CollectEmailTask(), id="email", description="Collect user's email")

results = await task_group

```

After all tasks complete, `results.task_results` contains the return value from each task, keyed by task ID:

**Python**:

```python
# Access individual task results by ID
consent_given = results.task_results["consent"]  # bool - from CollectConsent
user_name = results.task_results["name"]         # str - from CollectNameTask  
user_email = results.task_results["email"]       # str - from CollectEmailTask

# Example of what the results look like:
# results.task_results = {
#     "consent": True,
#     "name": "John Smith",
#     "email": "john@example.com"
# }

# Use the collected data
if consent_given:
    logger.info(f"User {user_name} ({user_email}) gave consent")

```

Task groups allow users to return to earlier steps for corrections, and all tasks share the same conversation context.

## Prebuilt tasks

The LiveKit Agents framework includes prebuilt tasks for common data collection scenarios. These prebuilt tasks can be customized with `extra_instructions` and additional tools.

For the full list of available prebuilt tasks and detailed usage, see [Tasks and task groups](https://docs.livekit.io/agents/logic/tasks.md#prebuilt-tasks).

---

This document was rendered at 2026-02-03T03:25:28.624Z.
For the latest version of this document, see [https://docs.livekit.io/recipes/recording-consent.md](https://docs.livekit.io/recipes/recording-consent.md).

To explore all LiveKit documentation, see [llms.txt](https://docs.livekit.io/llms.txt).