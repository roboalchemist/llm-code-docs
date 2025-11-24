# Source: https://dev.writer.com/agent-builder/api-trigger.md

# Trigger blueprints via API

> Enable external systems to trigger blueprints via HTTP API calls. Integrate agents with webhooks, schedulers, and third-party services programmatically.

The [**API Trigger**](/blueprints/apitrigger) block enables external systems to trigger your blueprint via HTTP API calls. Use it to integrate your agent with webhooks, external services, or other applications that need to programmatically execute your workflows.

Unlike the [**UI Trigger**](/blueprints/uitrigger) block that responds to user interactions in the interface, the **API Trigger** block accepts HTTP POST requests to trigger blueprint execution.

<Tip>
  You must deploy your agent before you can trigger a blueprint via API.
</Tip>

## Overview

When you add an **API Trigger** block to your blueprint, it creates a public HTTP endpoint that external systems can use to trigger your blueprint execution. This enables:

* **Webhook integration**: Receive notifications from external services like GitHub, Slack, or payment processors
* **API-first workflows**: Build workflows that can be triggered programmatically by other applications
* **Scheduled automation**: Use external schedulers like task schedulers or cloud functions to trigger workflows
* **Cross-service communication**: Enable microservices to trigger agent workflows
* **Third-party integrations**: Allow external tools and platforms to execute your agent's capabilities

## How it works

The API Trigger block creates an HTTP endpoint that external systems can use to trigger your blueprint.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-flow.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f4492dc843b55552043b95cd95250ab9" alt="API trigger flow showing how external systems send requests to endpoints that trigger blueprint execution" data-og-width="2485" width="2485" data-og-height="1860" height="1860" data-path="images/agent-builder/api-trigger-flow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-flow.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a11107a62acb2322915cba291a8e48e5 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-flow.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=438c45b1276076e713f2295cd00d0145 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-flow.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=15b1d89e555431f0faabdc3e67a29b39 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-flow.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=c621f53c4b74796224f466e17b63d9a8 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-flow.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b2d67aac1ba059b63545fe5d8c857a76 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-flow.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=323c6b488ee44a751694d478c6a1c9c3 2500w" />

Here's what happens when you add an API Trigger block:

### Endpoint creation

The block creates two HTTP endpoints using your agent and blueprint IDs:

* A synchronous endpoint for real-time responses
* An asynchronous endpoint for long-running tasks

### Request handling

When an external system calls your endpoint:

* The request body must contain an `inputs` field with your data
* Your blueprint receives this data as `@{result.inputs}`
* Your blueprint executes with this input data

<Tip>
  #### Accessing the payload data

  `@{result}` is only available in the block that immediately follows the API Trigger block. For subsequent blocks, you have two options to access the payload data:

  1. **Use a Set State block**: Make the first block after API Trigger a Set State block to store the payload data for use throughout your blueprint
  2. **Access via block ID**: Use `@{results.[api_trigger_block_id]}` where `[api_trigger_block_id]` is the unique identifier found in the API Trigger block's configuration menu
</Tip>

### Return values

To send data back to the API caller:

* Add a [**Return Value**](/blueprints/returnvalue) block at the end of your blueprint. The value from this block becomes the API response
* For synchronous calls, the result is the final event in the SSE stream
* For asynchronous calls, the result is available when polling the job status endpoint

### Blueprint structure requirements

When building blueprints that will be triggered via API, ensure your workflow ends with a [**Return Value**](/blueprints/returnvalue) block:

1. **Start with API Trigger**: Begin your blueprint with the API Trigger block
2. **Process your logic**: Add all the blocks needed for your workflow
3. **End with Return Value**: Always finish with a Return Value block to specify what gets returned to the API caller

**Example blueprint structure:**

```
API Trigger → [Your workflow blocks] → Return Value
```

The Return Value block returns any value as a string. If your blueprint returns a JSON object, it will be serialized as a JSON string. You may need to parse it using `JSON.parse()` in JavaScript or `json.loads()` in Python to access the individual fields.

## API endpoint

When you add an **API Trigger** block to your blueprint, it creates a public HTTP endpoint that you can use to trigger your blueprint. You can either use the synchronous endpoint for real-time execution and to get the result as soon as possible, or the asynchronous endpoint for long-running tasks. The asynchronous endpoint returns a job ID that you can poll for status updates and results.

### Authentication

All API calls require authentication using a Bearer token in the Authorization header:

```
Authorization: Bearer <your_api_key>
```

Learn how to [create and manage API keys](/api-reference/api-keys).

### Synchronous endpoint

