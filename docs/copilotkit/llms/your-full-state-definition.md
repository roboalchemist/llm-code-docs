# ... your full state definition

def chat_node(state: AgentState, config: RunnableConfig):

  state["approval"] = interrupt({ "type": "approval", "content": "please approve" })

  if not state.get("agent_name"):
    # Interrupt and wait for the user to respond with a name
    state["agent_name"] = interrupt({ "type": "ask", "content": "Before we start, what would you like to call me?" })

  # Tell the agent its name
  system_message = SystemMessage(
    content=f"You are a helpful assistant..."
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

### [Add multiple frontend handlers](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#add-multiple-frontend-handlers)

With the differentiator in mind, we will add a handler that takes care of any "ask" and any "approve" types.
With two `useLangGraphInterrupt` hooks in our page, we can leverage the `enabled` property to enable each in the right time:

app/page.tsx

```
import { useLangGraphInterrupt } from "@copilotkit/react-core";
// ...

const ApproveComponent = ({ content, onAnswer }: { content: string; onAnswer: (approved: boolean) => void }) => (
    // styles omitted for brevity
    <div>
        <h1>Do you approve?</h1>
        <button onClick={() => onAnswer(true)}>Approve</button>
        <button onClick={() => onAnswer(false)}>Reject</button>
    </div>
)

const AskComponent = ({ question, onAnswer }: { question: string; onAnswer: (answer: string) => void }) => (
// styles omitted for brevity
    <div>
        <p>{question}</p>
        <form onSubmit={(e) => {
            e.preventDefault();
            onAnswer((e.target as HTMLFormElement).response.value);
        }}>
            <input type="text" name="response" placeholder="Enter your response" />
            <button type="submit">Submit</button>
        </form>
    </div>
)

const YourMainContent = () => {
    // ...

    useLangGraphInterrupt({
        enabled: ({ eventValue }) => eventValue.type === 'ask',
        render: ({ event, resolve }) => (
            <AskComponent question={event.value.content} onAnswer={answer => resolve(answer)} />
        )
    });

    useLangGraphInterrupt({
        enabled: ({ eventValue }) => eventValue.type === 'approval',
        render: ({ event, resolve }) => (
            <ApproveComponent content={event.value.content} onAnswer={answer => resolve(answer)} />
        )
    });

    // ...
}
```

## [Preprocessing of an interrupt and programmatically handling an interrupt value](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#preprocessing-of-an-interrupt-and-programmatically-handling-an-interrupt-value)

When opting for custom chat UI, some cases may require pre-processing of the incoming values of interrupt event or even resolving it entirely without showing a UI for it.
This can be achieved using the `handler` property, which is not required to return a React component.

The return value of the handler will be passed to the `render` method as the `result` argument.

app/page.tsx

```
// We will assume an interrupt event in the following shape
type Department = 'finance' | 'engineering' | 'admin'
interface AuthorizationInterruptEvent {
    type: 'auth',
    accessDepartment: Department,
}

import { useLangGraphInterrupt } from "@copilotkit/react-core";

const YourMainContent = () => {
    const [userEmail, setUserEmail] = useState({ email: 'example@user.com' })
    function getUserByEmail(email: string): { id: string; department: Department } {
        // ... an implementation of user fetching
    }

    // ...
    // styles omitted for brevity

    useLangGraphInterrupt({
        handler: async ({ result, event, resolve }) => {
            const { department } = await getUserByEmail(userEmail)
            if (event.value.accessDepartment === department || department === 'admin') {
                // Following the resolution of the event, we will not proceed to the render method
                resolve({ code: 'AUTH_BY_DEPARTMENT' })
                return;
            }

            return { department, userId }
        },
        render: ({ result, event, resolve }) => (
            <div>
                <h1>Request for {event.value.type}</h1>
                <p>Members from {result.department} department cannot access this information</p>
                <p>You can request access from an administrator to continue.</p>
                <button
                    onClick={() => resolve({ code: 'REQUEST_AUTH', data: { department: result.department, userId: result.userId } })}
                >
                    Request Access
                </button>
                <button
                    onClick={() => resolve({ code: 'CANCEL' })}
                >
                    Cancel
                </button>
            </div>
        )
    });
    // ...

    return <div>{/* ... */}</div>
}
```

[Previous\\
\\
Human in the Loop (HITL)](https://docs.copilotkit.ai/coagents/human-in-the-loop) [Next\\
\\
Node-based](https://docs.copilotkit.ai/coagents/human-in-the-loop/node-flow)

### On this page

[What is this?](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#what-is-this) [When should I use this?](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#when-should-i-use-this) [Implementation](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#implementation) [Run and connect your agent](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#run-and-connect-your-agent) [Install the CopilotKit SDK](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#install-the-copilotkit-sdk) [Setup your agent state](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#setup-your-agent-state) [Call interrupt in your LangGraph agent](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#call-interrupt-in-your-langgraph-agent) [Handle the interrupt in your frontend](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#handle-the-interrupt-in-your-frontend) [Call copilotkit\_interrupt in your LangGraph agent](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#call-copilotkit_interrupt-in-your-langgraph-agent) [Give it a try!](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#give-it-a-try) [Make your agent aware of interruptions](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#make-your-agent-aware-of-interruptions) [Condition UI executions](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#condition-ui-executions) [Define multiple interrupts](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#define-multiple-interrupts) [Add multiple frontend handlers](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#add-multiple-frontend-handlers) [Preprocessing of an interrupt and programmatically handling an interrupt value](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#preprocessing-of-an-interrupt-and-programmatically-handling-an-interrupt-value)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/human-in-the-loop/interrupt-flow.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Writing Agent State
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?

[Shared State](https://docs.copilotkit.ai/coagents/shared-state)