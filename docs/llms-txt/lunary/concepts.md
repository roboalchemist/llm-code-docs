# Source: https://docs.lunary.ai/docs/more/concepts.md

# Concepts

Understanding these concepts can be useful for working with Lunary's APIs and SDKs, though they are not required to get started.

<Card title="Run" icon="play">
  Runs are the fundamental units in Lunary. They can represent an LLM request, an agent execution, a tool execution, a workflow, and more. Each run has an input and usually an output.

  You can track the number of runs on the billing page.

  Types of runs include:

  <Card title="LLM Calls" icon="microchip-ai">
    An LLM call refers to a request made to a large language model, such as GPT-4.

    In this context, `input` is the prompt or chat history you send to the model, and `output` is the response you get back.
  </Card>

  <Card title="Chains" icon="link">
    Chains denote sequences of connected runs, tools, and LLM calls.

    They help visualize the flow and dependencies in complex tasks, clarifying the interactions between different components of the system.

    They are useful for creating subtraces and subtrees inside agents.
  </Card>

  <Card title="Agents" icon="robot">
    An agent is usually composed of tools and LLM calls.

    It autonomously interacts with various components and might iterate over tasks until it finds a solution.
  </Card>

  <Card title="Tools" icon="wrench">
    A tool is a piece of code that your AI agent can invoke to perform external actions. A tool usually doesn't make AI queries itself (but it can).

    Examples of tools: Web search, Calculator, Database query, Random number generator

    In the context of a tool, `input` is the arguments you send to the tool, and `output` is the result you get back.
    Note that tools cannot be tracked standalone; they need to be part of an agent or a chain run.
  </Card>

  <Card title="Threads" icon="messages">
    A thread contains multiple `chat` runs and is used to represent a conversation or a chatbot session.

    You don't need to pass any `input` or `output` to a thread. You also don't need to end a thread explicitly.
  </Card>

  <Card title="Chat" icon="message">
    A chat is a run that represents a single interaction user->assistant in a conversation.
  </Card>
</Card>

<Card title="Traces" icon="list-tree">
  A trace is a collection of related runs.

  An agent will generate a trace every time it executes.

  Exploring traces on the dashboard helps you understand how your code is behaving and how the different LLM components are interacting.

  Using our SDKs, runs are automatically organized into traces.
</Card>

<Card title="Users" icon="users">
  A user is someone who uses your app. With all our SDKs, you can identify users.

  Sometimes, you might have multiple levels of users, such as organizations, teams within organizations, and individual users.

  Which to report as user then? It depends on your use case. For example, if you're building a chatbot, you might want to report the end-user as the user. If you're building a tool for a team, you might want to report the team as the user, to be able to track costs and usage grouped by team.

  In any case, you can pass an `organizationId` or `teamId` as metadata to identify those levels of users.

  [Learn more about users](/docs/features/users)
</Card>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt