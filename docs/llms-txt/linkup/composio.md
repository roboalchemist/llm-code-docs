# Source: https://docs.linkup.so/pages/integrations/composio/composio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Composio

> How to use Linkup in Composio

## Overview

Linkup can be used with [Composio](https://composio.dev) as a Tool to get contextual information from the internet. This integration allows your Composio workflows to search the web and incorporate up-to-date information.

## Setting Up Linkup in Composio

<Steps>
  <Step title="Access your Composio account">
    Log in to your Composio account at [composio.dev](https://composio.dev).
  </Step>

  <Step title="Find and select the Linkup tool">
    Navigate to the All Apps section in Composio and search for "Linkup".

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/composio/assets/search_tool.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=4a05af73fce70f359bb97f8711d095b9" alt="Search for tools in Composio" width="2940" height="1194" data-path="pages/integrations/composio/assets/search_tool.png" />

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/composio/assets/search_linkup.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=3402c6c591af9cd3245444869abfffa5" alt="Search results showing Linkup" width="2966" height="1552" data-path="pages/integrations/composio/assets/search_linkup.png" />
  </Step>

  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Configure the integration">
    Click on "Setup Linkup integration".

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/composio/assets/make_integration.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=f5813d1d5769f4434b84fa1abf5debaf" alt="Setup Linkup integration" width="2430" height="1010" data-path="pages/integrations/composio/assets/make_integration.png" />

    Enter your Linkup API Key in the provided field and click on "Try connecting default's linkup".

        <img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/composio/assets/enter_api_key.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=b48d4b72514bca2bf032ecd671444db2" alt="Enter your API key" width="1130" height="860" data-path="pages/integrations/composio/assets/enter_api_key.png" />
  </Step>
</Steps>

## Example with Composio and CrewAI

Composio gives you the ability to build with CrewAI, a powerful agentic framewwork.

<Steps>
  <Step title="Install required packages">
    ```bash  theme={null}
    pip install crewai langchain_openai composio_crewai
    ```
  </Step>

  <Step title="Get your API keys">
    You'll need:

    1. Your Composio API key
    2. An OpenAI API key (get one [here](https://openai.com/index/openai-api/))
  </Step>

  <Step title="Create your CrewAI script">
    Create a new Python file and add the following code:

    ```python  theme={null}
    from crewai import Agent, Task, Crew
    from langchain_openai import ChatOpenAI
    from composio_crewai import ComposioToolSet, Action, App

    # Initialize Composio toolset with your API key
    composio_toolset = ComposioToolSet(api_key="YOUR_COMPOSIO_API_KEY")

    # Get the Linkup search tool
    tools = composio_toolset.get_tools(actions=['LINKUP_PERFORM_A_SEARCH_QUERY'])

    # Create a CrewAI agent with the Linkup tool
    crewai_agent = Agent(
        role="Research Assistant",
        goal="""You analyze information and provide accurate answers based on 
                web searches using the Linkup tool.""",
        backstory=(
            "You are an AI research assistant that helps users find accurate and 
             up-to-date information from the web."
        ),
        verbose=True,
        tools=tools,
        llm=ChatOpenAI(api_key="YOUR_OPENAI_API_KEY"),
    )

    # Create a task for the agent
    task = Task(
        description="Can you tell me which women were awarded the Physics Nobel Prize",
        agent=crewai_agent,
        expected_output="A comprehensive list of female Nobel Physics Prize winners with years"
    )

    # Create and run the crew
    my_crew = Crew(agents=[crewai_agent], tasks=[task])
    result = my_crew.kickoff()

    # Print the result
    print(result)
    ```

    Be sure to replace `YOUR_COMPOSIO_API_KEY` and `YOUR_OPENAI_API_KEY` with your actual API keys.
  </Step>

  <Step title="Run your script">
    Execute your Python script:

    ```bash  theme={null}
    python your_script.py
    ```

    The script will use the Linkup tool through Composio to search for information about female Nobel Physics Prize winners and return the results.

    **Example Response**

    ```
    Four women have been awarded the Nobel Prize in Physics:

    1. Marie Curie (1903) - Awarded for her research on radiation phenomena
    2. Maria Goeppert Mayer (1963) - Awarded for discoveries concerning nuclear shell structure
    3. Donna Strickland (2018) - Awarded for groundbreaking inventions in laser physics
    4. Andrea Ghez (2020) - Awarded for the discovery of a supermassive compact object at the center of our galaxy

    Marie Curie was the first woman to win a Nobel Prize in any category and remains the only woman to win Nobel Prizes in two different scientific fields (Physics in 1903 and Chemistry in 1911).
    ```

    **Advanced Usage**

    You can expand your CrewAI agents to use additional Linkup capabilities by specifying different actions in the `get_tools()` function:

    ```python  theme={null}
    # Get multiple Linkup tools
    tools = composio_toolset.get_tools(actions=[
        'LINKUP_PERFORM_A_SEARCH_QUERY', 
        'LINKUP_PERFORM_A_DEEP_SEARCH_QUERY'
    ])
    ```
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).