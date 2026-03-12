# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-agent.md

# ALTER AGENT

Modifies the properties or specification for an existing [Cortex Agent](../../user-guide/snowflake-cortex/cortex-agents.md).

See also:
:   [CREATE AGENT](create-agent.md), [DESCRIBE AGENT](desc-agent.md), [DROP AGENT](drop-agent.md), [SHOW AGENTS](show-agents.md)

## Syntax

```sqlsyntax
ALTER AGENT <name> SET
  [ COMMENT = '<string>' ]
  [ PROFILE = '<string>' ]

ALTER AGENT <name> MODIFY LIVE VERSION SET SPECIFICATION = <specification>
```

## Required parameters

`name`
:   String that specifies the identifier (i.e. name) for the agent to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`SET ...`
:   Sets one or more specified properties or parameters for the agent:

    `COMMENT = comment`
    :   Specifies the description of the agent.

    `PROFILE = string`
    :   Specifies the agent profile information, such as display name, avatar, and color. Format the string as follows:

        ```none
        '{"display_name": "<display_name>", "avatar": "<avatar>", "color": "<color>"}'
        ```

        The following table describes the key-value pairs in the string:

        | Key | Type | Description |
        | --- | --- | --- |
        | `display_name` | String | Display name for the agent. |
        | `avatar` | String | Avatar image file name or identifier. |
        | `color` | String | Color theme for the agent (such as “blue”, “green”, “red”) |

`MODIFY LIVE VERSION SET SPECIFICATION specification`
:   Specifies the VARCHAR value containing the replacement settings for an agent as either a YAML or JSON object:

    * [Dollar-quoted literal](../data-types-text.md): $$ … $$
    * [Single-quoted string](../data-types-text.md): ‘…’

    The maximum length of the specification object is 100,000 bytes.

    > **Important:**
    >
    > The new specification completely replaces the existing one. Fields that are not included in the new specification are removed.

    The YAML object should have the following structure:

    ```yaml
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

    The JSON object should have the following structure:

    ```none
    {
      "models": {
        "orchestration": "<model_name>"
      },
      "orchestration": {
        "budget": {
          "seconds": <number_of_seconds>,
          "tokens": <number_of_tokens>
        }
      },
      "instructions": {
        "response": "<response_instructions>",
        "orchestration": "<orchestration_instructions>",
        "system": "<system_instructions>",
        "sample_questions": [
          {
            "question": "<sample_question>",
            "answer": "<sample_answer>"
          }
        ]
      },
      "tools": [
        {
          "tool_spec": {
            "type": "<tool_type>",
            "name": "<tool_name>",
            "description": "<tool_description>",
            "input_schema": {
              "type": "object",
              "properties": {
                "<property_name>": {
                  "type": "<property_type>",
                  "description": "<property_description>"
                }
              },
              "required": ["<required_property_names>"]
            }
          }
        }
      ],
      "tool_resources": {
        "<tool_name>": {
          "<resource_key>": "<resource_value>"
        }
      }
    }
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
| OWNERSHIP or MODIFY | Agent | Required to modify the agent properties or specification.  OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When modifying a live version’s specification, the new specification completely replaces the existing one.
  Fields that are not included in the new specification are removed.
* Both YAML and JSON formats are supported for specifications.
* Invalid specification fields result in an error.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Update the comment for an agent:

```sqlexample
ALTER AGENT my_support_agent SET COMMENT = 'Customer support agent for product inquiries';
```

Update the profile for an agent:

```sqlexample
ALTER AGENT my_support_agent SET PROFILE = '{"display_name": "Support Bot", "avatar": "bot-icon.png"}';
```

Update both the comment and profile together:

```sqlexample
ALTER AGENT my_support_agent
  SET COMMENT = 'Production support agent',
      PROFILE = '{"display_name": "Customer Assistant", "avatar": "assistant.png"}';
```

Update the live version specification using YAML format:

```sqlexample-yaml
ALTER AGENT my_support_agent
  MODIFY LIVE VERSION SET SPECIFICATION =
  $$
  models:
    orchestration: claude-4-sonnet

  orchestration:
    budget:
      seconds: 30
      tokens: 50000

  instructions:
    system: "You are a helpful customer support assistant."
    response: "Always be concise and accurate."
    sample_questions:
      - question: "What is the status of my order?"
        answer: "I can help you check your order status. Please provide your order number."
  $$;
```

Update the live version specification using JSON format:

```sqlexample
ALTER AGENT my_support_agent
  MODIFY LIVE VERSION SET SPECIFICATION = '{"models":{"orchestration":"claude-4-sonnet"},"orchestration":{"budget":{"seconds":45,"tokens":80000}}}';
```
