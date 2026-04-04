# Source: https://docs.crewai.com/en/observability/weave.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Weave Integration

> Learn how to use Weights & Biases (W&B) Weave to track, experiment with, evaluate, and improve your CrewAI applications.

# Weave Overview

[Weights & Biases (W\&B) Weave](https://weave-docs.wandb.ai/) is a framework for tracking, experimenting with, evaluating, deploying, and improving LLM-based applications.

<img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.gif?s=4a933830e3e3cf146c4c87cb44d46475" alt="Overview of W&B Weave CrewAI tracing usage" data-og-width="852" width="852" data-og-height="480" height="480" data-path="images/weave-tracing.gif" data-optimize="true" data-opv="3" />

Weave provides comprehensive support for every stage of your CrewAI application development:

* **Tracing & Monitoring**: Automatically track LLM calls and application logic to debug and analyze production systems
* **Systematic Iteration**: Refine and iterate on prompts, datasets, and models
* **Evaluation**: Use custom or pre-built scorers to systematically assess and enhance agent performance
* **Guardrails**: Protect your agents with pre- and post-safeguards for content moderation and prompt safety

Weave automatically captures traces for your CrewAI applications, enabling you to monitor and analyze your agents' performance, interactions, and execution flow. This helps you build better evaluation datasets and optimize your agent workflows.

## Setup Instructions

<Steps>
  <Step title="Install required packages">
    ```shell  theme={null}
    pip install crewai weave
    ```
  </Step>

  <Step title="Set up W&B Account">
    Sign up for a [Weights & Biases account](https://wandb.ai) if you haven't already. You'll need this to view your traces and metrics.
  </Step>

  <Step title="Initialize Weave in Your Application">
    Add the following code to your application:

    ```python  theme={null}
    import weave

    # Initialize Weave with your project name
    weave.init(project_name="crewai_demo")
    ```

    After initialization, Weave will provide a URL where you can view your traces and metrics.
  </Step>

  <Step title="Create your Crews/Flows">
    ```python  theme={null}
    from crewai import Agent, Task, Crew, LLM, Process

    # Create an LLM with a temperature of 0 to ensure deterministic outputs
    llm = LLM(model="gpt-4o", temperature=0)

    # Create agents
    researcher = Agent(
        role='Research Analyst',
        goal='Find and analyze the best investment opportunities',
        backstory='Expert in financial analysis and market research',
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    writer = Agent(
        role='Report Writer',
        goal='Write clear and concise investment reports',
        backstory='Experienced in creating detailed financial reports',
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    # Create tasks
    research_task = Task(
        description='Deep research on the {topic}',
        expected_output='Comprehensive market data including key players, market size, and growth trends.',
        agent=researcher
    )

    writing_task = Task(
        description='Write a detailed report based on the research',
        expected_output='The report should be easy to read and understand. Use bullet points where applicable.',
        agent=writer
    )

    # Create a crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        verbose=True,
        process=Process.sequential,
    )

    # Run the crew
    result = crew.kickoff(inputs={"topic": "AI in material science"})
    print(result)
    ```
  </Step>

  <Step title="View Traces in Weave">
    After running your CrewAI application, visit the Weave URL provided during initialization to view:

    * LLM calls and their metadata
    * Agent interactions and task execution flow
    * Performance metrics like latency and token usage
    * Any errors or issues that occurred during execution

    <Frame caption="Weave Tracing Dashboard">
      <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=f59e556fcc0ac8fcca8eaeef4c0551ae" alt="Weave tracing example with CrewAI" data-og-width="3456" width="3456" data-og-height="1986" height="1986" data-path="images/weave-tracing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=42efb320cedff3209765027d4f47e187 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=85318181f2afd6237c71cecedfda8104 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6124c3113060320d39847c47faa02ac4 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=e04300ff38ddf3624acc078bacf6712e 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c0ba473c3fa41c2939df4e28bc1098b5 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/weave-tracing.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6d860d735bc5a42fb68085fc4ef01b2c 2500w" />
    </Frame>
  </Step>
</Steps>

## Features

* Weave automatically captures all CrewAI operations: agent interactions and task executions; LLM calls with metadata and token usage; tool usage and results.
* The integration supports all CrewAI execution methods: `kickoff()`, `kickoff_for_each()`, `kickoff_async()`, and `kickoff_for_each_async()`.
* Automatic tracing of all [crewAI-tools](https://github.com/crewAIInc/crewAI-tools).
* Flow feature support with decorator patching (`@start`, `@listen`, `@router`, `@or_`, `@and_`).
* Track custom guardrails passed to CrewAI `Task` with `@weave.op()`.

For detailed information on what's supported, visit the [Weave CrewAI documentation](https://weave-docs.wandb.ai/guides/integrations/crewai/#getting-started-with-flow).

## Resources

* [📘 Weave Documentation](https://weave-docs.wandb.ai)
* [📊 Example Weave x CrewAI dashboard](https://wandb.ai/ayut/crewai_demo/weave/traces?cols=%7B%22wb_run_id%22%3Afalse%2C%22attributes.weave.client_version%22%3Afalse%2C%22attributes.weave.os_name%22%3Afalse%2C%22attributes.weave.os_release%22%3Afalse%2C%22attributes.weave.os_version%22%3Afalse%2C%22attributes.weave.source%22%3Afalse%2C%22attributes.weave.sys_version%22%3Afalse%7D\&peekPath=%2Fayut%2Fcrewai_demo%2Fcalls%2F0195c838-38cb-71a2-8a15-651ecddf9d89)
* [🐦 X](https://x.com/weave_wb)
