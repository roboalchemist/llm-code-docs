# Source: https://dev.writer.com/blueprints/uitrigger.md

# UI Trigger

Triggers an event based on UI interactions like button clicks or input changes.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=5d8867832427524aca6ade72304f9303" alt="" data-og-width="2198" width="2198" data-og-height="1450" height="1450" data-path="images/agent-builder/blueprints/ui-trigger-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=1d71ee9ede31a1fb0ae6ccb34086bd61 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6320e76971df3d8c42030daeb82604ea 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=d7f6bf92112de5821e18f93f4c434a27 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=80a30bbf12002e5c26d8e1d40062142b 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=9b63c335c8af39479e0f5901e5d73c66 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=4b0b85d243d0ea4536f01d730f64509a 2500w" />

## Overview

The **UI Trigger** block is the starting point for your blueprint if users interact with the agent's interface.

It starts a workflow in response to a user action in the UI, such as clicking a button or typing in a text area. Use it to connect frontend events to backend logic in your blueprint.

You can specify the event to listen for and any parameters to pass to the workflow.

## How it works

1. **Component Id**: Select the UI component that triggers this workflow; for example, a button click or chatbot message.
2. **Event type**: Specify the type of event to listen for; for example, clicks (`wf-click`) or text area changes (`wf-change`).
3. **Default result**: Optionally provide a default result when testing the blueprint from the "Run blueprint" button. This is useful for testing the workflow without having to interact with the interface. The default result should match the expected payload format for the selected event type. For example:
   * For a button click (`wf-click`), provide an object with modifier key states, like:
     ```json  theme={null}
     {
       "ctrl_key": false,
       "shift_key": false,
       "meta_key": false
     }
     ```
   * For a text input change (`wf-change`), provide the expected text value, like `"Sample text"`
   * For a file upload (`wf-file-change`), provide an array of file objects, like:
     ```json  theme={null}
     [
       {
         "name": "example.txt",
         "type": "text/plain",
         "data": "data:text/plain;base64,U2FtcGxlIHRleHQ="
       }
     ]
     ```

When the specified event occurs on the selected component, the block starts the workflow. The event payload is available as `@{payload}` in subsequent blocks.

## Examples

### Interactive dashboard updates

This example demonstrates how to handle real-time dashboard interactions and updates.

**Interface:**

1. A [Plotly chart](/components/plotlygraph) that a user can click to trigger the workflow.

**Blueprint Flow:**

1. **UI Trigger** → User clicks on dashboard widget
2. **HTTP Request** → Fetches updated data from external API
3. **Set state** → Updates dashboard state

**Block Configuration:**

* **Component Id:** Dashboard widget component
* **Event type:** `wf-click`
* **Default result:** Optional, but useful for testing the blueprint from the "Run blueprint" button. The default result below mimics the data that would be returned if a user clicked somewhere on a [Plotly chart](/components/plotlygraph) in the interface.

```json  theme={null}
[
  {
    "curveNumber": 0,
    "pointNumber": 1,
    "x": "Product B",
    "y": 150,
    "label": "Product B",
    "xaxis": {
      "anchor": "y"
    },
    "yaxis": {
      "anchor": "x"
    }
  }
]
```

This workflow enables real-time dashboard interactions with external data sources.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-workflow.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=fd7d0f5144f2f7d1392571ddad423ef0" alt="" data-og-width="1960" width="1960" data-og-height="1428" height="1428" data-path="images/agent-builder/blueprints/ui-trigger-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-workflow.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c18a173327cf5a63adb287f1eea19f7d 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-workflow.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=c8c311dd0d8d58214efbee860ddcc6c3 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-workflow.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=e122bf384fd140261a3c9324f585b24e 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-workflow.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=95f29900f123c697954b751a77cd2526 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-workflow.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ef3b6849fc3425fe464daf5907d06894 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/ui-trigger-workflow.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=dafb38492c9a806c580e6a840faefb85 2500w" />

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
      <td>Component Id</td>
      <td>Component Id</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>The id of the component that will trigger this branch.</td>

      <td>
        uiComponentsWithEvents
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Event type</td>
      <td>Component Event Type</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>The type of the event that will trigger this branch. For example, wf-click.</td>

      <td>
        eventTypes
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Default result</td>
      <td>Code</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>The result that is used when the blueprint is triggered from the "Run blueprint" button</td>

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
      <td>Trigger</td>
      <td>-</td>
      <td>success</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

The output of the **UI Trigger** block is the event payload. For example, if the event type is `wf-file-change` for a **File input** block, the payload contains the file that the user uploaded. You can access this value in any block in the blueprint as `@{payload}`.
