# Source: https://dev.writer.com/agent-builder/agent-architecture.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Understand agent architecture

> Understand how Agent Builder agents work. Learn about UI components, blueprints, state management, and how they connect to create functional agents.

<iframe className="w-full aspect-video rounded-xl" src="https://fast.wistia.com/embed/iframe/28xiogdl3c?version=v1x&playerColor=aae3d8" title="Your Video Title" frameBorder="0" allow="autoplay; fullscreen" allowFullScreen />

An Agent Builder agent consists of a UI, which is the agent's interface, and a blueprint, which is the agent's logic. The UI and blueprint are connected through the agent's state and UI triggers.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=35154169be3557ced366471ee8d79f1c" alt="Agent blueprint showing the relationship between UI, blueprint, and state" data-og-width="3992" width="3992" data-og-height="1108" height="1108" data-path="images/agent-builder/demo-agent-architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=a71d0176610fd21adec609d68a202725 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=7507b00a3e821ca78b9f3914a50d00a8 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d9cdc46a4e60a9f4eab76620fe33d647 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4c2c8100345ef45ccfd25e972c3bee04 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d20b310c2216ff7eacb0275b018ae977 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/demo-agent-architecture.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=592487bd21fedcd005afea4d51651446 2500w" />

## Agent components

An agent consists of the following components:

* **UI**: the interface that users interact with.
  * UIs are designed using elements like input fields, buttons, and embeds, including support for guided workflows with pagination.
  * They give users a structured, intuitive way to engage with agents, from simple chat interfaces to rich, interactive tools.
  * The UI is optional. If you do not need to receive user input or display output, you can build an agent without a UI by only using the blueprint.
* **Blueprint**: a visual map of the agent's business logic and behavior.
  * Blueprints are created using a library of configurable blocks for tool calling, built-in RAG, text generation, classification, state management, and more.
  * They define how the agent processes input, makes decisions, and takes action—enabling it to reliably orchestrate work across people, data, systems, and even other agents built in Writer.

An agent can also include:

* Custom Python code to extend its capabilities with more complex logic.
* [Secrets](/agent-builder/secrets) to store sensitive information like API keys, passwords, and other credentials and use them in your agent.

Check out the [demo agent walkthrough](/agent-builder/demo-agent) to see how these components work together in practice.

### Connecting components

Agents work by passing data between the UI and blueprint. The following variables are available to each block in the blueprint:

* `@{result}`: Access the output from the previous block in your blueprint
* `@{payload}`: Access data from UI interactions that triggered the blueprint, like button clicks or user messages
* `@{state_variable}`: Access values stored in your agent's state
* `@{vault.secret_name}`: Access secrets stored in your agent's secrets

These variables let you chain blocks together and create dynamic workflows. Learn more in [Using Data from Previous Blocks](/agent-builder/execution-environment).

### Key capabilities

Agent Builder enables agentic workflows with automation and intelligence by providing the following capabilities:

* **Control Flow**: Blueprints support control structures including:
  * Conditional branching based on input analysis or state conditions
  * Iterative loops for processing collections of data or retrying operations
  * Decision trees that route execution based on classification results or business rules
* **Memory**: Agents can use state, environment variables, and Knowledge Graphs to store and retrieve information across blocks and across agent sessions.
* **Knowledge Graph Integration**: Writer's Knowledge Graph provides:
  * Contextual information that enhances agent responses and decision making
  * Semantic search and content discovery
  * Data storage and retrieval across agent sessions
* **Tool calling**: Agents can dynamically analyze requests and intelligently orchestrate external tools, supporting advanced reasoning patterns like ReAct for step-by-step problem solving.
* **Multi-agent workflows**: Built-in blocks enable integration with other Writer agents for complex multi-agent workflows.

### Agent state

Agents use the agent's state to communicate information across components. The state is a shared memory for each part of the agent: the UI, blueprint, and custom Python code can all read and write data to the state.

Learn more in [Agent state](/agent-builder/state).

## Blueprint-only agents

If you don't need to receive user input or display output, you can build an agent without a UI by only using the blueprint.

To run the blueprint without a UI Trigger, press the **Run blueprint** button in the top right of the blueprint.

<img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/run-blueprint.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=a3f0120c9a4ab04b4ce5f8b7355eed47" alt="" data-og-width="412" width="412" data-og-height="128" height="128" data-path="images/agent-builder/run-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/run-blueprint.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=0af3e3bc9625efd98a86ba672ddfd8cd 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/run-blueprint.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f82ce16103e20ec9d41a83483e47b084 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/run-blueprint.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=70b6d779516643fe8c6fb7339f1c86c0 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/run-blueprint.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=800e63b93ad904785768cbba76410f7d 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/run-blueprint.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=ed7eaa9a94342c926866666a93013a06 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/run-blueprint.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=f96d3251f8efa113d19bd0bc8578b108 2500w" />

<feedback />
