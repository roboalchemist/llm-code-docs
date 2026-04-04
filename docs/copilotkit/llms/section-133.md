# ...

async def chat_node(state: AgentState, config: RunnableConfig):
    model = ChatOpenAI(model="gpt-4o")


    intermediate_message = "Thinking really hard..."
    await copilotkit_emit_message(config, intermediate_message)

    # simulate a long running task
    await asyncio.sleep(2)

    response = await model.ainvoke([\
        SystemMessage(content="You are a helpful assistant."),\
        *state["messages"]\
    ], config)

    return Command(
        goto=END,
        update={
            # Make sure to include the emitted message in the messages history
            "messages": [AIMessage(content=intermediate_message), response]
        }
    )
```

### [Give it a try!](https://docs.copilotkit.ai/coagents/advanced/emit-messages\#give-it-a-try)

Now when you talk to your agent you'll notice that it immediately responds with the message "Thinking really hard..."
before giving you a response 2 seconds later.

[Previous\\
\\
Disabling state streaming](https://docs.copilotkit.ai/coagents/advanced/disabling-state-streaming) [Next\\
\\
Exiting the agent loop](https://docs.copilotkit.ai/coagents/advanced/exit-agent)

### On this page

[What is this?](https://docs.copilotkit.ai/coagents/advanced/emit-messages#what-is-this) [When should I use this?](https://docs.copilotkit.ai/coagents/advanced/emit-messages#when-should-i-use-this) [Implementation](https://docs.copilotkit.ai/coagents/advanced/emit-messages#implementation) [Run and Connect Your Agent to CopilotKit](https://docs.copilotkit.ai/coagents/advanced/emit-messages#run-and-connect-your-agent-to-copilotkit) [Install the CopilotKit SDK](https://docs.copilotkit.ai/coagents/advanced/emit-messages#install-the-copilotkit-sdk) [Manually emit a message](https://docs.copilotkit.ai/coagents/advanced/emit-messages#manually-emit-a-message) [Give it a try!](https://docs.copilotkit.ai/coagents/advanced/emit-messages#give-it-a-try)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/advanced/emit-messages.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)