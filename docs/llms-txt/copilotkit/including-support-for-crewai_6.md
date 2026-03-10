# including support for crewai
poetry add copilotkit[crewai]
```

### [Manually emit a message](https://docs.copilotkit.ai/coagents/advanced/emit-messages\#manually-emit-a-message)

The `copilotkit_emit_message` method allows you to emit messages early in a node's execution to communicate status updates to the user. This is particularly useful for long running tasks.

PythonTypeScript

```
from langchain_core.messages import SystemMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableConfig
from copilotkit.langgraph import copilotkit_emit_message