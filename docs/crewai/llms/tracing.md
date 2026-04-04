# Source: https://docs.crewai.com/en/observability/tracing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CrewAI Tracing

> Built-in tracing for CrewAI Crews and Flows with the CrewAI AMP platform

# CrewAI Built-in Tracing

CrewAI provides built-in tracing capabilities that allow you to monitor and debug your Crews and Flows in real-time. This guide demonstrates how to enable tracing for both **Crews** and **Flows** using CrewAI's integrated observability platform.

> **What is CrewAI Tracing?** CrewAI's built-in tracing provides comprehensive observability for your AI agents, including agent decisions, task execution timelines, tool usage, and LLM calls - all accessible through the [CrewAI AMP platform](https://app.crewai.com).

<img src="https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=b7e95a8f56ed3c459699acf641b4ae5a" alt="CrewAI Tracing Interface" data-og-width="3680" width="3680" data-og-height="2382" height="2382" data-path="images/crewai-tracing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=280&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=432b91fbee9d71f0c152a097c1b87773 280w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=560&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=62b6417d4f5289617124df196c0a9c94 560w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=840&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=fb115418f8fb1c0bb79e9ac647158996 840w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=1100&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=bb955f30c027461597f15dbe436fc068 1100w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=1650&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=d891852f83abfd576cc6b2c3eb83749c 1650w, https://mintcdn.com/crewai/xsUWvx-8zGU3Skk0/images/crewai-tracing.png?w=2500&fit=max&auto=format&n=xsUWvx-8zGU3Skk0&q=85&s=67cbde03f418d19d66d4273df9427db2 2500w" />

## Prerequisites

Before you can use CrewAI tracing, you need:

