# Source: https://novita.ai/docs/guides/sandbox-agent-runtime-quick-start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Quick Start

This guide will help you **develop, deploy, and invoke your first Agent in 5 minutes**.

***

## Table of Contents

* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Step 1: Integrate SDK into Your Agent](#step-1-integrate-sdk-into-your-agent)
* [Step 2: Generate Configuration Files with CLI](#step-2-generate-configuration-files-with-cli)
* [Step 3: Deploy to Novita with One-Click](#step-3-deploy-to-novita-with-one-click)
* [Step 4: Invoke Agent via CLI or SDK](#step-4-invoke-agent-via-cli-or-sdk)
* [FAQ](#faq)

***

## Overview

The complete workflow consists of 4 steps:

1. ✅ **Integrate SDK** - Add decorators to your Agent code
2. ✅ **Configure Agent** - Generate configuration files using CLI
3. ✅ **Deploy Agent** - One-click deployment to the cloud
4. ✅ **Invoke Agent** - Call your Agent using SDK or CLI

***

## Prerequisites

Ensure you have the following prerequisites:

* ✅ Python 3.9+ and Node.js 20+ installed
* ✅ Beta version Python SDK and Node.js CLI installed (see [Installation Guide](/guides/sandbox-agent-runtime-installation))
* ✅ Novita AI API Key obtained (from the [Console](https://novita.ai/settings/key-management))
* ✅ [Docker](https://www.docker.com/products/docker-desktop/) installed

***

## Step 1: Integrate SDK into Your Agent

### 1.1 Create Agent Code

Create `app.py` in your project directory:

```python  theme={"system"}
from novita_sandbox.agent_runtime import AgentRuntimeApp

# Create Agent Runtime application instance
app = AgentRuntimeApp()

# Define Agent entry point with decorator
@app.entrypoint
def my_agent(request: dict) -> dict:
    """
    Agent entry function
    
    Args:
        request: Request data, which typically contains fields like prompt
        
    Returns:
        Response data dictionary
    """
    prompt = request.get("prompt", "")
    
    # Agent business logic
    # You can call LLMs, use Agent frameworks, or implement any custom logic here
    result = f"Received message: {prompt}"
    
    return {"result": result}

# Local run entry point
if __name__ == "__main__":
    app.run()
```

### 1.2 Prepare Dependencies File

Ensure your project root has a `requirements.txt` file with the required dependencies:

```txt  theme={"system"}
novita-sandbox>=1.1.0b1
# Your other dependencies...
```

### 1.3 Local Testing

Test locally before deployment:

```bash  theme={"system"}
# Start the Agent service
python app.py
```

In another terminal, test the endpoints:

```bash  theme={"system"}
# Test health check
curl http://localhost:8080/ping

# Test Agent invocation
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello, Agent!"}'
```

**Expected output**:

Health check should return:

```json  theme={"system"}
{"status": "Healthy"}
```

Agent invocation should return:

```json  theme={"system"}
{"result": "Received message: Hello, Agent!"}
```

***

## Step 2: Generate Configuration Files with CLI

Use CLI to interactively configure your Agent:

```bash  theme={"system"}
# Make sure environment variables are configured
export NOVITA_API_KEY=your-novita-api-key

# Run configuration command
npx novita-sandbox-cli agent configure
```

Follow the CLI prompts to configure the required information. When complete, the CLI will generate the following files in your project directory:

* `novita.Dockerfile` - Docker build file
* `.dockerignore` - Docker ignore file
* `.novita-agent.yaml` - Agent configuration file

***

## Step 3: Deploy to Novita AI with One-click

> ⚠️ **Important**: After successful deployment, an `agent_id` will be generated. This is the unique identifier for invoking your Agent—make sure to save it.

### 3.1 Deploy Command

Deploy with one-click using CLI:

```bash  theme={"system"}
npx novita-sandbox-cli agent launch
```

### 3.2 View Deployment Results

After successful deployment, the `.novita-agent.yaml` file will update the `status` field:

```yaml  theme={"system"}
status:
  phase: deployed
  agent_id: agent-xxxx  # ⭐ This is your Agent's unique identifier
  last_deployed: '2025-10-23T10:35:00Z'
  build_id: build_xyz789
```

**Record the `agent_id`—you'll need it for subsequent invocations.**

***

## Step 4: Invoke Agent via CLI or SDK

### Option 1: Quick Test with CLI

Quickly test your Agent using CLI:

```bash  theme={"system"}
npx novita-sandbox-cli agent invoke "Hello, Agent!"
```

**Note**: The CLI automatically reads the Agent ID from the `status.agent_id` field in `.novita-agent.yaml`.

**Expected output**:

```json  theme={"system"}
{"result": "Received message: Hello, Agent!"}
```

### Option 2: SDK Invocation (Recommended for Production)

Use the SDK to invoke your Agent in backend services:

#### Example Code

```python  theme={"system"}
import asyncio
import json
import os
from novita_sandbox.agent_runtime import AgentRuntimeClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Agent Runtime client
client = AgentRuntimeClient(
    api_key=os.getenv("NOVITA_API_KEY")
)

async def main():
    # Get from status.agent_id in .novita-agent.yaml after deployment
    agent_id = "agent-xxxx"
    
    # Prepare request data
    payload = json.dumps({
        "prompt": "Hello, Agent! Tell me something about AI."
    }).encode()
    
    # Invoke Agent
    print(f"🚀 Invoking agent: {agent_id}")
    response = await client.invoke_agent_runtime(
        agentId=agent_id,
        payload=payload,
        timeout=300
    )
    
    print(f"✅ Response: {response}")

if __name__ == "__main__":
    asyncio.run(main())
```

***

## FAQ

### Q1: How do I get the Agent ID?

After successful deployment, the Agent ID is saved in the `status.agent_id` field of the `.novita-agent.yaml` file:

```yaml  theme={"system"}
status:
  agent_id: agent-xxxxx  # Here
```

### Q2: What if deployment fails?

1. **Check dependencies file**: Ensure `requirements.txt` contains all dependencies
2. **View detailed logs**: Use the `--verbose` flag
3. **Check network connection**: Ensure you can access the Novita AI Sandbox domain (e.g., `sandbox.novita.ai`)
4. **Verify API Key**: Confirm `NOVITA_API_KEY` is correct

```bash  theme={"system"}
# Show detailed logs
npx novita-sandbox-cli agent launch --verbose
```

### Q3: How do I update a deployed Agent?

Modify your code and redeploy:

```bash  theme={"system"}
# Option 1: Create new version (Recommended)
npx novita-sandbox-cli agent configure --agent-version 1.1.0
npx novita-sandbox-cli agent launch

# Option 2: Update existing version
npx novita-sandbox-cli agent launch --update-existing
```

### Q4: Works locally but fails after deployment?

**Possible causes**:

1. Environment variables not passed to sandbox instance
2. Dependency package version inconsistencies
3. File path issues

**Solution**:

Pass environment variables to the sandbox instance via the `envVars` parameter:

```python  theme={"system"}
response = await client.invoke_agent_runtime(
    agentId=agent_id,
    payload=payload,
    envVars={
        "NOVITA_API_KEY": os.getenv("NOVITA_API_KEY"),
        "MODEL_NAME": "deepseek/deepseek-v3-0324"
    }
)
```


Built with [Mintlify](https://mintlify.com).