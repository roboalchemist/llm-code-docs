# Source: https://dev.writer.com/home/tool-calling.md

# Source: https://dev.writer.com/agent-builder/tool-calling.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Use tool calling in Agent Builder

> Add tool calling to Agent Builder blueprints and chatbots. Connect Knowledge Graphs and define custom functions with JSON Schema.

<Note>
  This page describes how to use tool calling in Agent Builder. If you're looking for an overview of tool calling, see [Introduction to tool calling](/agent-builder/tool-calling-intro).
</Note>

Agent Builder provides two ways to use tool calling:

* In a chatbot conversation with the [**Chat reply** block](/blueprints/chatreply). Use this block to add tool calling to your chatbot conversation.
* In a blueprint with the [**Tool calling** block](/blueprints/toolcalling). Use this block to add tool calling to your blueprint outside of a chatbot conversation.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=8210f07c636bcd842fab8a6a31e905dd" alt="Tool calling block example showing a tool calling block connected to a Knowledge Graph and a function" data-og-width="2850" width="2850" data-og-height="1474" height="1474" data-path="images/agent-builder/tool-calling-block-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3773a683a2da821b78b969664f1f496f 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=33e268b579da79a4b088ae4f25bc568d 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=089f200264aa6513b091bbe4d1a9d553 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f20f67014f413d0a35d9310d02e0dd55 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=5cd5dbb18dc2c3cd460508d87ecbb389 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=085c9de29b9c6d8993217f56c3616572 2500w" />

