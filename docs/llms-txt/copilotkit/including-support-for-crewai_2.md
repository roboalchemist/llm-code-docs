# including support for crewai
poetry add copilotkit[crewai]
```

### [Define the state](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates\#define-the-state)

We'll be defining a `observed_steps` field in the state, which will be updated as the agent writes different sections of the report.

PythonTypeScript

agent-py/sample\_agent/agent.py

```
from copilotkit import CopilotKitState
from typing import Literal

class AgentState(CopilotKitState):
    observed_steps: list[str]  # Array of completed steps
```

### [Emit the intermediate state](https://docs.copilotkit.ai/coagents/shared-state/predictive-state-updates\#emit-the-intermediate-state)

How would you like to emit state updates?

You can either manually emit state updates or configure specific tool calls to emit updates.

Manual Predictive State Updates

Manually emit state updates for maximum control over when updates occur.

Tool-Based Predictive State Updates

Configure specific tool calls to automatically emit intermediate state updates.

For long-running tasks, you can emit state updates progressively as predictions of the final state. In this example, we simulate a long-running task by executing a series of steps with a one second delay between each update.

PythonTypeScript

agent-py/sample\_agent/agent.py

```
from copilotkit.langgraph import copilotkit_emit_state