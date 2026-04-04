# Agent state inputs and outputs

Decide which state properties are received and returned to the frontend

## [What is this?](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution\#what-is-this)

Not all state properties are relevant for frontend-backend sharing.
This guide shows how to ensure only the right portion of state is communicated back and forth.

This guide is based on [LangGraph's Input/Output Schema feature](https://langchain-ai.github.io/langgraph/how-tos/input_output_schema/)

## [When should I use this?](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution\#when-should-i-use-this)

Depending on your implementation, some properties are meant to be processed internally, while some others are the way for the UI to communicate user input.
In addition, some state properties contain a lot of information. Syncing them back and forth between the agent and UI can be costly, while it might not have any practical benefit.

## [Implementation](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution\#implementation)

### [Examine our old state](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution\#examine-our-old-state)

LangGraph is stateful. As you transition between nodes, that state is updated and passed to the next node. For this example,
let's assume that the state our agent should be using, can be described like this:

PythonTypeScript

agent-py/sample\_agent/agent.py

```
from copilotkit import CopilotKitState
from typing import Literal

class AgentState(CopilotKitState):
    question: str
    answer: str
    resources: List[str]
```

### [Divide state to Input and Output](https://docs.copilotkit.ai/coagents/shared-state/workflow-execution\#divide-state-to-input-and-output)

Our example case lists several state properties, which with its own purpose:

- The question is being asked by the user, expecting the llm to answer
- The answer is what the LLM returns
- The resources list will be used by the LLM to answer the question, and should not be communicated to the user, or set by them.

PythonTypeScript

agent-py/sample\_agent/agent.py

```
from copilotkit import CopilotKitState
from typing import Literal