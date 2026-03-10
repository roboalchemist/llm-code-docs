# or to include crewai
pip install copilotkit[crewai]
```

## [Adding actions](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints\#adding-actions)

In this example, we provide a simple action to the Copilot:

```
from copilotkit import CopilotKitRemoteEndpoint, Action

sdk = CopilotKitRemoteEndpoint(
    actions=[\
        Action(\
            name="greet_user",\
            handler=greet_user_handler,\
            description="Greet the user",\
            parameters=[\
                {\
                    "name": "name",\
                    "type": "string",\
                    "description": "The name of the user"\
                }\
            ]\
        )\
    ]
)
```

You can also dynamically build actions by providing a callable that returns a list of actions.
In this example, we use "name" from the `properties` object to parameterize the action handler.

```
from copilotkit import CopilotKitRemoteEndpoint, Action

sdk = CopilotKitRemoteEndpoint(
    actions=lambda context: [\
        Action(\
            name="greet_user",\
            handler=make_greet_user_handler(context["properties"]["name"]),\
            description="Greet the user"\
        )\
    ]
)
```

Using the same approach, you can restrict the actions available to the Copilot:

```
from copilotkit import CopilotKitRemoteEndpoint, Action

sdk = CopilotKitRemoteEndpoint(
    actions=lambda context: (
        [action_a, action_b] if is_admin(context["properties"]["token"]) else [action_a]
    )
)
```

## [Adding agents](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints\#adding-agents)

Serving agents works in a similar way to serving actions:

```
from copilotkit import CopilotKitRemoteEndpoint, LangGraphAgent
from my_agent.agent import graph

sdk = CopilotKitRemoteEndpoint(
    agents=[\
        LangGraphAgent(\
            name="email_agent",\
            description="This agent sends emails",\
            graph=graph,\
        )\
    ]
)
```

To dynamically build agents, provide a callable that returns a list of agents:

```
from copilotkit import CopilotKitRemoteEndpoint, LangGraphAgent
from my_agent.agent import graph

sdk = CopilotKitRemoteEndpoint(
    agents=lambda context: [\
        LangGraphAgent(\
            name="email_agent",\
            description="This agent sends emails",\
            graph=graph,\
            langgraph_config={\
                "token": context["properties"]["token"]\
            }\
        )\
    ]
)
```

To restrict the agents available to the Copilot, simply return a different list of agents based on the `context`:

```
from copilotkit import CopilotKitRemoteEndpoint
from my_agents import agent_a, agent_b, is_admin

sdk = CopilotKitRemoteEndpoint(
    agents=lambda context: (
        [agent_a, agent_b] if is_admin(context["properties"]["token"]) else [agent_a]
    )
)
```

## [Serving the CopilotKit SDK](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints\#serving-the-copilotkit-sdk)

To serve the CopilotKit SDK, you can use the `add_fastapi_endpoint` function from the `copilotkit.integrations.fastapi` module:

```
from copilotkit.integrations.fastapi import add_fastapi_endpoint
from fastapi import FastAPI

app = FastAPI()
sdk = CopilotKitRemoteEndpoint(...)
add_fastapi_endpoint(app, sdk, "/copilotkit")

def main():
    uvicorn.run(
        "your_package:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
```

### [Parameters](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints\#parameters)

actionsOptional\[Union\[List\[Action\], Callable\[\[CopilotKitContext\], List\[Action\]\]\]\]

The actions to make available to the Copilot.

agentsOptional\[Union\[List\[Agent\], Callable\[\[CopilotKitContext\], List\[Agent\]\]\]\]

The agents to make available to the Copilot.

## [CopilotKitContext](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints\#copilotkitcontext)

CopilotKit Context

### [Parameters](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints\#parameters-1)

propertiesAnyrequired

The properties provided to the frontend via `<CopilotKit properties={...} />`

frontend\_urlOptional\[str\]

The current URL of the frontend

headersMapping\[str, str\]required

The headers of the request

[Previous\\
\\
CopilotTask](https://docs.copilotkit.ai/reference/classes/CopilotTask) [Next\\
\\
LangGraphAgent](https://docs.copilotkit.ai/reference/sdk/python/LangGraphAgent)

### On this page

[CopilotKitRemoteEndpoint](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints#copilotkitremoteendpoint) [Adding actions](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints#adding-actions) [Adding agents](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints#adding-agents) [Serving the CopilotKit SDK](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints#serving-the-copilotkit-sdk) [Parameters](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints#parameters) [CopilotKitContext](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints#copilotkitcontext) [Parameters](https://docs.copilotkit.ai/reference/sdk/python/RemoteEndpoints#parameters-1)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/reference/sdk/python/RemoteEndpoints.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## LangGraph SDK Overview
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pagecopilotkitCustomizeConfig

JavaScript