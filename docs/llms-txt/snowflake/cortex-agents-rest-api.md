# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-rest-api.md

# Cortex Agents REST API

> **Note:**
>
> Requests to the Cortex Agent REST API time out after 15 minutes.

You can use the Cortex Agent REST API to create, manage, and interact with Cortex Agent Objects in your Snowflake account.

## Create Cortex Agent

`POST /api/v2/databases/{database}/schemas/{schema}/agents`

Creates a new Cortex Agent Object with the specified attributes and specification.

### Request

#### Path parameters

| Parameter | Description |
| --- | --- |
| `database` | (Required) Your Snowflake Account URL. |
| `schema` | (Required) Schema identifier. |

#### Query parameters

| Parameter | Description |
| --- | --- |
| `createMode` | (Optional) Resource creation mode. Valid values:  *`errorIfExists`* `orReplace` * `ifNotExists` |

#### Request headers

| Header | Description |
| --- | --- |
| `Authorization` | (Required) Authorization token. For more information, see [Authentication](cortex-agents.md). |
| `Content-Type` | (Required) application/json |

#### Request body

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Name of the agent. |
| `comment` | string | Optional comment about the agent. |
| `profile` | AgentProfile | Agent profile information (display name, avatar, color, etc.). |
| `models` | ModelConfig | Model configuration for the agent. Includes the orchestration model (e.g., claude-4-sonnet). If not provided, a model is automatically selected. Currently only available for the `orchestration` step. |
| `instructions` | AgentInstructions | Instructions for the agent’s behavior, including response, orchestration, system, and sample questions. |
| `orchestration` | OrchestrationConfig | Orchestration configuration, including budget constraints (e.g., seconds, tokens). |
| `tools` | array of Tool | List of tools available for the agent to use. Each tool includes a tool_spec with type, name, description, and input schema. Tools may have a corresponding configuration in tool_resources. |
| `tool_resources` | map of ToolResource | Configuration for each tool referenced in the tools array. Keys must match the name of the respective tool. |

**Example**

