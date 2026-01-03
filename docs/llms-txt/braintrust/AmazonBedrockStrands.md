# Source: https://braintrust.dev/docs/cookbook/recipes/AmazonBedrockStrands.md

# Observability for Strands Agents on Amazon Bedrock

<div className="text-sm">[Contributed](https://github.com/braintrustdata/braintrust-cookbook/blob/main/examples/AmazonBedrockStrands/AmazonBedrockStrands.ipynb) by [Ishan Singh](https://www.linkedin.com/in/shan199434/) on 2025-11-18</div>

This cookbook guides you through how to deploy a Strands Agent to Amazon Bedrock AgentCore Runtime with built-in observability. The implementation uses Amazon Bedrock Claude models and sends telemetry data to Braintrust through OpenTelemetry.

By the end of this cookbook, you'll learn how to:

* Build a Strands Agent with web search capabilities using Amazon Bedrock Claude models
* Deploy the agent to Amazon Bedrock AgentCore Runtime for managed, scalable hosting
* Configure OpenTelemetry to send traces to Braintrust for observability
* Invoke the agent through both SDK and boto3 client

## Key components

* **Strands Agent**: Python framework for building LLM-powered agents with built-in telemetry support
* **Amazon Bedrock AgentCore Runtime**: Managed runtime service for hosting and scaling agents on AWS
* **OpenTelemetry**: Industry-standard protocol for collecting and exporting telemetry data

## Architecture

The agent is containerized and deployed to Amazon Bedrock AgentCore Runtime, which provides HTTP endpoints for invocation. Telemetry data flows from the Strands Agent through OTEL exporters to Braintrust for monitoring and debugging. The implementation uses a lazy initialization pattern to ensure proper configuration order.

<img src="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=62501bcb6f73eb1a9132007dea38d2a5" alt="Architecture diagram" data-og-width="2447" width="2447" data-og-height="1489" height="1489" data-path="cookbook/assets/AmazonBedrockStrands/configure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=280&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=73fec25d0adc7bfac0f7ae02ff735f4f 280w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=560&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=b45e817d49b5c84a61dbf2932590cdbe 560w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=840&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=ff52621975e550a656efaa011577a8b2 840w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=1100&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=c07b44a4572db367d636fbd7a769f6b9 1100w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=1650&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=24b85d0c8f41b8fe2216bf0d9b9f429e 1650w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=2500&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=837a54ad994817820170a14381bfb3d6 2500w" />

## Getting started

To get started, make sure you have:

* Python 3.10+
* AWS credentials configured with Bedrock and AgentCore permissions
* A [Braintrust account](https://www.braintrust.dev/signup) and [API key](https://www.braintrust.dev/app/settings?subroute=api-keys)
* Docker installed locally
* Access to Amazon Bedrock Claude models in us-west-2

You'll also want to install required dependencies from the `requirements.txt` file:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
%pip install --force-reinstall -U -r requirements.txt --quiet
```

## Agent implementation

The agent file (`strands_claude.py`) implements a travel agent with web search capabilities. The implementation uses a lazy initialization pattern to ensure telemetry is configured after environment variables, integrates Amazon Bedrock Claude models through the Strands framework, and includes web search via DuckDuckGo for real-time information. The agent is configured to send traces to Braintrust via OpenTelemetry:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
%%writefile strands_claude.py
import os
import logging
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent, tool
from strands.models import BedrockModel
from strands.telemetry import StrandsTelemetry
from ddgs import DDGS

logging.basicConfig(level=logging.ERROR, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(os.getenv("AGENT_RUNTIME_LOG_LEVEL", "INFO").upper())


@tool
def web_search(query: str) -> str:
    """
    Search the web for information using DuckDuckGo.

    Args:
        query: The search query

    Returns:
        A string containing the search results
    """
    try:
        ddgs = DDGS()
        results = ddgs.text(query, max_results=5)

        formatted_results = []
        for i, result in enumerate(results, 1):
            formatted_results.append(
                f"{i}. {result.get('title', 'No title')}\n"
                f"   {result.get('body', 'No summary')}\n"
                f"   Source: {result.get('href', 'No URL')}\n"
            )

        return "\n".join(formatted_results) if formatted_results else "No results found."

    except Exception as e:
        return f"Error searching the web: {str(e)}"

# Function to initialize Bedrock model
def get_bedrock_model():
    region = os.getenv("AWS_DEFAULT_REGION", "us-west-2")
    model_id = os.getenv("BEDROCK_MODEL_ID", "us.anthropic.claude-3-7-sonnet-20250219-v1:0")

    bedrock_model = BedrockModel(
        model_id=model_id,
        region_name=region,
        temperature=0.0,
        max_tokens=1024
    )
    return bedrock_model

# Initialize the Bedrock model
bedrock_model = get_bedrock_model()

# Define the agent's system prompt
system_prompt = """You are an experienced travel agent specializing in personalized travel recommendations
with access to real-time web information. Your role is to find dream destinations matching user preferences
using web search for current information. You should provide comprehensive recommendations with current
information, brief descriptions, and practical travel details."""

app = BedrockAgentCoreApp()

def initialize_agent():
    """Initialize the agent with proper telemetry configuration."""

    # Initialize Strands telemetry with 3P configuration
    strands_telemetry = StrandsTelemetry()
    strands_telemetry.setup_otlp_exporter()

    # Create and cache the agent
    agent = Agent(
        model=bedrock_model,
        system_prompt=system_prompt,
        tools=[web_search]
    )

    return agent

@app.entrypoint
def strands_agent_bedrock(payload, context=None):
    """
    Invoke the agent with a payload
    """
    user_input = payload.get("prompt")
    logger.info("[%s] User input: %s", context.session_id, user_input)

    # Initialize agent with proper configuration
    agent = initialize_agent()

    response = agent(user_input)
    return response.message['content'][0]['text']

if __name__ == "__main__":
    app.run()
```

## Configure AgentCore runtime deployment

Next we'll use the starter toolkit to configure the AgentCore Runtime deployment with an entrypoint, the execution role, and a requirements file. We'll also configure the starter kit to auto-create the Amazon ECR repository on launch.

During the configure step, your Dockerfile will be generated based on your application code.

<Callout type="info">
  When using the `bedrock_agentcore_starter_toolkit` to configure your agent, it configures AgentCore Observability by default. To use Braintrust, you need to disable AgentCore Observability by setting `disable_otel=True`.
</Callout>

<img src="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=62501bcb6f73eb1a9132007dea38d2a5" alt="Configure diagram" data-og-width="2447" width="2447" data-og-height="1489" height="1489" data-path="cookbook/assets/AmazonBedrockStrands/configure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=280&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=73fec25d0adc7bfac0f7ae02ff735f4f 280w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=560&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=b45e817d49b5c84a61dbf2932590cdbe 560w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=840&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=ff52621975e550a656efaa011577a8b2 840w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=1100&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=c07b44a4572db367d636fbd7a769f6b9 1100w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=1650&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=24b85d0c8f41b8fe2216bf0d9b9f429e 1650w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/configure.png?w=2500&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=837a54ad994817820170a14381bfb3d6 2500w" />

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from bedrock_agentcore_starter_toolkit import Runtime
from boto3.session import Session

boto_session = Session()
region = boto_session.region_name

agentcore_runtime = Runtime()
agent_name = "strands_braintrust_observability"

response = agentcore_runtime.configure(
    entrypoint="strands_claude.py",
    auto_create_execution_role=True,
    auto_create_ecr=True,
    requirements_file="requirements.txt",
    region=region,
    agent_name=agent_name,
    disable_otel=True,
)
response
```

## Deploy to AgentCore runtime

Now that we have a Dockerfile, let's launch the agent to the AgentCore Runtime. This will create the Amazon ECR repository and the AgentCore Runtime.

<img src="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/launch.png?fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=133049ac4d36da11ddb92b23cfd8325a" alt="Launch diagram" data-og-width="3854" width="3854" data-og-height="1650" height="1650" data-path="cookbook/assets/AmazonBedrockStrands/launch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/launch.png?w=280&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=e9549f7ddbce2772be7ea10662706a80 280w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/launch.png?w=560&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=b1061f77c70bf3a8eb6362523124fc4f 560w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/launch.png?w=840&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=6495016fc6d40147294c42a1944a20d6 840w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/launch.png?w=1100&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=951cbf6f665c0b6055a3dddbf12b15b5 1100w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/launch.png?w=1650&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=4760e08abc4c014c0206fa525be351ec 1650w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/launch.png?w=2500&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=b45d97b7a03c0ac52fcb9a04d9be65a8 2500w" />

### Configure observability

To enable observability, we need to configure the OpenTelemetry endpoint and authentication. The agent will send traces to Braintrust using the OTEL protocol.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
# Braintrust configuration
otel_endpoint = "https://api.braintrust.dev/otel"
braintrust_api_key = (
    "<braintrust-api-key>"  # For production, key should be securely stored
)
braintrust_project_id = "<braintrust-project-id>"
otel_auth_header = f"Authorization=Bearer {braintrust_api_key}, x-bt-parent=project_id:{braintrust_project_id}"


launch_result = agentcore_runtime.launch(
    env_vars={
        "BEDROCK_MODEL_ID": "us.anthropic.claude-3-7-sonnet-20250219-v1:0",  # Example model ID
        "OTEL_EXPORTER_OTLP_ENDPOINT": otel_endpoint,
        "OTEL_EXPORTER_OTLP_HEADERS": otel_auth_header,
        "DISABLE_ADOT_OBSERVABILITY": "true",
    }
)
launch_result
```

## Check deployment status

Wait for the runtime to be ready before invoking:

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import time

status_response = agentcore_runtime.status()
status = status_response.endpoint["status"]
end_status = ["READY", "CREATE_FAILED", "DELETE_FAILED", "UPDATE_FAILED"]

while status not in end_status:
    time.sleep(10)
    status_response = agentcore_runtime.status()
    status = status_response.endpoint["status"]
    print(status)

print(f"Final status: {status}")
```

## Invoke the agent

Finally, we can invoke our AgentCore Runtime with a payload.

<img src="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/invoke.png?fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=4b90f49bec4d3dbf9cff406c9efe9005" alt="Invoke diagram" data-og-width="4019" width="4019" data-og-height="1847" height="1847" data-path="cookbook/assets/AmazonBedrockStrands/invoke.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/invoke.png?w=280&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=6d2f9b41a255e7df5aafc3bb478df985 280w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/invoke.png?w=560&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=579b1335550d85ecb7b822eb240d390b 560w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/invoke.png?w=840&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=02700c641132b09d640285048cf3dd9e 840w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/invoke.png?w=1100&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=2316a3b9423050dcb2c4aaa389938c7f 1100w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/invoke.png?w=1650&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=a61cd77f9acc8690407354078356a3e8 1650w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/invoke.png?w=2500&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=11b65cbc2fcdd27728d9727c0c1f9b72 2500w" />

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
invoke_response = agentcore_runtime.invoke(
    {
        "prompt": "I'm planning a weekend trip to Orlando. What are the must-visit places and local food I should try?"
    }
)
```

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
from IPython.display import Markdown, display

display(Markdown("".join(invoke_response["response"])))
```

## Logging in Braintrust

When you invoke the agent, logs are automatically generated for each invocation. Each agent interaction is captured in its own trace, with individual spans for tool calls and model interactions. To view your logs, navigate to your Braintrust project and select the **Logs** tab.

The trace view shows the full execution tree, including all agent interactions, tool calls (such as web\_search), and model invocations with their latency and token usage.

<img src="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-trace.png?fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=f0192368eacdb2c1a90cc150960a5a61" alt="Trace View" data-og-width="1422" width="1422" data-og-height="777" height="777" data-path="cookbook/assets/AmazonBedrockStrands/logs-trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-trace.png?w=280&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=e98ff54c1be97efa4673db6d4a205ed0 280w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-trace.png?w=560&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=6ee6b01e8d35ed3a71275426e6618d60 560w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-trace.png?w=840&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=ce0cf17ec085d6658c0ffad24d32435f 840w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-trace.png?w=1100&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=0131cdedab09771bed011e2ee2e51efc 1100w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-trace.png?w=1650&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=9191d0524a472c4c77ff0f75fbd45380 1650w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-trace.png?w=2500&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=666679d47b843ea9696bc356d5b9a85c 2500w" />

The table view provides a summary of all traces with key metrics like duration, LLM duration, tool calls, and errors.

<img src="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-table.png?fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=e68526775c17bdc4b1a955f3620b19ac" alt="Table View" data-og-width="1421" width="1421" data-og-height="774" height="774" data-path="cookbook/assets/AmazonBedrockStrands/logs-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-table.png?w=280&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=ce1e9952f0b1e6aaf382c1d9308cc225 280w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-table.png?w=560&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=d49322e2d4808ea8a1e789375dee3a28 560w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-table.png?w=840&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=05b5f1579c7251934ceaf60c08818460 840w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-table.png?w=1100&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=015f088a3c2d91348ce84e30f67051e2 1100w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-table.png?w=1650&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=1203969b6f444b51958542f068ede938 1650w, https://mintcdn.com/braintrust/05q80NTQOgO_JK2g/cookbook/assets/AmazonBedrockStrands/logs-table.png?w=2500&fit=max&auto=format&n=05q80NTQOgO_JK2g&q=85&s=285f104e56356f6e7b49a679e352a49a 2500w" />

The traces include detailed information about agent invocation, tool calls, model interactions with latency and token usage, and complete request/response payloads.

## Cleanup

When you're finished, you can clean up the resources you're not using anymore. This step is optional, but a best practice.

```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
import boto3

# Delete the AgentCore Runtime and ECR repository
agentcore_control_client = boto3.client("bedrock-agentcore-control", region_name=region)

ecr_client = boto3.client("ecr", region_name=region)

# Delete the runtime
runtime_delete_response = agentcore_control_client.delete_agent_runtime(
    agentRuntimeId=launch_result.agent_id,
)

# Delete the ECR repository
response = ecr_client.delete_repository(
    repositoryName=launch_result.ecr_uri.split("/")[1], force=True
)

print("Cleanup completed")
```

## Next steps

Now that you have a working Strands Agent deployed to Amazon Bedrock AgentCore Runtime with full observability, you can build on this foundation:

* Add more [tools](/core/functions/tools) to expand agent capabilities beyond web search
* Create [custom scorers](/core/functions/scorers) to evaluate agent performance and accuracy
* Build [evaluation datasets](/core/datasets) from production logs to continuously improve your agent
* Use the [playground](/core/playground) to test and refine agent behavior before deploying updates


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt