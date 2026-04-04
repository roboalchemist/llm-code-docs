# Source: https://docs.crewai.com/en/observability/langdb.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LangDB Integration

> Govern, secure, and optimize your CrewAI workflows with LangDB AI Gateway—access 350+ models, automatic routing, cost optimization, and full observability.

# Introduction

[LangDB AI Gateway](https://langdb.ai) provides OpenAI-compatible APIs to connect with multiple Large Language Models and serves as an observability platform that makes it effortless to trace CrewAI workflows end-to-end while providing access to 350+ language models. With a single `init()` call, all agent interactions, task executions, and LLM calls are captured, providing comprehensive observability and production-ready AI infrastructure for your applications.

<Frame caption="LangDB CrewAI Trace Example">
  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-1.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6303d15055c19a7a6ec9d0c664f15c9f" alt="LangDB CrewAI trace example" data-og-width="1576" width="1576" data-og-height="892" height="892" data-path="images/langdb-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-1.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=da34c5dce0a82022f85feda11af459d4 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-1.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=902f87462033e4874e3d373953158a39 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-1.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=74c605bfb1a201c0f663d1c04b8daf60 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-1.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=880a223bb40e9c94724c6047b7a2e966 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-1.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=2c3dd2cac11506d6cc1aeba11c79759d 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-1.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a6d52809351409222de871b2f8018715 2500w" />
</Frame>

**Checkout:** [View the live trace example](https://app.langdb.ai/sharing/threads/3becbfed-a1be-ae84-ea3c-4942867a3e22)

## Features

### AI Gateway Capabilities

* **Access to 350+ LLMs**: Connect to all major language models through a single integration
* **Virtual Models**: Create custom model configurations with specific parameters and routing rules
* **Virtual MCP**: Enable compatibility and integration with MCP (Model Context Protocol) systems for enhanced agent communication
* **Guardrails**: Implement safety measures and compliance controls for agent behavior

### Observability & Tracing

* **Automatic Tracing**: Single `init()` call captures all CrewAI interactions
* **End-to-End Visibility**: Monitor agent workflows from start to finish
* **Tool Usage Tracking**: Track which tools agents use and their outcomes
* **Model Call Monitoring**: Detailed insights into LLM interactions
* **Performance Analytics**: Monitor latency, token usage, and costs
* **Debugging Support**: Step-through execution for troubleshooting
* **Real-time Monitoring**: Live traces and metrics dashboard

## Setup Instructions

<Steps>
  <Step title="Install LangDB">
    Install the LangDB client with CrewAI feature flag:

    ```bash  theme={null}
    pip install 'pylangdb[crewai]'
    ```
  </Step>

  <Step title="Set Environment Variables">
    Configure your LangDB credentials:

    ```bash  theme={null}
    export LANGDB_API_KEY="<your_langdb_api_key>"
    export LANGDB_PROJECT_ID="<your_langdb_project_id>"
    export LANGDB_API_BASE_URL='https://api.us-east-1.langdb.ai'
    ```
  </Step>

  <Step title="Initialize Tracing">
    Import and initialize LangDB before configuring your CrewAI code:

    ```python  theme={null}
    from pylangdb.crewai import init
    # Initialize LangDB
    init()
    ```
  </Step>

  <Step title="Configure CrewAI with LangDB">
    Set up your LLM with LangDB headers:

    ```python  theme={null}
    from crewai import Agent, Task, Crew, LLM
    import os

    # Configure LLM with LangDB headers
    llm = LLM(
        model="openai/gpt-4o", # Replace with the model you want to use
        api_key=os.getenv("LANGDB_API_KEY"),
        base_url=os.getenv("LANGDB_API_BASE_URL"),
        extra_headers={"x-project-id": os.getenv("LANGDB_PROJECT_ID")}
    )
    ```
  </Step>
</Steps>

## Quick Start Example

Here's a simple example to get you started with LangDB and CrewAI:

```python  theme={null}
import os
from pylangdb.crewai import init
from crewai import Agent, Task, Crew, LLM

# Initialize LangDB before any CrewAI imports
init()

def create_llm(model):
    return LLM(
        model=model,
        api_key=os.environ.get("LANGDB_API_KEY"),
        base_url=os.environ.get("LANGDB_API_BASE_URL"),
        extra_headers={"x-project-id": os.environ.get("LANGDB_PROJECT_ID")}
    )

# Define your agent
researcher = Agent(
    role="Research Specialist",
    goal="Research topics thoroughly",
    backstory="Expert researcher with skills in finding information",
    llm=create_llm("openai/gpt-4o"), # Replace with the model you want to use
    verbose=True
)

# Create a task
task = Task(
    description="Research the given topic and provide a comprehensive summary",
    agent=researcher,
    expected_output="Detailed research summary with key findings"
)

# Create and run the crew
crew = Crew(agents=[researcher], tasks=[task])
result = crew.kickoff()
print(result)
```

## Complete Example: Research and Planning Agent

This comprehensive example demonstrates a multi-agent workflow with research and planning capabilities.

### Prerequisites

```bash  theme={null}
pip install crewai 'pylangdb[crewai]' crewai_tools setuptools python-dotenv
```

### Environment Setup

```bash  theme={null}
# LangDB credentials
export LANGDB_API_KEY="<your_langdb_api_key>"
export LANGDB_PROJECT_ID="<your_langdb_project_id>"
export LANGDB_API_BASE_URL='https://api.us-east-1.langdb.ai'

# Additional API keys (optional)
export SERPER_API_KEY="<your_serper_api_key>"  # For web search capabilities
```

### Complete Implementation

```python  theme={null}
#!/usr/bin/env python3

import os
import sys
from pylangdb.crewai import init
init()  # Initialize LangDB before any CrewAI imports
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool

load_dotenv()

def create_llm(model):
    return LLM(
        model=model,
        api_key=os.environ.get("LANGDB_API_KEY"),
        base_url=os.environ.get("LANGDB_API_BASE_URL"),
        extra_headers={"x-project-id": os.environ.get("LANGDB_PROJECT_ID")}
    )

class ResearchPlanningCrew:
    def researcher(self) -> Agent:
        return Agent(
            role="Research Specialist",
            goal="Research topics thoroughly and compile comprehensive information",
            backstory="Expert researcher with skills in finding and analyzing information from various sources",
            tools=[SerperDevTool()],
            llm=create_llm("openai/gpt-4o"),
            verbose=True
        )
    
    def planner(self) -> Agent:
        return Agent(
            role="Strategic Planner",
            goal="Create actionable plans based on research findings",
            backstory="Strategic planner who breaks down complex challenges into executable plans",
            reasoning=True,
            max_reasoning_attempts=3,
            llm=create_llm("openai/anthropic/claude-3.7-sonnet"),
            verbose=True
        )
    
    def research_task(self) -> Task:
        return Task(
            description="Research the topic thoroughly and compile comprehensive information",
            agent=self.researcher(),
            expected_output="Comprehensive research report with key findings and insights"
        )
    
    def planning_task(self) -> Task:
        return Task(
            description="Create a strategic plan based on the research findings",
            agent=self.planner(),
            expected_output="Strategic execution plan with phases, goals, and actionable steps",
            context=[self.research_task()]
        )
    
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(), self.planner()],
            tasks=[self.research_task(), self.planning_task()],
            verbose=True,
            process=Process.sequential
        )

def main():
        topic = sys.argv[1] if len(sys.argv) > 1 else "Artificial Intelligence in Healthcare"
        
        crew_instance = ResearchPlanningCrew()
        
        # Update task descriptions with the specific topic
        crew_instance.research_task().description = f"Research {topic} thoroughly and compile comprehensive information"
    crew_instance.planning_task().description = f"Create a strategic plan for {topic} based on the research findings"
    
    result = crew_instance.crew().kickoff()
    print(result)

if __name__ == "__main__":
    main()
```

### Running the Example

```bash  theme={null}
python main.py "Sustainable Energy Solutions"
```

## Viewing Traces in LangDB

After running your CrewAI application, you can view detailed traces in the LangDB dashboard:

<Frame caption="LangDB Trace Dashboard">
  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-2.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=74a88afefce3f84fb6f9482a1790b413" alt="LangDB trace dashboard showing CrewAI workflow" data-og-width="1627" width="1627" data-og-height="890" height="890" data-path="images/langdb-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-2.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=8e43fd482dc80800788d7092a8e51f1c 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-2.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=02e4ddf9b1499b19d1e221628f5c21a4 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-2.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=31e9c94a264d2b33fc9bfbb6a744dc15 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-2.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=5de66fecea56248c974a91c918135e52 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-2.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e03d206dd7c466cc5b9de55bab46daf1 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/langdb-2.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=4c16c2587ec6b48bf8cff71b9df17d07 2500w" />
</Frame>

### What You'll See

* **Agent Interactions**: Complete flow of agent conversations and task handoffs
* **Tool Usage**: Which tools were called, their inputs, and outputs
* **Model Calls**: Detailed LLM interactions with prompts image.pngand responses
* **Performance Metrics**: Latency, token usage, and cost tracking
* **Execution Timeline**: Step-by-step view of the entire workflow

## Troubleshooting

### Common Issues

* **No traces appearing**: Ensure `init()` is called before any CrewAI imports
* **Authentication errors**: Verify your LangDB API key and project ID

## Resources

<CardGroup cols={3}>
  <Card title="LangDB Documentation" icon="book" href="https://docs.langdb.ai">
    Official LangDB documentation and guides
  </Card>

  <Card title="LangDB Guides" icon="graduation-cap" href="https://docs.langdb.ai/guides">
    Step-by-step tutorials for building AI agents
  </Card>

  <Card title="GitHub Examples" icon="github" href="https://github.com/langdb/langdb-samples/tree/main/examples/crewai">
    Complete CrewAI integration examples
  </Card>

  <Card title="LangDB Dashboard" icon="chart-line" href="https://app.langdb.ai">
    Access your traces and analytics
  </Card>

  <Card title="Model Catalog" icon="list" href="https://app.langdb.ai/models">
    Browse 350+ available language models
  </Card>

  <Card title="Enterprise Features" icon="building" href="https://docs.langdb.ai/enterprise">
    Self-hosted options and enterprise capabilities
  </Card>
</CardGroup>

## Next Steps

This guide covered the basics of integrating LangDB AI Gateway with CrewAI. To further enhance your AI workflows, explore:

* **Virtual Models**: Create custom model configurations with routing strategies
* **Guardrails & Safety**: Implement content filtering and compliance controls
* **Production Deployment**: Configure fallbacks, retries, and load balancing

For more advanced features and use cases, visit the [LangDB Documentation](https://docs.langdb.ai) or explore the [Model Catalog](https://app.langdb.ai/models) to discover all available models.
