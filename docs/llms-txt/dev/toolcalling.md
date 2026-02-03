# Source: https://dev.writer.com/blueprints/toolcalling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tool calling

Connects the Agent to external tools to complete tasks it cannot handle directly.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=8210f07c636bcd842fab8a6a31e905dd" alt="" data-og-width="2850" width="2850" data-og-height="1474" height="1474" data-path="images/agent-builder/tool-calling-block-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3773a683a2da821b78b969664f1f496f 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=33e268b579da79a4b088ae4f25bc568d 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=089f200264aa6513b091bbe4d1a9d553 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f20f67014f413d0a35d9310d02e0dd55 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=5cd5dbb18dc2c3cd460508d87ecbb389 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=085c9de29b9c6d8993217f56c3616572 2500w" />

## Overview

The **Tool calling** block enables your agent to interact with external systems, APIs, and custom functions to gather information, perform actions, or execute complex workflows that extend beyond the model's built-in capabilities.

When the tool calling block executes, the AI model analyzes the prompt and automatically determines which tools to use, when to use them, and how to combine the results to complete the requested task. The model can make multiple tool calls in sequence and use the results from one tool to inform subsequent tool calls.

## How tool calling works

* **Tool selection**: The model analyzes your prompt and determines which available tools are needed
* **Parameter extraction**: The model extracts the necessary parameters from the prompt and context to call each tool
* **Sequential execution**: Tools are called in the optimal order, with results from previous tools informing subsequent calls
* **Result synthesis**: The model combines all tool results with its own knowledge to generate the final response

To learn more about how tool calling works, see the [Tool calling introduction](/agent-builder/tool-calling-intro) documentation.

## Tool types

The tool calling block supports two types of tools:

* **Function tools**: Custom workflows you build within the blueprint using other blocks
* **Built-in tools**: Pre-configured integrations with external services. Currently only [Knowledge Graphs](/home/knowledge-graph) are supported.

### Function tools

Function tools allow you to define custom logic using other blueprint blocks. Each function tool requires:

* **Tool name**: A unique identifier for the tool
* **Description**: Clear explanation of what the tool does and when to use it
* **Parameters**: Input fields the model should provide when calling the tool
* **Implementation**: The workflow of blocks that execute when the tool is called

<Warning>
  When you implement the chain of blocks that make up a function tool, you must use include a [Return value](/blueprints/returnvalue) block at the end of the chain to return a value to back to the model.
</Warning>

The model uses the tool name and description to determine when to call the tool, and uses the parameter definitions to extract the correct values from the prompt context.

#### Tool definitions

The tool definition for a `Function` tool follows the [JSON Schema](https://json-schema.org/) format. You provide the definition when adding the tool to the **Tool calling** block.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=13a33c67238f7eb1ac80ddd29476d699" alt="" data-og-width="1846" width="1846" data-og-height="800" height="800" data-path="images/agent-builder/add-function-tool-calling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b54f0a8f05551fae83447f715cee6230 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=2fa5c57ba9ab776b735031f4a87c0438 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=9ffb98f8f212775b186b5ce8a0ab1ccc 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a9894b9e75ef29e2d9c62a13ba47477f 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=52b59748d5d3d93c70525f770c121683 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=8149db43b94962e05652c3f7819d8539 2500w" />

The definition has the following structure:

| Parameter               | Type   | Description                                                                                                                      |
| ----------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `name`                  | string | The name of the tool                                                                                                             |
| `description`           | string | A description of what the tool does and when the model should use it                                                             |
| `parameters`            | object | An object containing the tool's input parameters                                                                                 |
| `parameters.type`       | string | The type of the parameter, which is `object` for a JSON schema                                                                   |
| `parameters.properties` | object | An object containing the tool's parameters in the form of a [JSON schema](https://json-schema.org/). See below for more details. |
| `parameters.required`   | array  | An array of the tool's required parameters                                                                                       |

#### Example tool definition

Below is an example of a tool definition that gets the details of a package's shipping status. It takes a tracking number and a carrier name as input parameters and returns the shipping status of the package.

```json  theme={null}
{
  "name": "check_shipping_status",
  "description": "Gets real-time shipping and tracking information for a package",
  "parameters": {
    "type": "object",
    "properties": {
      "tracking_number": {
        "type": "string",
        "description": "The shipping carrier's tracking number"
      },
      "carrier": {
        "type": "string",
        "enum": ["fedex", "ups", "usps", "dhl"],
        "description": "Shipping carrier name"
      }
    },
    "required": ["tracking_number", "carrier"]
  }
}
```

### Knowledge Graph tools

Knowledge Graph tools allow you to connect to one or more [Knowledge Graph](/home/knowledge-graph) to get information about a specific topic.

To add a Knowledge Graph tool, select the Knowledge Graph(s) you want to use from the dropdown of available Knowledge Graphs.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5d140ef33d204a34445d55836a02f8fc" alt="" data-og-width="1924" width="1924" data-og-height="922" height="922" data-path="images/agent-builder/add-kg-tool-calling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=0aa8c6f45f3a923f9d78c7355b88668a 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=73e609e47a0502e614ed1a5291acb34f 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=47e92a6094b8a2713b6daaae58141ee3 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a5487d848229ea5867e2fbab98d0496b 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a5d8d9421c7b53bc0a62934fa12e5dd1 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f48d30c41aeb58c81a0521267830ec5f 2500w" />

## Prompt engineering for tool calling

While AI models are highly intelligent and can reason about complex tasks, a well-structured prompt is essential for effective tool calling. The prompt serves as a blueprint that clearly defines what tools are available, guides the model through the decision-making workflow, and specifies the expected output format. Without this guidance, the model might miss important steps, use tools inefficiently, or produce results that don't match your requirements.

### Key elements of effective tool calling prompts:

* **Clear tool descriptions**: Explain what each tool does and when to use it
* **Decision logic**: Provide step-by-step workflow guidance
* **Output format**: Specify the structure and format of the expected response
* **Context handling**: Include relevant background information and constraints

## Example

Below is an example of a Tool calling block that is connected to multiple tools that run Python code or call external APIs.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=7ea6f52ba3f6a26cdb0fcff07d5404bc" alt="" data-og-width="3456" width="3456" data-og-height="1806" height="1806" data-path="images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b10a295f72b8dd93317d5acbbb706676 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=9f76f0636739ea24946c677e10ba4749 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3a978254b56e8cdc7b2b910b0d0e6129 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=febffef411dac0c2183cd7120c0348d5 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=129b749f513561cd0c8ede4e6b26f15a 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-tutorial/tool-calling-full-blueprint.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=56501e8b880f4137459e7ff00fd03c7b 2500w" />

For a complete walkthrough of building an agent with tool calling, see the [Tool calling with external APIs](/agent-builder/tool-calling-tutorial) tutorial.

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
      <td>Prompt</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>The task that needs to be carried out.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Model</td>
      <td>Model Id</td>
      <td>-</td>

      <td>
        <code>palmyra-x5</code>
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
      <td>Max iterations</td>
      <td>Number</td>
      <td>-</td>

      <td>
        <code>10</code>
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
      <td>Tools</td>
      <td>Tools</td>
      <td>-</td>

      <td>
        <code>
          {"{}"}
        </code>
      </td>

      <td>-</td>

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
      <td>Tools</td>
      <td>tools</td>
      <td>dynamic</td>
      <td>Run associated tools.</td>
    </tr>

    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>The task was completed successfully.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>There was an error completing the task.</td>
    </tr>
  </tbody>
</table>

The `dynamic` end state means that the exact values of this end state change based on how you define the block.
