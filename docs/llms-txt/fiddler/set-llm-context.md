# Source: https://docs.fiddler.ai/api/fiddler-strands-agents-sdk/attributes/set-llm-context.md

# Source: https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/set-llm-context.md

# set\_llm\_context

Sets additional context information on a language model instance.

This context provides environmental or operational information that will be attached to all spans created for this model. Use this to add relevant metadata such as user preferences, session state, or runtime conditions that influenced the LLM's behavior. This is valuable for debugging and understanding why the model produced specific outputs.

Supports both BaseLanguageModel instances and RunnableBinding objects. When a RunnableBinding is provided, the context is automatically set on the underlying bound object (which must be a BaseLanguageModel).

For more information on RunnableBinding, see: <https://python.langchain.com/api\\_reference/core/runnables/langchain\\_core.runnables.base.RunnableBinding.html>

## Parameters

| Parameter | Type                | Required          | Default | Description                                                            |
| --------- | ------------------- | ----------------- | ------- | ---------------------------------------------------------------------- |
| `llm`     | \`BaseLanguageModel | RunnableBinding\` | ✓       | `-`                                                                    |
| `context` | `str`               | ✓                 | `-`     | The context string to add. This will be included in span attributes as |

## Raises

**TypeError** -- If a RunnableBinding is provided but its bound object is not a BaseLanguageModel. **Return type:** None

## Examples

Basic usage with ChatOpenAI:

```python
from langchain_openai import ChatOpenAI
from fiddler_langgraph.tracing.instrumentation import set_llm_context

llm = ChatOpenAI(model="gpt-4")
set_llm_context(llm, "User prefers concise responses")
```

With user preferences:

```python
set_llm_context(llm, "User language: Spanish, Expertise: Beginner")
```

Using with RunnableBinding:

```python
bound_llm = llm.bind(temperature=0.7, max_tokens=100)
set_llm_context(bound_llm, "Creative writing mode with token limits")
```

Adding session context:

```python
import uuid
session_id = uuid.uuid4()
set_llm_context(llm, f"Session: {session_id}, Environment: Production")
```
