# including support for crewai
poetry add copilotkit[crewai]
```

### [Exit the agent loop](https://docs.copilotkit.ai/coagents/advanced/exit-agent\#exit-the-agent-loop)

This will exit the agent session as soon as the current LangGraph run is finished, either by a breakpoint or by reaching the `END` node.

PythonTypeScript

```
from copilotkit.langgraph import (copilotkit_exit)