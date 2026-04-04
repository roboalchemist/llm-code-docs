# Compiled graph might be invoked with the initial state to start.
compiled_graph.invoke({
    "messages": [\
        ("user", "Why Qdrant is the best vector database out there?"),\
    ]
})

```

Each node of the process is just a Python function that does certain operation. You can call an LLM of your choice
inside of them, if you want to, but there is no assumption about the messages being created by any AI. **LangGraph**
**rather acts as a runtime that launches these functions in a specific order, and passes the state between them**. While
[LangGraph](https://www.langchain.com/langgraph) integrates well with the LangChain ecosystem, it can be used
independently. For teams looking for additional support and features, there’s also a commercial offering called
LangGraph Platform. The framework is available for both Python and JavaScript environments, making it possible to be
used in different tech stacks.

### [Anchor](https://qdrant.tech/articles/agentic-rag/\#crewai) CrewAI

CrewAI is another popular choice for building agents, including agentic RAG. It’s a high-level framework that assumes
there are some LLM-based agents working together to achieve a common goal. That’s where the “crew” in CrewAI comes from.
CrewAI is designed with multi-agent systems in mind. Contrary to LangGraph, the developer does not create a graph of
processing, but defines agents and their roles within the crew.

Some of the key concepts of CrewAI include:

- **Agent** \- a unit that has a specific role and goal, controlled by an LLM. It can optionally use some external tools
to communicate with the outside world, but generally steered by prompt we provide to the LLM.
- **Process** \- currently either sequential or hierarchical. It defines how the task will be executed by the agents.
In a sequential process, agents are executed one after another, while in a hierarchical process, agent is selected
by the manager agent, which is responsible for making decisions about which agent to use in a given situation.
- **Roles and goals** \- each agent has a certain role within the crew, and the goal it should aim to achieve. These are
set when we define an agent and are used to make decisions about which agent to use in a given situation.
- **Memory** \- an extensive memory system consists of short-term memory, long-term memory, entity memory, and contextual
memory that combines the other three. There is also user memory for preferences and personalization. **This is where**
**Qdrant comes into play, as it might be used as a long-term memory layer.**

CrewAI provides a rich set of tools integrated into the framework. That may be a huge advantage for those who want to
combine RAG with e.g. code execution, or image generation. The ecosystem is rich, however brining your own tools is
not a big deal, as CrewAI is designed to be extensible.

A simple agentic RAG application implemented in CrewAI could look like this:

```python
from crewai import Crew, Agent, Task
from crewai.memory.entity.entity_memory import EntityMemory
from crewai.memory.short_term.short_term_memory import ShortTermMemory
from crewai.memory.storage.rag_storage import RAGStorage

class QdrantStorage(RAGStorage):
    ...

response_generator_agent = Agent(
    role="Generate response based on the conversation",
    goal="Provide the best response, or admit when the response is not available.",
    backstory=(
        "I am a response generator agent. I generate "
        "responses based on the conversation."
    ),
    verbose=True,
)

query_reformulation_agent = Agent(
    role="Reformulate the query",
    goal="Rewrite the query to get better results. Fix typos, grammar, word choice, etc.",
    backstory=(
        "I am a query reformulation agent. I reformulate the "
        "query to get better results."
    ),
    verbose=True,
)

task = Task(
    description="Let me know why Qdrant is the best vector database out there.",
    expected_output="3 bullet points",
    agent=response_generator_agent,
)

crew = Crew(
    agents=[response_generator_agent, query_reformulation_agent],
    tasks=[task],
    memory=True,
    entity_memory=EntityMemory(storage=QdrantStorage("entity")),
    short_term_memory=ShortTermMemory(storage=QdrantStorage("short-term")),
)
crew.kickoff()

