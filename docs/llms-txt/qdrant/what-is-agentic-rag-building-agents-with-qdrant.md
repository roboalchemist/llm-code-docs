# What is Agentic RAG? Building Agents with Qdrant

Kacper Łukawski

·

November 22, 2024

![What is Agentic RAG? Building Agents with Qdrant](https://qdrant.tech/articles_data/agentic-rag/preview/title.jpg)

Standard [Retrieval Augmented Generation](https://qdrant.tech/articles/what-is-rag-in-ai/) follows a predictable, linear path: receive
a query, retrieve relevant documents, and generate a response. In many cases that might be enough to solve a particular
problem. In the worst case scenario, your LLM will just decide to not answer the question, because the context does not
provide enough information.

![Standard, linear RAG pipeline](https://qdrant.tech/articles_data/agentic-rag/linear-rag.png)

On the other hand, we have agents. These systems are given more freedom to act, and can take multiple non-linear steps
to achieve a certain goal. There isn’t a single definition of what an agent is, but in general, it is an application
that uses LLM and usually some tools to communicate with the outside world. LLMs are used as decision-makers which
decide what action to take next. Actions can be anything, but they are usually well-defined and limited to a certain
set of possibilities. One of these actions might be to query a vector database, like Qdrant, to retrieve relevant
documents, if the context is not enough to make a decision. However, RAG is just a single tool in the agent’s arsenal.

![AI Agent](https://qdrant.tech/articles_data/agentic-rag/ai-agent.png)

## [Anchor](https://qdrant.tech/articles/agentic-rag/\#agentic-rag-combining-rag-with-agents) Agentic RAG: Combining RAG with Agents

Since the agent definition is vague, the concept of **Agentic RAG** is also not well-defined. In general, it refers to
the combination of RAG with agents. This allows the agent to use external knowledge sources to make decisions, and
primarily to decide when the external knowledge is needed. We can describe a system as Agentic RAG if it breaks the
linear flow of a standard RAG system, and gives the agent the ability to take multiple steps to achieve a goal.

A simple router that chooses a path to follow is often described as the simplest form of an agent. Such a system has
multiple paths with conditions describing when to take a certain path. In the context of Agentic RAG, the agent can
decide to query a vector database if the context is not enough to answer, or skip the query if it’s enough, or when the
question refers to common knowledge. Alternatively, there might be multiple collections storing different kinds of
information, and the agent can decide which collection to query based on the context. The key factor is that the
decision of choosing a path is made by the LLM, which is the core of the agent. A routing agent never comes back to the
previous step, so it’s ultimately just a conditional decision-making system.

![Routing Agent](https://qdrant.tech/articles_data/agentic-rag/routing-agent.png)

However, routing is just the beginning. Agents can be much more complex, and extreme forms of agents can have complete
freedom to act. In such cases, the agent is given a set of tools and can autonomously decide which ones to use, how to
use them, and in which order. LLMs are asked to plan and execute actions, and the agent can take multiple steps to
achieve a goal, including taking steps back if needed. Such a system does not have to follow a DAG structure (Directed
Acyclic Graph), and can have loops that help to self-correct the decisions made in the past. An agentic RAG system
built in that manner can have tools not only to query a vector database, but also to play with the query, summarize the
results, or even generate new data to answer the question. Options are endless, but there are some common patterns
that can be observed in the wild.

![Autonomous Agent](https://qdrant.tech/articles_data/agentic-rag/autonomous-agent.png)

### [Anchor](https://qdrant.tech/articles/agentic-rag/\#solving-information-retrieval-problems-with-llms) Solving Information Retrieval Problems with LLMs

Generally speaking, tools exposed in an agentic RAG system are used to solve information retrieval problems which are
not new to the search community. LLMs have changed how we approach these problems, but the core of the problem remains
the same. What kind of tools you can consider using in an agentic RAG? Here are some examples:

- **Querying a vector database** \- the most common tool used in agentic RAG systems. It allows the agent to retrieve
relevant documents based on the query.
- **Query expansion** \- a tool that can be used to improve the query. It can be used to add synonyms, correct typos, or
even to generate new queries based on the original one.
![Query expansion example](https://qdrant.tech/articles_data/agentic-rag/query-expansion.png)
- **Extracting filters** \- vector search alone is sometimes not enough. In many cases, you might want to narrow down
the results based on specific parameters. This extraction process can automatically identify relevant conditions from
the query. Otherwise, your users would have to manually define these search constraints.
![Extracting filters](https://qdrant.tech/articles_data/agentic-rag/extracting-filters.png)
- **Quality judgement** \- knowing the quality of the results for given query can be used to decide whether they are good
enough to answer, or if the agent should take another step to improve them somehow. Alternatively it can also admit
the failure to provide good response.
![Quality judgement](https://qdrant.tech/articles_data/agentic-rag/quality-judgement.png)

These are just some of the examples, but the list is not exhaustive. For example, your LLM could possibly play with
Qdrant search parameters or choose different methods to query it. An example? If your users are searching using some
specific keywords, you may prefer sparse vectors to dense vectors, as they are more efficient in such cases. In that
case you have to arm your agent with tools to decide when to use sparse vectors and when to use dense vectors. Agent
aware of the collection structure can make such decisions easily.

Each of these tools might be a separate agent on its own, and multi-agent systems are not uncommon. In such cases,
agents can communicate with each other, and one agent can decide to use another agent to solve a particular problem.
Pretty useful component of an agentic RAG is also a human in the loop, which can be used to correct the agent’s
decisions, or steer it in the right direction.

## [Anchor](https://qdrant.tech/articles/agentic-rag/\#where-are-agents-used) Where are Agents Used?

Agents are an interesting concept, but since they heavily rely on LLMs, they are not applicable to all problems. Using
Large Language Models is expensive and tend to be slow, what in many cases, it’s not worth the cost. Standard RAG
involves just a single call to the LLM, and the response is generated in a predictable way. Agents, on the other hand,
can take multiple steps, and the latency experienced by the user adds up. In many cases, it’s not acceptable.
Agentic RAG is probably not that widely applicable in ecommerce search, where the user expects a quick response, but
might be fine for customer support, where the user is willing to wait a bit longer for a better answer.

## [Anchor](https://qdrant.tech/articles/agentic-rag/\#which-framework-is-best) Which Framework is Best?

There are lots of frameworks available to build agents, and choosing the best one is not easy. It depends on your
existing stack or the tools you are familiar with. Some of the most popular LLM libraries have already drifted towards
the agent paradigm, and they are offering tools to build them. There are, however, some tools built primarily for
agents development, so let’s focus on them.

### [Anchor](https://qdrant.tech/articles/agentic-rag/\#langgraph) LangGraph

Developed by the LangChain team, LangGraph seems like a natural extension for those who already use LangChain for
building their RAG systems, and would like to start with agentic RAG.

Surprisingly, LangGraph has nothing to do with Large Language Models on its own. It’s a framework for building
graph-based applications in which each **node** is a step of the workflow. Each node takes an application **state** as
an input, and produces a modified state as an output. The state is then passed to the next node, and so on. **Edges**
between the nodes might be conditional what makes branching possible. Contrary to some DAG-based tool (i.e. Apache
Airflow), LangGraph allows for loops in the graph, which makes it possible to implement cyclic workflows, so an agent
can achieve self-reflection and self-correction. Theoretically, LangGraph can be used to build any kind of applications
in a graph-based manner, not only LLM agents.

Some of the strengths of LangGraph include:

- **Persistence** \- the state of the workflow graph is stored as a checkpoint. That happens at each so-called super-step
(which is a single sequential node of a graph). It enables replying certain steps of the workflow, fault-tolerance,
and including human-in-the-loop interactions. This mechanism also acts as a **short-term memory**, accessible in a
context of a particular workflow execution.
- **Long-term memory** \- LangGraph also has a concept of memories that are shared between different workflow runs.
However, this mechanism has to explicitly handled by our nodes. **Qdrant with its semantic search capabilities is**
**often used as a long-term memory layer**.
- **Multi-agent support** \- while there is no separate concept of multi-agent systems in LangGraph, it’s possible to
create such an architecture by building a graph that includes multiple agents and some kind of supervisor that
makes a decision which agent to use in a given situation. If a node might be anything, then it might be another agent
as well.

Some other interesting features of LangGraph include the ability to visualize the graph, automate the retries of failed
steps, and include human-in-the-loop interactions.

A minimal example of an agentic RAG could improve the user query, e.g. by fixing typos, expanding it with synonyms, or
even generating a new query based on the original one. The agent could then retrieve documents from a vector database
based on the improved query, and generate a response. The LangGraph app implementing this approach could look like this:

```python
from typing import Sequence
from typing_extensions import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langgraph.constants import START, END
from langgraph.graph import add_messages, StateGraph

class AgentState(TypedDict):
    # The state of the agent includes at least the messages exchanged between the agent(s)
    # and the user. It is, however, possible to include other information in the state, as
    # it depends on the specific agent.
    messages: Annotated[Sequence[BaseMessage], add_messages]

def improve_query(state: AgentState):
    ...

def retrieve_documents(state: AgentState):
    ...

def generate_response(state: AgentState):
    ...