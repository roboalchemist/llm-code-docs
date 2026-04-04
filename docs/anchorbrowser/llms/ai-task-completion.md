# Source: https://docs.anchorbrowser.io/agentic-browser-control/ai-task-completion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Task Completion

Anchor Browser delivers a state-of-the-art 89% Score on the industry-standard benchmark WebVoyager, leveraging browser-use as a core component of the automation capability.

<video autoPlay muted loop playsInline className="w-full aspect-video" src="https://mintcdn.com/anchor-b3ec2715/PYJUK4ovynFtrEAT/images/video-playground.mp4?fit=max&auto=format&n=PYJUK4ovynFtrEAT&q=85&s=9597d75a98b85978c08b9861c99474f4" data-path="images/video-playground.mp4" />

## The agent task method

Anchor Browser provides within its SDK the `agent.task` method that enables natural language control over web browsing sessions. This capability allows you to **automate complex web tasks without coding the whole flow.**

<Note>
  Looking for Tasks? Visit the [Tasks Page](/advanced/tasks).
</Note>

### Code Example

<CodeGroup>
  ```javascript node.js theme={null}
  import Anchorbrowser from 'anchorbrowser';

  const anchorClient = new Anchorbrowser({
    apiKey: process.env.ANCHORBROWSER_API_KEY
  });

  const response = await anchorClient.agent.task(
    'Extract the main heading',                     // Required
    {
      taskOptions: {
        url: 'https://example.com',                 // Either sessionId or url is required
        humanIntervention: false,                   // Disable human intervention during task execution (disabled by default)
        detectElements: true,                       // Improves the agent's ability to identify and interact with UI elements
        maxSteps: 40,                               // Maximum number of steps the agent can take
        agent: 'browser-use',                       // browser-use (default), openai-cua, or gemini-computer-use
        provider: 'openai',                         // For browser-use agent only, openai, gemini, groq, azure, xai
        model: 'gpt-5',                             // For browser-use agent only, see model list below
        extendedSystemMessage: 'Focus on extracting the main heading from the page',
        secretValues: {                             // Secret values to pass to the agent for secure credential handling
          API_KEY: 'your-secret-key'
        }
      }
    }
  );

  console.log(response);
  ```

  ```python python theme={null}
  from anchorbrowser import Anchorbrowser
  import os

  anchor_client = Anchorbrowser(api_key=os.environ.get("ANCHORBROWSER_API_KEY"))

  response = anchor_client.agent.task(
      'Extract the main heading',                    # Required
      task_options={
          url='https://example.com',                 # Either session_id or url is required
          human_intervention=False,                  # Disable human intervention during task execution (disabled by default)
          detect_elements=True,                      # Improves the agent's ability to identify and interact with UI elements
          max_steps=40,                              # Maximum number of steps the agent can take
          agent='browser-use',                       # browser-use (default), openai-cua, or gemini-computer-use
          provider='openai',                           # For browser-use agent only, openai, gemini, groq, azure, xai
          model='gpt-5',               # For browser-use agent only, see model list below
          extended_system_message='Focus on extracting the main heading from the page',
          secret_values={                            # Secret values to pass to the agent for secure credential handling
              'API_KEY': 'your-secret-key'
          }
      }
  )

  print(response)
  ```
</CodeGroup>

## Structured Output

The AI object can also be used to extract structured data from the browser. This is done by providing a **JSON schema** to the AI object, which will then return the structured data.
The following demonstrates using **Zod** and **Pydantic** to utilize the structured output capability.

