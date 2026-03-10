# including support for crewai
poetry add copilotkit[crewai]
```

### [Inheriting from CopilotKitState](https://docs.copilotkit.ai/coagents/frontend-actions\#inheriting-from-copilotkitstate)

To access the frontend actions provided by CopilotKit, you can inherit from CopilotKitState in your agent's state definition:

PythonTypeScript

agent-py/sample\_agent/agent.py

```
from copilotkit import CopilotKitState

class YourAgentState(CopilotKitState):
    your_additional_properties: str
```

By doing this, your agent's state will include the `copilotkit` property, which contains the frontend actions that can be accessed and invoked.

### [Accessing Frontend Actions](https://docs.copilotkit.ai/coagents/frontend-actions\#accessing-frontend-actions)

Once your agent's state includes the `copilotkit` property, you can access the frontend actions and utilize them within your agent's logic.

Here's how you can call a frontend action from your agent:

PythonTypeScript

agent-py/sample\_agent/agent.py

```
async def agent_node(state: YourAgentState, config: RunnableConfig):
    # Access the actions from the copilotkit property

    actions = state.get("copilotkit", {}).get("actions", [])
    model = ChatOpenAI(model="gpt-4o").bind_tools(actions)

    # ...
```

These actions are automatically populated by CopilotKit and are compatible with LangChain's tool call definitions, making it straightforward to integrate them into your agent's workflow.

### [Give it a try!](https://docs.copilotkit.ai/coagents/frontend-actions\#give-it-a-try)

You've now given your agent the ability to directly call any CopilotActions you've defined. These actions will be available as tools to the agent where they can be used as needed.

[Previous\\
\\
Predictive state updates](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates) [Next\\
\\
Multi-Agent Flows](https://docs.copilotkit.ai/coagents/multi-agent-flows)

### On this page

[What is this?](https://docs.copilotkit.ai/coagents/frontend-actions#what-is-this) [When should I use this?](https://docs.copilotkit.ai/coagents/frontend-actions#when-should-i-use-this) [Implementation](https://docs.copilotkit.ai/coagents/frontend-actions#implementation) [Setup CopilotKit](https://docs.copilotkit.ai/coagents/frontend-actions#setup-copilotkit) [Create a frontend action](https://docs.copilotkit.ai/coagents/frontend-actions#create-a-frontend-action) [Modify your agent](https://docs.copilotkit.ai/coagents/frontend-actions#modify-your-agent) [Install the CopilotKit SDK](https://docs.copilotkit.ai/coagents/frontend-actions#install-the-copilotkit-sdk) [Inheriting from CopilotKitState](https://docs.copilotkit.ai/coagents/frontend-actions#inheriting-from-copilotkitstate) [Accessing Frontend Actions](https://docs.copilotkit.ai/coagents/frontend-actions#accessing-frontend-actions) [Give it a try!](https://docs.copilotkit.ai/coagents/frontend-actions#give-it-a-try)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/frontend-actions.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Generative UI Overview
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is Generative UI?