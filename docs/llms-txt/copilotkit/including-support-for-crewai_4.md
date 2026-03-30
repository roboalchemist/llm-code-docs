# including support for crewai
poetry add copilotkit[crewai]
```

### [Setup your agent state](https://docs.copilotkit.ai/coagents/human-in-the-loop/interrupt-flow\#setup-your-agent-state)

We're going to have the agent ask us to name it, so we'll need a state property to store the name.

PythonTypeScript

agent/sample\_agent/agent.py

```