1. **CrewAI AMP Account**: Sign up for a free account at [app.crewai.com](https://app.crewai.com)
2. **CLI Authentication**: Use the CrewAI CLI to authenticate your local environment

```bash  theme={null}
crewai login
```

## Setup Instructions

### Step 1: Create Your CrewAI AMP Account

Visit [app.crewai.com](https://app.crewai.com) and create your free account. This will give you access to the CrewAI AMP platform where you can view traces, metrics, and manage your crews.

### Step 2: Install CrewAI CLI and Authenticate

If you haven't already, install CrewAI with the CLI tools:

```bash  theme={null}
uv add crewai[tools]
```

Then authenticate your CLI with your CrewAI AMP account:

```bash  theme={null}
crewai login
```

This command will:

1. Open your browser to the authentication page
2. Prompt you to enter a device code
3. Authenticate your local environment with your CrewAI AMP account
4. Enable tracing capabilities for your local development

### Step 3: Enable Tracing in Your Crew

You can enable tracing for your Crew by setting the `tracing` parameter to `True`:

```python  theme={null}
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool

# Define your agents
researcher = Agent(
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments in AI and data science",
    backstory="""You work at a leading tech think tank.
    Your expertise lies in identifying emerging trends.
    You have a knack for dissecting complex data and presenting actionable insights.""",
    verbose=True,
    tools=[SerperDevTool()],
)

writer = Agent(
    role="Tech Content Strategist",
    goal="Craft compelling content on tech advancements",
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
    You transform complex concepts into compelling narratives.""",
    verbose=True,
)

# Create tasks for your agents
research_task = Task(
    description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
    Identify key trends, breakthrough technologies, and potential industry impacts.""",
    expected_output="Full analysis report in bullet points",
    agent=researcher,
)

writing_task = Task(
    description="""Using the insights provided, develop an engaging blog
    post that highlights the most significant AI advancements.
    Your post should be informative yet accessible, catering to a tech-savvy audience.""",
    expected_output="Full blog post of at least 4 paragraphs",
    agent=writer,
)

# Enable tracing in your crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential,
    tracing=True,  # Enable built-in tracing
    verbose=True
)

# Execute your crew
result = crew.kickoff()
```

### Step 4: Enable Tracing in Your Flow

Similarly, you can enable tracing for CrewAI Flows:

```python  theme={null}
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class ExampleState(BaseModel):
    counter: int = 0
    message: str = ""

class ExampleFlow(Flow[ExampleState]):
    def __init__(self):
        super().__init__(tracing=True)  # Enable tracing for the flow

    @start()
    def first_method(self):
        print("Starting the flow")
        self.state.counter = 1
        self.state.message = "Flow started"
        return "continue"

    @listen("continue")
    def second_method(self):
        print("Continuing the flow")
        self.state.counter += 1
        self.state.message = "Flow continued"
        return "finish"

    @listen("finish")
    def final_method(self):
        print("Finishing the flow")
        self.state.counter += 1
        self.state.message = "Flow completed"

# Create and run the flow with tracing enabled
flow = ExampleFlow(tracing=True)
result = flow.kickoff()
```

### Step 5: View Traces in the CrewAI AMP Dashboard

After running the crew or flow, you can view the traces generated by your CrewAI application in the CrewAI AMP dashboard. You should see detailed steps of the agent interactions, tool usages, and LLM calls.
Just click on the link below to view the traces or head over to the traces tab in the dashboard [here](https://app.crewai.com/crewai_plus/trace_batches)
<img src="https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=72981ddafcda030270c059f08b98db03" alt="CrewAI Tracing Interface" data-og-width="3272" width="3272" data-og-height="162" height="162" data-path="images/view-traces.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=280&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=ccd01161e9258840e74ef1c451f84269 280w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=560&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=d8feaccbddc300723769a977ca3e0ff9 560w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=840&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=2b404956f27d32dd38b0a5d4bf48ab58 840w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=1100&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=8bc1f5f99f4289ee1dd7ebe2e60bb189 1100w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=1650&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=1ab7e96c4017cf1cbab719c695884969 1650w, https://mintcdn.com/crewai/iG0g1htk7RWkFuad/images/view-traces.png?w=2500&fit=max&auto=format&n=iG0g1htk7RWkFuad&q=85&s=3ab9ea0309e81741969db86307657b90 2500w" />

### Alternative: Environment Variable Configuration

You can also enable tracing globally by setting an environment variable:

```bash  theme={null}
export CREWAI_TRACING_ENABLED=true
```

Or add it to your `.env` file:

```env  theme={null}
CREWAI_TRACING_ENABLED=true
```

When this environment variable is set, all Crews and Flows will automatically have tracing enabled, even without explicitly setting `tracing=True`.

## Viewing Your Traces

### Access the CrewAI AMP Dashboard

1. Visit [app.crewai.com](https://app.crewai.com) and log in to your account
2. Navigate to your project dashboard
3. Click on the **Traces** tab to view execution details

### What You'll See in Traces

CrewAI tracing provides comprehensive visibility into:

* **Agent Decisions**: See how agents reason through tasks and make decisions
* **Task Execution Timeline**: Visual representation of task sequences and dependencies
* **Tool Usage**: Monitor which tools are called and their results
* **LLM Calls**: Track all language model interactions, including prompts and responses
* **Performance Metrics**: Execution times, token usage, and costs
* **Error Tracking**: Detailed error information and stack traces

### Trace Features

* **Execution Timeline**: Click through different stages of execution
* **Detailed Logs**: Access comprehensive logs for debugging
* **Performance Analytics**: Analyze execution patterns and optimize performance
* **Export Capabilities**: Download traces for further analysis

### Authentication Issues

If you encounter authentication problems:

1. Ensure you're logged in: `crewai login`
2. Check your internet connection
3. Verify your account at [app.crewai.com](https://app.crewai.com)

### Traces Not Appearing

If traces aren't showing up in the dashboard:

1. Confirm `tracing=True` is set in your Crew/Flow
2. Check that `CREWAI_TRACING_ENABLED=true` if using environment variables
3. Ensure you're authenticated with `crewai login`
4. Verify your crew/flow is actually executing
