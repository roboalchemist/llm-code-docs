# add the agent state definition from the previous step
class AgentState(CopilotKitState):
    agent_name: str

def chat_node(state: AgentState, config: RunnableConfig):
    if not state.get("agent_name"):
    # Interrupt and wait for the user to respond with a name
    state["agent_name"] = interrupt("Before we start, what would you like to call me?")

    # Tell the agent its name
    system_message = SystemMessage(
        content=f"You are a helpful assistant named {state.get('agent_name')}..."
    )

    response = ChatOpenAI(model="gpt-4o").invoke(
        [system_message, *state["messages"]],
        config
    )

    return {
        **state,
        "messages": response,
    }
```

### [Handle the interrupt in your frontend](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#handle-the-interrupt-in-your-frontend)

At this point, your LangGraph agent's `interrupt` will be called. However, we currently have no handling for rendering or
responding to the interrupt in the frontend.

To do this, we'll use the `useLangGraphInterrupt` hook, give it a component to render, and then call `resolve` with the user's response.

app/page.tsx

```
import { useLangGraphInterrupt } from "@copilotkit/react-core";
// ...

const YourMainContent = () => {
// ...

// styles omitted for brevity
useLangGraphInterrupt({
    render: ({ event, resolve }) => (
        <div>
            <p>{event.value}</p>
            <form onSubmit={(e) => {
                e.preventDefault();
                resolve((e.target as HTMLFormElement).response.value);
            }}>
                <input type="text" name="response" placeholder="Enter your response" />
                <button type="submit">Submit</button>
            </form>
        </div>
    )
});
// ...

return <div>{/* ... */}</div>
}
```

### [Give it a try!](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#give-it-a-try)

Try talking to your agent, you'll see that it now pauses execution and waits for you to respond!

## [Make your agent aware of interruptions](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#make-your-agent-aware-of-interruptions)

By default, your agent will not be made aware of LangGraph `interrupts`. This is because the decision is not saved into the message's state.
For simple and sensitive flows, this is ideal. However, you may want to make your agent aware of these interactions.

If you've been using the "As Message" implementation, you may have noticed that the messages are returned from the interrupt function.
These can be used to notify the LLM about the recent communication:

PythonTypeScript

agent-py/sample\_agent/agent.py

```
from copilotkit import copilotkit_interrupt