<CodeGroup>
  ```javascript node.js theme={null}
  import { z } from 'zod';
  import { zodToJsonSchema } from 'zod-to-json-schema';

  const anchorClient = new Anchorbrowser()

  // Define the expected output structure using Zod schema
  const outputSchema = z.object({
    nodes_cpu_usage: z.array(
      z.object({
        node: z.string(),                 // Node name
        cluster: z.string(),              // Cluster identifier
        cpu_avg_percentage: z.number(),   // CPU usage percentage
      })
    )
  });

  // Execute the AI task with structured output
  const result = await anchorClient.agent.task('Collect the node names and their CPU average %', {
    taskOptions: {
      outputSchema: zodToJsonSchema(outputSchema), // Convert to JSON Schema
      url: 'https://play.grafana.org/a/grafana-k8s-app/navigation/nodes?from=now-1h&to=now&refresh=1m',
    }
  });
  console.info(result);
  ```

  ```python python theme={null}
  # Define data models using Pydantic for structured output
  class NodeCpuUsage(BaseModel):
      node: str                    # Node name
      cluster: str                 # Cluster identifier
      cpu_avg_percentage: float    # CPU usage percentage

  class OutputSchema(BaseModel):
      nodes_cpu_usage: List[NodeCpuUsage]  # List of node CPU usage data

  # Create task payload with structured output schema
  task_payload = {
      'prompt': 'Collect the node names and their CPU average %',
      'output_schema': OutputSchema.model_json_schema()  # Convert to JSON Schema
  }

  result = anchor_client.agent.task('Collect the node names and their CPU average %',
      task_options={
          'output_schema': OutputSchema.model_json_schema(),
          'url': 'https://play.grafana.org/a/grafana-k8s-app/navigation/nodes?from=now-1h&to=now&refresh=1m',
      }
  )
  print(result)
  ```
</CodeGroup>

<Expandable title="Configuration Options">
  ## Configuration Options

  The AI agent can be configured with the following parameters:

  <Note>
    Parameter names use `snake_case` in Python and `camelCase` in JavaScript/TypeScript (e.g., `max_steps` vs `maxSteps`).
  </Note>

  * **agent** (string): AI agent to use (`browser-use`, `openai-cua`, `gemini-computer-use`). Defaults to `browser-use`.
  * **secret\_values** | **secretValues** (object): Secret values to pass to the agent for secure credential handling.
  * **human\_intervention** | **humanIntervention** (boolean): Allow human intervention during task execution.
  * **provider** (string): AI provider to use (`openai`, `gemini`, `groq`, `azure`, `xai`).
  * **model** (string): Specific model to use (see [Available Models](#available-models) below).
  * **url** (string): Target URL to navigate to before executing the task.
  * **output\_schema** | **outputSchema** (object): JSON Schema defining the expected structure of the output data.
  * **max\_steps** | **maxSteps** (integer): Maximum number of steps the agent can take (default: 40).
  * **detect\_elements** | **detectElements** (boolean): Enable element detection for better interaction accuracy.
  * **extended\_system\_message** | **extendedSystemMessage** (string): Custom system message to provide additional context or instructions to the agent.
  * **use\_vision** | **useVision** (boolean): Enable vision capabilities for enhanced visual understanding.
</Expandable>

## Secret Values

<p>Securely pass credentials and sensitive data to AI agents during task execution. Secret values are not logged and automatically cleaned up after completion.</p>
<p><a href="/agentic-browser-control/secret-values">Learn more about Secret Values →</a></p>

## Available Models For Browser-Use

<Expandable title="Available Models" defaultOpen>
  <Tabs>
    <Tab title="OpenAI">
      <div className="grid grid-cols-3 gap-2">
        <div>gpt-5.2</div>
        <div>gpt-5</div>
        <div>gpt-5-mini</div>
        <div>gpt-5-nano</div>
        <div>gpt-4o</div>
        <div>gpt-4o-mini</div>
        <div>gpt-4.1</div>
        <div>gpt-4.1-mini</div>
      </div>
    </Tab>

    <Tab title="Gemini">
      <div className="grid grid-cols-3 gap-2">
        <div>gemini-3-flash-preview</div>
        <div>gemini-3-pro-preview</div>
        <div>gemini-2.5-flash</div>
        <div>gemini-2.5-flash-lite</div>
        <div>gemini-2.5-pro</div>
        <div>gemini-2.0-flash</div>
        <div>gemini-2.0-flash-exp</div>
        <div>gemini-2.0-flash-lite</div>
      </div>
    </Tab>

    <Tab title="Groq">
      <div className="grid grid-cols-3 gap-2">
        <div>openai/gpt-oss-120b</div>
        <div>meta-llama/llama-4-maverick-17b-128e-instruct</div>
        <div>meta-llama/llama-4-scout-17b-16e-instruct</div>
        <div>moonshotai/kimi-k2-instruct</div>
      </div>
    </Tab>

    <Tab title="Azure">
      <div className="grid grid-cols-3 gap-2">
        <div>o4-mini</div>
        <div>o3</div>
        <div>o3-mini</div>
        <div>o1</div>
      </div>
    </Tab>
  </Tabs>
</Expandable>
