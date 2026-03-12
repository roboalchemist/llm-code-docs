# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-02-18-snowflake-intelligence-usage-history-view.md

# Feb 18, 2026: Account Usage New SNOWFLAKE_INTELLIGENCE_USAGE_HISTORY view (*Preview*)

The ACCOUNT_USAGE schema now includes a new [SNOWFLAKE_INTELLIGENCE_USAGE_HISTORY](../../../sql-reference/account-usage/snowflake_intelligence_usage_history_view.md)
view that provides visibility into the usage history of Snowflake Intelligence.

The information in the view includes the number of credits consumed each time a user interacts
with Snowflake Intelligence. A request results in one or more calls to underlying agents and any
tools (for example, Cortex Analyst and Cortex Search). Each row in the view represents a call to the agent and provides detail on
the aggregated tokens and credits in the call as well as granular detail. The view also includes
relevant metadata, such as the user ID, request ID, Snowflake Intelligence ID, and the agent ID.

For more information, see [SNOWFLAKE_INTELLIGENCE_USAGE_HISTORY view](../../../sql-reference/account-usage/snowflake_intelligence_usage_history_view.md).
