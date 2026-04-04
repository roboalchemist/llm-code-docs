# Frontend Actions

Create frontend actions and use them within your agent.

This video shows the [coagents starter](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter) repo with the [implementation](https://docs.copilotkit.ai/coagents/frontend-actions#implementation) section applied to it!

## [What is this?](https://docs.copilotkit.ai/coagents/frontend-actions\#what-is-this)

Frontend actions are powerful tools that allow your AI agents to directly interact with and update your application's user interface. Think of them as bridges that connect your agent's decision-making capabilities with your frontend's interactive elements.

## [When should I use this?](https://docs.copilotkit.ai/coagents/frontend-actions\#when-should-i-use-this)

Frontend actions are essential when you want to create truly interactive AI applications where your agent needs to:

- Dynamically update UI elements
- Trigger frontend animations or transitions
- Show alerts or notifications
- Modify application state
- Handle user interactions programmatically

Without frontend actions, agents are limited to just processing and returning data. By implementing frontend actions, you can create rich, interactive experiences where your agent actively drives the user interface.

## [Implementation](https://docs.copilotkit.ai/coagents/frontend-actions\#implementation)

### [Setup CopilotKit](https://docs.copilotkit.ai/coagents/frontend-actions\#setup-copilotkit)

To use frontend actions, you'll need to setup CopilotKit first. For the sake of brevity, we won't cover it here.

Check out our [getting started guide](https://docs.copilotkit.ai/coagents/quickstart/langgraph) and come back here when you're setup!

### [Create a frontend action](https://docs.copilotkit.ai/coagents/frontend-actions\#create-a-frontend-action)

First, you'll need to create a frontend action using the [useCopilotAction](https://docs.copilotkit.ai/reference/hooks/useCopilotAction) hook. Here's a simple one to get you started
that says hello to the user.

page.tsx

```
import { useCopilotAction } from "@copilotkit/react-core"

export function Page() {
  // ...


  useCopilotAction({
    name: "sayHello",
    description: "Say hello to the user",
    available: "remote", // optional, makes it so the action is *only* available to the agent
    parameters: [\
      {\
        name: "name",\
        type: "string",\
        description: "The name of the user to say hello to",\
        required: true,\
      },\
    ],
    handler: async ({ name }) => {
      alert(`Hello, ${name}!`);
    },
  });

  // ...
}
```

### [Modify your agent](https://docs.copilotkit.ai/coagents/frontend-actions\#modify-your-agent)

Now, we'll need to modify the agent to access these frontend actions. In your terminal, navigate to your agent's folder and continue from there!

### [Install the CopilotKit SDK](https://docs.copilotkit.ai/coagents/frontend-actions\#install-the-copilotkit-sdk)

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic
experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

Poetrypipconda

```
poetry add copilotkit