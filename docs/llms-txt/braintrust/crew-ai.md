# Source: https://braintrust.dev/docs/integrations/sdk-integrations/crew-ai.md

# CrewAI

[CrewAI](https://www.crewai.com/) is a framework for orchestrating role-playing AI agents. Braintrust traces CrewAI applications using OpenTelemetry to capture agent interactions, task executions, and crew orchestration.

## Setup

This integration uses Braintrust's [Python SDK OpenTelemetry configuration](/integrations/sdk-integrations/opentelemetry#python-sdk-configuration).

Install CrewAI with OpenTelemetry instrumentation:

<CodeGroup>
  ```bash Python theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  pip install "braintrust[otel]" crewai opentelemetry-instrumentation-openai opentelemetry-instrumentation-crewai python-dotenv
  ```
</CodeGroup>

Configure your environment variables:

```bash title=".env" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
BRAINTRUST_API_KEY=your-api-key
BRAINTRUST_PARENT=project_name:crewai-demo
OPENAI_API_KEY=your-openai-key
```

## Trace with CrewAI

When you create your crew, enable telemetry and export the data using OpenTelemetry:

```python title="crewai_braintrust.py" theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import os
from typing import Any, Dict

from braintrust.otel import BraintrustSpanProcessor
from crewai import Agent, Crew, Task
from crewai.llm import LLM
from opentelemetry import trace
from opentelemetry.instrumentation.crewai import CrewAIInstrumentor
from opentelemetry.instrumentation.openai import OpenAIInstrumentor
from opentelemetry.sdk.trace import TracerProvider

def setup_tracing() -> None:
    current_provider = trace.get_tracer_provider()
    if isinstance(current_provider, TracerProvider):
        provider = current_provider
    else:
        provider = TracerProvider()
        trace.set_tracer_provider(provider)

    provider.add_span_processor(BraintrustSpanProcessor())
    CrewAIInstrumentor().instrument(tracer_provider=provider)
    OpenAIInstrumentor().instrument(tracer_provider=provider)

def create_simple_crew() -> Crew:
    """Create a simple crew with a software developer agent."""
    llm = LLM(model="gpt-4o-mini")

    coder = Agent(
        role="Software developer",
        goal="Write clear, concise code on demand",
        backstory="An expert coder with a keen eye for software trends.",
        verbose=True,
        llm=llm,
    )

    task = Task(
        description="Define the HTML for making a simple website with heading- Hello World! Braintrust monitors your CrewAI agent!",
        expected_output="A clear and concise HTML code",
        agent=coder,
    )

    crew = Crew(
        agents=[coder],
        tasks=[task],
        verbose=True,
    )

    return crew

def run_crew() -> Dict[str, Any]:
    crew = create_simple_crew()
    result = crew.kickoff()

    return {
        "result": str(result),
        "agents_count": len(crew.agents),
        "tasks_count": len(crew.tasks),
    }

if __name__ == "__main__":
    setup_tracing()
    result = run_crew()
```

## Resources

* [CrewAI documentation](https://docs.crewai.com/)
* [Braintrust OpenTelemetry guide](/integrations/sdk-integrations/opentelemetry)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt