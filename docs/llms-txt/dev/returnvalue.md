# Source: https://dev.writer.com/blueprints/returnvalue.md

# Return value

Returns a value from this block to the caller. Use to pass results to another blueprint.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=3a1354d786dc46b7c9b3928b4bcda7b3" alt="" data-og-width="2310" width="2310" data-og-height="1488" height="1488" data-path="images/agent-builder/blueprints/return-value-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=67aa8224e6b916924f83de8cd1e13b28 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=beee30c0733ee74a791cc90f22f38c05 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=d71f9277716b0ba7212b9531199f19d3 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7e4c2770914bf2c015ee6f1afd2fafea 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e3d19fba12ff889f57620a3405d114d3 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=df1b17f37e048d6edf1414c187f1f9b2 2500w" />

## Overview

The **Return value** block allows you to chain multiple steps together to perform certain actions, and return a single value at the end of the chain. You can use it in the following scenarios:

* To return a value in [tool calling](/agent-builder/tool-calling)
* To return a value when a blueprint is invoked with the [**Run blueprint** block](/blueprints/runblueprint)

It passes the value specified in the **Value** field at the end of a chain of blocks.

### Return a value in tool calling

When an **Tool calling** block decides to run a tool, the tool can include any number of blocks and return a final value to the **Tool calling** block. Use the **Return value** block to define what the final return value is.

If you do not use the **Return value** block, the tool call executes the blocks that follow it but doesn't return a value to the **Tool calling** block.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-tool-calling.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=57dc4439756ba669b0a674ff1fd7192e" alt="" data-og-width="2874" width="2874" data-og-height="1470" height="1470" data-path="images/agent-builder/blueprints/return-value-tool-calling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-tool-calling.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=12fc0c2d3c255e22f6e9b45bdc0a8126 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-tool-calling.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=946b9024dd737f9fb8ff9a88f54e152c 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-tool-calling.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6187c7801758043194432d5c84367203 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-tool-calling.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0225a14eaf25ddd8ca5d6f5f3a128188 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-tool-calling.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=3263523cf558c5d611aaf3a00a8468be 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-tool-calling.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=1bab4aad1a382609478edfaea9522230 2500w" />

In the example above, the two **Return value** blocks provide the values of the "Call shipping API" block and the "Call order status API" HTTP Request blocks to the **Tool calling** block.

Without the **Return value** blocks, the "Call shipping API" and "Call order status API" blocks would execute, but their results would not be returned to the **Tool calling** block.

### Return a value from a blueprint

Use the **Return value** block to pass results to another blueprint.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-run-blueprint.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c39673550087f2f05075b04b60859086" alt="" data-og-width="2484" width="2484" data-og-height="876" height="876" data-path="images/agent-builder/blueprints/return-value-run-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-run-blueprint.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7b9713959e10ea2c4c5d0a6509273935 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-run-blueprint.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=41c97b91329c41c0767b8034ef91164d 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-run-blueprint.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=51ff0bf2c074f5da89e72976d52c67d8 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-run-blueprint.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c813c51d80967c95473fa1db913af16d 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-run-blueprint.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ea937c853320efd27009187c725fc34c 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/return-value-run-blueprint.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=a1c5d4e7ad5398c2dd4baa3a796f2e72 2500w" />

In the example above, the **Return value** block follows the **Text generation** block. It sets the results from the text generation block as the final return value of the blueprint. The blueprint passes this value when it is invoked with the **Run blueprint** block.

Without the **Return value** block, the blueprint would run and the **Text generation** block would execute, but its result would not be returned to the block that ran the blueprint.

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
      <td>Value</td>
      <td>Text</td>
      <td>Textarea</td>

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
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>If the function doesn't raise an Exception.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>If the function raises an Exception.</td>
    </tr>
  </tbody>
</table>
