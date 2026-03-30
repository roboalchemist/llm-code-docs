# ...
```

## [Condition UI executions](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#condition-ui-executions)

When opting for custom chat UI while having multiple `interrupt` events in the agent, there could be conflicts between multiple `useLangGraphInterrupt` hooks calls in the UI.
For this reason, the hook can take an `enabled` argument which will apply it conditionally:

### [Define multiple interrupts](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#define-multiple-interrupts)

First, let's define two different interrupts. We will include a "type" property to differentiate them.

PythonTypeScript

agent/sample\_agent/agent.py

```
from langgraph.types import interrupt
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI