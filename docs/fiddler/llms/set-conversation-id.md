# Source: https://docs.fiddler.ai/api/fiddler-strands-agents-sdk/attributes/set-conversation-id.md

# Source: https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/set-conversation-id.md

# set\_conversation\_id

Enables end-to-end tracing of multi-step workflows and conversations.

The primary purpose of set\_conversation\_id is to enable end-to-end tracing of a multi-step workflow. Modern agentic applications often involve a complex sequence of events to fulfill a single user request. The result in your Fiddler dashboard is that you can instantly filter for and view the entire, ordered sequence of operations that constituted a single conversation or task. This is crucial for debugging complex failures, analyzing latency across an entire workflow, and understanding the agent's behavior from start to finish.

This will remain in use until it is called again with a new conversation ID.

## Parameters

| Parameter         | Type  | Required | Default | Description                                     |
| ----------------- | ----- | -------- | ------- | ----------------------------------------------- |
| `conversation_id` | `str` | ✓        | `-`     | Unique identifier for the conversation session. |

## Returns

None

**Return type:** None

## Examples

```python
from langgraph.prebuilt import create_react_agent
from fiddler_langgraph.tracing.instrumentation import set_conversation_id
import uuid

# Basic usage
agent = create_react_agent(model, tools=[])
conversation_id = str(uuid.uuid4())
set_conversation_id(conversation_id)
agent.invoke({"messages": [{"role": "user", "content": "Write me a novel"}]})

# Multi-turn conversation tracking
def handle_conversation(user_id, session_id):
    # Create a unique conversation ID combining user and session
    conversation_id = f"{user_id}_{session_id}_{uuid.uuid4()}"
    set_conversation_id(conversation_id)
    return conversation_id

# Different conversation types
business_conversation_id = f"business_{uuid.uuid4()}"
support_conversation_id = f"support_{uuid.uuid4()}"
```
