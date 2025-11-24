# Source: https://docs.anchorbrowser.io/advanced/tasks.md

# Automation Tasks

> Create, manage, and execute reusable browser automation tasks

## Overview

The Tasks API enables you to **create, version, and execute reusable browser automation code** in your Anchor Browser sessions. Tasks allow you to:

<img className="mx-auto" src="https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-dashboard.webp?fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=e09aa109ce8d538f24e6ec9f962aee96" alt="Tasks dashboard showing task management interface" data-og-width="3114" width="3114" data-og-height="990" height="990" data-path="images/tasks-dashboard.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-dashboard.webp?w=280&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=402d433a756f4e156b514486f590ef4f 280w, https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-dashboard.webp?w=560&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=2bdebe264cab33f3181ea8365a706842 560w, https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-dashboard.webp?w=840&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=69819a8b4ae6165048f21b31e817f930 840w, https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-dashboard.webp?w=1100&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=9a081e4540b6ec2c02479956bdaed79c 1100w, https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-dashboard.webp?w=1650&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=bf7882bf4eb1281c5aeb9cea27015f2d 1650w, https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-dashboard.webp?w=2500&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=329285515c213c06247e7cd8c2f115cf 2500w" />

<Info>
  Tasks are executed in a secure sandbox environment and can access the full Anchor Browser API for automation capabilities.
</Info>

## Creating Your First Task

## Writing Task Code

For reliable execution, **follow these guidelines:**

* Write your **code in TypeScript.**
* **Export** a single **default async function.**
* In that function, **return** whatever your workflow requires as **output** (e.g., status, messages, domain data).

<Info>
  Tasks can receive values as inputs. **All input names must be prefixed with `ANCHOR_`**
</Info>

### Basic Task Example

<CodeGroup>
  ```typescript typescript theme={null}
  import AnchorClient from 'anchorbrowser';

  // Initialize the Anchor client with your API key
  const anchorClient = new AnchorClient({
      apiKey: process.env.ANCHOR_API_KEY,
  });

  // Export the main function as the default export
  export default async function run() {

      // Create a new browser instance
      const browser = await anchorClient.browser.create();
      const page = browser.contexts()[0].pages()[0];

      // Access input values
      const targetUrl = process.env.ANCHOR_TARGET_URL;
      const maxPages = parseInt(process.env.ANCHOR_MAX_PAGES || '10');

      // Implement your automation logic
      await page.goto(targetUrl);
      console.log(`Scraping up to ${maxPages} pages from ${targetUrl}`);

      // Always close the browser when done
      await browser.close();

      // Return a result object with success status and message
      return {
          success: true,
          message: 'Task completed successfully'
      };
  }
  ```
</CodeGroup>

### Using the SDK

Create your task in Anchor:

