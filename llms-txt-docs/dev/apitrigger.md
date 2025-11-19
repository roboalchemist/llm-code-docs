# Source: https://dev.writer.com/blueprints/apitrigger.md

# API Trigger

Triggers an event via API call.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/api-trigger.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=64ff5eadb04a77a005ead9612c2bfba5" alt="" data-og-width="2306" width="2306" data-og-height="1478" height="1478" data-path="images/agent-builder/blueprints/api-trigger.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/api-trigger.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c765c9de5242a9303fee56a6460bcd40 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/api-trigger.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=634339d48e6971c2a5d3ebf69e9e7672 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/api-trigger.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=cd36c23da789c9443b35893426f1b758 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/api-trigger.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7efa07cd97bd2e6f4a056ae43a16a29e 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/api-trigger.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f045b6219c0177e6c7d8ade5b9629bb1 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/api-trigger.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=59e073bbfb7e6cf24e53ec025ed95c30 2500w" />

## Overview

The **API Trigger** block enables external systems to trigger your blueprint via HTTP API calls. Use it to integrate your agent with webhooks, external services, or other applications that need to programmatically execute your workflows.

Unlike the [**UI Trigger**](/blueprints/uitrigger) block that responds to user interactions in the interface, the **API Trigger** block accepts HTTP POST requests to trigger blueprint execution.

<Tip>
  You must deploy your agent before you can trigger a blueprint via API.
</Tip>

## How it works

1. **Agent and Blueprint IDs**: Each API trigger block is associated with a specific agent and blueprint ID that becomes part of the API endpoint URL
2. **HTTP endpoints**: Creates two endpoints:
   * A synchronous POST endpoint that accepts JSON payloads and returns Server-Sent Events (SSE)
   * An asynchronous POST endpoint that returns a job ID for polling results
3. **JSON input processing**: The HTTP request body becomes available as `@{result}` in your blueprint execution, with your data nested under the `inputs` key
4. **Return Value**: To return a value from your blueprint to the API caller, you include a [**Return Value**](/blueprints/returnvalue) block at the end of your blueprint workflow

### Blueprint structure requirements

When building blueprints that will be triggered via API, ensure your workflow ends with a **Return Value** block:

1. **Start with API Trigger**: Begin your blueprint with the API Trigger block
2. **Process your logic**: Add all the blocks needed for your workflow
3. **End with Return Value**: Always finish with a Return Value block to specify what gets returned to the API caller

**Example blueprint structure:**

```
API Trigger → [Your workflow blocks] → Return Value
```

## API endpoint

When you add an **API Trigger** block to your blueprint, it creates a public HTTP endpoint that you can use to trigger your blueprint. See [API Trigger usage guide](/agent-builder/api-trigger) for more details about the API endpoints and how to use them.

### Synchronous endpoint

```
POST https://api.writer.com/v1/agents/{agent_id}/blueprints/{blueprint_id}
```

### Asynchronous endpoint

```
POST https://api.writer.com/v1/agents/{agent_id}/blueprints/{blueprint_id}/jobs
```

### Authentication

All API calls require authentication using a Bearer token in the Authorization header. Learn how to [get your API key](/api-reference/api-keys).

```
Authorization: Bearer <your_api_key>
```

## Request format

Send a POST request with a JSON body containing the data you want to pass to your blueprint under the `inputs` key:

```json  theme={null}
{
  "inputs": {
    "user_id": "123",
    "action": "process_order"
  }
}
```

This data is available in your blueprint as `@{result.inputs.user_id}` and `@{result.inputs.action}`.

<Warning>
  The `inputs` key is required for the JSON payload. If you don't include it, the API will return an error.
</Warning>

## Response format

The synchronous API returns Server-Sent Events (SSE) with real-time execution status:

```
data: {"status":"in progress","message":null}
data: {"status":"executing","message":"Executing blueprint..."}
data: {"delta":"We have placed the order"}
data: [DONE]
```

The asynchronous API returns a job ID that you can poll for status updates using the following endpoint:

```
GET https://api.writer.com/v1/agents/jobs/{job_id}
```

When the job is complete, the response from the asynchronous API contains the result from the **Return Value** block in the `artifact` field.

## Testing

You can test your API trigger using the **Run blueprint** button in the Agent Builder editor. The **Default result** field provides sample data for testing without making actual HTTP requests.

## Learn more

For comprehensive implementation details, examples, and troubleshooting, see the [API Trigger usage guide](/agent-builder/api-trigger).

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Blueprint ID</td>
      <td>Blueprint Id</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Default result</td>
      <td>Code</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>The result that is used when the blueprint is triggered from the "Run blueprint" button</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Trigger</td>
      <td>-</td>
      <td>success</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

The **API Trigger** block returns the input payload that was sent to the API endpoint.

When triggered via API, the HTTP request body becomes available as `@{result}` in your blueprint execution, with your data nested under the `inputs` key. For example, if you send `{"inputs": {"user_id": "123"}}`, you can access it in your blueprint using `@{result.inputs.user_id}`.
