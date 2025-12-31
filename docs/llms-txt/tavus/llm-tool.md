# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/llm-tool.md

# Tool Calling for LLM

> Set up tool calling to trigger functions from user speech using Tavus-hosted or custom LLMs.

**LLM tool calling** works with OpenAI’s <a href="https://platform.openai.com/docs/guides/function-calling" target="_blank">Function Calling</a> and can be set up in the `llm` layer. It allows an AI agent to trigger functions based on user speech during a conversation.

<Note>
  You can use tool calling with our **hosted models** or any **OpenAI-compatible custom LLM**.
</Note>

## Defining Tool

### Top-Level Fields

| Field      | Type   | Required | Description                                                                                              |
| ---------- | ------ | -------- | -------------------------------------------------------------------------------------------------------- |
| `type`     | string | ✅        | Must be `"function"` to enable tool calling.                                                             |
| `function` | object | ✅        | Defines the function that can be called by the LLM. Contains metadata and a strict schema for arguments. |

#### `function`

| Field         | Type   | Required | Description                                                                                                                  |
| ------------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `name`        | string | ✅        | A unique identifier for the function. Must be in `snake_case`. The model uses this to refer to the function when calling it. |
| `description` | string | ✅        | A natural language explanation of what the function does. Helps the LLM decide when to call it.                              |
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

| Field              | Type   | Required | Description                                                                                 |
| ------------------ | ------ | -------- | ------------------------------------------------------------------------------------------- |
| `<parameter_name>` | object | ✅        | Each key is a named parameter (e.g., `location`). The value is a schema for that parameter. |

Optional subfields for each parameter:

| Subfield      | Type   | Required | Description                                                                                 |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------------------- |
| `type`        | string | ✅        | Data type (e.g., `string`, `number`, `boolean`).                                            |
| `description` | string | ❌        | Explains what the parameter represents and how it should be used.                           |
| `enum`        | array  | ❌        | Defines a strict list of allowed values for this parameter. Useful for categorical choices. |

## Example Configuration

Here’s an example of tool calling in the `llm` layers:

<Tip>
  **Best Practices:**

  * Use clear, specific function names to reduce ambiguity.
  * Add detailed `description` fields to improve selection accuracy.
</Tip>

```json LLM Layer [expandable] theme={null}
"llm": {
  "model": "tavus-llama-4",
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_time",
        "description": "Fetch the current local time for a specified location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The name of the city or region, e.g. New York, Tokyo"
            }
          },
          "required": ["location"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "convert_time_zone",
        "description": "Convert time from one time zone to another",
        "parameters": {
          "type": "object",
          "properties": {
            "time": {
              "type": "string",
              "description": "The original time in ISO 8601 or HH:MM format, e.g. 14:00 or 2025-05-28T14:00"
            },
            "from_zone": {
              "type": "string",
              "description": "The source time zone, e.g. PST, EST, UTC"
            },
            "to_zone": {
              "type": "string",
              "description": "The target time zone, e.g. CET, IST, JST"
            }
          },
          "required": ["time", "from_zone", "to_zone"]
        }
      }
    }
  ]
}
```

## How Tool Calling Works

Tool calling is triggered during an active conversation when the LLM model needs to invoke a function. Here’s how the process works:

<Note>
  This example explains the `get_current_time` function from the [example configuration](#example-configuration) above.
</Note>

<Frame>
    <img src="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/llm-tool-calling.png?fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=54e4483d6fb3d2d2aa5c0a7d1ee18804" alt="" data-og-width="2315" width="2315" data-og-height="1502" height="1502" data-path="images/llm-tool-calling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/llm-tool-calling.png?w=280&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=4e569933ca1e077b72260b6968489bca 280w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/llm-tool-calling.png?w=560&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=38777a0216b23b2aaf564ea9da30ad9a 560w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/llm-tool-calling.png?w=840&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=eaac1ab19296fd2afabd183243034b4f 840w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/llm-tool-calling.png?w=1100&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=07041d80e3e5035e5aeb783ff18feb36 1100w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/llm-tool-calling.png?w=1650&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=10c9106e46062f88ac5840619967aaab 1650w, https://mintcdn.com/tavus/yrvSX4NJrNH338WQ/images/llm-tool-calling.png?w=2500&fit=max&auto=format&n=yrvSX4NJrNH338WQ&q=85&s=4cdf41d3a1f4944f5c6270f83007f141 2500w" />
</Frame>

## Modify Existing Tools

You can update `tools` definitions using the <a href="/api-reference/personas/patch-persona" target="_blank">Update Persona API</a>.

```shell [expandable] theme={null}
curl --request PATCH \
  --url https://tavusapi.com/v2/personas/{persona_id} \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api-key>' \
  --data '[
    {
      "op": "replace",
      "path": "/layers/llm/tools",
      "value": [
        {
          "type": "function",
          "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                },
                "unit": {
                  "type": "string",
                  "enum": ["celsius", "fahrenheit"]
                }
              },
              "required": ["location", "unit"]
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
