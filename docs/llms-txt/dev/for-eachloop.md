# Source: https://dev.writer.com/blueprints/for-eachloop.md

# For-each loop

export const item_0 = undefined

export const itemId_0 = undefined

export const prefix_item_0 = undefined

export const prefix_itemId_0 = undefined

Loops through each item in a list to run the same logic.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=bbc6254daef003626690709b7cd5b200" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/for-each-loop-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2f094fda9cda37d0f8bb686ca6c8f655 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=8d4ae9a348b10197b9c90001a6f2eb1b 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=420d8fa3b8caef0308aa1c7a081fe507 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=4fa7534f21056831879760c36da9b171 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6fa62de59e96450ca625bcadab02d523 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2e0c3c128c3ee43d7aac26b99504863a 2500w" />

## Overview

The **For-each loop** block iterates over a list or dictionary and executes a workflow for each item.

The following variables are available in the workflow when iterating with the **For-each loop** block:

* For a list of items (for example, `["a", "b", "c"]`):
  * `@{item}`: The current item in the list (for example, `"a"`, `"b"`, or `"c"`)
  * `@{itemId}`: The current item's index in the list, starting at 0 (for example, `0`, `1`, or `2`)
* For a dictionary of items (for example, `{"a": "apple", "b": "banana", "c": "cherry"}`):
  * `@{item}`: The current item's value in the dictionary (for example, `"apple"`, `"banana"`, or `"cherry"`)
  * `@{itemId}`: The current item's key in the dictionary (for example, "a", "b", or "c")

## Example

The following example shows a **For-each loop** block that loops over a list of file IDs and makes an HTTP request to the Writer API delete each file in the list by ID. It then sets a state variable to display a success message when it's done.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-example.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=88de5b30417585c07a64f502a4489c0e" alt="" data-og-width="2230" width="2230" data-og-height="1262" height="1262" data-path="images/agent-builder/blueprints/for-each-loop-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-example.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=01821ae2768eeb34a23bc33a76585e2a 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-example.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=4e1b67effb4945a01dc8dbce9acf46e7 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-example.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=1c2205f8b3057d16d7bea902bc2a1367 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-example.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=1bfdba7ea2c0a9540ada12a26ae8ed76 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-example.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ac319845919ac5e3f5a67c7f6aaa1076 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-example.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=a0bbdd642e4bcb6c6dc86818f470e54a 2500w" />

<Info>In this example, the list of file IDs is a hardcoded list of strings. In a more realistic example, the list of file IDs would be returned from a previous block or stored in state, rather than hardcoded. In that case, you could use the environment variable such as `@{payload}` or `@{state_element}` to access the list in the `Items` field.</Info>

The **For-each loop** block iterates over the list of items in the `Items` field and executes the blocks that follow for each item. To reference the current item in the loop, you can use the environment variable `@{item}`. To reference the current item's index in the list, you can use the environment variable `@{itemId}`.

The HTTP request in this example uses the `@{item}` environment variable to reference the current file ID in the HTTP request's `URL` field.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-http-request.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=d0a3733edc23eef057989659f229389e" alt="" data-og-width="2300" width="2300" data-og-height="1438" height="1438" data-path="images/agent-builder/blueprints/for-each-loop-http-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-http-request.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b2498968934886da7dc8e4b4d36fcee7 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-http-request.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=37780710d7f82aaf95a99fc8795e4933 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-http-request.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=879e2327af0544555b324c91f99e6670 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-http-request.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c3b5c7f226ffe7506054b2823fb1bfc0 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-http-request.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=20a17efd034a67de1961c30654853b9c 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/for-each-loop-http-request.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=83bfb0502d82ae330c505e6e87184d49 2500w" />

When the **For-each loop** block is done, it moves to the next block connected to the **Success** connection point. In this example, the next block is a **Set state** block that sets a state variable to display a success message when it's done.

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
      <td>Items</td>
      <td>Object</td>
      <td>Textarea</td>

      <td>
        <code>\[]</code>
      </td>

      <td>The item value will be passed in the execution environment and will be available at @{item_0}, its id at @{itemId_0}. You can use either a list or a dictionary.</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Prefix</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>If set, the item will be available at @{prefix_item_0} and the item id at @{prefix_itemId_0}.</td>

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
      <td>Loop</td>
      <td>-</td>
      <td>dynamic</td>
      <td>Connect the branch that you'd like to loop on. The branch plugged in here will be executed once per item.</td>
    </tr>

    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>The branch referenced executed successfully for each item.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>The branch referenced has failed for at least one of the items.</td>
    </tr>
  </tbody>
</table>

The `dynamic` end state means that the exact values of this end state change based on how you define the block.