Both blocks allow you to either connect to Knowledge Graphs or define the functions you want to provide to the model as [JSON Schema](https://json-schema.org/) objects. Then, when the model decides to use a tool, it either queries the Knowledge Graphs or sends the call to your blueprint, which executes the tool and sends the results back to the model.

## Add tool calling to your blueprint

To add tool calling to your blueprint, you need to:

1. [Add the **Tool calling** block to your blueprint](#add-the-tool-calling-block)
2. [Write a prompt that explains what the tool calling block is trying to accomplish](#write-a-prompt)
3. [Define the tools you want to provide to the model](#define-your-tools)
4. [Connect the tool calling block to the blocks that execute the tools](#connect-the-tool-calling-connectors-to-the-blocks-that-execute-the-tools)
5. [Add a **Return value** block to the end of the tool calling block](#add-a-return-value-block)

### Add the tool calling block

Add either the [**Tool calling** block](/blueprints/toolcalling) to your blueprint or the [**Chat reply** block](/blueprints/chatreply) to your chatbot conversation.

### Write a prompt

The prompt you write for the tool calling block in the **Prompt** field guides the model's behavior and decision making. It should explain what the tool calling block is trying to accomplish and what tools are available to use.

### Define your tools

Define the tools you want to provide to the **Tool calling** block, so that it knows what tools are available to use.

To add a new tool, click the **Add tool+** button in the **Tool calling** block's configuration menu.

In the **Add tool** modal that appears, select the **Tool type** from the dropdown, either:

* **Function**: A function that the model can call
* **Knowledge Graph**: A Knowledge Graph that the model can query

<Tabs>
  <Tab title="Function">
    If you're using a function, enter the function name and definition. See [tool definition](#tool-definition) for more details about how to define the function.
    <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=13a33c67238f7eb1ac80ddd29476d699" alt="" data-og-width="1846" width="1846" data-og-height="800" height="800" data-path="images/agent-builder/add-function-tool-calling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b54f0a8f05551fae83447f715cee6230 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=2fa5c57ba9ab776b735031f4a87c0438 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=9ffb98f8f212775b186b5ce8a0ab1ccc 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a9894b9e75ef29e2d9c62a13ba47477f 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=52b59748d5d3d93c70525f770c121683 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-function-tool-calling.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=8149db43b94962e05652c3f7819d8539 2500w" />
  </Tab>

  <Tab title="Knowledge Graph">
    If you're using a Knowledge Graph, select the Knowledge Graph(s) you want to use from the dropdown of available Knowledge Graphs.
    <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=5d140ef33d204a34445d55836a02f8fc" alt="" data-og-width="1924" width="1924" data-og-height="922" height="922" data-path="images/agent-builder/add-kg-tool-calling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=0aa8c6f45f3a923f9d78c7355b88668a 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=73e609e47a0502e614ed1a5291acb34f 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=47e92a6094b8a2713b6daaae58141ee3 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a5487d848229ea5867e2fbab98d0496b 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a5d8d9421c7b53bc0a62934fa12e5dd1 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-kg-tool-calling.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=f48d30c41aeb58c81a0521267830ec5f 2500w" />
  </Tab>
</Tabs>

<Note>
  If you are using the Knowledge Graph tool, you only need to select which Knowledge Graphs you want to use. You do not need to define the tool or connect it to the blocks that execute the tools as described below. The following steps are only for the Function tool type.
</Note>

#### Tool definition

The tool definition for a `Function` tool follows the [JSON Schema](https://json-schema.org/) format and has the following structure:

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

### Connect the tool calling connectors to the blocks that execute the tools

When you define a `Function` tool in the block's configuration, it adds a connection point, shown as a purple circle, to the block. This allows you to connect it to another block or chain of blocks that perform the tool's work.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=8210f07c636bcd842fab8a6a31e905dd" alt="" data-og-width="2850" width="2850" data-og-height="1474" height="1474" data-path="images/agent-builder/tool-calling-block-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3773a683a2da821b78b969664f1f496f 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=33e268b579da79a4b088ae4f25bc568d 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=089f200264aa6513b091bbe4d1a9d553 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f20f67014f413d0a35d9310d02e0dd55 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=5cd5dbb18dc2c3cd460508d87ecbb389 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-block-example.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=085c9de29b9c6d8993217f56c3616572 2500w" />

The example above shows the following setup for a tool that, among other functions, can check the status of a package:

<Steps>
  <Step>
    Create an **HTTP Request** block that calls a shipping status API. Access the arguments to the tool call by the names you provided in the tool definition; for example, `@{tracking_number}` and `@{carrier}`.
  </Step>

  <Step>
    Add a **Return value** block to the end of the **HTTP Request** block to send the result back to the model.
  </Step>

  <Step>
    Provide a [tool definition](#example-tool-definition) to the **Tool calling** block that indicates there's a tool that can check the status of a package and it needs the tracking number and carrier name as input parameters.
  </Step>

  <Step>
    Connect the **HTTP Request** block to the **Tool calling** block at the `check_shipping_status` connection point.
  </Step>
</Steps>

When the model decides to use the tool, it sends the tool call to the **HTTP Request** block, which executes the tool. The **HTTP Request** block runs and passes the result to the **Return value** block, which sends the results back to the model

<Tip>
  Every `Function` tool call needs a **Return value** block at the end that sends the results back to the model.
</Tip>

When the **Tool calling** block completes all tool calls and integrates the results into the response, it moves to the next block in the blueprint that's connected to the `Success` transition. The `@{result}` variable is available in the next block with the tool calling block's final output.

## View tool calls logs

When a Tool Calling block executes, it provides a list of thoughts and actions that it took to complete the task. You can observe these in the logs of the blueprint.

Expand the **Logs** section at the bottom of the blueprint. Find the **Tool calling** log and click the **Trace** button to see the full trace of the tool calls.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-logs.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=76f3f2111c2d42ce6b29fde2b44c0edd" alt="" data-og-width="3358" width="3358" data-og-height="250" height="250" data-path="images/agent-builder/tool-calling-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-logs.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=ba27cf48769bbefc9d4e8fc64ad81d18 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-logs.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=1a56cf972c755d9f09606a7bbcb1785f 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-logs.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=46efc933f562d97944b17ae177eb0f16 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-logs.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=90d3439cb3a6aa13f54902e634625a1f 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-logs.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=89e26578aa8eec6fee2d0354d8d3daee 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-logs.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=840dc87fd464566b590879448e6ee595 2500w" />

The trace shows the series of thoughts, actions, and tool calls that the model made to complete the task.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-trace-example.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=03b605bb36685cedd60e8569f7c2157a" alt="" data-og-width="2664" width="2664" data-og-height="476" height="476" data-path="images/agent-builder/tool-calling-trace-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-trace-example.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=a39c84efe7328ffe7d6335ee82b0c79c 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-trace-example.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f9d68c6ee5c0ed870c48f63f4edd93ad 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-trace-example.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=3507a6b86e9483e83ee90c308759c2e2 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-trace-example.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=2fbf1a7b46ace20973fb700f0e4d2a3d 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-trace-example.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=b2b11cb64b9d461f232456549a82a051 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-trace-example.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=0d6a3bd4b295bba7327d87744b6115d4 2500w" />

<feedback />
