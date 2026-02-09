# Source: https://docs.anchorbrowser.io/agentic-browser-control/async-perform-web-task.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Async Perform Web Task

> Run perform-web-task asynchronously and poll for results

## Basic Usage

To run `perform-web-task` asynchronously, set the `async` parameter to `true` in your request. The API will return immediately with a `workflow_id` that you can use to poll for results.

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
  apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  // Start async task
  const response = await anchorClient.tools.performWebTask({
  prompt: 'Extract the main heading and first paragraph from the page',
  url: 'https://docs.anchorbrowser.io',
  async: true
  });

  console.log('Workflow ID:', response.data.workflow_id);
  console.log('Status:', response.data.status);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  # Start async task
  response = anchor_client.tools.perform_web_task(
      prompt='Extract the main heading and first paragraph from the page',
      url='https://docs.anchorbrowser.io',
      async_=True
  )

  print('Workflow ID:', response.data.workflow_id)
  print('Status:', response.data.status)
  ```
</CodeGroup>

<Expandable title="Parameters">
  ## Parameters

  The async `perform-web-task` accepts the following parameters:

  | Parameter            | Type    | Required | Description                                                                                                                                                     |
  | -------------------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `prompt`             | string  | Yes      | The task to be autonomously completed                                                                                                                           |
  | `url`                | string  | No       | The URL of the webpage. If not provided, the tool will use the current page in the session                                                                      |
  | `sessionId`          | string  | No       | An optional browser session identifier to reference an existing running browser session. When passed, the tool will be executed on the provided browser session |
  | `async`              | boolean | No       | Whether to run the task asynchronously. If `true`, the task will be run asynchronously and the response will include a workflow ID. Defaults to `false`         |
  | `agent`              | string  | No       | The AI agent to use for task completion. Options: `browser-use` (default), `openai-cua`, `gemini-computer-use`, `anthropic-cua`                                 |
  | `provider`           | string  | No       | The AI provider to use for task completion. Options: `openai`, `gemini`, `groq`, `azure`, `xai`                                                                 |
  | `model`              | string  | No       | The specific model to use for task completion. See [Available Models](/agentic-browser-control/ai-task-completion#available-models) for more information        |
  | `detect_elements`    | boolean | No       | Enable element detection for better interaction accuracy. Improves the agent's ability to identify and interact with UI elements                                |
  | `human_intervention` | boolean | No       | Allow human intervention during task execution. When enabled, the agent can request human input for ambiguous situations                                        |
  | `max_steps`          | integer | No       | Maximum number of steps the agent can take to complete the task. Defaults to `200`                                                                              |
  | `secret_values`      | object  | No       | Secret values to pass to the agent for secure credential handling. Keys and values are passed as environment variables to the agent                             |
  | `highlight_elements` | boolean | No       | Whether to highlight elements during task execution for better visibility                                                                                       |
  | `output_schema`      | object  | No       | JSON Schema defining the expected structure of the output data                                                                                                  |
</Expandable>

## Polling for Results

After starting an async task, you'll receive a `workflow_id` in the response. Use this ID to poll the status endpoint until the task completes.

### Status Endpoint

<CodeGroup>
  ```javascript node.js theme={null}
  const statusResponse = await anchorClient.tools.getPerformWebTaskStatus(workflowId);

  // Status can be: 'RUNNING', 'COMPLETED', or 'FAILED'
  if (statusResponse.data.status === 'RUNNING') {
      console.log('Still running...');
  } else if (statusResponse.data.status === 'COMPLETED') {
      console.log('Result:', statusResponse.data.result);
  } else if (statusResponse.data.status === 'FAILED') {
      console.error('Error:', statusResponse.data.error);
  }
  ```

  ```python python theme={null}
  status_response = anchor_client.tools.get_perform_web_task_status(workflow_id)

  # Status can be: 'RUNNING', 'COMPLETED', or 'FAILED'
  if status_response['data']['status'] == 'RUNNING':
      print('Still running...')
  elif status_response['data']['status'] == 'COMPLETED':
      print('Result:', status_response['data']['result'])
  elif status_response['data']['status'] == 'FAILED':
      print('Error:', status_response['data']['error'])
  ```
</CodeGroup>

### Response Statuses

* **`RUNNING`**: The workflow is currently executing
* **`COMPLETED`**: The workflow has completed. The `result` field contains the task output as a string.

<Note>
  The status will be `COMPLETED` even if the agent fails to complete the task, since the workflow execution itself succeeded. Always check the `result` field to verify whether the agent completed the task successfully or encountered an error.
</Note>

* **`FAILED`**: The workflow has failed. The `error` field contains the error message

## Complete Example

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  (async () => {
    const anchorClient = new Anchorbrowser({
      apiKey: process.env.ANCHORBROWSER_API_KEY
    });

    // Start multiple async tasks in parallel
    const responses = await Promise.all([
      anchorClient.tools.performWebTask({
        prompt: 'Extract the main heading',
        url: 'https://docs.anchorbrowser.io',
        async: true
      }),
      anchorClient.tools.performWebTask({
        prompt: 'Get the first paragraph',
        url: 'https://example.com',
        async: true
      })
    ]);

    const workflowIds = responses.map(response => response.data.workflow_id);
    console.log('Started', workflowIds.length, 'tasks');

    // Poll all tasks
    const results = await Promise.all(
      workflowIds.map(async (wokflowId) => {
        let status = 'RUNNING';
        while (status === 'RUNNING') {
          await new Promise(resolve => setTimeout(resolve, 2000));
          const statusResponse = await anchorClient.tools.getPerformWebTaskStatus(wokflowId);
          status = statusResponse.data.status;

          if (status === 'COMPLETED') {
            return statusResponse.data.result;
          } else if (status === 'FAILED') {
            throw new Error(statusResponse.data.error);
          }
        }
      })
    );

    console.log('All tasks completed:', results);
  })();
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os
  import time
  import requests

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  # Start multiple async tasks in parallel
  responses = [
      anchor_client.tools.perform_web_task(
          prompt='Extract the main heading',
          url='https://docs.anchorbrowser.io',
          async_=True
      ),
      anchor_client.tools.perform_web_task(
          prompt='Get the first paragraph',
          url='https://example.com',
          async_=True
      )
  ]

  workflow_ids = [response.data.workflow_id for response in responses]
  print('Started', len(workflow_ids), 'tasks')

  # Poll all tasks
  results = []
  for workflow_id in workflow_ids:
      status = 'RUNNING'
      while status == 'RUNNING':
          time.sleep(2)

          status_response = anchor_client.tools.get_perform_web_task_status(workflow_id)
          status = status_response['data']['status']

          if status == 'COMPLETED':
              results.append(status_response['data']['result'])
              break
          elif status == 'FAILED':
              raise Exception(status_response['data']['error'])

  print('All tasks completed:', results)
  ```
</CodeGroup>
