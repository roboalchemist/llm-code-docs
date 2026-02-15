# Source: https://exa.ai/docs/reference/crewai.md

> **Documentation Index**
> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# CrewAI

> Learn how to add Exa retrieval capabilities to your CrewAI agents.

***

[CrewAI](https://crewai.com/) is a framework for orchestrating AI agents that work together to accomplish complex tasks.
In this guide, we'll create a crew of two agents that generate a newsletter based on Exa's search results. We'll go over how to:

1. Create a custom Exa-powered CrewAI tool
2. Set up agents and assign them specific roles that use the Exa-powered search tool
3. Organize the agents into a crew that will write a newsletter

***

## Get Started

<Steps>
  <Step title="Pre-requisites and installation">
    Install the crewAI core, crewAI tools and Exa Python SDK libraries.

    ```Python Python theme={null}
    pip install crewai 'crewai[tools]' exa_py
    ```
  </Step>

  <Step title="Defining a custom Exa-based tool in crewAI">
    We set up a [custom tool](https://docs.crewai.com/concepts/tools) using the crewAI [@tool decorator ](https://docs.crewai.com/concepts/tools#utilizing-the-tool-decorator). Within the tool, we can initialize the Exa class from the [Exa Python SDK](https://github.com/exa-labs/exa-py), make a request, and return a parsed out result.

    ```Python Python theme={null}
    from crewai_tools import tool
    from exa_py import Exa
    import os

    exa_api_key = os.getenv("EXA_API_KEY")

    @tool("Exa search and get contents")
    def search_and_get_contents_tool(question: str) -> str:
        """Tool using Exa's Python SDK to run semantic search and return result highlights."""

        exa = Exa(exa_api_key)

        response = exa.search_and_contents(
            question,
            type="neural",
            num_results=3,
            highlights=True
        )

        parsedResult = ''.join([
          f'<Title id={idx}>{eachResult.title}</Title>
          f'<URL id={idx}>{eachResult.url}</URL>
          f'<Highlight id={idx}>{"".join(eachResult.highlights)}</Highlight>'
          for (idx, eachResult) in enumerate(response.results)
        ])

        return parsedResult
    ```

    <Note> Make sure your API keys are initialized properly. For this demonstration, the environment variable names are `OPENAI_API_KEY` and `EXA_API_KEY` for OpenAI and Exa keys respectively. </Note>

    <Card title="Get your Exa API key" icon="key" horizontal href="https://dashboard.exa.ai/api-keys" />
  </Step>

  <Step title="Setting up CrewAI agent">
    Import the relevant crewAI modules. Then, define `exa_tools` to reference the custom search method we defined above.

    ```Python Python theme={null}
    from crewai import Task, Crew, Agent

    exa_tools = search_and_get_contents_tool
    ```

    We then set up[ two agents](https://docs.crewai.com/concepts/Agents/) and place them in a [crew together](https://docs.crewai.com/concepts/Crews/):

    * One to research with Exa (providing the custom tool defined above)
    * Another to write a newsletter as an output (using an LLM)

    ```Python Python theme={null}
    # Creating a senior researcher agent with memory and verbose mode
    researcher = Agent(
      role='Researcher',
      goal='Get the latest research on {topic}',
      verbose=True,
      memory=True,
      backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
      ),
      tools=[exa_tools],
      allow_delegation=False
    )

    article_writer = Agent(
      role='Researcher',
      goal='Write a great newsletter article on {topic}',
      verbose=True,
      memory=True,
      backstory=(
        "Driven by a love of writing and passion for"
        "innovation, you are eager to share knowledge with"
        "the world."
      ),
      tools=[exa_tools],
      allow_delegation=False
    )
    ```
  </Step>

  <Step title="Defining tasks for the agents">
    Next, we'll define [tasks](https://docs.crewai.com/concepts/Tasks/) for each agent and create the crew overall using all of the components we've set up above.

    ```Python Python theme={null}
    `research_task = Task(
      description=(
        "Identify the latest research in {topic}."
        "Your final report should clearly articulate the key points,"
      ),
      expected_output='A comprehensive 3 paragraphs long report on the {topic}.',
      tools=[exa_tools],
      agent=researcher,
    )

    write_article = Task(
      description=(
        "Write a newsletter article on the latest research in {topic}."
        "Your article should be engaging, informative, and accurate."
        "The article should address the audience with a greeting to the newsletter audience \"Hi readers!\", plus a similar signoff"
      ),
      expected_output='A comprehensive 3 paragraphs long newsletter article on the {topic}.',
      agent=article_writer,
    )

    crew = Crew(
      agents=[researcher, article_writer],
      tasks=[research_task, write_article],
      memory=True,
      cache=True,
      max_rpm=100,
      share_crew=True
    )
    ```
  </Step>

  <Step title="Kicking off the crew">
    Finally, we kick off the crew by providing a research topic as our input query.

    ```Python Python theme={null}
    response = crew.kickoff(inputs={'topic': 'Latest AI research'})

    print(response)
    ```
  </Step>

  <Step title="Output">
    As you can see, Exa's search results enriched the output generation!

    ```Stdout Stdout theme={null}
    `[... Prior output truncated ...]

    > Finished chain.
    Hi readers!

    As we step into the promising arena of 2024, we bring you some of the most significant advancements in the field of AI research. The year witnessed a considerable focus on the development of AI agents and LLMs (Large Language Models). Adept, a frontrunner in the space, showcased an agent that can find apartments on Redfin, input information into Salesforce, and interact with spreadsheets using natural language. While there is no clear winner on the commercial front yet, this development promises a future where AI can perform tasks for us.

    The year also saw a continued focus on LLMs, with efforts directed towards matching the text performance of GPT-4 with smaller models. An interesting outcome of these efforts was the Falcon 7B model, which matches the performance of the 8B PaLM model. This model, interestingly, uses 100% web data for pretraining. It's worth mentioning that LLMs were also used to generate imitation models, which mimic the style of upstream LLMs. One study found that these models are highly rated by crowd workers.

    In the field of computer vision, there were numerous developments. One noteworthy mention is the ASSET paper that introduced an architecture capable of modifying an input high-resolution image according to a user's edits on its semantic segmentation map. This advancement points to the possibility of synthesizing interesting phenomena in scenes, which has the potential to revolutionize the way we interact with digital imagery.

    As we continue to explore the ever-evolving landscape of AI, we hope to bring you more such exciting updates. Stay tuned and until next time, keep exploring!

    Best,
    [Your Name]
    ```
  </Step>
</Steps>
