# Source: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/view/view-introduction.md

# Manage views

The Snowflake REST [View API](/developer-guide/snowflake-rest-api/reference/view.md) provides the following endpoints to access, update, and perform certain actions on View resources.

Snowflake REST View API endpoints

| Endpoint | Description |
| --- | --- |
| `GET /api/v2/databases/database/schemas/`.`schema/views` | Lists available views. |
| `POST /api/v2/databases/database/schemas/`.`schema/views` | Creates a view. |
| `GET /api/v2/databases/database/schemas/`.`schema/views/name` | Fetches a view. |
| `DELETE /api/v2/databases/database/schemas/`.`schema/views/name` | Deletes a view. |

For reference documentation, see [Snowflake View API reference](/developer-guide/snowflake-rest-api/reference/view.md).
