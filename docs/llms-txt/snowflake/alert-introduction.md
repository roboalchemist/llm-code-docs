# Source: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/alert/alert-introduction.md

# Manage alerts

The Snowflake REST [Alert API](/developer-guide/snowflake-rest-api/reference/alert.md) provides the following endpoints to access, update, and perform certain actions on Alert resources.

Snowflake REST Alert API endpoints

| Endpoint | Description |
| --- | --- |
| `GET /api/v2/databases/database/schemas/`.`schema/alerts` | Lists alerts. |
| `POST /api/v2/databases/database/schemas/`.`schema/alerts` | Creates an alert. |
| `GET /api/v2/databases/database/schemas/`.`schema/alerts/name` | Fetches an alert. |
| `DELETE /api/v2/databases/database/schemas/`.`schema/alerts/name` | Deletes an alert. |
| `POST /api/v2/databases/database/schemas/`.`schema/alerts/name:clone` | Creates a new alert by cloning from the specified resource. |
| `POST /api/v2/databases/database/schemas/`.`schema/alerts/name:execute` | Executes an alert. |

For reference documentation, see [Snowflake Alert API reference](/developer-guide/snowflake-rest-api/reference/alert.md).
