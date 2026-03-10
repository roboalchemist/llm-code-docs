# Add the CopilotKit endpoint to your FastAPI app
add_fastapi_endpoint(app, sdk, "/copilotkit_remote")

def main():
    """Run the uvicorn server."""
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()
```

### [Run Your FastAPI Server](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#run-your-fastapi-server)

Since we've added the entry point in `server.py`, you can run your FastAPI server directly by executing the script:

Poetrypipconda

```
poetry run python3 server.py
```

**Note:** Ensure that you're in the same directory as `server.py` when running this command.

## [Connect your app to the remote endpoint](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#connect-your-app-to-the-remote-endpoint)

Now that you've set up your FastAPI server with the backend actions, integrate it into your CopilotKit application by modifying your `CopilotRuntime` configuration.

Copilot Cloud (Recommended)

I want to use Copilot Cloud to connect to my remote endpoint.

Self-Hosted Copilot Runtime

I want to use a self-hosted Copilot Runtime to connect to my remote endpoint.

To connect a FastAPI server to Copilot Cloud, we leverage a concept called "Remote Endpoints"
which allow CopilotKit runtime to connect to various backends.

To get started, [navigate to Copilot Cloud](https://go.copilotkit.ai/copilot-cloud-button-docs?ref=docs&session_id=0196217c-93b4-7a50-92fd-231e440765bd).

Don't want to use a tunnel?

Just skip the tunnel setup and use your hosted FastAPI server address instead.

```
npx copilotkit@latest dev --port <port_number>
```

![Configure Remote Endpoint](https://docs.copilotkit.aihttps://cdn.copilotkit.ai/docs/copilotkit/images/copilot-cloud/cpk-cloud-remote-endpoint-setup.gif)

You should now see your CopilotKit runtime in the list of available agents in CopilotKit!

### [Test Your Implementation](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#test-your-implementation)

After setting up the remote endpoint and modifying your `CopilotRuntime`, you can test your implementation by asking the copilot to perform actions that invoke your Python backend. For example, ask the copilot: "Fetch the name for user ID `123`."

### [Advanced](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#advanced)

#### [Configuring the Thread Pool Executor](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#configuring-the-thread-pool-executor)

The request to the remote endpoint is made in a thread pool executor. You can configure the size of the thread pool executor by passing the `max_workers` parameter to the `add_fastapi_endpoint` function.

```
add_fastapi_endpoint(app, sdk, "/copilotkit_remote", max_workers=10) # default is 10
```

#### [Dynamically returning actions and agents](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint\#dynamically-returning-actions-and-agents)

Both the `actions` and `agents` parameters can optionally be functions that return a list of actions or agents. This allows you to dynamically return actions and agents based on the user's request.

For example, to dynamically configure an agent based on properties from the frontend, set the properties on the frontend first:

```
<CopilotKit properties={{someProperty: "xyz"}}>
   <YourApp />
</CopilotKit>
```

Then, in your backend, use a function to return dynamically configured agents:

```
def build_agents(context):
    return [\
        LangGraphAgent(\
            name="some_agent",\
            description="This agent does something",\
            graph=graph,\
            langgraph_config={\
                "some_property": context["properties"]["someProperty"]\
            }\
        )\
    ]


app = FastAPI()
sdk = CopilotKitRemoteEndpoint(
    agents=build_agents,
)
```

* * *

[Previous\\
\\
LangServe actions](https://docs.copilotkit.ai/guides/backend-actions/langserve-backend-actions) [Next\\
\\
Remote Endpoint (LangGraph Platform)](https://docs.copilotkit.ai/guides/backend-actions/langgraph-platform-endpoint)

### On this page

[Stand up a FastAPI server using the CopilotKit Python SDK](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#stand-up-a-fastapi-server-using-the-copilotkit-python-sdk) [Install CopilotKit Python SDK and Dependencies](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#install-copilotkit-python-sdk-and-dependencies) [Initialize a New Poetry Project](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#initialize-a-new-poetry-project) [Install Dependencies](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#install-dependencies) [Set Up a Virtual Environment (optional)](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#set-up-a-virtual-environment-optional) [Install Dependencies](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#install-dependencies-1) [Create a New Conda Environment](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#create-a-new-conda-environment) [Install Dependencies](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#install-dependencies-2) [Set Up a FastAPI Server](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#set-up-a-fastapi-server) [Define Your Backend Actions](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#define-your-backend-actions) [Run Your FastAPI Server](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#run-your-fastapi-server) [Connect your app to the remote endpoint](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#connect-your-app-to-the-remote-endpoint) [Troubleshooting](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#troubleshooting) [Test Your Implementation](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#test-your-implementation) [Advanced](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#advanced) [Configuring the Thread Pool Executor](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#configuring-the-thread-pool-executor) [Dynamically returning actions and agents](https://docs.copilotkit.ai/guides/backend-actions/remote-backend-endpoint#dynamically-returning-actions-and-agents)

[Edit on GitHub](https://github.com/CopilotKit/CopilotKit/blob/main/docs/content/docs/(root)/guides/backend-actions/remote-backend-endpoint.mdx)

![](https://static.scarf.sh/a.png?x-pxid=ffc9f65d-0186-4575-b065-61d62ea9d7d3)

## Human-in-the-Loop Overview
CrewAI CrewAI support is here! Checkout the [Crew](https://docs.copilotkit.ai/crewai-crews) and [Flow](https://docs.copilotkit.ai/crewai-flows) documentation.

Search docs

`⌘`  `K`

On this pageWhat is Human-in-the-Loop (HITL)?