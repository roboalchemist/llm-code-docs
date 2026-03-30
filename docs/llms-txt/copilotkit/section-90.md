# ...
async def chat_node(state: AgentState, config: RunnableConfig) -> Command[Literal["cpk_action_node", "tool_node", "__end__"]]:
    # ...

    # Simulate executing steps one by one
    steps = [\
        "Analyzing input data...",\
        "Identifying key patterns...",\
        "Generating recommendations...",\
        "Formatting final output..."\
    ]

    for step in steps:
        self.state["observed_steps"] = self.state.get("observed_steps", []) + [step]
        await copilotkit_emit_state(config, state)
        await asyncio.sleep(1)

    # ...
```

### [Observe the predictions](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates\#observe-the-predictions)

These predictions will be emitted as the agent runs, allowing you to track its progress before the final state is determined.

ui/app/page.tsx

```
import { useCoAgent, useCoAgentStateRender } from '@copilotkit/react-core';

// ...
type AgentState = {
    observed_steps: string[];
};

const YourMainContent = () => {
    // Get access to both predicted and final states
    const { state } = useCoAgent<AgentState>({ name: "sample_agent" });

    // Add a state renderer to observe predictions
    useCoAgentStateRender({
        name: "sample_agent",
        render: ({ state }) => {
            if (!state.observed_steps?.length) return null;
            return (
                <div>
                    <h3>Current Progress:</h3>
                    <ul>
                        {state.observed_steps.map((step, i) => (
                            <li key={i}>{step}</li>
                        ))}
                    </ul>
                </div>
            );
        },
    });

    return (
        <div>
            <h1>Agent Progress</h1>
            {state.observed_steps?.length > 0 && (
                <div>
                    <h3>Final Steps:</h3>
                    <ul>
                        {state.observed_steps.map((step, i) => (
                            <li key={i}>{step}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    )
}
```

### [Give it a try!](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates\#give-it-a-try)

Now you'll notice that the state predictions are emitted as the agent makes progress, giving you insight into its work before the final state is determined.
You can apply this pattern to any long-running task in your agent.

[Previous\\
\\
Agent state inputs and outputs](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution) [Next\\
\\
Frontend Actions](https://docs.copilotkit.ai/coagents/frontend-actions)

### On this page

[What is this?](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates#what-is-this) [When should I use this?](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates#when-should-i-use-this) [Important Note](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates#important-note) [Implementation](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates#implementation) [Install the CopilotKit SDK](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates#install-the-copilotkit-sdk) [Define the state](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates#define-the-state) [Emit the intermediate state](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates#emit-the-intermediate-state) [Observe the predictions](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates#observe-the-predictions) [Give it a try!](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates#give-it-a-try)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/shared-state/predictive-state-updates.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## CopilotKit Migration Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this page