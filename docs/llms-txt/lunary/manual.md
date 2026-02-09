# Source: https://docs.lunary.ai/docs/integrations/python/manual.md

# Source: https://docs.lunary.ai/docs/integrations/javascript/manual.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Manual Usage

If your application requires more flexibility and you can't use the `wrap` helpers, you can use the `trackEvent` method directly.

The `trackEvent` method is used to track and log runs in your application. It takes three parameters: `type`, `event`, and `data`.

### Parameters:

| Parameter | Type                                  | Description                   |
| --------- | ------------------------------------- | ----------------------------- |
| `type`    | `agent`, `tool`, `llm` or `chain`     | The type of the run           |
| `event`   | `start`, `end`, `error` or `feedback` | The name of the event.        |
| `data`    | `Partial<RunEvent>`                   | Data associated with the run. |

The `RunEvent` type is composed of the following properties:

| Field       | Type                                     | Description                               | Required |
| ----------- | ---------------------------------------- | ----------------------------------------- | -------- |
| runId       | string                                   | Unique identifier                         | Yes      |
| input       | JSON                                     | Input data                                | No       |
| output      | JSON                                     | Output data                               | No       |
| tokensUsage | `{ completion: number, prompt: number }` | Number of tokens used in the run.         | No       |
| userId      | string                                   | The user ID.                              | No       |
| userProps   | JSON                                     | The user properties.                      | No       |
| parentRunId | string                                   | The parent run ID.                        | No       |
| extra       | JSON                                     | Any extra data associated with the event. | No       |
| tags        | string\[]                                | Tags associated with the event.           | No       |
| error       | `{ message: string, stack?: string }`    | Error object if an error occurred.        | No       |

### Example to track an agent:

```ts  theme={null}
// Assuming you have an instance of Lunary
// Define your agent function
async function myAgentFunction(input: string): Promise<string> {
  // Start of the agent function
  const runId = 'unique_run_id'; // Replace with a unique run ID for each run
  lunary.trackEvent('agent', 'start', {
    runId,
    input,
    name: 'MySuperAgent',
    extra: { extra: 'data' },
    tags: ['tag1', 'tag2']
  });

  try {

    const output = await someAsyncOperation(input);

    lunary.trackEvent('agent', 'end', {
      runId,
      output,
    });

    return output;
  } catch (error) {

    lunary.trackEvent('agent', 'error', {
      runId,
      error: error.message, // Replace with actual error message
      name: 'myAgentFunction'
    })
  }
}

// Use the agent function
myAgentFunction('some input')
  .then(output => console.log('Output:', output))
  .catch(error => console.error('Error:', error));

```

### Using the `parentRunId` parameter

To create traces with sub-agents, you can use the `parentRunId` parameter to link child runs.

```ts  theme={null}
async function someTool(input: string, parentRunId: string): Promise<string> {

  const subRunId = 'sub_run_id'; 
  lunary.trackEvent('tool', 'start', {
    runId: subRunId,
    parentRunId,
    input,
    name: 'MyTool',
    tags: ['tag1', 'tag2']
  });

  try {

    const output = await someAsyncOperation(input);

    lunary.trackEvent('tool', 'end', {
      runId: subRunId,
      parentRunId,
      output,
    });

    return output;
  } catch (error) {

    lunary.trackEvent('tool', 'error', {
      runId: subRunId,
      parentRunId,
      error: error.message, // Replace with actual error message
      name: 'mySubAgentFunction'
    });

  }
}

// Use the main agent function
myAgentFunction('some input')
  .then(output => console.log('Output:', output))
  .catch(error => console.error('Error:', error));
```
