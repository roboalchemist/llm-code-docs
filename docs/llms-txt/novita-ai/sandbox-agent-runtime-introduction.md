# Source: https://novita.ai/docs/guides/sandbox-agent-runtime-introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

## What is Novita Agent Runtime?

Novita Agent Runtime is a lightweight framework for deploying AI Agents that enables you to **deploy AI Agents quickly and cost-effectively**.

No need to worry about infrastructure configuration, container orchestration, service exposure, or other complex details—just focus on developing your Agent's business logic.

***

## Core Components

Novita Agent Runtime is included in the Novita Sandbox SDK and CLI tools:

| Component              | Description                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Novita Sandbox SDK** | Provides decorator-based APIs to expose your Agent as a standard HTTP service, and methods to invoke Agents |
| **Novita Sandbox CLI** | One-click configuration and deployment of Agents to the Novita Agent Sandbox ecosystem                      |

***

## Deployment Workflow

The complete deployment and usage workflow consists of three steps:

### Step 1: Develop and Integrate Your Agent

Integrate the SDK into your Agent code by adding decorators:

```python  theme={"system"}
from novita_sandbox.agent_runtime import AgentRuntimeApp

app = AgentRuntimeApp()

@app.entrypoint
def my_agent(request: dict):
    # Agent business logic
    return {"result": "..."}
```

### Step 2: Configure and Deploy

Use the CLI tool to configure and deploy to the cloud:

```bash  theme={"system"}
# Configure Agent
novita-sandbox-cli agent configure

# Deploy to cloud
novita-sandbox-cli agent launch
```

* Generates `Dockerfile` and `.novita-agent.yaml` configuration files
* Builds sandbox template and uploads it
* Generates Agent ID (format: `agent_<name>_v<version>`)

### Step 3: Invoke Agent

After successful deployment, you can invoke your Agent via CLI or SDK:

**Option 1: Quick test with CLI**

```bash  theme={"system"}
novita-sandbox-cli agent invoke "Hello, Agent!"
```

**Option 2: Invoke via SDK in your application**

```python  theme={"system"}
import json
from novita_sandbox.agent_runtime import AgentRuntimeClient

client = AgentRuntimeClient(api_key="your-api-key")

# Prepare request data (converted to a JSON string and encoded as bytes)
payload = json.dumps({"prompt": "Hello, Agent!"}).encode()

response = await client.invoke_agent_runtime(
    agentId="agent-xxxxx",
    payload=payload
)
```

**Agent invocation execution flow**:

* Creates an isolated sandbox instance from the sandbox template
* Executes the Agent in an isolated environment
* Returns the processed result

***

## Key Benefits

SDK:

* ✅ **Minimal Changes**: Just modify a few lines of code with decorators
* ✅ **Framework Agnostic**: Supports LangChain, LangGraph, CrewAI, and other popular AI frameworks
* ✅ **Streaming Support**: Native streaming responses for real-time LLM generation scenarios
* ✅ **Health Checks**: Built-in health check endpoint with customizable health status

CLI:

* ✅ **Smart Detection**: Auto-detects project structure, entry files, and dependency management files
* ✅ **Auto Build**: Automatically generates Dockerfile and project configuration
* ✅ **Version Management**: Supports multiple versions coexisting with independent deployments
* ✅ **Quick Testing**: Built-in invoke command for rapid deployment verification

Runtime:

* ✅ **Environment Isolation**: Each sandbox instance runs independently without interference
* ✅ **Session Persistence**: Multiple invocations to the same sandbox instance, supporting multi-turn interactive Agents
* ✅ **Secure Sandbox**: Securely isolated sandbox environment with restricted filesystem access


Built with [Mintlify](https://mintlify.com).