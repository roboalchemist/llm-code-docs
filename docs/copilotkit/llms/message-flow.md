# Message flow

Message management in CoAgents operates with CopilotKit as the "ground truth" for the full chat session.
When an CoAgent session begins, it receives the existing CopilotKit chat history to maintain conversational
continuity across different agents.

While all of this information is great to know, in most cases you won't need to worry about these details to
build rich agentic applications. Use the information here as a reference when getting really deep into
the CoAgent internals.

### [Can I modify the message history?](https://docs.copilotkit.ai/coagents/concepts/message-management\#can-i-modify-the-message-history)

You can modify the message history from LangGraph by using the `RemoveMessage` class. For example to remove all messages from the chat history:

```
from langchain_core.messages import RemoveMessage

def a_node(state: AgentState, config):
    # ...
    return {"messages":  [RemoveMessage(id=m.id) for m in state['messages']]}
```

See the [LangGraph documentation](https://langchain-ai.github.io/langgraph/how-tos/memory/delete-messages/) for more information.

Editing the message history is not currently supported on the front-end, but will be soon.

### [Can I persist chat history?](https://docs.copilotkit.ai/coagents/concepts/message-management\#can-i-persist-chat-history)

Yes! There are a few ways to persist various portions of a chat's history:

- [Threads](https://docs.copilotkit.ai/coagents/persistence/threads)
- [Message Persistence](https://docs.copilotkit.ai/coagents/persistence/message-persistence)
- [Agent State](https://docs.copilotkit.ai/coagents/persistence/loading-agent-state)

## [Types of LLM Messages](https://docs.copilotkit.ai/coagents/concepts/message-management\#types-of-llm-messages)

Modern LLM interactions produce two distinct types of messages:

1. **Communication Messages**: Direct responses and interactions with users
2. **Internal Messages**: Agent "thoughts" and reasoning processes

A well known example of this pattern is OpenAI's o1 model, which has sophisticated reasoning capabilities and thoughts. Its internal
thought processes are presented distinctly from 'communication messages' which are clearly visible to the end-user.

LangGraph agents can operate similarly. An LLM call's output can be considered either a communication message, or an internal message.

### [Emitting Messages for long running tasks](https://docs.copilotkit.ai/coagents/concepts/message-management\#emitting-messages-for-long-running-tasks)

Sometimes you'll have a task that is running for a long time, and you want the user to be aware of what's happening. By default, LangGraph does not support this, because messages are only emitted on node transitions. However, CopilotKit allows you to accomplish this by using the `copilotkit_emit_message` function.

```
async def ask_name_node(state: GreetAgentState, config: RunnableConfig):
    """
    Ask the user for their name.
    """

    content = "Hey, what is your name? 🙂"

    await copilotkit_emit_message(config, content)

    # something long running here...

    return {
        "messages": AIMessage(content=content),
    }
```

Want some more help managing messages in your CoAgent application? Check out our guide on [emitting messages](https://docs.copilotkit.ai/coagents/advanced/emit-messages).

## [Message Flow](https://docs.copilotkit.ai/coagents/concepts/message-management\#message-flow)

Messages flow between CopilotKit and LangGraph in a specific way:

- All messages from LangGraph are forwarded to CopilotKit
- On a fresh agent invocation, the full CopilotKit chat history is provided to the LangGraph agent as its pre-existing chat history.

When a CoAgent completes its execution, its relevant messages become part of CopilotKit's persistent chat history. This allows for all future agent invocations to get context from the full chat history.

[Previous\\
\\
LangGraph](https://docs.copilotkit.ai/coagents/concepts/langgraph) [Next\\
\\
Common Issues](https://docs.copilotkit.ai/coagents/troubleshooting/common-issues)

### On this page

[Can I modify the message history?](https://docs.copilotkit.ai/coagents/concepts/message-management#can-i-modify-the-message-history) [Can I persist chat history?](https://docs.copilotkit.ai/coagents/concepts/message-management#can-i-persist-chat-history) [Types of LLM Messages](https://docs.copilotkit.ai/coagents/concepts/message-management#types-of-llm-messages) [Emitting Messages for long running tasks](https://docs.copilotkit.ai/coagents/concepts/message-management#emitting-messages-for-long-running-tasks) [Message Flow](https://docs.copilotkit.ai/coagents/concepts/message-management#message-flow)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/concepts/message-management.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Exiting Agent Loop
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageInstall the CopilotKit SDK

Advanced