```json
{
  "name": "MY_AGENT",
  "comment": "An agent to answer questions about all my data",
  "profile": {
    "display_name": "My Agent"
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

### Response

A successful response returns a JSON object with details about the status of Cortex Agent creation.

#### Response body

```json
{"status": "Agent xxxx successfully created."}
```

## Describe Cortex Agent

`GET /api/v2/databases/{database}/schemas/{schema}/agents/{name}`

Describes a Cortex Agent.

### Request

#### Path parameters

| Parameter | Description |
| --- | --- |
| `database` | (Required) Identifier for the database to which the resource belongs. You can use the /api/v2/databases GET request to get a list of available databases. |
| `schema` | (Required) Identifier for the schema to which the resource belongs. You can use the /api/v2/databases/{database}/schemas GET request to get a list of available schemas for the specified database. |
| `name` | (Required) Identifier for the agent. |

#### Request headers

| Header | Description |
| --- | --- |
| `Authorization` | (Required) Authorization token. For more information, see [Authentication](cortex-agents.md). |
| `Content-Type` | (Required) application/json |

### Response

A successful response returns a JSON object describing the Cortex Agent.

#### Response headers

| Header | Description |
| --- | --- |
| `X-Snowflake-Request-ID` | Unique ID of the API request. |
| `Link` | Links to the page of results (e.g. the first page, the last page, etc.). The header can include multiple url entries with different rel attribute values that specify the page to return (first, next, prev, and last). |

#### Response body

The response body contains the details of the Cortex Agent.

```json
{
  "agent_spec": "{\"models\":{\"orchestration\":\"llama3.1-70B\"},\"experimental\":{\"foo\":\"bar\",\"nested\":{\"key\":\"value\"}},\"orchestration\":{\"budget\":{\"seconds\":30,\"tokens\":16000}},\"instructions\":{\"response\":\"You will respond in a friendly but concise manner\",\"orchestration\":\"For any revenue question use Analyst; for policy use Search\",\"system\":\"You are a friendly agent.\",\"sample_questions\":[{\"question\":\"question 1\"},{\"question\":\"question 2\"},{\"question\":\"question 3\"}]},\"tools\":[{\"tool_spec\":{\"type\":\"cortex_analyst_text_to_sql\",\"name\":\"Analyst1\",\"description\":\"test\"}},{\"tool_spec\":{\"type\":\"cortex_analyst_sql_exec\",\"name\":\"SQL_exec1\"}},{\"tool_spec\":{\"type\":\"cortex_search\",\"name\":\"Search1\"}},{\"tool_spec\":{\"type\":\"web_search\",\"name\":\"web_search_1\"}},{\"tool_spec\":{\"type\":\"generic\",\"name\":\"get_weather\",\"input_schema\":{\"type\":\"object\",\"properties\":{\"location\":{\"type\":\"string\",\"description\":\"The city and state\"}},\"required\":[\"Location\"]}}}],\"tool_unable_to_answer\":\"I don't know the answer to that\",\"tool_resources\":{\"Analyst1\":{\"semantic_model_file\":\"stage1\"},\"Analyst2\":{\"semantic_view\":\"db.schema.semantic_view\"},\"Search1\":{\"name\":\"db.schema.service_name\",\"Max_results\":\"5\",\"filter\":{\"@eq\":{\"region\":\"North America\"}},\"Title_column\":\"<title_name>\",\"ID_column\":\"<column_name>\"},\"SQL_exec1\":{\"Name\":\"my_warehouse\",\"Timeout\":\"30\",\"AutoExecute\":\"true\"},\"web_search\":{\"name\":\"web_search_1\",\"Function\":\"db/schema/search_web\"}}}",
  "name": "MY_AGENT1",
  "database_name": "TEST_DATABASE",
  "schema_name": "TEST_SCHEMA",
  "owner": "ACCOUNTADMIN",
  "created_on": "1967-06-23T07:00:00.123+00:00"
}
```

## Update Cortex Agent

`PUT /api/v2/databases/{database}/schemas/{schema}/agents/{name}`

Updates an existing Cortex Agent with the specified attributes and specification.

### Request

#### Path parameters

| Parameter | Description |
| --- | --- |
| `database` | (Required) Your Snowflake Account URL. You can use the `/api/v2/databases` GET request to get a list of available databases. |
| `schema` | (Required) Schema identifier. You can use the `/api/v2/databases/{database}/schemas` GET request to get a list of available schemas for the specified database. |
| `name` | (Required) Name of the agent. |

#### Request headers

| Header | Description |
| --- | --- |
| `Authorization` | (Required) Authorization token. For more information, see [Authentication](cortex-agents.md). |
| `Content-Type` | (Required) application/json |

#### Request body

| Field | Type | Description |
| --- | --- | --- |
| `comment` | string | Optional comment about the agent. |
| `profile` | AgentProfile | Agent profile information (display name, avatar, color, etc.). |
| `models` | ModelConfig | Model configuration for the agent. Includes the orchestration model (e.g., claude-4-sonnet). If not provided, a model is automatically selected. Currently only available for the `orchestration` step. |
| `instructions` | AgentInstructions | Instructions for the agent’s behavior, including response, orchestration, system, and sample questions. |
| `orchestration` | OrchestrationConfig | Orchestration configuration, including budget constraints (e.g., seconds, tokens). |
| `tools` | array of Tool | List of tools available for the agent to use. Each tool includes a tool_spec with type, name, description, and input schema. Tools may have a corresponding configuration in tool_resources. |
| `tool_resources` | map of ToolResource | Configuration for each tool referenced in the tools array. Keys must match the name of the respective tool. |

**Example**

```json
{
  "comment": "An agent to answer questions about all my data",
  "profile": {
    "display_name": "My Agent"
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

### Response

A successful response returns a JSON object with details about the status of Cortex Agent update.

#### Response body

```json
{"status": "Agent xxxx successfully updated."}
```

## List Cortex Agents

`GET /api/v2/databases/{database}/schemas/{schema}/agents`

Lists the Cortex Agents under the specified database and schema.

### Request

#### Path parameters

| Parameter | Description |
| --- | --- |
| `database` | (Required) Identifier for the database to which the resource belongs. You can use the /api/v2/databases GET request to get a list of available databases. |
| `schema` | (Required) Identifier for the schema to which the resource belongs. You can use the /api/v2/databases/{database}/schemas GET request to get a list of available schemas for the specified database. |

#### Query parameters

| Parameter | Description |
| --- | --- |
| `like` | (Optional) Filter the output by resource name. Uses case-insensitive pattern matching with support for SQL wildcard characters. |
| `fromName` | (Optional) Enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. |
| `showLimit` | (Optional) Limit the maximum number of rows returned by the command. Minimum: 1. Maximum: 10000. |

#### Request headers

| Header | Description |
| --- | --- |
| `Authorization` | (Required) Authorization token. For more information, see [Authentication](cortex-agents.md). |
| `Content-Type` | (Required) application/json |

### Response

A successful response returns a JSON array of Cortex Agent resources.

#### Response headers

| Header | Description |
| --- | --- |
| `X-Snowflake-Request-ID` | Unique ID of the API request. |
| `Link` | Links to the page of results (e.g. the first page, the last page, etc.). The header can include multiple url entries with different rel attribute values that specify the page to return (first, next, prev, and last). |

#### Response body

```json
[
 {
  "name": "my_agent",
  "database": "TEST_DB",
  "schema": "TEST_SCHEMA",
  "created_on": "2024-06-01T12:00:00Z",
  "owner": "ACCOUNTADMIN",
  "comment": "Sample agent"
 },
 {
  "name": "another_agent",
  "database": "TEST_DB",
  "schema": "TEST_SCHEMA",
  "created_on": "2024-06-02T08:30:00Z",
  "owner": "SYSADMIN",
  "comment": ""
 }
]
```

## Delete Cortex Agent

`DELETE /api/v2/databases/{database}/schemas/{schema}/agents/{name}`

Deletes a Cortex Agent with the specified name. If the `ifExists` parameter is set to `true`, the operation succeeds even if the agent does not exist. Otherwise, the operation fails if the agent cannot be deleted.

### Request

#### Path parameters

| Parameter | Description |
| --- | --- |
| `database` | (Required) Identifier for the database to which the resource belongs. You can use the /api/v2/databases GET request to get a list of available databases. |
| `schema` | (Required) Identifier for the schema to which the resource belongs. You can use the /api/v2/databases/{database}/schemas GET request to get a list of available schemas for the specified database. |
| `name` | (Required) Identifier for the agent. |

#### Query parameters

| Parameter | Description |
| --- | --- |
| `ifExists` | (Optional) Specifies how to handle the request if the agent does not exist.   *`true`: The endpoint does not throw an error if the agent does not exist. It returns a 200 success response, but does not take any action.* `false`: The endpoint throws an error if the agent does not exist. |

#### Request headers

| Header | Description |
| --- | --- |
| `Authorization` | (Required) Authorization token. For more information, see [Authentication](cortex-agents.md). |
| `Content-Type` | (Required) application/json |

### Response

A successful response returns a confirmation message.

#### Response body

```json
{
 "status": "Request successfully completed"
}
```

## Schemas

### `AgentInstructions`

| Field | Type | Description |
| --- | --- | --- |
| `response` | string | Instructions for response generation. |
| `orchestration` | string | These custom instructions are used when the agent is planning which tools to use. |
| `system` | string | System instructions for the agent. |

**Example**

```json
{
  "response": "You will respond in a friendly but concise manner",
  "orchestration": "For any query related to revenue we should use Analyst; For all policy questions we should use Search",
  "system": "You are a friendly agent ..."
}
```

### `AgentProfile`

The profile information for a Data Cortex agent.

| Field | Type | Description |
| --- | --- | --- |
| `display_name` | string | Display name for the agent. |

**Example**

```json
{
  "display_name": "My Agent"
}
```

### `BudgetConfig`

| Field | Type | Description |
| --- | --- | --- |
| `seconds` | integer | Time budget in seconds. |
| `tokens` | integer | Token budget. |

**Example**

```json
{
  "seconds": 30,
  "tokens": 16000
}
```

### `ExecutionEnvironment`

Configuration for server-executed tools.

| Field | Type | Description |
| --- | --- | --- |
| `type` | string | The type of execution environment, currently only `warehouse` is supported. |
| `warehouse` | string | The name of the warehouse. Case-sensitive, if it is an unquoted identifier, provide the name in all-caps. |
| `query_timeout` | integer | The query timeout in seconds |

**Example**

```json
{
  "type": "warehouse",
  "warehouse": "MY_WAREHOUSE",
  "query_timeout": 60
}
```

### `ModelConfig`

| Field | Type | Description |
| --- | --- | --- |
| `orchestration` | string | Model to use for orchestration. If not provided, a model is automatically selected. |

**Example**

```json
{
  "orchestration": "claude-4-sonnet"
}
```

### `OrchestrationConfig`

| Field | Type | Description |
| --- | --- | --- |
| `budget` | BudgetConfig | Budget constraints for the agent. If more than one constraint is specified, whichever is first hit will end the request. |

**Example**

```json
{
  "budget": {
    "seconds": 30,
    "tokens": 16000
  }
}
```

### `Tool`

Defines a tool that can be used by the agent. Tools provide specific capabilities like data analysis, search, or generic functions.

| Field | Type | Description |
| --- | --- | --- |
| `tool_spec` | ToolSpec | Specification of the tool’s type, configuration, and input requirements. |

**Example**

```json
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
```

### `ToolInputSchema`

| Field | Type | Description |
| --- | --- | --- |
| `type` | string | The type of the input schema object. |
| `description` | string | A description of what the input is. |
| `properties` | map of ToolInputSchema | If type is `object`, definitions of each input parameter. |
| `items` | ToolInputSchema | If type is `array`, the schema for the elements of the array. |
| `required` | array of string | If type is `object`, list of required input parameter names. |

**Example**

```json
{
  "type": "object",
  "description": "Input for my custom tool",
  "properties": {
    "location": {
      "type": "string",
      "description": "The city and state, e.g. San Francisco, CA"
    }
  },
  "items": {},
  "required": [
    "location"
  ]
}
```

### `ToolResource`

> cortex_analyst_text_to_sqlcortex_searchgenericweb_search
>
> Configuration for text-to-SQL analysis tool. Provides parameters for SQL query generation and execution. Exactly one of semantic_model_file or semantic_view must be provided.
>
> | Field | Type | Description |
> | --- | --- | --- |
> | `semantic_model_file` | string | The path to a file stored in a Snowflake Stage holding the semantic model yaml. |
> | `semantic_view` | string | The name of the Snowflake native semantic model object. |
> | `execution_environment` | ExecutionEnvironment | Configuration for how to execute the generated SQL query. |
>
> **Example**
>
> ```json
> {
>   "semantic_model_file": "@db.schema.stage/semantic_model.yaml",
>   "semantic_view": "db.schema.semantic_view",
>   "execution_environment": {
>     "type": "warehouse",
>     "warehouse": "MY_WAREHOUSE",
>     "query_timeout": 60
>   }
> }
> ```
>
> Configuration for search functionality. Defines how document search and retrieval should be performed.
>
> | Field | Type | Description |
> | --- | --- | --- |
> | `search_service` | string | The fully qualified name of the search service. |
> | `title_column` | string | The title column of the document. |
> | `id_column` | string | The ID column of the document. |
> | `filter` | object | Filter query for search results. |
>
> **Example**
>
> ```json
> {
>   "search_service": "database.schema.service_name",
>   "title_column": "account_name",
>   "id_column": "account_id",
>   "filter": {
>     "@eq": {
>       "<column>": "<value>"
>     }
>   }
> }
> ```
>
> | Field | Type | Description |
> | --- | --- | --- |
> | `type` | string | If the tool is server-side executed, whether it is a Stored Procedure or a UDF. |
> | `execution_environment` | ExecutionEnvironment |  |
> | `identifier` | string | Fully qualified name of the Stored Procedure or UDF. |
>
> **Example**
>
> ```json
> {
>   "type": "function",
>   "execution_environment": {
>     "type": "warehouse",
>     "warehouse": "MY_WAREHOUSE",
>     "query_timeout": 60
>   },
>   "identifier": "MY_DB.MY_SCHEMA.MY_UDF"
> }
> ```
>
> Configuration for web search functionality.
>
> | Field | Type | Description |
> | --- | --- | --- |
> | `max_results` | integer | Max web search results returned. |
>
> **Example**
>
> ```json
> {
>   "max_results": 20
> }
> ```

### `ToolSpec`

Specification of the tool’s type, configuration, and input requirements.

| Field | Type | Description |
| --- | --- | --- |
| `type` | string | The type of tool capability. Can be specialized types like ‘cortex_analyst_text_to_sql’ or ‘generic’ for general-purpose tools. |
| `name` | string | Unique identifier for referencing this tool instance. Used to match with configuration in tool_resources. |
| `description` | string | Description of the tool to be considered for tool use. |
| `input_schema` | ToolInputSchema | JSON Schema definition of the expected input parameters for this tool. This will be fed to the agent so it knows the structure it should follow for when generating the input for ToolUses. Required for generic tools to specify their input parameters. |

**Example**

```json
{
  "type": "generic",
  "name": "get_weather",
  "description": "lorem ipsum",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The city and state, e.g. San Francisco, CA"
      }
    },
    "required": [
      "location"
    ]
  }
}
```