```

_Disclaimer: QdrantStorage is not a part of the CrewAI framework, but it’s taken from the Qdrant documentation on [how\_\
_to integrate Qdrant with CrewAI](https://qdrant.tech/documentation/frameworks/crewai/)._

Although it’s not a technical advantage, CrewAI has a [great documentation](https://docs.crewai.com/introduction). The
framework is available for Python, and it’s easy to get started with it. CrewAI also has a commercial offering, CrewAI
Enterprise, which provides a platform for building and deploying agents at scale.

### [Anchor](https://qdrant.tech/articles/agentic-rag/\#autogen) AutoGen

AutoGen emphasizes multi-agent architectures as a fundamental design principle. The framework requires at least two
agents in any system to really call an application agentic - typically an assistant and a user proxy exchange messages
to achieve a common goal. Sequential chat with more than two agents is also supported, as well as group chat and nested
chat for internal dialogue. However, AutoGen does not assume there is a structured state that is passed between the
agents, and the chat conversation is the only way to communicate between them.

There are many interesting concepts in the framework, some of them even quite unique:

- **Tools/functions** \- external components that can be used by agents to communicate with the outside world. They are
defined as Python callables, and can be used for any external interaction we want to allow the agent to do. Type
annotations are used to define the input and output of the tools, and Pydantic models are supported for more complex
type schema. AutoGen supports only OpenAI-compatible tool call API for the time being.
- **Code executors** \- built-in code executors include local command, Docker command, and Jupyter. An agent can write
and launch code, so theoretically the agents can do anything that can be done in Python. None of the other frameworks
made code generation and execution that prominent. Code execution being the first-class citizen in AutoGen is an
interesting concept.

Each AutoGen agent uses at least one of the components: human-in-the-loop, code executor, tool executor, or LLM.
A simple agentic RAG, based on the conversation of two agents which can retrieve documents from a vector database,
or improve the query, could look like this:

```python
from os import environ

from autogen import ConversableAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from qdrant_client import QdrantClient

client = QdrantClient(...)

response_generator_agent = ConversableAgent(
    name="response_generator_agent",
    system_message=(
        "You answer user questions based solely on the provided context. You ask to retrieve relevant documents for "
        "your query, or reformulate the query, if it is incorrect in some way."
    ),
    description="A response generator agent that can answer your queries.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",
)

user_proxy = RetrieveUserProxyAgent(
    name="retrieval_user",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": environ.get("OPENAI_API_KEY")}]},
    human_input_mode="NEVER",
    retrieve_config={
        "task": "qa",
        "chunk_token_size": 2000,
        "vector_db": "qdrant",
        "db_config": {"client": client},
        "get_or_create": True,
        "overwrite": True,
    },
)

result = user_proxy.initiate_chat(
    response_generator_agent,
    message=user_proxy.message_generator,
    problem="Why Qdrant is the best vector database out there?",
    max_turns=10,
)

```

For those new to agent development, AutoGen offers AutoGen Studio, a low-code interface for prototyping agents. While
not intended for production use, it significantly lowers the barrier to entry for experimenting with agent
architectures.

![AutoGen Studio](https://qdrant.tech/articles_data/agentic-rag/autogen-studio.png)

It’s worth noting that AutoGen is currently undergoing significant updates, with version 0.4.x in development
introducing substantial API changes compared to the stable 0.2.x release. While the framework currently has limited
built-in persistence and state management capabilities, these features may evolve in future releases.

### [Anchor](https://qdrant.tech/articles/agentic-rag/\#openai-swarm) OpenAI Swarm

Unliked the other frameworks described in this article, OpenAI Swarm is an educational project, and it’s not ready for
production use. It’s worth mentioning, though, as it’s pretty lightweight and easy to get started with. OpenAI Swarm
is an experimental framework for orchestrating multi-agent workflows that focuses on agent coordination through direct
handoffs rather than complex orchestration patterns.

With that setup, **agents** are just exchanging messages in a chat, optionally calling some Python functions to
communicate with external services, or handing off the conversation to another agent, if the other one seems to be more
suitable to answer the question. Each agent has a certain role, defined by the instructions we have to define.
We have to decide which LLM will a particular agent use, and a set of functions it can call. For example, **a retrieval**
**agent could use a vector database to retrieve documents**, and return the results to the next agent. That means, there
should be a function that performs the semantic search on its behalf, but the model will decide how the query should
look like.

Here is how a similar agentic RAG application, implemented in OpenAI Swarm, could look like:

```python
from swarm import Swarm, Agent

client = Swarm()

def retrieve_documents(query: str) -> list[str]:
    """
    Retrieve documents based on the query.
    """
    ...

def transfer_to_query_improve_agent():
    return query_improve_agent

query_improve_agent = Agent(
    name="Query Improve Agent",
    instructions=(
        "You are a search expert that takes user queries and improves them to get better results. You fix typos and "
        "extend queries with synonyms, if needed. You never ask the user for more information."
    ),
)

response_generation_agent = Agent(
    name="Response Generation Agent",
    instructions=(
        "You take the whole conversation and generate a final response based on the chat history. "
        "If you don't have enough information, you can retrieve the documents from the knowledge base or "
        "reformulate the query by transferring to other agent. You never ask the user for more information. "
        "You have to always be the last participant of each conversation."
    ),
    functions=[retrieve_documents, transfer_to_query_improve_agent],
)