<Steps>
  <Step title="Save your typescript code as a .ts file">
    <Warning>
      Make sure it follows the guidelines from above.
    </Warning>
  </Step>

  <Step title="Get the base64 version of the file">
    Run the script to show your base64 file version

    ```bash terminal theme={null}
    # Convert your TypeScript file to base64
    base64 -i your-task.ts
    ```

    Copy the output for later.
  </Step>

  <Step title="Create your Task in Anchor">
    <CodeGroup>
      ```typescript node.js theme={null}
      import Anchorbrowser from 'anchorbrowser';

      const client = new Anchorbrowser({
        apiKey: process.env.ANCHORBROWSER_API_KEY,
      });

      // Create a new task
      const task = await client.task.create({
        name: 'example-task',
        language: 'typescript',
        description: 'A task to scrape product information from e-commerce sites',
        code: "<base64-string>" // Replace with the output of the last step.
      });

      const taskId = task.data.id
      console.log('Task created:', taskId);
      ```

      ```python python theme={null}
      import os
      from anchorbrowser import Anchorbrowser

      client = Anchorbrowser(
          api_key=os.environ.get("ANCHORBROWSER_API_KEY")
      )

      # Create a new task
      task = client.task.create(
          name="example-task",
          language="typescript",
          description="A task to scrape product information from e-commerce sites",
          code="<base64-string>" # Replace with the output of the last step.
      )

      # Save the id for later
      task_id = task.data.id
      print(f"Task created: {task_id}")
      ```
    </CodeGroup>
  </Step>

  <Step title="Running Tasks">
    <CodeGroup>
      ```typescript node.js theme={null}
      // Run the task with inputs
      const execution = await client.task.run({
        taskId: taskId,
        version: 'draft',
        inputs: {
          ANCHOR_TARGET_URL: 'https://example.com',
          ANCHOR_MAX_PAGES: '10'
        }
      });

      console.log('Task execution started:', execution.data);
      ```

      ```python python theme={null}
      # Run the task with inputs
      execution = client.task.run(
          task_id=task_id,
          version="draft",
          inputs={
              "ANCHOR_TARGET_URL": "https://example.com",
              "ANCHOR_MAX_PAGES": "10"
          }
      )

      print(f"Task execution started: {execution.data}")
      ```
    </CodeGroup>

    <img className="mx-auto" src="https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-run.webp?fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=490b5c70ac63d3e3679f00b57ab07a57" alt="Running a task with inputs" data-og-width="3394" width="3394" data-og-height="1860" height="1860" data-path="images/tasks-run.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-run.webp?w=280&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=ecd2573a4b04cd5434164c79c29aed51 280w, https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-run.webp?w=560&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=27bf90d63c0a344a98e8e9ac7ea36c28 560w, https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-run.webp?w=840&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=5c0691a4162ef9063a9b124912135c62 840w, https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-run.webp?w=1100&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=b75f0ffee38daef512a7453f72a7e47d 1100w, https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-run.webp?w=1650&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=f5c8df3e1aefb4bd75970063ad871fd8 1650w, https://mintcdn.com/anchor-b3ec2715/tCZ8ZZdZSDFlzsaC/images/tasks-run.webp?w=2500&fit=max&auto=format&n=tCZ8ZZdZSDFlzsaC&q=85&s=4d194a4374e773c0d481515d66c65c31 2500w" />
  </Step>

  <Step title="Deploy Task">
    <CodeGroup>
      ```typescript node.js theme={null}
      // Deploy the task to make it available for production use
      const deployment = await client.task.deploy({
        taskId: taskId,
        code: "<base64-string>", // Replace with the base64 encoded code
        language: 'typescript',
        description: 'Optional description for this version'
      });

      console.log('Task deployed:', deployment.data);
      ```

      ```python python theme={null}
      # Deploy the task to make it available for production use
      deployment = client.task.deploy(
          task_id=task_id,
          code="<base64-string>",  # Replace with the base64 encoded code
          language="typescript",
          description="Optional description for this version"
      )

      print(f"Task deployed: {deployment.data}")
      ```
    </CodeGroup>
  </Step>
</Steps>

## Async Task

By default, task execution is **synchronous** - the API call waits for the task to complete before returning results. For long-running tasks, you can use **asynchronous execution** to start the task and check results later.

### Running Tasks Asynchronously

When you set `async: true`, the API returns immediately with a confirmation that the task has started. You can then poll for execution results using the task execution history endpoint.

<CodeGroup>
  ```typescript node.js theme={null}
  // Run the task asynchronously
  const execution = await client.task.run({
    taskId: taskId,
    version: '1',
    async: true, // Enable async execution
    inputs: {
      ANCHOR_TARGET_URL: 'https://example.com',
      ANCHOR_MAX_PAGES: '10'
    }
  });

  console.log('Task execution started:', execution.data);
  // Response: { async: true, success: true, message: 'Task execution started', taskId: '...' }
  ```

  ```python python theme={null}
  # Run the task asynchronously
  execution = client.task.run(
      task_id=task_id,
      version="1",
      async=True,  # Enable async execution
      inputs={
          "ANCHOR_TARGET_URL": "https://example.com",
          "ANCHOR_MAX_PAGES": "10"
      }
  )

  print(f"Task execution started: {execution.data}")
  # Response: {'async': True, 'success': True, 'message': 'Task execution started', 'taskId': '...'}
  ```
</CodeGroup>

### Checking Execution Results

After starting an async task, you can check its execution status and results by querying the task's execution history endpoint:

