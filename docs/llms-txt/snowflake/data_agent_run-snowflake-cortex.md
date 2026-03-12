# Source: https://docs.snowflake.com/en/sql-reference/functions/data_agent_run-snowflake-cortex.md

Categories:
:   [String & binary functions](../functions-string.md) (AI Functions)

# DATA_AGENT_RUN (SNOWFLAKE.CORTEX)

Runs a [Cortex Agent](../../user-guide/snowflake-cortex/cortex-agents.md) and returns the response as JSON.

You can use this function to run a Cortex Agent, which orchestrates across both structured and unstructured data sources to deliver insights. This includes planning tasks, using tools to execute these tasks, and generating responses.

> **Note:**
>
> `SNOWFLAKE.CORTEX.DATA_AGENT_RUN` is a utility wrapper around the [Cortex Agents Run API](../../user-guide/snowflake-cortex/cortex-agents-run.md).
> For most application integrations, Snowflake recommends calling the **streaming REST API** directly.

See also:
:   [CREATE AGENT](../sql/create-agent.md) , [SHOW AGENTS](../sql/show-agents.md) , [DESCRIBE AGENT](../sql/desc-agent.md) , [DROP AGENT](../sql/drop-agent.md)

## Syntax

```sqlsyntax
SNOWFLAKE.CORTEX.DATA_AGENT_RUN( '<agent_name>', <request_body> )
```

## Arguments

`'agent_name'`
:   Fully qualified name of the agent to run, in the form `database.schema.agent_name`.

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
      }
    }
    ```

> **Important:**
>
> The `stream` field is ignored. A non-streaming response is always returned.

## Returns

Returns a JSON string containing the agent’s response.

## Access control requirements

To run an agent, you must use a role that can access Cortex Agents and the agent object you’re calling.
For details, see [Access control requirements](../../user-guide/snowflake-cortex/cortex-agents.md).

## Usage notes

* The function returns a JSON string. Pass this string to [TRY_PARSE_JSON](try_parse_json.md) to convert the response to a VARIANT value.

## Examples

Run an agent and parse the response JSON:

```sqlexample
SELECT
  TRY_PARSE_JSON(
    SNOWFLAKE.CORTEX.DATA_AGENT_RUN(
      'MY_DB.MY_SCHEMA.MY_AGENT',
      $${
        "parent_message_id": 1234,
        "thread_id": 5678,
        "messages": [
          {
            "role": "user",
            "content": [
              { "type": "text", "text": "What are some types of products?" }
            ]
          }
        ]
      }$$
    )
  ) AS resp;
```

Sample return value:

```json
{
  "role": "assistant",
  "content": [
    {
      "thinking": {
        "text": "\n...\n"
      },
      "type": "thinking"
    },
    {
      "tool_use": {
        "input": {
          "...": "..."
        },
        "name": "<tool_name>",
        "tool_use_id": "<tool_use_id>",
        "type": "<tool_type>"
      },
      "type": "tool_use"
    },
    {
      "text": "Based on the data available, there are two main types of products...",
      "type": "text"
    }
  ],
  "metadata": {
    "run_id": "<run_id>"
  }
}
```
