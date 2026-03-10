# For TypeScript with Node 18 or above
npx @langchain/langgraph-cli dev --host localhost --port 8000
```

After starting the LangGraph server, the deployment URL will be `http://localhost:8000`.

### Having trouble?

### [Setup your Copilot Runtime](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint\#setup-your-copilot-runtime)

Copilot Cloud (Recommended)

I'm already using or want to use Copilot Cloud.

Self-Hosted

I'm using or want to use a self-hosted Copilot Runtime.

If you followed the [Copilot Cloud Quickstart](https://docs.copilotkit.ai/docs/quickstart) and opted to use CopilotCloud,
you only need to add your LangGraph Platform deployment URL and LangSmith API key to your CopilotCloud.

### Haven't setup Copilot Cloud yet? Click here!

To connect to LangGraph agents through Copilot Cloud, we leverage a concept called "Remote Endpoints"
which allow CopilotKit runtime to connect to various backends.

Navigate to [cloud.copilotkit.ai](https://go.copilotkit.ai/copilot-cloud-button-docs?ref=docs&session_id=0196217c-152e-758e-a4fb-d41efea3cec3) and follow the video!

You'll need a LangSmith API key which you can get with [this guide](https://docs.smith.langchain.com/administration/how_to_guides/organization_management/create_account_api_key#create-an-api-key) on LangSmith's website.

### Using LangGraph Studio

![Configure Remote Endpoint LangGraph](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/copilot-cloud/cpk-cloud-lgp-endpoint.gif)

🎉 You should now see your LangGraph agent in the list of available agents in CopilotKit!

### [Test Your Implementation](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint\#test-your-implementation)

After setting up the remote endpoint and modifying your `CopilotRuntime`, you can test your implementation by asking the copilot to perform actions that invoke your agent.

The graph and interactions can viewed in [LangGraph Studio](https://docs.copilotkit.ai/guides/backend-actions/smith.langchain.com/studio) and any logs should be available on [LangSmith](https://docs.copilotkit.ai/guides/backend-actions/smith.langchain.com)

* * *

## [Troubleshooting](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint\#troubleshooting)

A few things to try if you are running into trouble:

1. Make sure that you listed your agents according to the graphs mentioned in the `langgraph.json` file
2. Make sure the agent names are the same between the agent Python implementation, the `langgraph.json` file and the remote endpoint declaration
3. Make sure the LangGraph Platform deployment has all environment variables listed as you need them to be, according to your agent implementation

[Previous\\
\\
Remote Endpoint (Python)](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint) [Next\\
\\
Customize Instructions](https://docs.copilotkit.ai/guides/custom-ai-assistant-behavior)

### On this page

[Deploy a Graph to LangGraph Platform](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint#deploy-a-graph-to-langgraph-platform) [Deploy your agent](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint#deploy-your-agent) [Setup your Copilot Runtime](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint#setup-your-copilot-runtime) [Test Your Implementation](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint#test-your-implementation) [Troubleshooting](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint#troubleshooting)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/guides/backend-actions/langgraph-platform-endpoint.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Remote Backend Integration
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageStand up a FastAPI server using the CopilotKit Python SDK

[Backend Actions & Agents](https://docs.copilotkit.ai/guides/backend-actions)