<CodeGroup>
  ```typescript node.js theme={null}
  // Get execution results
  const response = await fetch(`https://api.anchorbrowser.io/v1/task/${taskId}/executions?page=1&limit=1&version=1`, {
    headers: {
      'anchor-api-key': process.env.ANCHORBROWSER_API_KEY,
      'Content-Type': 'application/json'
    }
  });

  const results = await response.json();
  console.log('Execution results:', results.data);
  ```

  ```python python theme={null}
  import os
  import requests

  # Get execution results
  response = requests.get(
      f"https://api.anchorbrowser.io/v1/task/{task_id}/executions",
      params={
    #     "status": "success",  #Optional: filter by status (success, failure, timeout, cancelled)
          "page": 1,
          "limit": 1,
          "version": "1"    # Optional: filter by version
      },
      headers={
          "anchor-api-key": os.environ.get("ANCHORBROWSER_API_KEY"),
          "Content-Type": "application/json"
      }
  )

  results = response.json()
  print(f"Execution results: {results['data']}")
  ```
</CodeGroup>

**Example response:**

```json  theme={null}
{
  "data": {
    "results": [
      {
        "id": "550e8400-e29b-41d4-a716-446655440000",
        "status": "success",
        "executionTime": 5234,
        "output": "{\"success\": true, \"message\": \"Task completed successfully\"}",
        "errorMessage": null,
        "startTime": "2024-01-15T10:30:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 1,
      "total": 1,
      "totalPages": 1
    }
  }
}
```

<Warning>
  Async task executions have a maximum duration of **3 hours**. Tasks that exceed this limit will be automatically cancelled.

  **Note:** Tasks must be deployed (not just in draft) to appear in the execution results list.
</Warning>

### Polling for Results

For async tasks, you can implement polling to wait for completion:

<CodeGroup>
  ```typescript node.js theme={null}
  // Poll for task completion
  async function waitForTaskCompletion(taskId: string, maxAttempts: number = 60) {
    for (let i = 0; i < maxAttempts; i++) {
      const response = await fetch(`https://api.anchorbrowser.io/v1/task/${taskId}/executions?page=1&limit=1`, {
        headers: {
          'anchor-api-key': process.env.ANCHORBROWSER_API_KEY,
          'Content-Type': 'application/json'
        }
      });
      
      const results = await response.json();
      const latestResult = results.data?.results?.[0];
      if (latestResult) {
        if (latestResult.status === 'success' || latestResult.status === 'failure') {
          return latestResult;
        }
      }
      
      // Wait 2 seconds before next poll
      await new Promise(resolve => setTimeout(resolve, 2000));
    }
    
    throw new Error('Task execution timeout');
  }

  // Usage
  const execution = await client.task.run({
    taskId: taskId,
    version: '1',
    async: true,
    inputs: { ANCHOR_TARGET_URL: 'https://example.com' }
  });

  const result = await waitForTaskCompletion(taskId);
  console.log('Task completed:', result);
  ```

  ```python python theme={null}
  import os
  import time
  import requests

  # Poll for task completion
  def wait_for_task_completion(task_id: str, max_attempts: int = 60):
      for _ in range(max_attempts):
          response = requests.get(
              f"https://api.anchorbrowser.io/v1/task/{task_id}/executions",
              params={"page": 1, "limit": 1},
              headers={
                  "anchor-api-key": os.environ.get("ANCHORBROWSER_API_KEY"),
                  "Content-Type": "application/json"
              }
          )
          
          results = response.json()
          latest_result = results['data']['results'][0] if results['data']['results'] else None
          if latest_result:
              if latest_result['status'] in ['success', 'failure']:
                  return latest_result
          
          # Wait 2 seconds before next poll
          time.sleep(2)
      
      raise Exception('Task execution timeout')

  # Usage
  execution = client.task.run(
      task_id=task_id,
      version="1",
      async=True,
      inputs={"ANCHOR_TARGET_URL": "https://example.com"}
  )

  result = wait_for_task_completion(task_id)
  print(f"Task completed: {result}")
  ```
</CodeGroup>

## Support

For additional help with the Tasks API:

* Check the [API Reference](/api-reference/browser-sessions/start-browser-session/) for detailed tasks endpoint documentation
* Contact Anchor Browser support at [support@anchorbrowser.io](mailto:support@anchorbrowser.io)
