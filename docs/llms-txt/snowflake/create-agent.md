# Source: https://docs.snowflake.com/en/sql-reference/sql/create-agent.md

# CREATE AGENT

Creates a new [Cortex Agent](../../user-guide/snowflake-cortex/cortex-agents.md) object with the specified attributes and specification.

See also:
:   [ALTER AGENT](alter-agent.md), [DESCRIBE AGENT](desc-agent.md), [DROP AGENT](drop-agent.md), [SHOW AGENTS](show-agents.md), [DATA_AGENT_RUN (SNOWFLAKE.CORTEX)](../functions/data_agent_run-snowflake-cortex.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] AGENT [ IF NOT EXISTS ] <name>
  [ COMMENT = '<comment>' ]
  [ PROFILE = '<profile_object>' ]
  FROM SPECIFICATION
  $$
  <specification_object>
  $$;
```

## Required parameters

`name`
:   String that specifies the identifier (i.e. name) for the agent; must be unique for the schema in which the agent is created.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`COMMENT = comment`
:   Description of the agent.

`PROFILE = profile_object`
:   Specifies the [OBJECT](../data-types-semistructured.md) value containing agent profile information, such as display name, avatar, and color. Serialize the `profile_object` into a string as follows:

    ```none
    '{"display_name": "<display_name>", "avatar": "<avatar>", "color": "<color>"}'
    ```

    The following table describes the key-value pairs in this object:

    | Key | Type | Description |
    | --- | --- | --- |
    | `display_name` | String | Display name for the agent. |
    | `avatar` | String | Avatar image file name or identifier. |
    | `color` | String | Color theme for the agent (such as “blue”, “green”, “red”) |

`FROM SPECIFICATION $$ specification_object $$`
:   Specifies the VARCHAR value containing the settings for an agent as a YAML object. The maximum length of the specification object is 100,000 bytes.

    The YAML object should have the following structure:

    ```YAML
    models:
      orchestration: <model_name>

    orchestration:
      budget:
          seconds: <number_of_seconds>
          tokens: <number_of_tokens>

    instructions:
      response: '<response_instructions>'
      orchestration: '<orchestration_instructions>'
      system: '<system_instructions>'
      sample_questions:
          - question: '<sample_question>'
            answer: '<sample_answer>'
          ...

    tools:
      - tool_spec:
          type: '<tool_type>'
          name: '<tool_name>'
          description: '<tool_description>'
          input_schema:
              type: 'object'
              properties:
                <property_name>:
                  type: '<property_type>'
                  description: '<property_description>'
              required: <required_property_names>
      ...

    tool_resources:
      <tool_name>:
        <resource_key>: '<resource_value>'
        ...
      ...
    ```

    The following table describes the key-value pairs in this object:

    | Key | Type | Description |
    | --- | --- | --- |
    | `models` | [ModelConfig](../../user-guide/snowflake-cortex/cortex-agents-rest-api.md) | An optional model configuration for the agent. Includes the orchestration model (e.g., claude-4-sonnet). If not provided, a model is automatically selected. Currently only available for the `orchestration` step. |
    | `orchestration` | [OrchestrationConfig](../../user-guide/snowflake-cortex/cortex-agents-rest-api.md) | An optional orchestration configuration, including budget constraints (e.g., seconds, tokens). |
    | `instructions` | [AgentInstructions](../../user-guide/snowflake-cortex/cortex-agents-rest-api.md) | Optional instructions for the agent’s behavior, including response, orchestration, system, and sample questions. |
    | `tools` | array of [Tool](../../user-guide/snowflake-cortex/cortex-agents-rest-api.md) | An optional list of tools available for the agent to use. Each tool includes a `tool_spec` with type, name, description, and input schema. Tools may have a corresponding configuration in `tool_resources`. |
    | `tool_resources` | map of [ToolResource](../../user-guide/snowflake-cortex/cortex-agents-rest-api.md) | An optional configuration for each tool referenced in the tools array. Keys must match the name of the respective tool. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE AGENT | Schema | Required to create the Cortex Agent. |
| USAGE | Cortex Search service | Required to run the Cortex Search services in the Cortex Agents request. |
| USAGE | Database, schema, table | Required to access the objects referenced in the Cortex Agents semantic model. |

## Usage notes

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

```sqlexample
CREATE OR REPLACE AGENT my_agent1
  COMMENT = 'agent level comment'
  PROFILE = '{"display_name": "My Business Assistant", "avatar":  "business-icon.png", "color": "blue"}'
  FROM SPECIFICATION
  $$
  models:
    orchestration: claude-4-sonnet

  orchestration:
    budget:
      seconds: 30
      tokens: 16000

  instructions:
    response: "You will respond in a friendly but concise manner"
    orchestration: "For any revenue question use Analyst; for policy use Search"
    system: "You are a friendly agent that helps with business questions"
    sample_questions:
      - question: "What was our revenue last quarter?"
        answer: "I'll analyze the revenue data using our financial database."

  tools:
    - tool_spec:
        type: "cortex_analyst_text_to_sql"
        name: "Analyst1"
        description: "Converts natural language to SQL queries for financial analysis"
    - tool_spec:
        type: "cortex_search"
        name: "Search1"
        description: "Searches company policy and documentation"

  tool_resources:
    Analyst1:
      semantic_view: "db.schema.semantic_view"
    Search1:
      name: "db.schema.service_name"
      max_results: "5"
      filter:
        "@eq":
          region: "North America"
      title_column: "<title_name>"
      id_column: "<column_name>"
  $$;
```
