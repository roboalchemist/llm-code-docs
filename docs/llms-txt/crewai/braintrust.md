# Source: https://docs.crewai.com/en/observability/braintrust.md

# Braintrust

> Braintrust integration for CrewAI with OpenTelemetry tracing and evaluation

# Braintrust Integration

This guide demonstrates how to integrate **Braintrust** with **CrewAI** using OpenTelemetry for comprehensive tracing and evaluation. By the end of this guide, you will be able to trace your CrewAI agents, monitor their performance, and evaluate their outputs using Braintrust's powerful observability platform.

> **What is Braintrust?** [Braintrust](https://www.braintrust.dev) is an AI evaluation and observability platform that provides comprehensive tracing, evaluation, and monitoring for AI applications with built-in experiment tracking and performance analytics.

## Get Started

We'll walk through a simple example of using CrewAI and integrating it with Braintrust via OpenTelemetry for comprehensive observability and evaluation.

### Step 1: Install Dependencies

```bash  theme={null}
uv add braintrust[otel] crewai crewai-tools opentelemetry-instrumentation-openai opentelemetry-instrumentation-crewai python-dotenv
```

### Step 2: Set Up Environment Variables

Setup Braintrust API keys and configure OpenTelemetry to send traces to Braintrust. You'll need a Braintrust API key and your OpenAI API key.

```python  theme={null}
import os
from getpass import getpass

# Get your Braintrust credentials
BRAINTRUST_API_KEY = getpass("🔑 Enter your Braintrust API Key: ")

# Get API keys for services
OPENAI_API_KEY = getpass("🔑 Enter your OpenAI API key: ")

# Set environment variables
os.environ["BRAINTRUST_API_KEY"] = BRAINTRUST_API_KEY
os.environ["BRAINTRUST_PARENT"] = "project_name:crewai-demo"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
```

### Step 3: Initialize OpenTelemetry with Braintrust

Initialize the Braintrust OpenTelemetry instrumentation to start capturing traces and send them to Braintrust.

```python  theme={null}
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
    """Setup OpenTelemetry tracing with Braintrust."""
    current_provider = trace.get_tracer_provider()
    if isinstance(current_provider, TracerProvider):
        provider = current_provider
    else:
        provider = TracerProvider()
        trace.set_tracer_provider(provider)

    provider.add_span_processor(BraintrustSpanProcessor())
    CrewAIInstrumentor().instrument(tracer_provider=provider)
    OpenAIInstrumentor().instrument(tracer_provider=provider)


setup_tracing()
```

### Step 4: Create a CrewAI Application

We'll create a CrewAI application where two agents collaborate to research and write a blog post about AI advancements, with comprehensive tracing enabled.

```python  theme={null}
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool

def create_crew() -> Crew:
    """Create a crew with multiple agents for comprehensive tracing."""
    llm = LLM(model="gpt-4o-mini")
    search_tool = SerperDevTool()

    # Define agents with specific roles
    researcher = Agent(
        role="Senior Research Analyst",
        goal="Uncover cutting-edge developments in AI and data science",
        backstory="""You work at a leading tech think tank.
        Your expertise lies in identifying emerging trends.
        You have a knack for dissecting complex data and presenting actionable insights.""",
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[search_tool],
    )

    writer = Agent(
        role="Tech Content Strategist",
        goal="Craft compelling content on tech advancements",
        backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
        You transform complex concepts into compelling narratives.""",
        verbose=True,
        allow_delegation=True,
        llm=llm,
    )

    # Create tasks for your agents
    research_task = Task(
        description="""Conduct a comprehensive analysis of the latest advancements in {topic}.
        Identify key trends, breakthrough technologies, and potential industry impacts.""",
        expected_output="Full analysis report in bullet points",
        agent=researcher,
    )

    writing_task = Task(
        description="""Using the insights provided, develop an engaging blog
        post that highlights the most significant {topic} advancements.
        Your post should be informative yet accessible, catering to a tech-savvy audience.
        Make it sound cool, avoid complex words so it doesn't sound like AI.""",
        expected_output="Full blog post of at least 4 paragraphs",
        agent=writer,
        context=[research_task],
    )

    # Instantiate your crew with a sequential process
    crew = Crew(
        agents=[researcher, writer], 
        tasks=[research_task, writing_task], 
        verbose=True, 
        process=Process.sequential
    )

    return crew

def run_crew():
    """Run the crew and return results."""
    crew = create_crew()
    result = crew.kickoff(inputs={"topic": "AI developments"})
    return result

# Run your crew
if __name__ == "__main__":
    # Instrumentation is already initialized above in this module
    result = run_crew()
    print(result)
```

### Step 5: View Traces in Braintrust

After running your crew, you can view comprehensive traces in Braintrust through different perspectives:

<Tabs>
  <Tab title="Trace">
    <Frame>
      <img src="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=311f727eeadf1c39380c08e992278dd0" alt="Braintrust Trace View" data-og-width="1446" width="1446" data-og-height="1117" height="1117" data-path="images/braintrust-trace-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=280&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=897e860f9b8d3493999f62a9a19c8fb8 280w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=560&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=a5f185d667eac4272b983878a6851206 560w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=840&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=a633e5f94ed2b81419c17894d803342a 840w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=1100&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=941454a8d9339cb1873525af08a3278c 1100w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=1650&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=9617559998fb4906d5c81d7a77803077 1650w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-trace-view.png?w=2500&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=413a16f22e69897e63d899ac77601ab7 2500w" />
    </Frame>
  </Tab>

  <Tab title="Timeline">
    <Frame>
      <img src="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=03090206aecd3a7b2f21a24af2514b08" alt="Braintrust Timeline View" data-og-width="1449" width="1449" data-og-height="950" height="950" data-path="images/braintrust-timeline-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=280&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=0795dce3045c51b3f954282196e21189 280w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=560&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=73c0b619f3b04b19b0efb255157a4ef5 560w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=840&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=e28b62d2fb6da5cc43c770796a1cf3ca 840w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=1100&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=7ccb443569f6a8e9bd6ae267fd0d83b3 1100w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=1650&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=94b8fecd6f45755faf0d6ced848a7da1 1650w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-timeline-view.png?w=2500&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=0fb8a89b44b1c5bcc16886d3bd61f8f0 2500w" />
    </Frame>
  </Tab>

  <Tab title="Thread">
    <Frame>
      <img src="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=1bc0a6842a5dd9e6d7c2dd742417e79b" alt="Braintrust Thread View" data-og-width="1452" width="1452" data-og-height="989" height="989" data-path="images/braintrust-thread-view.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=280&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=1a7d95a7eeee928ea1ee0e84d4f172f7 280w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=560&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=8414267a22466d638441e87588c0c3b5 560w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=840&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=7695d8fe70972f93f69201a7f9e4f19f 840w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=1100&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=2d5051293c140b63ae391cd0879aa313 1100w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=1650&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=69bf97bbeb0e0b1a323cc535666d0517 1650w, https://mintcdn.com/crewai/sTI-JqU6hicMPzD1/images/braintrust-thread-view.png?w=2500&fit=max&auto=format&n=sTI-JqU6hicMPzD1&q=85&s=e0b50e3d14fad48ca9a48795c3d36bc9 2500w" />
    </Frame>
  </Tab>
</Tabs>

### Step 6: Evaluate via SDK (Experiments)

You can also run evaluations using Braintrust's Eval SDK. This is useful for comparing versions or scoring outputs offline. Below is a Python example using the `Eval` class with the crew we created above:

```python  theme={null}
# eval_crew.py
from braintrust import Eval
from autoevals import Levenshtein

def evaluate_crew_task(input_data):
    """Task function that wraps our crew for evaluation."""
    crew = create_crew()
    result = crew.kickoff(inputs={"topic": input_data["topic"]})
    return str(result)

Eval(
    "AI Research Crew",  # Project name
    {
        "data": lambda: [
            {"topic": "artificial intelligence trends 2024"},
            {"topic": "machine learning breakthroughs"},
            {"topic": "AI ethics and governance"},
        ],
        "task": evaluate_crew_task,
        "scores": [Levenshtein],
    },
)
```

Setup your API key and run:

```bash  theme={null}
export BRAINTRUST_API_KEY="YOUR_API_KEY"
braintrust eval eval_crew.py
```

See the [Braintrust Eval SDK guide](https://www.braintrust.dev/docs/start/eval-sdk) for more details.

### Key Features of Braintrust Integration

* **Comprehensive Tracing**: Track all agent interactions, tool usage, and LLM calls
* **Performance Monitoring**: Monitor execution times, token usage, and success rates
* **Experiment Tracking**: Compare different crew configurations and models
* **Automated Evaluation**: Set up custom evaluation metrics for crew outputs
* **Error Tracking**: Monitor and debug failures across your crew executions
* **Cost Analysis**: Track token usage and associated costs

### Version Compatibility Information

* Python 3.8+
* CrewAI >= 0.86.0
* Braintrust >= 0.1.0
* OpenTelemetry SDK >= 1.31.0

### References

* [Braintrust Documentation](https://www.braintrust.dev/docs) - Overview of the Braintrust platform
* [Braintrust CrewAI Integration](https://www.braintrust.dev/docs/integrations/crew-ai) - Official CrewAI integration guide
* [Braintrust Eval SDK](https://www.braintrust.dev/docs/start/eval-sdk) - Run experiments via the SDK
* [CrewAI Documentation](https://docs.crewai.com/) - Overview of the CrewAI framework
* [OpenTelemetry Docs](https://opentelemetry.io/docs/) - OpenTelemetry guide
* [Braintrust GitHub](https://github.com/braintrustdata/braintrust) - Source code for Braintrust SDK
