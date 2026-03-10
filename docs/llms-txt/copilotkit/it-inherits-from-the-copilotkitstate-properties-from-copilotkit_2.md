# It inherits from the CopilotKitState properties from CopilotKit.
class AgentState(CopilotKitState):
    searches: list[dict]
```

### [Simulate state updates](https://docs.copilotkit.ai/coagents/generative-ui/agentic\#simulate-state-updates)

Next, let's write some logic into our agent that will simulate state updates occurring.

PythonTypeScript

agent-py/sample\_agent/agent.py

```
import asyncio
from typing import TypedDict
from langchain_core.runnables import RunnableConfig
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from copilotkit import CopilotKitState
from copilotkit.langgraph import copilotkit_emit_state

class Searches(TypedDict):
    query: str
    done: bool

class AgentState(CopilotKitState):
    searches: list[Searches] = []

async def chat_node(state: AgentState, config: RunnableConfig):
    state["searches"] = [\
        {"query": "Initial research", "done": False},\
        {"query": "Retrieving sources", "done": False},\
        {"query": "Forming an answer", "done": False},\
    ]
    await copilotkit_emit_state(config, state)

    # Simulate state updates
    for search in state["searches"]:
        await asyncio.sleep(1)
        search["done"] = True
        await copilotkit_emit_state(config, state)

    # Run the model to generate a response
    response = await ChatOpenAI(model="gpt-4o").ainvoke([\
        SystemMessage(content="You are a helpful assistant."),\
        *state["messages"],\
    ], config)
```

### [Render state of the agent in the chat](https://docs.copilotkit.ai/coagents/generative-ui/agentic\#render-state-of-the-agent-in-the-chat)

Now we can utilize `useCoAgentStateRender` to render the state of our agent **in the chat**.

app/page.tsx

```
// ...
import { useCoAgentStateRender } from "@copilotkit/react-core";
// ...

// Define the state of the agent, should match the state of the agent in your LangGraph.
type AgentState = {
  searches: {
    query: string;
    done: boolean;
  }[];
};

function YourMainContent() {
  // ...


  // styles omitted for brevity
  useCoAgentStateRender<AgentState>({
    name: "sample_agent", // the name the agent is served as
    render: ({ state }) => (
      <div>
        {state.searches?.map((search, index) => (
          <div key={index}>
            {search.done ? "✅" : "❌"} {search.query}{search.done ? "" : "..."}
          </div>
        ))}
      </div>
    ),
  });

  // ...

  return <div>...</div>;
}
```

### [Render state outside of the chat](https://docs.copilotkit.ai/coagents/generative-ui/agentic\#render-state-outside-of-the-chat)

You can also render the state of your agent **outside of the chat**. This is useful when you want to render the state of your agent anywhere
other than the chat.

app/page.tsx

```
import { useCoAgent } from "@copilotkit/react-core";
// ...

// Define the state of the agent, should match the state of the agent in your LangGraph.
type AgentState = {
  searches: {
    query: string;
    done: boolean;
  }[];
};

function YourMainContent() {
  // ...


  const { state } = useCoAgent<AgentState>({
    name: "sample_agent", // the name the agent is served as
  })

  // ...

  return (
    <div>
      {/* ... */}
      <div className="flex flex-col gap-2 mt-4">

        {state.searches?.map((search, index) => (
          <div key={index} className="flex flex-row">
            {search.done ? "✅" : "❌"} {search.query}
          </div>
        ))}
      </div>
    </div>
  )
}
```

### [Give it a try!](https://docs.copilotkit.ai/coagents/generative-ui/agentic\#give-it-a-try)

You've now created a component that will render the agent's state in the chat.

[Previous\\
\\
Generative UI](https://docs.copilotkit.ai/coagents/generative-ui) [Next\\
\\
Tool-based Generative UI](https://docs.copilotkit.ai/coagents/generative-ui/tool-based)

### On this page

[What is this?](https://docs.copilotkit.ai/coagents/generative-ui/agentic#what-is-this) [When should I use this?](https://docs.copilotkit.ai/coagents/generative-ui/agentic#when-should-i-use-this) [Implementation](https://docs.copilotkit.ai/coagents/generative-ui/agentic#implementation) [Run and Connect your LangGraph to CopilotKit](https://docs.copilotkit.ai/coagents/generative-ui/agentic#run-and-connect-your-langgraph-to-copilotkit) [Define your agent state](https://docs.copilotkit.ai/coagents/generative-ui/agentic#define-your-agent-state) [Simulate state updates](https://docs.copilotkit.ai/coagents/generative-ui/agentic#simulate-state-updates) [Render state of the agent in the chat](https://docs.copilotkit.ai/coagents/generative-ui/agentic#render-state-of-the-agent-in-the-chat) [Render state outside of the chat](https://docs.copilotkit.ai/coagents/generative-ui/agentic#render-state-outside-of-the-chat) [Give it a try!](https://docs.copilotkit.ai/coagents/generative-ui/agentic#give-it-a-try)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/generative-ui/agentic.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## TypeScript Backend Actions
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageModify CopilotRuntime to include TypeScript/Node.js actions

[Backend Actions & Agents](https://docs.copilotkit.ai/guides/backend-actions)