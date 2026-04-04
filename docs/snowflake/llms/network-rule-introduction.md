# Source: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/network-rule/network-rule-introduction.md

# Manage network rules

The Snowflake REST [Network Rule API](/developer-guide/snowflake-rest-api/reference/network-rule.md) provides the following endpoints to access, update, and perform certain actions on Network Rule resources.

Snowflake REST Network Rule API endpoints

| Endpoint | Description |
| --- | --- |
| `GET /api/v2/databases/database/`.`schemas/schema/network-rules` | Lists network rules. |
| `POST /api/v2/databases/database/`.`schemas/schema/network-rules` | Creates a network rule. |
| `GET /api/v2/databases/database/`.`schemas/schema/network-rules/name` | Fetches a network rule. |
| `DELETE /api/v2/databases/database/`.`schemas/schema/network-rules/name` | Deletes a network rule. |

For reference documentation, see [Snowflake Network Rule API reference](/developer-guide/snowflake-rest-api/reference/network-rule.md).
