# Source: https://docs.snowflake.com/en/sql-reference/functions/agent_run-snowflake-cortex.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# AGENT_RUN (SNOWFLAKE.CORTEX)

Runs a [Cortex Agent](../../user-guide/snowflake-cortex/cortex-agents.md) without an agent object and returns the response as JSON.

You can use this function to interact with Cortex Agents directly without first creating an agent object. You provide the configuration, including the orchestration model and tools, in the request body.

> **Note:**
>
> `SNOWFLAKE.CORTEX.AGENT_RUN` is a utility wrapper around the [Cortex Agents Run REST API](../../user-guide/snowflake-cortex/cortex-agents-run.md).
> For most application integrations, Snowflake recommends calling the **streaming REST API** directly.

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.AGENT_RUN( <request_body> )
```

## Arguments

`request_body`
:   JSON request body to send to the agent. This value must be a string (for example, a `$$...$$` literal).

    The following fields are supported in the request body:

    | Field | Type | Description |
    | --- | --- | --- |
    | `thread_id` | integer | The thread ID for the conversation. If thread_id is used, then parent_message_id must be passed as well. |
    | `parent_message_id` | integer | The ID of the parent message in the thread. If this is the first message, parent_message_id should be 0. |
    | `messages` | array of [Message](../../user-guide/snowflake-cortex/cortex-agents-run.md) | If thread_id and parent_message_id are passed in the request, messages includes the current user message in the conversation. Else, messages includes the conversation history and the current message. Messages contains both user queries and assistant responses in chronological order. |
    | `stream` | boolean | Whether to return a streaming response (`text/event-stream`) or a non-streaming JSON response (`application/json`). If true, the response will be streamed as Server-Sent Events. If false, the response will be returned as JSON. |
    | `tool_choice` | [ToolChoice](../../user-guide/snowflake-cortex/cortex-agents-run.md) | Configures how the agent should select and use tools during the interaction. Controls whether tool use is automatic, required, or whether specific tools should be used. |
    | `models` | [ModelConfig](../../user-guide/snowflake-cortex/cortex-agents-run.md) | Model configuration for the agent. Includes the orchestration model (e.g., claude-4-sonnet). If not provided, a model is automatically selected. Currently only available for the `orchestration` step. |
    | `instructions` | [AgentInstructions](../../user-guide/snowflake-cortex/cortex-agents-run.md) | Instructions for the agent’s behavior, including response, orchestration, system, and sample questions. |
    | `orchestration` | [OrchestrationConfig](../../user-guide/snowflake-cortex/cortex-agents-run.md) | Orchestration configuration, including budget constraints (e.g., seconds, tokens). |
    | `tools` | array of [Tool](../../user-guide/snowflake-cortex/cortex-agents-run.md) | List of tools available for the agent to use. Each tool includes a tool_spec with type, name, description, and input schema. Tools may have a corresponding configuration in tool_resources. |
    | `tool_resources` | map of [ToolResource](../../user-guide/snowflake-cortex/cortex-agents-run.md) | Configuration for each tool referenced in the tools array. Keys must match the name of the respective tool. |

    **Example**

    ```json
    {
      "thread_id": 0,
      "parent_message_id": 0,
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": "What is the total revenue for 2023?"
            }
          ]
        }
      ],
      "stream": false,
      "tool_choice": {
        "type": "auto",
        "name": [
          "analyst_tool",
          "search_tool"
        ]
      },
      "models": {
        "orchestration": "claude-4-sonnet"
      },
      "instructions": {
        "response": "You will respond in a friendly but concise manner",
        "orchestration": "For any query related to revenue we should use Analyst; For all policy questions we should use Search",
        "system": "You are a friendly agent ..."
      },
      "orchestration": {
        "budget": {
          "seconds": 30,
          "tokens": 16000
        }
      },
      "tools": [
        {
          "tool_spec": {
            "type": "generic",
            "name": "get_revenue",
            "description": "Fetch the delivery revenue for a location.",
            "input_schema": {
              "type": "object",
              "properties": {
                "location": {
                  "type": "string",
                  "description": "The city and state, e.g. San Francisco, CA"
                }
              }
            },
            "required": [
              "location"
            ]
          }
        }
      ],
      "tool_resources": {
        "get_revenue": {
          "type": "function",
          "execution_environment": {
            "type": "warehouse",
            "warehouse": "MY_WH"
          },
          "identifier": "DB.SCHEMA.UDF"
        }
      }
    }
    ```

> **Important:**
>
> The `stream` field is ignored. A non-streaming response is always returned.

## Returns

Returns a JSON string containing the agent’s response.

## Access control requirements

To run an agent, you must use a role that can access Cortex Agents.
For details, see [Access control requirements](../../user-guide/snowflake-cortex/cortex-agents.md).

## Usage notes

* The function returns a JSON string. Pass this string to [TRY_PARSE_JSON](try_parse_json.md) to convert the response to a VARIANT value.
* Unlike [DATA_AGENT_RUN (SNOWFLAKE.CORTEX)](data_agent_run-snowflake-cortex.md), this function does not require you to create an agent object first. Instead, you provide the configuration directly in the request body.

## Examples

Run an agent and parse the response JSON:

```sqlexample
SELECT
  TRY_PARSE_JSON(
    SNOWFLAKE.CORTEX.AGENT_RUN(
      $${
        "messages": [
          {
            "role": "user",
            "content": [
              {
                "type": "text",
                "text": "What is the total revenue for 2025?"
              }
            ]
          }
        ],
        "models": {
          "orchestration": "claude-4-sonnet"
        }
      }$$
    )
  ) AS resp;
```

Sample return value:

```json
{
  "content": [
    {
      "text": "The total revenue for 2025 was $100,000.",
      "type": "text"
    }
  ],
  "metadata": {
    "usage": {
      "tokens_consumed": [
        {
          "context_window": 200000,
          "input_tokens": {
            "cache_read": 0,
            "cache_write": 0,
            "total": 67,
            "uncached": 67
          },
          "model_name": "claude-4-sonnet",
          "output_tokens": {
            "total": 38
          }
        }
      ]
    }
  },
  "role": "assistant"
}
```
