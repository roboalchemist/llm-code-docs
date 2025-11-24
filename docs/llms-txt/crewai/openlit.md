# Source: https://docs.crewai.com/en/observability/openlit.md

# OpenLIT Integration

> Quickly start monitoring your Agents in just a single line of code with OpenTelemetry.

# OpenLIT Overview

[OpenLIT](https://github.com/openlit/openlit?src=crewai-docs) is an open-source tool that makes it simple to monitor the performance of AI agents, LLMs, VectorDBs, and GPUs with just **one** line of code.

It provides OpenTelemetry-native tracing and metrics to track important parameters like cost, latency, interactions and task sequences.
This setup enables you to track hyperparameters and monitor for performance issues, helping you find ways to enhance and fine-tune your agents over time.

<Frame caption="OpenLIT Dashboard">
  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=2b7fe9d84e9ec2b33c5eae6fa5668bee" alt="Overview Agent usage including cost and tokens" data-og-width="3024" width="3024" data-og-height="1720" height="1720" data-path="images/openlit1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c971bf515a852fd31020a8b1324f1c1c 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=84c289d1cb65df00729c0265b937953d 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a2f16c0fff510b112190d86e4d660f57 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d16913f544b0bab3b1b6df63f9d221eb 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=f3fb2555418f5a64d567b5ab2c16da87 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=58ca748851de32f75bfeb36bb2cbdcfa 2500w" />

  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=74bb57f622b6eeb67fd33d93d682df26" alt="Overview of agent otel traces and metrics" data-og-width="3024" width="3024" data-og-height="1728" height="1728" data-path="images/openlit2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=5f8faf220f9d7a5660652ec531dd07f9 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a02410c4bf920c9aafe972416e52a400 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=21b69af51e7ed46fb5b38a932a64471b 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=b32ebaa0e210ff7151bb831d4e2fd5fc 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c360d0388bd1af92dedde1967e41017f 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9f14c8d65a0ca1177c2aa848c7a57aaa 2500w" />

  <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=734cbc0c8fee538986d74b063c20cef6" alt="Overview of agent traces in details" data-og-width="3024" width="3024" data-og-height="1720" height="1720" data-path="images/openlit3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=37d3f6eb4f5b66f6466fba0c02137aec 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9769fd3fdadf6acd8eadb2f80b4cc352 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=0f3367e37d8642fe4aa81f444c17b03d 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a2c9c17452fde4610823a981d60ce226 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=bf6526be4832980353137d0e19e38768 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit3.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a0c09334de9c7d1bb7f90a7ea636379f 2500w" />
</Frame>

### Features

* **Analytics Dashboard**: Monitor your Agents health and performance with detailed dashboards that track metrics, costs, and user interactions.
* **OpenTelemetry-native Observability SDK**: Vendor-neutral SDKs to send traces and metrics to your existing observability tools like Grafana, DataDog and more.
* **Cost Tracking for Custom and Fine-Tuned Models**: Tailor cost estimations for specific models using custom pricing files for precise budgeting.
* **Exceptions Monitoring Dashboard**: Quickly spot and resolve issues by tracking common exceptions and errors with a monitoring dashboard.
* **Compliance and Security**: Detect potential threats such as profanity and PII leaks.
* **Prompt Injection Detection**: Identify potential code injection and secret leaks.
* **API Keys and Secrets Management**: Securely handle your LLM API keys and secrets centrally, avoiding insecure practices.
* **Prompt Management**: Manage and version Agent prompts using PromptHub for consistent and easy access across Agents.
* **Model Playground** Test and compare different models for your CrewAI agents before deployment.

## Setup Instructions

<Steps>
  <Step title="Deploy OpenLIT">
    <Steps>
      <Step title="Git Clone OpenLIT Repository">
        ```shell  theme={null}
        git clone git@github.com:openlit/openlit.git
        ```
      </Step>

      <Step title="Start Docker Compose">
        From the root directory of the [OpenLIT Repo](https://github.com/openlit/openlit), Run the below command:

        ```shell  theme={null}
        docker compose up -d
        ```
      </Step>
    </Steps>
  </Step>

  <Step title="Install OpenLIT SDK">
    ```shell  theme={null}
    pip install openlit
    ```
  </Step>

  <Step title="Initialize OpenLIT in Your Application">
    Add the following two lines to your application code:

    <Tabs>
      <Tab title="Setup using function arguments">
        ```python  theme={null}
        import openlit
        openlit.init(otlp_endpoint="http://127.0.0.1:4318")
        ```

        Example Usage for monitoring a CrewAI Agent:

        ```python  theme={null}
        from crewai import Agent, Task, Crew, Process
        import openlit

        openlit.init(disable_metrics=True)
        # Define your agents
        researcher = Agent(
            role="Researcher",
            goal="Conduct thorough research and analysis on AI and AI agents",
            backstory="You're an expert researcher, specialized in technology, software engineering, AI, and startups. You work as a freelancer and are currently researching for a new client.",
            allow_delegation=False,
            llm='command-r'
        )


        # Define your task
        task = Task(
            description="Generate a list of 5 interesting ideas for an article, then write one captivating paragraph for each idea that showcases the potential of a full article on this topic. Return the list of ideas with their paragraphs and your notes.",
            expected_output="5 bullet points, each with a paragraph and accompanying notes.",
        )

        # Define the manager agent
        manager = Agent(
            role="Project Manager",
            goal="Efficiently manage the crew and ensure high-quality task completion",
            backstory="You're an experienced project manager, skilled in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
            allow_delegation=True,
            llm='command-r'
        )

        # Instantiate your crew with a custom manager
        crew = Crew(
            agents=[researcher],
            tasks=[task],
            manager_agent=manager,
            process=Process.hierarchical,
        )

        # Start the crew's work
        result = crew.kickoff()

        print(result)
        ```
      </Tab>

      <Tab title="Setup using Environment Variables">
        Add the following two lines to your application code:

        ```python  theme={null}
        import openlit

        openlit.init()
        ```

        Run the following command to configure the OTEL export endpoint:

        ```shell  theme={null}
        export OTEL_EXPORTER_OTLP_ENDPOINT = "http://127.0.0.1:4318"
        ```

        Example Usage for monitoring a CrewAI Async Agent:

        ```python  theme={null}
        import asyncio
        from crewai import Crew, Agent, Task
        import openlit

        openlit.init(otlp_endpoint="http://127.0.0.1:4318")

        # Create an agent with code execution enabled
        coding_agent = Agent(
          role="Python Data Analyst",
          goal="Analyze data and provide insights using Python",
          backstory="You are an experienced data analyst with strong Python skills.",
          allow_code_execution=True,
          llm="command-r"
        )

        # Create a task that requires code execution
        data_analysis_task = Task(
          description="Analyze the given dataset and calculate the average age of participants. Ages: {ages}",
          agent=coding_agent,
          expected_output="5 bullet points, each with a paragraph and accompanying notes.",
        )

        # Create a crew and add the task
        analysis_crew = Crew(
          agents=[coding_agent],
          tasks=[data_analysis_task]
        )

        # Async function to kickoff the crew asynchronously
        async def async_crew_execution():
            result = await analysis_crew.kickoff_async(inputs={"ages": [25, 30, 35, 40, 45]})
            print("Crew Result:", result)

        # Run the async function
        asyncio.run(async_crew_execution())
        ```
      </Tab>
    </Tabs>

    Refer to OpenLIT [Python SDK repository](https://github.com/openlit/openlit/tree/main/sdk/python) for more advanced configurations and use cases.
  </Step>

  <Step title="Visualize and Analyze">
    With the Agent Observability data now being collected and sent to OpenLIT, the next step is to visualize and analyze this data to get insights into your Agent's performance, behavior, and identify areas of improvement.

    Just head over to OpenLIT at `127.0.0.1:3000` on your browser to start exploring. You can login using the default credentials

    * **Email**: `user@openlit.io`
    * **Password**: `openlituser`

    <Frame caption="OpenLIT Dashboard">
      <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=2b7fe9d84e9ec2b33c5eae6fa5668bee" alt="Overview Agent usage including cost and tokens" data-og-width="3024" width="3024" data-og-height="1720" height="1720" data-path="images/openlit1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c971bf515a852fd31020a8b1324f1c1c 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=84c289d1cb65df00729c0265b937953d 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a2f16c0fff510b112190d86e4d660f57 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=d16913f544b0bab3b1b6df63f9d221eb 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=f3fb2555418f5a64d567b5ab2c16da87 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit1.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=58ca748851de32f75bfeb36bb2cbdcfa 2500w" />

      <img src="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=74bb57f622b6eeb67fd33d93d682df26" alt="Overview of agent otel traces and metrics" data-og-width="3024" width="3024" data-og-height="1728" height="1728" data-path="images/openlit2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=280&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=5f8faf220f9d7a5660652ec531dd07f9 280w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=560&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=a02410c4bf920c9aafe972416e52a400 560w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=840&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=21b69af51e7ed46fb5b38a932a64471b 840w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=b32ebaa0e210ff7151bb831d4e2fd5fc 1100w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=1650&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=c360d0388bd1af92dedde1967e41017f 1650w, https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/openlit2.png?w=2500&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=9f14c8d65a0ca1177c2aa848c7a57aaa 2500w" />
    </Frame>
  </Step>
</Steps>
