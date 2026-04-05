<!--
source: https://desearch.ai/docs/guide/integrations/crewai-agents
title: CrewAI Agents with Desearch - Integrations Documentation | Desearch
captured: 2026-04-04
-->
# CrewAI Agents with Desearch - Integrations Documentation | Desearch

Source: https://desearch.ai/docs/guide/integrations/crewai-agents

---

Home
Guide
API Reference
SDKs
API Console
API Status
GitHub
Discord
Blog
Search guides...
⌘K
INTRODUCTION
Desearch AI
Desearch Console
Glossary
APIS
Desearch API
Desearch x Bittensor
API Keys
Authorization
Pricing and Billing
SDK
Desearch API SDK
Python SDK Specification
JavaScript SDK Specification
INTEGRATIONS
MCP
OpenAI Wrapper
Function Calling with GPT
Function Calling with Claude
RAG with LangChain x Desearch
RAG with LlmaIndex x Desearch
ElizaOs Agents with Desearch
CrewAI Agents with Desearch
Browser Use x Desearch
OpenClaw Agent with Desearch
Numinous SN6 × Desearch Integration
USE CASES
Search Engine Use Cases
AI-Driven Chat Use Cases
Intelligent Agent Task Automation
CAPABILITIES
X (Twitter) Queries
CrewAI Agents with Desearch

<Anchor label="CrewAI " target="_blank" href="https://www.crewai.com/">CrewAI </Anchor>is a framework for coordinating AI agents to tackle complex tasks together. In this guide, you’ll build a two-agent crew that creates a digest using Desearch’s search results. You’ll learn how to:

Build a custom CrewAI tool powered by Desearch
Set up agents with defined roles using that tool
Assemble the agents into a crew that generates a digest
🚀 CrewAI Example: Twitter News Digest

This guide sets up a CrewAI team that produces a daily Twitter news digest on any topic using Desearch’s Twitter tool.

1. Install Required Packages

Use pip to install the required packages for the project.

BASH
pip install crewai 'crewai[tools]' desearch_py
2. Custom Tool: Desearch for Twitter

We create a <Anchor label="custom tool" target="_blank" href="https://docs.crewai.com/concepts/tools">custom tool</Anchor> using the crewAI <Anchor label="@tool decorator" target="_blank" href="https://docs.crewai.com/concepts/tools#utilizing-the-tool-decorator">@tool decorator</Anchor> . Inside it, we initialize the Desearch class from the <Anchor label="Desearch Python SDK" target="_blank" href="https://github.com/desearch-ai/desearch.py">Desearch Python SDK</Anchor>, send a query, and return the parsed results.

PYTHON
from crewai.tools import tool
from desearch_py import Desearch
import os

desearch_api_key = os.getenv("DESEARCH_API_KEY")

@tool("Twitter Trend Search")
def desearch_ai_search_tool(question: str) -> str:
    """Get trending Twitter posts on a topic using Desearch's Twitter source."""

    desearch = Desearch(api_key=desearch_api_key)

    response = desearch.ai_search(
        prompt=question,
        tools=["twitter"],
        date_filter="PAST_24_HOURS",
        streaming=False,
    )

    return str(response)

📘 Select Desearch Methods to Use

In this example, we’re only using the ai_search method from Desearch, so we connect that directly to our agent’s toolset.

1. Create Agents

Start by importing the necessary CrewAI modules.

PYTHON
from crewai import Task, Crew, Agent

Next, we create two agents and group them into a crew: one uses the Desearch tool to gather insights, and the other writes a digest based on those findings.

PYTHON

## Creating a senior researcher agent with memory and verbose mode

twitter_analyst = Agent(
  role='Twitter Analyst',
  goal='Find the most interesting tweets and discussions about {topic} from the past 24 hours',
  verbose=True,
  memory=True,
  backstory="You're a social media researcher who specializes in Twitter trends.",
  tools=[desearch_ai_search_tool],
  allow_delegation=False
)

digest_writer = Agent(
  role='Digest Writer',
  goal='Write a fun and engaging digest about what people are saying on Twitter about {topic}',
  verbose=True,
  memory=True,
  backstory="You craft lively daily digests from raw social buzz and trends.",
  tools=[desearch_ai_search_tool],
  allow_delegation=False
)

1. Create Tasks

Now let’s assign <Anchor label="tasks" target="_blank" href="https://docs.crewai.com/concepts/Tasks/">tasks</Anchor> to each agent and bring everything together by creating the full crew.

PYTHON
research_task = Task(
  description=(
    "Summarize the top Twitter conversations about {topic}."
    "Highlight key tweets and trends."
  ),
  expected_output='A list of 5–7 summarized tweets with short context on the {topic}.',
  tools=[desearch_ai_search_tool],
  agent=twitter_analyst,
)

write_digest = Task(
  description=(
    "Write a Twitter news digest on {topic}."
    "Start with 'Hi folks!' and end with a playful sign-off like 'Catch you on the timeline!'"
  ),
  expected_output='A short, punchy 3-paragraph Twitter roundup article on the {topic}.',
  agent=digest_writer,
)

crew = Crew(
  agents=[twitter_analyst, digest_writer],
  tasks=[research_task, write_digest],
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

1. Run the Crew

Finally, we launch the crew by passing in a topic for them to research and write about.

PYTHON
response = crew.kickoff(inputs={'topic': 'AI and robotics'})

print(response)

1. Output

As you can see, Desearch’s results added valuable context that enhanced the final output!

Output

Hi folks!

In the latest buzz, AI and robotics are hitting the headlines with some exciting developments! Sam Altman, the pioneering brains behind OpenAI, is dreaming big about humanoid robots, forecasting their arrival within 5–10 years. But don’t get too excited just yet; the engineering challenges of creating a human-like body remain a tough nut to crack! (Check it out here).

On the practical side of things, businesses are harnessing AI to supercharge their supply chains. One company recently reported a whopping 32% efficiency boost in just a week after deploying AI-driven models in their warehouses. Can you imagine robots darting around autonomously, optimizing inventory in real time? (Read more). And if that's not enough, firms like Hexagon Manufacturing have introduced groundbreaking platforms that revolutionize robotic motion and path planning—engineering magic in action! (More info here).

As if that wasn’t enough, we have #Mech, the first AI-powered superhumanoid robot, tackling tough tasks in demanding environments. From cooking pancakes with custom-designed tools to handling serious warehouse chores, the future of robotics looks super fun! Robots are not just for factories anymore; they’re on their way to becoming part of our daily routines (See for yourself, and here).

Catch you on the timeline!

🛠️ Desearch Tool Functions
ai_search_tool: The Desearch API allows you to perform AI-powered web searches, gathering relevant information from multiple sources, including web pages, research papers, and social media discussions.
twitter_search_tool: The X Search API enables users to retrieve relevant links and tweets based on specified search queries without utilizing AI-driven models. It analyzes links from X posts that align with the provided search criteria.
web_search_tool: This API allows users to search for any information on the web. This replicates a typical search engine experience, where users can search for any information they need.
🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
