# Source: https://dev.writer.com/blueprints/logmessage.md

# Log message

Prints a message to the console for debugging or monitoring app flow.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=283846fdfff49f6b07427a2a51fa6733" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/log-message-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=5328b13d078e40b1866f119c670b7c39 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=117b874e80bd18fd02bffea23f8cc0ee 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=607622d0c5180c9d69e85e7a6d295a1f 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=9c1bc6dd050ef79154c485eb07e10d84 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=79b4f471ea3f0c81867aa3f261797643 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=48d5dcfbc2d008aa5488f029c8136b10 2500w" />

## Overview

The **Log message** block writes a message to the workflow log. Use it to record information, debug workflows, or track the progress of your blueprint execution.

You can specify any message, including variables or state values, to help with troubleshooting or monitoring.

To view the logs, click the **Log** tab in the Agent Builder editor.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f967cb2175e60d76e82fb6727769ef69" alt="" data-og-width="1708" width="1708" data-og-height="324" height="324" data-path="images/agent-builder/blueprints/log-message-block-example-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2914cbf557f27964b6cdf6c2cc57a219 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=fa8bb90513596996519756ce2f063d6f 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b30e46e94032c53ef4f20f5fe2399ae1 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=cd160ab6781932661fe88acbfc03fc7d 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f42969f35c4f021f4b0b08b1cc6e6a5e 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7b0daf0280bf94b9e1e1c013be21af18 2500w" />

## Common use cases

* Debugging workflow execution by logging variable values
* Tracking the progress of a workflow
* Recording errors or important events
* Auditing workflow steps for compliance

## How it works

1. **Message**: Enter the message to log. You can log variables using the `@{variable_name}` syntax. For example, to log the value of the `@{payload}` variable, you can use the message `"Payload: @{payload}"`.
2. **Type**: Choose the type of message to log. You can choose from the following options:
   * **info**: Log a message with information.
   * **error**: Log a message with an error.

The block writes the message to the log. The message is available in the workflow execution logs for review.

## Examples

### Debug workflow execution

This example shows how to add logging throughout a workflow that processes multiple resumes from job applicants. The workflow extracts key information from each resume PDF and generates a summary report. The log message block is used to record the progress of the workflow.

**Blueprint Flow:**

1. **UI Trigger** → HR manager uploads multiple resumes for processing
2. **For-each loop** → Processes document sections
3. **Log message** → Records section completion and confirms parsing success
4. **Parse PDF** → Parses the PDF file
5. **Text generation** → Assembles final document

**Block Configuration:**

* **Message:** `Processing resume for @{itemId}.`
* **Type:** `info`

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=0c12cd1e7affa4e2ef3b9486bb5b2734" alt="" data-og-width="2782" width="2782" data-og-height="1440" height="1440" data-path="images/agent-builder/blueprints/log-message-block-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=6386584d6a3dfd24de6124c8cc141f39 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=195e2634ad8705757166762165196553 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b8f8e92ad688cc4190aa5600619eb068 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=75043f009952c244c6afc6694b79d584 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=9bb4ef2c9c28c685960d41e33d791586 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=10dcbaff1fea615643639b7bbc9adfee 2500w" />

The logs display the progress of the workflow as it processes each resume. You can see the logs in the **Log** tab of the Agent Builder editor.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f967cb2175e60d76e82fb6727769ef69" alt="" data-og-width="1708" width="1708" data-og-height="324" height="324" data-path="images/agent-builder/blueprints/log-message-block-example-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2914cbf557f27964b6cdf6c2cc57a219 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=fa8bb90513596996519756ce2f063d6f 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=b30e46e94032c53ef4f20f5fe2399ae1 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=cd160ab6781932661fe88acbfc03fc7d 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f42969f35c4f021f4b0b08b1cc6e6a5e 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/log-message-block-example-logs.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=7b0daf0280bf94b9e1e1c013be21af18 2500w" />

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
      <td>Type</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <code>info</code>
      </td>

      <td>-</td>

      <td>
        <ul>
          <li>info - Info</li>

          <li>error - Error</li>
        </ul>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Message</td>
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
      <td>The request was successful.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>The blueprint was executed successfully.</td>
    </tr>
  </tbody>
</table>

The return value of the **Log message** block is the message that was logged. You can access the return value in the next block in the workflow using the `@{result}` variable.
