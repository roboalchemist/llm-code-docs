# Source: https://dev.writer.com/connectors/snowflake.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Snowflake connector

> Connect WRITER Agent to Snowflake to access SQL analytics, Cortex tools, object metadata, and semantic views

This guide shows you how to configure the [Snowflake](https://www.snowflake.com/) connector for WRITER Agent. After setting up this connector, WRITER Agent can translate natural-language queries into Snowflake calls across Cortex tools (Analyst, Search, Agent), SQL operations, object management, and Semantic Manager functions for querying semantic views, dimensions, and metrics.

<Warning>
  The Snowflake connector uses Snowflake's native role-based permissions. Users have the same permissions in Writer that they have in Snowflake. For example, if a user's Snowflake role allows write operations like `CREATE TABLE`, `INSERT`, `UPDATE`, or `DELETE`, they can perform those same operations through Writer.
</Warning>

## Set up the Snowflake connector

Configure the Snowflake connector in [AI Studio](https://app.writer.com/aistudio) under **Connectors & Tools**. The Snowflake connector requires organization-managed OAuth authentication.

<Note>
  The Snowflake connector only supports organization-managed OAuth. You must create an MCP Server and configure OAuth in your Snowflake account. WRITER-managed OAuth is not available for Snowflake.
</Note>

### Create a Snowflake MCP Server

Set up an MCP Server and OAuth in Snowflake:

1. In the [Snowflake web interface](https://app.snowflake.com/), open a SQL worksheet and set the database and schema context where the MCP Server should live

2. Create the MCP Server:
   ```sql  theme={null}
   CREATE MCP SERVER <server_name>
    FROM SPECIFICATION $$
      tools:
        - name: "sql_exec_tool"
          type: "SYSTEM_EXECUTE_SQL"
          title: "SQL Execution Tool"
          description: "Execute SQL queries against the connected Snowflake database"
        - name: "analyst_tool"
          type: "CORTEX_ANALYST_MESSAGE"
          title: "Cortex Analyst Tool"
          identifier: "<database>.<schema>.<semantic_view>"
          description: "Query data using natural language through Cortex Analyst"
        - name: "search_tool"
          type: "CORTEX_SEARCH_SERVICE_QUERY"
          title: "Cortex Search Tool"
          identifier: "<database>.<schema>.<search_service>"
          description: "Search unstructured data using Cortex Search"
    $$;
   ```
   Snowflake currently supports the following MCP tool types:
   * `SYSTEM_EXECUTE_SQL`: Execute SQL queries against Snowflake
   * `CORTEX_ANALYST_MESSAGE`: Query data using natural language through semantic views
   * `CORTEX_SEARCH_SERVICE_QUERY`: Search unstructured data using Cortex Search
   * `CORTEX_AGENT_RUN`: Invoke a Cortex Agent
   * `GENERIC`: Call custom user-defined functions or stored procedures

3. Grant the [required Snowflake privileges](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp#access-control) based on the MCP tools you exposed in step 2:
   ```sql  theme={null}
    -- Allow the role to access the MCP Server
    GRANT USAGE ON MCP SERVER <server_name> TO ROLE <role_name>;

    -- Required for SYSTEM_EXECUTE_SQL
    GRANT USAGE ON WAREHOUSE <warehouse_name> TO ROLE <role_name>;
    GRANT USAGE ON DATABASE <database> TO ROLE <role_name>;
    GRANT USAGE ON SCHEMA <database>.<schema> TO ROLE <role_name>;
    GRANT SELECT ON ALL TABLES IN SCHEMA <database>.<schema> TO ROLE <role_name>;

    -- Required only if you expose Cortex tools
    -- Cortex Analyst (semantic views)
    GRANT SELECT ON SEMANTIC VIEW <database>.<schema>.<semantic_view> TO ROLE <role_name>;

    -- Cortex Search
    GRANT USAGE ON CORTEX SEARCH SERVICE <database>.<schema>.<search_service> TO ROLE <role_name>;
   ```

4. Create the [security integration](https://docs.snowflake.com/sql-reference/sql/create-security-integration-oauth-snowflake) with the Writer redirect URI and refresh token support:
   ```sql  theme={null}
    CREATE OR REPLACE SECURITY INTEGRATION <integration_name>
    TYPE = OAUTH
    OAUTH_CLIENT = CUSTOM
    ENABLED = TRUE
    OAUTH_CLIENT_TYPE = 'CONFIDENTIAL'
    OAUTH_REDIRECT_URI = 'https://app.writer.com/mcp/oauth/callback'
    OAUTH_ISSUE_REFRESH_TOKENS = TRUE;
   ```

5. Retrieve and copy your **client ID** and **client secret** for use in [AI Studio](#configure-the-connector-in-ai-studio):
   ```sql  theme={null}
   SELECT SYSTEM$SHOW_OAUTH_CLIENT_SECRETS('<INTEGRATION_NAME>');
   ```

6. Note your **Snowflake MCP Server URL**, which combines your tenant URL and MCP Server path for use in [AI Studio](#configure-the-connector-in-ai-studio):
   ```
   https://<account_identifier>.snowflakecomputing.com/api/v2/databases/<database>/schemas/<schema>/mcp-servers/<mcp_server_name>
   ```

For detailed instructions, see [Snowflake's managed MCP server guide](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp).

### Configure the connector in AI Studio

After creating your Snowflake MCP Server and OAuth integration:

1. Navigate to **Connectors & Tools** in [AI Studio](https://app.writer.com/aistudio)
2. Select the Snowflake connector
3. Select who has access by default (all users or specific teams)
4. Enter your Snowflake tenant URL (MCP Server URL), OAuth client ID, and client secret
5. Complete the OAuth authorization flow

## Next steps

* [Set up connectors](https://support.writer.com/article/299-setting-up-connectors): Learn how to configure and enable connectors in AI Studio
* [Tool calling guide](/home/tool-calling): Understand how AI agents use tools in conversations
* [WRITER Agent guide](https://support.writer.com/article/293-how-to-use-action-agent): Learn how to use WRITER Agent with connected tools
* [MCP gateway overview](/home/mcp-gateway): Learn about Writer's MCP gateway architecture
* [Snowflake-managed MCP server](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp): Learn about creating and configuring MCP servers in Snowflake
