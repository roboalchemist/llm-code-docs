# Source: https://docs.crewai.com/en/observability/opik.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Opik Integration

> Learn how to use Comet Opik to debug, evaluate, and monitor your CrewAI applications with comprehensive tracing, automated evaluations, and production-ready dashboards.

# Opik Overview

With [Comet Opik](https://www.comet.com/docs/opik/), debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, automated evaluations, and production-ready dashboards.

<Frame caption="Opik Agent Dashboard">
  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/opik-crewai-dashboard.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=6b313c7d767211f2287d7dd074f9dfeb" alt="Opik agent monitoring example with CrewAI" data-og-width="1538" width="1538" data-og-height="877" height="877" data-path="images/opik-crewai-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/opik-crewai-dashboard.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=b0fd3eca42762838a806dc0d38d0313f 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/opik-crewai-dashboard.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=ba1166f8b42afee86b3cd88532002fde 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/opik-crewai-dashboard.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d7905602ba2ac1dbca66a008be49ca26 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/opik-crewai-dashboard.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=51c2c8ce83af0d81fdf851dd378fe6f6 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/opik-crewai-dashboard.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=5184c8370b92c51a03d970a01c7daba5 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/opik-crewai-dashboard.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=80d3fb638cd8ace74953775242cb68cd 2500w" />
</Frame>

Opik provides comprehensive support for every stage of your CrewAI application development:

* **Log Traces and Spans**: Automatically track LLM calls and application logic to debug and analyze development and production systems. Manually or programmatically annotate, view, and compare responses across projects.
* **Evaluate Your LLM Application's Performance**: Evaluate against a custom test set and run built-in evaluation metrics or define your own metrics in the SDK or UI.
* **Test Within Your CI/CD Pipeline**: Establish reliable performance baselines with Opik's LLM unit tests, built on PyTest. Run online evaluations for continuous monitoring in production.
* **Monitor & Analyze Production Data**: Understand your models' performance on unseen data in production and generate datasets for new dev iterations.

## Setup

Comet provides a hosted version of the Opik platform, or you can run the platform locally.

To use the hosted version, simply [create a free Comet account](https://www.comet.com/signup?utm_medium=github\&utm_source=crewai_docs) and grab you API Key.

To run the Opik platform locally, see our [installation guide](https://www.comet.com/docs/opik/self-host/overview/) for more information.

For this guide we will use CrewAI’s quickstart example.

<Steps>
  <Step title="Install required packages">
    ```shell  theme={null}
    pip install crewai crewai-tools opik --upgrade
    ```
  </Step>

  <Step title="Configure Opik">
    ```python  theme={null}
    import opik
    opik.configure(use_local=False)
    ```
  </Step>

  <Step title="Prepare environment">
    First, we set up our API keys for our LLM-provider as environment variables:

    ```python  theme={null}
    import os
    import getpass

    if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
    ```
  </Step>

  <Step title="Using CrewAI">
    The first step is to create our project. We will use an example from CrewAI’s documentation:

    ```python  theme={null}
    from crewai import Agent, Crew, Task, Process


    class YourCrewName:
        def agent_one(self) -> Agent:
            return Agent(
                role="Data Analyst",
                goal="Analyze data trends in the market",
                backstory="An experienced data analyst with a background in economics",
                verbose=True,
            )

        def agent_two(self) -> Agent:
            return Agent(
                role="Market Researcher",
                goal="Gather information on market dynamics",
                backstory="A diligent researcher with a keen eye for detail",
                verbose=True,
            )

        def task_one(self) -> Task:
            return Task(
                name="Collect Data Task",
                description="Collect recent market data and identify trends.",
                expected_output="A report summarizing key trends in the market.",
                agent=self.agent_one(),
            )

        def task_two(self) -> Task:
            return Task(
                name="Market Research Task",
                description="Research factors affecting market dynamics.",
                expected_output="An analysis of factors influencing the market.",
                agent=self.agent_two(),
            )

        def crew(self) -> Crew:
            return Crew(
                agents=[self.agent_one(), self.agent_two()],
                tasks=[self.task_one(), self.task_two()],
                process=Process.sequential,
                verbose=True,
            )

    ```

    Now we can import Opik’s tracker and run our crew:

    ```python  theme={null}
    from opik.integrations.crewai import track_crewai

    track_crewai(project_name="crewai-integration-demo")

    my_crew = YourCrewName().crew()
    result = my_crew.kickoff()

    print(result)
    ```

    After running your CrewAI application, visit the Opik app to view:

    * LLM traces, spans, and their metadata
    * Agent interactions and task execution flow
    * Performance metrics like latency and token usage
    * Evaluation metrics (built-in or custom)
  </Step>
</Steps>

## Resources

* [🦉 Opik Documentation](https://www.comet.com/docs/opik/)
* [👉 Opik + CrewAI Colab](https://colab.research.google.com/github/comet-ml/opik/blob/main/apps/opik-documentation/documentation/docs/cookbook/crewai.ipynb)
* [🐦 X](https://x.com/cometml)
* [💬 Slack](https://slack.comet.com/)
