# Remote Endpoint (LangGraph Platform)

Connect your CopilotKit application to an agent deployed on LangGraph Platform.

This guide assumes you've created a LangGraph agent, and have a `langgraph.json` file set up. If you need a quick introduction, check out [this brief example\\
from the LangGraph docs](https://langchain-ai.github.io/langgraph/) or follow one of our demos.

## [Deploy a Graph to LangGraph Platform](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint\#deploy-a-graph-to-langgraph-platform)

### [Deploy your agent](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint\#deploy-your-agent)

First, you need to host your agent so that CopilotKit can access it.

Local (LangGraph Studio)Self hosted (FastAPI)LangGraph Platform

For local development, you can use the [LangGraph CLI](https://langchain-ai.github.io/langgraph/cloud/reference/cli/) to start a development server and LangGraph studio session.

You will need a [LangSmith account](https://smith.langchain.com/) to use this method.

```