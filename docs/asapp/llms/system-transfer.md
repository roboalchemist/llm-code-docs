# Source: https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/system-transfer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# System Transfer Functions

> Signal conversation control transfer to external systems with System Transfer Functions.

System Transfer Functions signal that control of the conversation should be transferred from GenerativeAgent to an external system. They can also return reference variables (e.g., a determined "intent," or details about a charge) for further processing outside of GenerativeAgent.

By using a System Transfer Function, you can:

* End the conversation gracefully, indicating that GenerativeAgent is finished.
* Hand control back to the calling application or IVR once a goal is met.
* Send relevant conversation data (e.g., identified charges, subscription flags, or determined intent) for follow-up workflows.

To create a system transfer function:

1. [Create a function](#step-1-create-a-new-function)
2. [Define input parameters](#step-2-define-input-parameters-json)
3. [Set variables (optional)](#step-3-optional-set-variables)
4. [Save the function](#step-4-save-your-function)
5. [Use the function in a task](#step-6-using-the-system-transfer-function-in-the-conversation)
6. [Handle the system transfer event](#step-5-handle-the-system-transfer-event)

## Step 1: Create a New Function

Navigate to the Functions page and click "Create Function."

1. Select "System transfer" and click "Next: Function details"
   <Frame>
     <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SetSystemTransferFunction.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=ce845cf910a4af5ddbed38183a43c285" data-og-width="1210" width="1210" data-og-height="596" height="596" data-path="images/generativeagent/SetSystemTransferFunction.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SetSystemTransferFunction.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=321beb3029f8be3b6be5601d09e2ec7d 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SetSystemTransferFunction.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d9e652aaf674d69d1d841fcd7ef79c5a 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SetSystemTransferFunction.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=593f2a2473844b9650af997ed1cfdeb8 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SetSystemTransferFunction.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=af2ee82a44258592e3452d190a14316a 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SetSystemTransferFunction.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=4bbe35a744534c16b5e22abdd38fc5e5 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SetSystemTransferFunction.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=dd1abcbced8221088bd82f5c532f66ce 2500w" />
   </Frame>
2. Specify the Name and Purpose of the Function
   * **Function Name**: Provide a concise, unique name, using underscores (e.g., `issue_refund_request`).
   * **Function Purpose**: Briefly describe what the function does (e.g., "Takes the collected charge info and indicates a refund request should be processed").
     * GenerativeAgent uses this description to determine if/when it should call the function.

## Step 2: Define Input Parameters (JSON)

The input parameters are the values that GenerativeAgent needs to pass when calling this function to transfer control to the external system.

Under "Input Parameters," enter a valid JSON schema describing the required parameters. GenerativeAgent gathers the necessary information (from user messages or prior context) before calling the function.

```json Example Input Schema theme={null}
{
  "type": "object",
  "required": [
    "line_item_number",
    "is_eligible_for_refund",
    "is_subscription"
  ],
  "properties": {
    "line_item_number": {
      "type": "string",
      "description": "The line item number associated with the charge"
    },
    "is_eligible_for_refund": {
      "type": "boolean", 
      "description": "Whether or not the line item is eligible for a refund"
    },
    "is_subscription": {
      "type": "boolean",
      "description": "Whether or not the charge is associated with a subscription"
    }
  }
}
```

## Step 3: (Optional) Set Variables

Though System Transfer Functions typically return control to an external system, you can still configure one or more reference variables:

* Configure variables to rename or transform parameter values for the external system
* Use [Jinja2](https://jinja.palletsprojects.com/en/stable/) for transformations if needed
* Toggle "Include return variable as part of function response" to make variables immediately available

### Jinja2 Templates

Use Jinja2 to transform values before transfer. For example, to convert a string boolean to a proper boolean:

```jinja2  theme={null}
true if params.get("is_subscription") == "True" else false
```

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SystemTransferFunction.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=945e3d5bc9e7695844e4c1a720be8202" data-og-width="1658" width="1658" data-og-height="1618" height="1618" data-path="images/generativeagent/SystemTransferFunction.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SystemTransferFunction.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=6a16fbb35c3a4810f6d72b1fc27007d2 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SystemTransferFunction.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d1351769f7d4f38ef5b22fbc3db9428f 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SystemTransferFunction.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=be5725fc2eabff185400550a33ba2831 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SystemTransferFunction.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=18f4887ad1b86d695ce3904a37d57a11 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SystemTransferFunction.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=3b744a5bcafd269cde32bb23d1b267d1 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/SystemTransferFunction.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=828863d751eb58f905b5e59f93b5379a 2500w" />
</Frame>

## Step 4: Save Your Function

With your function defined, save it by clicking "Create Function".

After saving, you'll see a detail page showing the JSON schema and any configured reference variables.

## Step 5: Using the System Transfer Function in the Conversation

Once you have created your system transfer function, add it to the task's list of available functions for GenerativeAgent to use it.

GenerativeAgent may call the function proactively, but we recommend you instruct GenerativeAgent to call the function explicitly.

Always make sure to test your functions with Previewer to ensure they work as expected.

Here's how the function works within a task and conversation flow:

1. GenerativeAgent collects the required parameters from the user (or context).
2. (Optional) The system can display a "Message before Sending" to the user, clarifying why GenerativeAgent is transferring control.
3. Jinja2 transformations convert or combine inputs, if defined.
4. GenerativeAgent calls the System Transfer Function, signaling that control returns to the external system.
   * All reference variables collected during the conversation are passed along.
   * If configured, the function's specific variables also appear in the final response.

<Accordion title="Example scenario using a System Transfer Function">
  ```jinja  theme={null}
  # Objective
  Identify the line item for an unrecognized charge, verify refund eligibility, and transfer control to the external system once the user confirms a refund request.

  # Context
  - We already have a list of recent transactions.
  - The user has confirmed which charge is disputed.

  # Instructions
  1. **Identify the Charge:**
     - Gather details: date, amount, and merchant to confirm the correct line item.
     - Store "line_item_number" once identified.

  2. **Check Refund Eligibility:**
     - If the line item meets the refund criteria, set "is_eligible_for_refund" to true.
     - If part of a subscription, set "is_subscription" to true for any special handling.

  3. **Offer Refund:**
     - {% if vars.get("is_eligible_for_refund") == true %}
       - Ask the customer: "Shall we proceed with the refund?"
       - If yes:
         - Call the `issue_refund_request` System Transfer Function.
     - {% else %}
       - Apologize, indicate no refund is possible. Offer further assistance.
     - {% endif %}
  ```
</Accordion>

### Best Practices

<AccordionGroup>
  <Accordion title="Use Meaningful Names and Descriptions">
    Choose function names like "issue\_refund\_request" or "complete\_intent\_transfer." Provide concise descriptions so GenerativeAgent knows when to transfer control.
  </Accordion>

  <Accordion title="Leverage Conditions">
    If you only want the system transfer to occur after specific statuses or variables are set, configure "Conditions" in the Task's function list so GenerativeAgent calls it at the correct time.
  </Accordion>

  <Accordion title="Stay Focused with Your Schema">
    Your function schema should cover only the data needed by the external system. Minimizing extra fields ensures smoother handoff.
  </Accordion>

  <Accordion title="Use Jinja2 for Variable Transformations">
    Handle naming or logic differences between GenerativeAgent and your external system with optional Jinja2 transformations (e.g., rename "is\_subscription" to "subscriptionFlag").
  </Accordion>
</AccordionGroup>

## Step 6: Handle the System Transfer Event

When the function is called in your task, the system transfers the conversation to your system. The system communicates this transfer via the [generative agent events](/generativeagent/integrate/handling-events) that the system sends as part of the conversation handling.

The system passes all currently set reference variables as `referenceVariables`, and the system passes any variables set in the function as `transferVariables`.

```json Example System Transfer Event theme={null}
{
  "generativeAgentMessageId": "bba4320f-de53-4874-83b4-6c8704d3620c",
  "externalConversationId": "33411121",
  "conversationId": "01HMVXRVSA1EGC0CHQTF1X2RN3",
  "type": "systemTransfer",
  "systemTransfer": {
    "referenceVariables": {
      "customerName": "John Smith",
      "accountNumber": "12345",
      "isActive": true
    },
    "transferVariables": {
      "line_item_number": "1234567890",
      "is_eligible_for_refund": true,
      "is_subscription": false
    },
    "currentTaskName": "handle_refund_requests"
  }
}
```

## Next Steps

<CardGroup>
  <Card title="Task Best Practices" href="/generativeagent/configuring/task-best-practices">
    Learn more about best practices for task and function configuration.
  </Card>

  <Card title="Set Variable Functions" href="/generativeagent/configuring/tasks-and-functions/set-variable">
    Learn how to store and manipulate conversation data with Set Variable Functions.
  </Card>

  <Card title="Connecting Your APIs" href="/generativeagent/configuring/connect-apis">
    Connect your external systems to enable system transfers.
  </Card>

  <Card title="Previewer" href="/generativeagent/configuring/previewer">
    Test your system transfer functions in real-time with the Previewer tool.
  </Card>
</CardGroup>
