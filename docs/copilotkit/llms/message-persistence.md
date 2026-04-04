# Message Persistence

To learn about how to load previous messages and agent states, check out the [Loading Message History](https://docs.copilotkit.ai/coagents/persistence/loading-message-history) and [Loading Agent State](https://docs.copilotkit.ai/coagents/persistence/loading-agent-state) pages.

To persist LangGraph messages to a database, you can use either `AsyncPostgresSaver` or `AsyncSqliteSaver`. Set up the asynchronous memory by configuring the graph within a lifespan function, as follows:

```
from contextlib import asynccontextmanager
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with AsyncPostgresSaver.from_conn_string(
        "postgresql://postgres:postgres@127.0.0.1:5432/postgres"
    ) as checkpointer:
        # NOTE: you need to call .setup() the first time you're using your checkpointer
        await checkpointer.setup()
        # Create an async graph
        graph = workflow.compile(checkpointer=checkpointer)

        # Create SDK with the graph
        sdk = CopilotKitRemoteEndpoint(
            agents=[\
                LangGraphAgent(\
                    name="research_agent",\
                    description="Research agent.",\
                    graph=graph,\
                ),\
            ],
        )

        # Add the CopilotKit FastAPI endpoint
        add_fastapi_endpoint(app, sdk, "/copilotkit")
        yield

app = FastAPI(lifespan=lifespan)
```

To learn more about persistence in LangGraph, check out the [LangGraph documentation](https://langchain-ai.github.io/langgraph/how-tos/#persistence).

[Previous\\
\\
Threads](https://docs.copilotkit.ai/coagents/persistence/loading-message-history) [Next\\
\\
Using Agent Execution Parameters](https://docs.copilotkit.ai/coagents/advanced/adding-runtime-configuration)

### On this page

No Headings

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/coagents/persistence/message-persistence.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Emit Messages in Agents
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is this?

Advanced