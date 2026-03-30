# add all the different nodes and edges and compile the graph
builder.add_node("answer_node", answer_node)
builder.add_edge(START, "answer_node")
builder.add_edge("answer_node", END)
graph = builder.compile()
```

### [Give it a try!](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution\#give-it-a-try)

Now that we know which state properties our agent emits, we can inspect the state and expect the following to happen:

- While we are able to provide a question, we will not receive it back from the agent. If we are using it in our UI, we need to remember the UI is the source of truth for it
- Answer will change once it's returned back from the agent
- The UI has no access to resources.

```
import { useCoAgent } from "@copilotkit/react-core";

type AgentState = {
  question: string;
  answer: string;
}

const { state } = useCoAgent<AgentState>({
  name: "sample_agent",
  initialState: {
    question: "How's the weather in SF?",
  }
});

console.log(state) // You can expect seeing "answer" change, while the others are not returned from the agent
```

[Previous\\
\\
Writing agent state](https://docs.copilotkit.ai/coagents/shared-state/in-app-agent-write) [Next\\
\\
Predictive state updates](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates)

### On this page

[What is this?](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution#what-is-this) [When should I use this?](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution#when-should-i-use-this) [Implementation](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution#implementation) [Examine our old state](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution#examine-our-old-state) [Divide state to Input and Output](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution#divide-state-to-input-and-output) [Give it a try!](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution#give-it-a-try)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/shared-state/workflow-execution.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Predictive State Updates
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?

[Shared State](https://docs.copilotkit.ai/coagents/shared-state)