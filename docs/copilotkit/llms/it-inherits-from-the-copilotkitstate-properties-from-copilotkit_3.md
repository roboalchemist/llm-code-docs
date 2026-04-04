# It inherits from the CopilotKitState properties from CopilotKit.
class AgentState(CopilotKitState):
    agent_name: str
```

Choose how to display the interrupt to the user

As a Custom Chat UI

I'd like to display a custom UI in the chat window

As Message

I'd like to display the interrupt as a copilot message

### [Call `interrupt` in your LangGraph agent](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#call-interrupt-in-your-langgraph-agent)

Now we can call `interrupt` in our LangGraph agent.

Your agent will not be aware of the `interrupt` interaction by default in LangGraph.

If you want this behavior, see the [section on it below](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow#make-your-agent-aware-of-interruptions).

PythonTypeScript

agent/sample\_agent/agent.py

```
from langgraph.types import interrupt
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from copilotkit import CopilotKitState