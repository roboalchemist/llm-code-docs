# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-monitor.md

# Monitor Cortex Agent requests

Cortex Agents log detailed traces of all conversations for auditing and debugging purposes. With monitoring,
you can access the conversation history of an Agent deployed via Snowflake Intelligence or Agent API.
In addition to conversation history, you can review detailed tracing of the agent’s planning process,
tool selection, execution results, and final response generation.

## Information collected in Cortex Agent logs

Cortex Agent logs include the following information:

* Conversation history associated with a thread
* Agent’s execution trace with spans including:

  * LLM planning
  * Tool execution (Cortex Search, Cortex Analyst, web search)
  * LLM response generation
  * SQL execution
  * Chart generation
* Inputs and outputs associated with each span
* User feedback for each Agent response

## Access Cortex Agent logs

To view Cortex Agent conversation logs in Snowsight, do the following:

1. Sign in to [Snowsight](../ui-snowsight-gs.md).
2. In the navigation menu, select AI & ML » Agents.
3. Select the Agent whose logs you wish to view.
4. Navigate to the Monitoring pane of the Agent view.

The monitoring logs associated with the Agent are stored in the [event table](../../developer-guide/logging-tracing/event-table-setting-up.md) SNOWFLAKE.LOCAL.AI_OBSERVABILITY_EVENTS. Entries in this table can’t be modified.

Administrators with the AI_OBSERVABILITY_ADMIN application role can delete entries in the
SNOWFLAKE.LOCAL.AI_OBSERVABILITY_EVENTS table.

### View feedback provided by users

To view user feedback about agents programmatically, run the following SQL command:

> ```sqlexample
> SELECT * FROM TABLE(SNOWFLAKE.LOCAL.GET_AI_OBSERVABILITY_EVENTS('<database_name>', '<schema_name>', '<agent_name>', 'CORTEX AGENT')) WHERE RECORD:name='CORTEX_AGENT_FEEDBACK';
> ```

The resulting table contains columns that include information about the agent, the user who provided feedback, feedback provided by the user, and whether the feedback was positive or negative.

## Access control and permissions

To view Cortex Agent logs, users must have the following privileges:

* OWNERSHIP or MONITOR privileges on the AGENT object
* The CORTEX_USER database role

The following example uses the ACCOUNTADMIN role to create a new role `agent_monitoring_user_role`
with the required permissions to view Cortex Agent logs. This new role is then assigned to `some_user`.

```sqlexample
USE ROLE ACCOUNTADMIN;
CREATE ROLE agent_monitoring_user_role;
GRANT MONITOR ON AGENT my_agent TO ROLE agent_monitoring_user_role;
GRANT DATABASE ROLE SNOWFLAKE.CORTEX_USER TO ROLE agent_monitoring_user_role;
GRANT ROLE agent_monitoring_user_role TO USER some_user;
```

### Grant monitoring access to future agents

To grant a role monitoring access on future agents created in a schema, use the following SQL command:

```sqlexample
GRANT MONITOR ON FUTURE AGENTS IN SCHEMA <database_name>.<schema_name> TO ROLE <role_name>;
```
