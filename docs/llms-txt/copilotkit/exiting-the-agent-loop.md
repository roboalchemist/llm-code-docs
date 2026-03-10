# Exiting the agent loop

After your agent has finished a workflow, you'll usually want to explicitly end that loop by calling the CopilotKit exit method in your agent code.

Exiting the agent has different effects depending on mode:

- **Router Mode**: Exiting the agent hands responsibility for handling input back to the router, which can initiate chat, call actions, other agents, etc. The router can return to this agent later (starting a new loop) to satisfy a user request.

- **Agent Lock Mode**: Exiting the agent restarts the workflow loop for the current agent.


In this example from [our email-sending app](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-qa), the `send_email` node explicitly exits, then manually sends a response back to the user as a `ToolMessage`:

### [Install the CopilotKit SDK](https://docs.copilotkit.ai/coagents/advanced/exit-agent\#install-the-copilotkit-sdk)

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic
experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

Poetrypipconda

```
poetry add copilotkit