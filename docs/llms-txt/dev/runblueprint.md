# Source: https://dev.writer.com/blueprints/runblueprint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run blueprint

export const payload_0 = undefined

Starts another blueprint by key. Useful for breaking logic into smaller, reusable parts.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=8606940f7f4f2654f95539ab18d4f3bf" alt="" data-og-width="2192" width="2192" data-og-height="1450" height="1450" data-path="images/agent-builder/blueprints/run-blueprint-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c89763467b1a2d43ed382fe656c77b9b 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=8f376ec9b430946bfe2563b89af97d47 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=75a4450af7b5a71122e63f3fd7099cdb 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0ffa680c40f2c2099d8ae827312a3563 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=d9f4a42c885c271913eb4f8d14516ae2 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e90a72fe8c718d28f56ddafe0f388fe7 2500w" />

## Overview

The **Run blueprint** block allows you to call another blueprint from within your current workflow. This enables modular, reusable logic and lets you break complex workflows into smaller, manageable pieces.

You can specify the blueprint to run and pass input parameters. The output of the called blueprint is available for use in subsequent blocks.

## Common use cases

* Reusing logic across multiple workflows
* Breaking up large blueprints into smaller, maintainable components
* Creating shared utility blueprints
* Running conditional or dynamic workflows

## How it works

1. **Blueprint Key**: Select the blueprint to run by its key. The blueprint must have a key set in its settings. If the blueprint doesn't have a key, it does not show in the list of available blueprints.
2. **Payload**: Provide input data as text that will be available as `@{payload}` in the called blueprint. The payload is treated as plain text.

The block executes the specified blueprint and returns any output that the called blueprint returns with the **Return value** block.

<Tip>
  **No trigger required:** Blueprints called with the Run blueprint block don't need a UI trigger or any other trigger. They start execution immediately when called and can access the payload data you pass in.
</Tip>

## Examples

### Document processing workflow

This example demonstrates a document processing system that handles different file types using specialized blueprints.

**Blueprint Flow:**

1. **UI Trigger** → User uploads document through file input
2. **Classification** → Identifies document type (invoice, resume, or contract)
3. **Conditional routing** → Routes to appropriate processing blueprint
4. **Run blueprint** → Executes specialized document processor
5. **Set state** → Stores the processing result to display in the UI

**Block Configuration:**
For invoice processing:

* **Blueprint Key:** `invoice_processor`
* **Payload:** `@{file_data}`

**Called Blueprint Access:**
In the `invoice_processor` blueprint, you can access the passed data using `@{payload}`. Then you can return a value from the blueprint using the **Return value** block.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-workflow.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c5cf052b37a9ca43ab55016e53a39dbe" alt="" data-og-width="2750" width="2750" data-og-height="1430" height="1430" data-path="images/agent-builder/blueprints/run-blueprint-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-workflow.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ea18c2f9c0769ba8ab2685c1880cc829 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-workflow.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=a57294ac75f4c09c2140f7b4a1685f61 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-workflow.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=d4e02430e0335c1a3805440c06a8a844 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-workflow.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=8e7bf88905814165aad96326b1ab788a 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-workflow.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=85588800df45053a856a3a89af9907f7 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/run-blueprint-workflow.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=d2f998e12630c382219f2093cad20fcf 2500w" />

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
      <td>Blueprint Key</td>
      <td>Blueprint Key</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        Format: writer#blueprintKey
      </td>
    </tr>

    <tr>
      <td>Payload</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <code>
          {"{}"}
        </code>
      </td>

      <td>The value specified will be available using the template syntax, e.g. @{payload_0}.</td>

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
      <td>The request was successful.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>The blueprint execution failed.</td>
    </tr>
  </tbody>
</table>

The output of the **Run blueprint** block is the return value from the called blueprint. This is typically the result of the last block in the called blueprint, or a specific return value if the called blueprint has a **Return value** block. You can access this output in subsequent blocks using `@{result}`.
