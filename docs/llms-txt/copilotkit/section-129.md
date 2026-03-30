# ...
async def send_email_node(state: EmailAgentState, config: RunnableConfig):
    """Send an email."""

    await copilotkit_exit(config)

    # get the last message and cast to ToolMessage
    last_message = cast(ToolMessage, state["messages"][-1])
    if last_message.content == "CANCEL":
        return {
            "messages": [AIMessage(content="❌ Cancelled sending email.")],
        }
    else:
        return {
            "messages": [AIMessage(content="✅ Sent email.")],
        }
```

[Previous\\
\\
Manually emitting messages](https://docs.copilotkit.ai/coagents/advanced/emit-messages) [Next\\
\\
Overview](https://docs.copilotkit.ai/coagents/tutorials/agent-native-app)

### On this page

[Install the CopilotKit SDK](https://docs.copilotkit.ai/coagents/advanced/exit-agent#install-the-copilotkit-sdk) [Exit the agent loop](https://docs.copilotkit.ai/coagents/advanced/exit-agent#exit-the-agent-loop)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/advanced/exit-agent.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Message Persistence Guide
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this page

Persistence