The endpoint URL follows this pattern:

```
POST https://api.writer.com/v1/agents/{agent_id}/blueprints/{blueprint_id}
```

Where:

* `{agent_id}` is the unique identifier for your deployed agent. You can find this in the URL of your agent's page in the [Agent Builder](https://app.writer.com/agents) or via the [/agents API endpoint](#list-available-agents-and-blueprints).
* `{blueprint_id}` is the unique identifier for your blueprint. You find this in **Blueprint ID** field of the blueprint in the Agent Builder UI, or via the [/agents API endpoint](#list-available-agents-and-blueprints).

The synchronous endpoint is used for real-time execution. It accepts a JSON payload and returns [Server-Sent Events (SSE)](https://en.wikipedia.org/wiki/Server-sent_events) with real-time execution status.

### Request format

Send a POST request with a JSON body containing the data you want to pass to your blueprint.

<Warning>
  The `inputs` key is required for the JSON payload. If you don't include it, the API will return an error. Include the rest of your data under the `inputs` key. The value of the `inputs` key can be any JSON-serializable value.
</Warning>

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST "https://api.writer.com/v1/agents/123e4567-e89b-12d3-a456-426614174000/blueprints/ooamr04yng7" \
    -H "Authorization: Bearer <your_api_key>" \
    -H "Content-Type: application/json" \
    -d '{"inputs": {"document_id": "doc_67890", "file_url": "https://storage.example.com/documents/invoice_2024_001.pdf", "document_type": "invoice", "priority": "high"}}'
  ```

  ```python Python theme={null}
  import os
  import requests

  # Note about streaming
  # The Python `requests` library with `stream=True` will collect the entire SSE
  # stream and then process it line by line. For true real-time streaming,
  # consider using libraries like `httpx` or `aiohttp` that support async streaming.

  response = requests.post(
      "https://api.writer.com/v1/agents/123e4567-e89b-12d3-a456-426614174000/blueprints/ooamr04yng7",
      headers={"Authorization": f"Bearer {os.environ.get('WRITER_API_KEY')}"},
      json={"inputs": {"document_id": "doc_67890", "file_url": "https://storage.example.com/documents/invoice_2024_001.pdf", "document_type": "invoice", "priority": "high"}},
      stream=True
  )

  # Process Server-Sent Events stream
  for line in response.iter_lines():
      if line:
          line = line.decode('utf-8')
          if line.startswith('data: '):
              data = line[6:]  # Remove 'data: ' prefix
              if data == '[DONE]':
                  break
              print(f"Received: {data}")
  ```

  ```javascript JavaScript theme={null}
  import fetch from 'node-fetch';

  const response = await fetch(
      "https://api.writer.com/v1/agents/123e4567-e89b-12d3-a456-426614174000/blueprints/ooamr04yng7",
      {
          method: 'POST',
          headers: { 
              'Authorization': `Bearer ${process.env.WRITER_API_KEY}`,
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({
              inputs: { document_id: "doc_67890", file_url: "https://storage.example.com/documents/invoice_2024_001.pdf", document_type: "invoice", priority: "high" }
          })
      }
  );

  // Process Server-Sent Events stream
  const reader = response.body.getReader();
  const decoder = new TextDecoder();

  while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      
      const chunk = decoder.decode(value);
      const lines = chunk.split('\n');
      
      for (const line of lines) {
          if (line.startsWith('data: ')) {
              const data = line.slice(6); // Remove 'data: ' prefix
              if (data === '[DONE]') {
                  return;
              }
              console.log('Received:', data);
          }
      }
  }
  ```
</CodeGroup>

This data you send in the request is available in your blueprint under `@{result.inputs}`; for example, `@{result.inputs.document_id}`, `@{result.inputs.file_url}`, etc.

### Response format

The API returns Server-Sent Events (SSE) with real-time execution status:

```
data: {"status":"in progress","message":null}
data: {"status":"initializing","message":"Initializing session..."}
data: {"status":"validating","message":"Validating blueprint..."}
data: {"status":"executing","message":"Executing blueprint: ooamr04yng7..."}
data: {"status":"running","message":"Blueprint is running. Awaiting output..."}
data: {"status":"processing","message":"Processing blueprint result..."}
data: {"delta":"Document processed and routed to accounting team"}
data: [DONE]
```

### Asynchronous execution

For long-running workflows, you can also use the asynchronous endpoint:

```
POST https://api.writer.com/v1/agents/{agent_id}/blueprints/{blueprint_id}/jobs
```

This returns a job ID that you can poll for status updates using:

```
GET https://api.writer.com/v1/agents/jobs/{job_id}
```

#### Example job result

When you poll the job status, you'll receive a response like this:

```json  theme={null}
{
  "job_id": "6f6919ba-d97f-4315-bddf-191e5c3efb89",
  "agent_id": "5d746de9-73e7-4c0e-b264-a514f672a3f9",
  "blueprint_id": "ooamr04yng7",
  "status": "completed",
  "artifact": "Document processed and routed to accounting team",
  "error": null,
  "started_at": "2025-08-14T22:26:06.259540Z",
  "finished_at": "2025-08-14T22:26:06.700431Z"
}
```

The actual return value from your agent is in the `artifact` field of the JSON response. The `result` field contains metadata about the job execution.

The `artifact` field always contains a string. If your blueprint returns a JSON object, it will be serialized as a JSON string. You may need to parse it using `JSON.parse()` in JavaScript or `json.loads()` in Python to access the individual fields.

#### Creating and polling async jobs

Here is an example of how to create an async job and then poll for results:

<CodeGroup>
  ```bash cURL theme={null}
  # 1. Create the async job
  curl -X POST "https://api.writer.com/v1/agents/123e4567-e89b-12d3-a456-426614174000/blueprints/ooamr04yng7/jobs" \
    -H "Authorization: Bearer <your_api_key>" \
    -H "Content-Type: application/json" \
    -d '{"inputs": {"document_id": "doc_67890", "file_url": "https://storage.example.com/documents/invoice_2024_001.pdf", "document_type": "invoice", "priority": "high"}}'

  # Response: {"job_id": "job_abc123def456", "status": "queued"}

  # 2. Poll for job status and result
  curl -X GET "https://api.writer.com/v1/agents/jobs/job_abc123def456" \
    -H "Authorization: Bearer <your_api_key>"
  ```

  ```python Python theme={null}
  import os
  import requests
  import time

  def create_and_poll_job(agent_id, blueprint_id, inputs):
      # 1. Create the async job
      url = f"https://api.writer.com/v1/agents/{agent_id}/blueprints/{blueprint_id}/jobs"
      headers = {
          'Authorization': f"Bearer {os.environ.get('WRITER_API_KEY')}",
          'Content-Type': 'application/json'
      }
      
      response = requests.post(url, headers=headers, json={'inputs': inputs})
      job_data = response.json()
      job_id = job_data['job_id']
      
      print(f"Job created: {job_id}")
      
      # 2. Poll for completion
      while True:
          poll_url = f"https://api.writer.com/v1/agents/jobs/{job_id}"
          poll_response = requests.get(poll_url, headers=headers)
          job_status = poll_response.json()
          
          print(f"Job status: {job_status['status']}")
          
          if job_status['status'] in ['completed', 'error']:
              return job_status
          
          time.sleep(2)  # Wait 2 seconds before polling again

  # Example usage
  result = create_and_poll_job(
      '123e4567-e89b-12d3-a456-426614174000',
      'ooamr04yng7',
      {'document_id': 'doc_67890', 'file_url': 'https://storage.example.com/documents/invoice_2024_001.pdf', 'document_type': 'invoice', 'priority': 'high'}
  )
  print(f"Final result: {result}")
  print(f"Artifact: {result['artifact']}")
  ```

  ```javascript JavaScript theme={null}
  import fetch from 'node-fetch';

  async function createAndPollJob(agentId, blueprintId, inputs) {
      // 1. Create the async job
      const createResponse = await fetch(
          `https://api.writer.com/v1/agents/${agentId}/blueprints/${blueprintId}/jobs`,
          {
              method: 'POST',
              headers: {
                  'Authorization': `Bearer ${process.env.WRITER_API_KEY}`,
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify({ inputs }),
          }
      );
      
      const jobData = await createResponse.json();
      const jobId = jobData.job_id;
      
      console.log(`Job created: ${jobId}`);
      
      // 2. Poll for completion
      while (true) {
          const pollResponse = await fetch(
              `https://api.writer.com/v1/agents/jobs/${jobId}`,
              {
                  headers: {
                      'Authorization': `Bearer ${process.env.WRITER_API_KEY}`,
                  },
              }
          );
          
          const jobStatus = await pollResponse.json();
          console.log(`Job status: ${jobStatus.status}`);
          
          if (jobStatus.status === 'completed' || jobStatus.status === 'error') {
              return jobStatus;
          }
          
          // Wait 2 seconds before polling again
          await new Promise(resolve => setTimeout(resolve, 2000));
      }
  }

  // Example usage
  createAndPollJob(
      '123e4567-e89b-12d3-a456-426614174000',
      'ooamr04yng7',
      { document_id: 'doc_67890', file_url: 'https://storage.example.com/documents/invoice_2024_001.pdf', document_type: 'invoice', priority: 'high' }
  ).then(result => {
      console.log('Final result:', result);
      console.log('Artifact:', result.artifact);
  });
  ```
</CodeGroup>

### List available agents and blueprints

To see a list of all your agents and blueprints, you can use the following API endpoint:

```
GET https://api.writer.com/v1/agents?type=builder
```

This returns a list of all your deployed Agent Builder agents and includes any API-triggered blueprints associated with them. You can then use the agent and blueprint IDs to trigger the blueprint via API.

Below is an example of how to list all your agents and blueprints:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X GET "https://api.writer.com/v1/agents?type=builder" \
    -H "Authorization: Bearer <your_api_key>"
  ```

  ```python Python theme={null}
  import os
  import requests

  response = requests.get(
      "https://api.writer.com/v1/agents?type=builder",
      headers={"Authorization": f"Bearer {os.environ.get('WRITER_API_KEY')}"}
  )

  print(response.json())
  ```

  ```javascript JavaScript theme={null}
  import fetch from 'node-fetch';

  const response = await fetch(
      "https://api.writer.com/v1/agents?type=builder",
      { headers: { Authorization: `Bearer ${process.env.WRITER_API_KEY}` } }
  );

  console.log(await response.json());
  ```
</CodeGroup>

## Testing

You can test your API trigger using the **Run blueprint** button in the Agent Builder editor.

Under **Test your trigger** in the API Trigger block, you can provide sample data for testing without making actual HTTP requests.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-run-blueprint.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=46f6d38ae7deb7849e2acfbba54fb4cf" alt="" data-og-width="2294" width="2294" data-og-height="1594" height="1594" data-path="images/agent-builder/api-trigger-run-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-run-blueprint.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=be09132cc72ce6bf93f53bb107ddfab5 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-run-blueprint.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=623b73372b10db86d3a9b489d88716a2 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-run-blueprint.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=fdafc8c41f54393751d8b973bf827587 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-run-blueprint.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=02cc034485efb2bc0c2553c4e9ac5954 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-run-blueprint.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b2fca547c64c3a7e4229b51cbaf30069 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/api-trigger-run-blueprint.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=abbc1fbcf01ebf5b6cd121e3d7eba4c7 2500w" />

You can also test your API trigger by sending a POST request to the API endpoint.

## Troubleshooting

### Common issues and solutions

#### I can't see or trigger my agent via the API

**Problem**: Your agent doesn't appear in the API or you get errors when trying to trigger it.

**Solution**: Check that your agent is deployed. Only deployed agents are accessible via the API.

#### I don't see my blueprint when looking via the API

**Problem**: Your blueprint doesn't show up in the list of available blueprints for your agent.

**Solution**: Ensure your blueprint starts with an **API Trigger** block. Only blueprints that begin with an API Trigger block are exposed via the API.

#### The blueprint isn't returning anything

**Problem**: Your blueprint executes but doesn't return any data to the API caller.

**Solution**: Make sure you have a [**Return Value**](/blueprints/returnvalue) block at the end of your blueprint workflow. This block is required to return data to the API caller.

#### My blueprint isn't receiving any input values

**Problem**: You can't access the data you sent in your API request.

**Solution**: Remember that your data is nested under the `inputs` key. Use `@{result.inputs.field_name}` instead of `@{result.field_name}`.

### Debugging tips

Since there are limited logs and execution visibility, use the **Return Value** block for debugging:

**Test payload structure**: Create a simple blueprint with just `API Trigger → Return Value` and set the return value to `@{result}`. This will show you exactly what data structure the blueprint is receiving.

**Test specific values**: Use `@{result.inputs}` to see just the inputs portion of your payload.

**Test state variables**: Return `@{state[key]}` to see the value of a specific state variable in your blueprint execution.

**Note**: Since `@{result}` is only available in the block immediately following the API Trigger, consider using a Set State block as your first block to store the payload data for debugging purposes.

## Next steps

* Learn how to [add file inputs and parse PDFs](/agent-builder/summarize-pdfs)
* Explore [tool calling](/agent-builder/tool-calling) for intelligent integrations with external tools
* Build [data tables with DataFrames](/agent-builder/dataframes) to display structured data
* Add [custom Python code](/agent-builder/python-code) to extend your agent's capabilities

<feedback />
