# CrewAIAgent

CrewAIAgent lets you define your agent for use with CopilotKit.

## [CrewAIAgent](https://docs.copilotkit.ai/reference/sdk/python/CrewAIAgent\#crewaiagent)

CrewAIAgent lets you define your agent for use with CopilotKit.

To install, run:

```
pip install copilotkit[crewai]
```

Every agent must have the `name` and either `crew` or `flow` properties defined. An optional
`description` can also be provided. This is used when CopilotKit is dynamically routing requests
to the agent.

## [Serving a Crew based agent](https://docs.copilotkit.ai/reference/sdk/python/CrewAIAgent\#serving-a-crew-based-agent)

To serve a Crew based agent, pass in a `Crew` object to the `crew` parameter.

Note:
You need to make sure to have a `chat_llm` set on the `Crew` object.
See [the CrewAI docs](https://docs.crewai.com/concepts/cli#9-chat) for more information.

```
from copilotkit import CrewAIAgent


CrewAIAgent(
    name="email_agent_crew",
    description="This crew based agent sends emails",
    crew=SendEmailCrew(),
)
```

## [Serving a Flow based agent](https://docs.copilotkit.ai/reference/sdk/python/CrewAIAgent\#serving-a-flow-based-agent)

To serve a Flow based agent, pass in a `Flow` object to the `flow` parameter.

```
CrewAIAgent(
    name="email_agent_flow",
    description="This flow based agent sends emails",
    flow=SendEmailFlow(),
)
```

Note:
Either a `crew` or `flow` must be provided to CrewAIAgent.

### [Parameters](https://docs.copilotkit.ai/reference/sdk/python/CrewAIAgent\#parameters)

namestrrequired

The name of the agent.

crewCrewrequired

When using a Crew based agent, pass in a `Crew` object to the `crew` parameter.

flowFlowrequired

When using a Flow based agent, pass in a `Flow` object to the `flow` parameter.

descriptionOptional\[str\]

The description of the agent.

copilotkit\_configOptional\[CopilotKitConfig\]

The CopilotKit config to use with the agent.

## [CopilotKitConfig](https://docs.copilotkit.ai/reference/sdk/python/CrewAIAgent\#copilotkitconfig)

CopilotKit config for CrewAIAgent

This is used for advanced cases where you want to customize how CopilotKit interacts with
CrewAI.

```