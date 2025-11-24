# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/perception-tool.md

# Tool Calling for Perception

> Configure tool calling with `raven-0` to trigger functions from visual input.

**Perception tool calling** works with OpenAI’s <a href="https://platform.openai.com/docs/guides/function-calling" target="_blank">Function Calling</a> and can be configured in the `perception` layer. It allows an AI agent to trigger functions based on visual cues during a conversation.

<Note>
  The perception layer tool calling is only available for `raven-0`.
</Note>

## Defining Tool

### Top-Level Fields

| Field      | Type   | Required | Description                                                                                                |
| ---------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------- |
| `type`     | string | ✅        | Must be `"function"` to enable tool calling.                                                               |
| `function` | object | ✅        | Defines the function that can be called by the model. Contains metadata and a strict schema for arguments. |

#### `function`

| Field         | Type   | Required | Description                                                                                                                  |
| ------------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `name`        | string | ✅        | A unique identifier for the function. Must be in `snake_case`. The model uses this to refer to the function when calling it. |
| `description` | string | ✅        | A natural language explanation of what the function does. Helps the perception model decide when to call it.                 |
| `parameters`  | object | ✅        | A JSON Schema object that describes the expected structure of the function’s input arguments.                                |

#### `function.parameters`

| Field        | Type             | Required | Description                                                                               |
| ------------ | ---------------- | -------- | ----------------------------------------------------------------------------------------- |
| `type`       | string           | ✅        | Always `"object"`. Indicates the expected input is a structured object.                   |
| `properties` | object           | ✅        | Defines each expected parameter and its corresponding type, constraints, and description. |
| `required`   | array of strings | ✅        | Specifies which parameters are mandatory for the function to execute.                     |

<Note>
  Each parameter should be included in the required list, even if they might seem optional in your code.
</Note>

##### `function.parameters.properties`

Each key inside `properties` defines a single parameter the model must supply when calling the function.

| Field              | Type   | Required | Description                                                              |
| ------------------ | ------ | -------- | ------------------------------------------------------------------------ |
| `<parameter_name>` | object | ✅        | Each key is a named parameter. The value is a schema for that parameter. |

Optional subfields for each parameter:

| Subfield      | Type   | Required | Description                                                                                 |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------------------- |
| `type`        | string | ✅        | Data type (e.g., `string`, `number`, `boolean`).                                            |
| `description` | string | ❌        | Explains what the parameter represents and how it should be used.                           |
| `enum`        | array  | ❌        | Defines a strict list of allowed values for this parameter. Useful for categorical choices. |

## Example Configuration

Here’s an example of tool calling in `perception` layers:

<Tip>
  **Best Practices:**

  * Use clear, specific function names to reduce ambiguity.
  * Add detailed `description` fields to improve selection accuracy.
</Tip>

```json Perception Layer [expandable] theme={null}
"perception": {
  "perception_model": "raven-0",
  "ambient_awareness_queries": [
      "Is the user showing an ID card?",
      "Is the user wearing a mask?"
  ],
  "perception_tool_prompt": "You have a tool to notify the system when an ID card is detected, named `notify_if_id_shown`.",
  "perception_tools": [
    {
      "type": "function",
      "function": {
        "name": "notify_if_id_shown",
        "description": "Use this function when a drivers license or passport is detected in the image with high confidence. After collecting the ID, internally use final_ask()",
        "parameters": {
          "type": "object",
          "properties": {
            "id_type": {
              "type": "string",
              "description": "best guess on what type of ID it is",
            },
          },
          "required": ["id_type"],
        },
      },
    },
    {
      "type": "function",
      "function": {
        "name": "notify_if_bright_outfit_shown",
        "description": "Use this function when a bright outfit is detected in the image with high confidence",
        "parameters": {
          "type": "object",
          "properties": {
            "outfit_color": {
              "type": "string",
              "description": "Best guess on what color of outfit it is"
            }
          },
          "required": ["outfit_color"]
        }
      }
    }
  ]
}
```

## How Perception Tool Calling Works

Perception Tool calling is triggered during an active conversation when the perception model detects a visual cue that matches a defined function. Here’s how the process works:

<Note>
  This example explains the `notify_if_id_shown` function from the [example configuration](#example-configuration) above.
</Note>

<Frame>
    <img src="https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/perception-tool-call.png?fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=7e231c29aaf93a4bdf856d74a590da00" alt="" data-og-width="2497" width="2497" data-og-height="1502" height="1502" data-path="images/perception-tool-call.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/perception-tool-call.png?w=280&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=58e5661c61652b2bb76b2a3bbca37667 280w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/perception-tool-call.png?w=560&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=79cc72fe52ae2352a2c29a0cfa9f0d5b 560w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/perception-tool-call.png?w=840&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=347637d011ba1e947f1770ad2d610385 840w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/perception-tool-call.png?w=1100&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=7831fe7c91decf020210c4be179494e7 1100w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/perception-tool-call.png?w=1650&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=077f0822d392b7f32ec914f0b58c30e7 1650w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/perception-tool-call.png?w=2500&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=3fb5fbe4494f1b8a3b0e6c63e5b6eff9 2500w" />
</Frame>

<Note>
  The same process applies to other functions like `notify_if_bright_outfit_shown`, which is triggered if a bright-colored outfit is visually detected.
</Note>

## Modify Existing Tools

You can update the `perception_tools` definitions using the <a href="/api-reference/personas/patch-persona" target="_blank">Update Persona API</a>.

```shell [expandable] theme={null}
curl --request PATCH \
  --url https://tavusapi.com/v2/personas/{persona_id} \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '[
    {
      "op": "replace",
      "path": "/layers/perception/perception_tools",
      "value": [
        {
          "type": "function",
          "function": {
            "name": "detect_glasses",
            "description": "Trigger this function if the user is wearing glasses in the image",
            "parameters": {
              "type": "object",
              "properties": {
                "glasses_type": {
                  "type": "string",
                  "description": "Best guess on the type of glasses (e.g., reading, sunglasses)"
                }
              },
              "required": ["glasses_type"]
            }
          }
        }
      ]
    }
  ]'

```

<Note>
  Replace `<api_key>` with your actual API key. You can generate one in the <a href="https://platform.tavus.io/api-keys" target="_blank">Developer Portal</a>.
</Note>
