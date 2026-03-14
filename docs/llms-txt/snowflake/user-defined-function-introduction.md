# Source: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/user-defined-function/user-defined-function-introduction.md

# Manage user-defined functions

The Snowflake REST [User-Defined Function API](/developer-guide/snowflake-rest-api/reference/user-defined-function.md) provides the following endpoints to access, update, and perform certain actions on User-Defined Function resources.

Snowflake REST User-Defined Function API endpoints

| Endpoint | Description |
| --- | --- |
| `GET /api/v2/databases/database/schemas/`.`schema/user-defined-functions` | Lists available user-defined functions. |
| `POST /api/v2/databases/database/schemas/`.`schema/user-defined-functions` | Creates a user-defined function. |
| `GET /api/v2/databases/database/schemas/`.`schema/user-defined-functions/nameWithArgs` | Fetches a user-defined function. |
| `DELETE /api/v2/databases/database/schemas/`.`schema/user-defined-functions/nameWithArgs` | Deletes a user-defined function. |
| `POST /api/v2/databases/database/schemas/`.`schema/user-defined-functions/name:execute` | Executes a user-defined function. |
| `POST /api/v2/databases/database/schemas/`.`schema/user-defined-functions/`.`nameWithArgs:rename` | Renames a user-defined function. |

For reference documentation, see [Snowflake User-Defined Function API reference](/developer-guide/snowflake-rest-api/reference/user-defined-function.md).
