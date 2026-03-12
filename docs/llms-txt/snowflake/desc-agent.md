# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-agent.md

# DESCRIBE AGENT

Describes the properties of a [Cortex Agent](../../user-guide/snowflake-cortex/cortex-agents.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [ALTER AGENT](alter-agent.md), [CREATE AGENT](create-agent.md), [DROP AGENT](drop-agent.md), [SHOW AGENTS](show-agents.md), [DATA_AGENT_RUN (SNOWFLAKE.CORTEX)](../functions/data_agent_run-snowflake-cortex.md)

## Syntax

```sqlsyntax
{ DESC | DESCRIBE } AGENT <name>
```

## Parameters

`name`
:   Specifies the name for the agent to describe.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Output

The command output provides Cortex Agent properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| `name` | Name of the agent. |
| `database_name` | Database containing the agent. |
| `schema_name` | Schema containing the agent. |
| `owner` | Owner role of the agent. |
| `comment` | Comment text for the agent. |
| `profile` | Agent profile JSON (display_name, avatar, color). |
| `agent_spec` | Complete YAML specification of the agent. |
| `created_on` | Timestamp when the agent was created. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| Any one of these privileges: OWNERSHIP, USAGE, MONITOR or OPERATE | Agent |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Examples

Describe a Cortex Agent named `MY_AGENT1` in the `TEST_DATABASE` database and `TEST_SCHEMA` schema:

```sqlexample
DESCRIBE AGENT mydb.myschema.my_agent;
```

The statement in the example prints the following output:

```output
+--------------+---------+---------------+-------------+-----------+-----------------------+-------------------------------------+
| name  | database_name | schema_name | owner     | comment          | profile                            | agent_spec                       | created_on         |
|--------------+---------+---------------+-------------+-----------+-----------------------+-------------------------------------|
|| TEST_AGENT | EXAMPLE_DB   | AGENTS | TEST_ROLE | null | {"display_name":"test"} | "{\"models\":{\"orchestration\":\"llama3.1-70B\"},\"nested\":{\"key\":\"value\"}},\"orchestration\":{\"budget\":{\"seconds\":30,\"tokens\":16000}},\"instructions\":{\"response\":\"You will respond in a friendly but concise manner\",\"orchestration\":\"For any revenue question use Analyst; for policy use Search\",\"system\":\"You are a friendly agent.\",\"sample_questions\":[{\"question\":\"question 1\"},{\"question\":\"question 2\"},{\"question\":\"question 3\"}]},\"tools\":[{\"tool_spec\":{\"type\":\"cortex_analyst_text_to_sql\",\"name\":\"Analyst1\",\"description\":\"test\"}},{\"tool_spec\":{\"type\":\"cortex_analyst_sql_exec\",\"name\":\"SQL_exec1\"}},{\"tool_spec\":{\"type\":\"cortex_search\",\"name\":\"Search1\"}},{\"tool_spec\":{\"type\":\"web_search\",\"name\":\"web_search_1\"}},{\"tool_spec\":{\"type\":\"generic\",\"name\":\"get_weather\",\"input_schema\":{\"type\":\"object\",\"properties\":{\"location\":{\"type\":\"string\",\"description\":\"The city and state\"}},\"required\":[\"Location\"]}}}],\"tool_unable_to_answer\":\"I don't know the answer to that\",\"tool_resources\":{\"Analyst1\":{\"semantic_model_file\":\"stage1\"},\"Analyst2\":{\"semantic_view\":\"db.schema.semantic_view\"},\"Search1\":{\"name\":\"db.schema.service_name\",\"Max_results\":\"5\",\"filter\":{\"@eq\":{\"region\":\"North America\"}},\"Title_column\":\"<title_name>\",\"ID_column\":\"<column_name>\"},\"SQL_exec1\":{\"Name\":\"my_warehouse\",\"Timeout\":\"30\",\"AutoExecute\":\"true\"},\"web_search\":{\"name\":\"web_search_1\",\"Function\":\"db/schema/search_web\"}}}" | 2025-09-15 17:04:37.263 +0000 |
+--------------+---------+---------------+-------------+-----------+-----------------------+-------------------------------------+
```

The following example describes an agent in the current schema:

```sqlexample
DESCRIBE AGENT my_agent;
```

The following example describes the agent as a resource in JSON format:

```sqlexample
DESCRIBE AS RESOURCE AGENT my_agent;
```
