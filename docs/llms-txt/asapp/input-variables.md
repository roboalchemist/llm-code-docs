# Source: https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/input-variables.md

# Input Variables

> Learn how to pass information from your application to GenerativeAgent.

Input Variables allow you to provide contextual information to GenerativeAgent when analyzing a conversation. This is the main way to pass information from your application to GenerativeAgent. These variables can then be referenced in the task instructions and functions.

Use Input Variables provide GenerativeAgent with context information like:

* Entities extracted from a previous system or API call
* Relevant customer metadata
* Conversation context, like a summary of previous interactions
* Instructions on the next steps for a given task

## Add Input Variables to a conversation

To add input variables to a conversation, you needs to:

<Steps>
  <Step title="Add Input Variables with /analyze">
    Call [`analyze`](/apis/generativeagent/analyze-conversation), adding the `inputVariables` attributes. `inputVariables` is an untyped JSON object and you can pass any key-value pairs. You need to ensure you are consistent in the key names you use between `/analyze` and the task instructions.

    With each call, any new input variable is added to the conversation context.

    ```bash  theme={null}
    curl --request POST \
      --url https://api.sandbox.asapp.com/generativeagent/v1/analyze \
      --header 'Content-Type: application/json' \
      --header 'asapp-api-id: <api-key>' \
      --header 'asapp-api-secret: <api-key>' \
      --data '{
      "conversationId": "01BX5ZZKBKACTAV9WEVGEMMVS0",
      "message": {
        "text": "Hello, I would like to upgrade my internet plan to GOLD.",
        "sender": {
          "role": "agent",
          "externalId": 123
        },
        "timestamp": "2021-11-23T12:13:14.555Z"
      },
      "taskName": "UpgradePlan",
      "inputVariables": {
        "context": "Customer called to upgrade their current plan to GOLD",
        "customer_info": {
          "current_plan": "SILVER",
          "customer_since": "2020-01-01"
        }
      }
    }'
    ```
  </Step>

  <Step title="Reference Input Variables in Task Instructions">
    Once the Input Variables are added to the conversation, they are made part of GenerativeAgents' Context. GenerativeAgent will consider them when interacting with your users.

    You can also reference them directly in the task instructions.

    ```
    The customer has a plan status of {{ input_vars.get("customer_info.current_plan") }}
    ```

    Input variables can be used as part of [Conditional Templates](/generativeagent/configuring/tasks-and-functions/conditional-templates).
  </Step>
</Steps>

## Add Input Variables in the Previewer

While you are iterating on your tasks, you simulate how GenerativeAgent responds with added Input Variables in the [Previewer](/generativeagent/configuring/previewer#input-variables)

<Frame>
  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=867cfca044e67cb9cefc81e0a4c6fdfd" data-og-width="534" width="534" data-og-height="1236" height="1236" data-path="images/generativeagent/InputVariables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=8ee07535e7db6ee619d91355d00fbdac 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=55028fab1a5c01bb0f5127e56aef2a61 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=e4fcdb030d1a64324a53638c1ae63370 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=82aa95bed8e5003ce1beb742fd773ac8 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=cfe3e3b949cc960abb902c9d0b5ae153 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=da9555c5f20c726e502624d0b4f67fad 2500w" />
</Frame>

You can also simulate directly launching the customer into a specific task, instead of allowing GenerativeAgent to choose a task.

<Tip>
  In a scenario where a IVR has already gathered information, you can ensure GenerativeAgent picks up from where the IVR left off.
</Tip>