response = client.run(
    agent=response_generation_agent,
    messages=[\
        {\
            "role": "user",\
            "content": "Why Qdrant is the best vector database out there?"\
        }\
    ],
)

```

Even though we don’t explicitly define the graph of processing, the agents can still decide to hand off the processing
to a different agent. There is no concept of a state, so everything relies on the messages exchanged between different
components.

OpenAI Swarm does not focus on integration with external tools, and **if you would like to integrate semantic search**
**with Qdrant, you would have to implement it fully yourself**. Obviously, the library is tightly coupled with OpenAI
models, and while using some other ones is possible, it requires some additional work like setting up proxy that will
adjust the interface to OpenAI API.

### [Anchor](https://qdrant.tech/articles/agentic-rag/\#the-winner) The winner?

Choosing the best framework for your agentic RAG system depends on your existing stack, team expertise, and the
specific requirements of your project. All the described tools are strong contenders, and they are developed at rapid
pace. It’s worth keeping an eye on all of them, as they are likely to evolve and improve over time. Eventually, you
should be able to build the same processes with any of them, but some of them may be more suitable in a specific
ecosystem of the tools you want your agent to interact with.

There are, however, some important factors to consider when choosing a framework for your agentic RAG system:

- **Human-in-the-loop** \- even though we aim to build autonomous agents, it’s often important to include the feedback
from the human, so our agents cannot perform malicious actions.
- **Observability** \- how easy it is to debug the system, and how easy it is to understand what’s happening inside.
Especially important, since we are dealing with lots of LLM prompts.

Still, choosing the right toolkit depends on the state of your project, and the specific requirements you have. If you
want to integrate your agent with number of external tools, CrewAI might be the best choice, as the set of
out-of-the-box integrations is the biggest. However, LangGraph integrates well with LangChain, so if you are familiar
with that ecosystem, it may suit you better.

All the frameworks have different approaches to building agents, so it’s worth experimenting with all of them to see
which one fits your needs the best. LangGraph and CrewAI are more mature and have more features, while AutoGen and
OpenAI Swarm are more lightweight and more experimental. However, **none of the existing frameworks solves all the**
**mentioned Information Retrieval problems**, so you still have to build your own tools to fill the gaps.

## [Anchor](https://qdrant.tech/articles/agentic-rag/\#building-agentic-rag-with-qdrant) Building Agentic RAG with Qdrant

No matter which framework you choose, Qdrant is a great tool to build agentic RAG systems. Please check out [our\\
integrations](https://qdrant.tech/documentation/frameworks/) to choose the best one for your use case and preferences. The easiest way to
start using Qdrant is to use our managed service, [Qdrant Cloud](https://cloud.qdrant.io/). A free 1GB cluster is
available for free, so you can start building your agentic RAG system in minutes.

### [Anchor](https://qdrant.tech/articles/agentic-rag/\#further-reading) Further Reading

See how Qdrant integrates with:

- [Autogen](https://qdrant.tech/documentation/frameworks/autogen/)
- [CrewAI](https://qdrant.tech/documentation/frameworks/crewai/)
- [LangGraph](https://qdrant.tech/documentation/frameworks/langgraph/)
- [Swarm](https://qdrant.tech/documentation/frameworks/swarm/)

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/agentic-rag.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/agentic-rag.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

![Company Logo](https://cdn.cookielaw.org/logos/static/ot_company_logo.png)

## Privacy Preference Center

Cookies used on the site are categorized, and below, you can read about each category and allow or deny some or all of them. When categories that have been previously allowed are disabled, all cookies assigned to that category will be removed from your browser.
Additionally, you can see a list of cookies assigned to each category and detailed information in the cookie declaration.


[More information](https://qdrant.tech/legal/privacy-policy/#cookies-and-web-beacons)

Allow All

### Manage Consent Preferences

#### Targeting Cookies

Targeting Cookies

These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.

#### Functional Cookies

Functional Cookies

These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.

#### Strictly Necessary Cookies

Always Active

These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.

#### Performance Cookies

Performance Cookies

These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.

Back Button

### Cookie List

Search Icon

Filter Icon

Clear

checkbox labellabel

ApplyCancel

ConsentLeg.Interest

checkbox labellabel

checkbox labellabel

checkbox labellabel

Reject AllConfirm My Choices

[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

<|page-145-lllmstxt|>
## database-tutorials
- [Documentation](https://qdrant.tech/documentation/)
- Using the Database