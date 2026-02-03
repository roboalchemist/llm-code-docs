# Source: https://braintrust.dev/docs/integrations/agent-frameworks/autogen.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Autogen

[AutoGen](https://microsoft.github.io/autogen/stable/) is a Microsoft framework for building multi-agent conversational systems. Braintrust traces AutoGen applications using OpenTelemetry to capture agent conversations, task planning, and tool executions.

## Setup

This integration uses Braintrust's [Python SDK OpenTelemetry configuration](/integrations/sdk-integrations/opentelemetry#python-sdk-configuration).

Install AutoGen with OpenTelemetry instrumentation:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install "braintrust[otel]" autogen-agentchat opentelemetry-instrumentation-openai python-dotenv
  ```
</CodeGroup>

Configure your environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=your-api-key
BRAINTRUST_PARENT=project_name:autogen-demo
OPENAI_API_KEY=your-openai-key
```

## Trace with AutoGen

Configure OpenTelemetry with Braintrust's span processor and enable instrumentation:

```python title="autogen_braintrust.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import asyncio
import os
from typing import Optional

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.ui import Console
from autogen_core import SingleThreadedAgentRuntime
from autogen_ext.models.openai import OpenAIChatCompletionClient
from braintrust.otel import BraintrustSpanProcessor
from dotenv import load_dotenv
from opentelemetry import trace
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider

def setup_tracing() -> None:
    provider = TracerProvider()
    provider.add_span_processor(BraintrustSpanProcessor(filter_ai_spans=True))
    trace.set_tracer_provider(provider)
    OpenAIInstrumentor().instrument()

def percentage_change_tool(start: float, end: float) -> float:
    if start == 0:
        return float("inf")
    return ((end - start) / start) * 100

async def main(task: Optional[str] = None) -> None:
    load_dotenv()
    setup_tracing()

    model_client = OpenAIChatCompletionClient(model="gpt-4o")

    tracer = trace.get_tracer("autogen-demo-bot")
    with tracer.start_as_current_span("run_team"):
        planning_agent = AssistantAgent(
            "PlanningAgent",
            description="Plans tasks and delegates.",
            model_client=model_client,
            system_message=(
                "You are a planning agent. You only plan and delegate tasks; do not execute them.\n"
                "When assigning tasks, use this format: 1. <agent> : <task>\n"
                'After all tasks are complete, summarize the findings and end with "TERMINATE".'
            ),
        )

        data_analyst_agent = AssistantAgent(
            "DataAnalystAgent",
            description="Performs calculations.",
            model_client=model_client,
            tools=[percentage_change_tool],
            system_message=("You are a data analyst. Use the tools provided to compute numeric results."),
        )

        termination = TextMentionTermination("TERMINATE") | MaxMessageTermination(max_messages=25)

        if not task:
            task = "You started with 100 apples, now you have 120 apples. what is the percentage change?"

        runtime = SingleThreadedAgentRuntime(tracer_provider=trace.get_tracer_provider())
        runtime.start()

        selector_prompt = (
            "Select an agent to perform task.\n\n{roles}\n\nCurrent conversation context:\n{history}\n\n"
            "Read the above conversation, then select an agent from {participants} to perform the next task.\n"
            "Make sure the planner agent has assigned tasks before other agents start working.\nOnly select one agent."
        )

        team = SelectorGroupChat(
            [planning_agent, data_analyst_agent],
            model_client=model_client,
            termination_condition=termination,
            selector_prompt=selector_prompt,
            allow_repeated_speaker=True,
            runtime=runtime,
        )

        await Console(team.run_stream(task=task))

        await runtime.stop()

    await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Resources

* [AutoGen documentation](https://microsoft.github.io/autogen/stable/)
* [Braintrust OpenTelemetry guide](/integrations/sdk-integrations/opentelemetry)
