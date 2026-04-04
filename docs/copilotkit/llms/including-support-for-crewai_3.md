# including support for crewai
poetry add copilotkit[crewai]
```

### [Add a `useCopilotAction` to your Frontend](https://docs.copilotkit.ai/coagents/human-in-the-loop/node-flow\#add-a-usecopilotaction-to-your-frontend)

First, we'll create a component that renders the agent's essay draft and waits for user approval.

ui/app/page.tsx

```
import { useCopilotAction } from "@copilotkit/react-core"
import { Markdown } from "@copilotkit/react-ui"

function YourMainContent() {
  // ...

  useCopilotAction({
    name: "writeEssay",
    available: "remote",
    description: "Writes an essay and takes the draft as an argument.",
    parameters: [\
      { name: "draft", type: "string", description: "The draft of the essay", required: true },\
    ],

    renderAndWaitForResponse: ({ args, respond, status }) => {
      return (
        <div>
          <Markdown content={args.draft || 'Preparing your draft...'} />

          <div className={`flex gap-4 pt-4 ${status !== "executing" ? "hidden" : ""}`}>
            <button
              onClick={() => respond?.("CANCEL")}
              disabled={status !== "executing"}
              className="border p-2 rounded-xl w-full"
            >
              Try Again
            </button>
            <button
              onClick={() => respond?.("SEND")}
              disabled={status !== "executing"}
              className="bg-blue-500 text-white p-2 rounded-xl w-full"
            >
              Approve Draft
            </button>
          </div>
        </div>
      );
    },
  });

  // ...
}
```

### [Setup the LangGraph Agent](https://docs.copilotkit.ai/coagents/human-in-the-loop/node-flow\#setup-the-langgraph-agent)

Now we'll setup the LangGraph agent. Node-based flows are hard to understand without a complete example, so below
is the complete implementation of the agent with explanations.

Some main things to note:

- The agent's state inherits from `CopilotKitState` to bring in the CopilotKit actions.
- CopilotKit's actions are binded to the model as tools.
- If the `writeEssay` action is found in the model's response, the agent will transition to the `user_feedback_node`.
- The agent is interrupted before the `user_feedback_node` to allow for user input.

PythonTypeScript

agent/sample\_agent/agent.py

```
from typing_extensions import Literal
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command
from copilotkit import CopilotKitState