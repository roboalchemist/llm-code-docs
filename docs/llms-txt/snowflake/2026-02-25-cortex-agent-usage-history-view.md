# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-02-25-cortex-agent-usage-history-view.md

# Feb 25, 2026: Account Usage CORTEX_AGENT_USAGE_HISTORY view (*General availability*)

The [CORTEX_AGENT_USAGE_HISTORY](../../../sql-reference/account-usage/cortex_agent_usage_history.md)
view in the ACCOUNT_USAGE schema is now generally available. This view provides visibility into the usage history of Cortex Agents.

The information in the view includes the number of credits consumed each time a user interacts
with Cortex Agents. A request results in one or more calls to underlying tools (for example, Cortex Analyst and Cortex Search). Each row in the view represents a call to the agent and provides detail about
the aggregated tokens and credits in the call as well as granular detail. The view also includes
relevant metadata, such as the user ID, request ID, and the agent ID.

For more information, see [CORTEX_AGENT_USAGE_HISTORY view](../../../sql-reference/account-usage/cortex_agent_usage_history.md).
