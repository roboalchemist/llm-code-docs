# The Start block

![Start block](https://assets.postman.com/postman-docs/v11/flows-reference-blocks-start-v11.54.6.jpg)

The **Start** block is automatically added to every new flow module. You can add inputs that receive data from [scenarios](/docs/postman-flows/build-flows/configure/scenarios/). Also, if you bring the flow into another flow, or into an [action](/docs/postman-flows/build-flows/structure/actions/), the **Start** block's inputs in the original flow become the [**Flow Module**](/docs/postman-flows/reference/blocks/flow-module/) block's inputs in the new one.

## Inputs

By default, the **Start** block has no input ports. You can [add inputs](#receive-data-with-inputs) as desired.

## Output

By default, the **Start** block has a single output port that will be connected to the first block you add by clicking buttons during [setup](#setup). Otherwise, the output port sends the data provided by the first [input you add](#receive-data-with-inputs). You can also leave the **Start** block as is, without inputs or connected blocks - in that case, the output won't send any data.

## Setup

The **Start** block appears automatically on every new flow's canvas. A new **Start** block is connected to three buttons you can click to do the following:

- Add an [**HTTP Request**](/docs/postman-flows/reference/blocks/http-request/) block to your canvas.
- Open the [blocks list](/docs/postman-flows/build-flows/create/create-blocks/) to add a block.
- Explore the [Flows Catalog](/docs/postman-flows/get-started/flows-catalog/).

### Receive data with inputs

You can add inputs to the **Start** block. Each input will appear as an inline [data block](/docs/postman-flows/reference/overview-data-blocks/). You must also create a [scenario](/docs/postman-flows/build-flows/configure/scenarios/) to send data to all the inputs.

For each input you add, Postman adds an output to the **Start** block. When you run the flow, the **Start** block sends data through the outputs to any connected blocks.

To add an input to the **Start** block, do the following:

1. In the **Start** block, click \[![Add input](https://assets.postman.com/postman-docs/aether-icons/action-add-stroke.svg#icon)\] **Add input**. A **String** block is inserted into the **Start** block.
2. (Optional) Click the dropdown list if you want to select a data block other than **String**. Use \[![Locked icon](https://assets.postman.com/postman-docs/aether-icons/state-locked-stroke.svg#icon)\] **Secret** for sensitive string values like API keys. To learn how secret inputs work, see [Secrets in scenarios](/docs/postman-flows/build-flows/configure/scenarios/#secrets-in-scenarios).
3. Enter a name for the input.
4. Create a scenario to send data to the input. If you run the flow without creating the scenario first, Postman will automatically create a scenario for you, using minimal or empty values like `0` for a **Number** block, `[]` for a **List** block, or the empty string for a **String** block.

### Specify inputs for a flow module

When a [**Flow Module** block](/docs/postman-flows/reference/blocks/flow-module/) references a flow whose **Start** block has inputs, those inputs appear as named input ports in the **Flow Module** block. When other blocks send data to these ports, the **Flow Module** block will send that data to the corresponding inputs in the referenced flow's **Start** block. The values that the referenced flow produces will then be available through the **Flow Module** block's outputs. To learn more, see [Build a "Hello, world" flow module](/docs/postman-flows/get-started/build-your-first-flow/).

The scenarios you created to provide data to the inputs in the referenced flow's **Start** block won't be available to the **Flow Module** block. This means that in the flow or action containing the **Flow Module** block, you need to add blocks or scenarios to supply data to the inputs.

## Example

Suppose you make the following flow into a module, with the idea of referencing it in an action:

![HTTP Request block with variables](https://assets.postman.com/postman-docs/v11/flows-reference-blocks-http-start-ex1-v11-56.0.jpg)

You name the flow **Module to build wx message** and use a **Flow Module** block to reference it in an action. Encapsulating all the original flow's blocks in a single module makes your action simpler and easier to grasp.

Providing data to the **Flow Module** block's inputs is required. When testing the action, you create a scenario to provide the data. The result looks like this:

![HTTP Request block with variables](https://assets.postman.com/postman-docs/v11/flows-reference-blocks-http-start-ex4-v11-56.0.jpg)

## Related blocks

Upon creation, every flow module has a **Start** block with a connected [**HTTP Request**](/docs/postman-flows/reference/blocks/http-request/) block. If you add inputs to a **Start** block, they will become inputs in any [**Flow Module**](/docs/postman-flows/reference/blocks/flow-module/) block referencing the flow that contains the **Start** block.