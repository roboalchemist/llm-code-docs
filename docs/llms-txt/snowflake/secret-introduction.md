# Source: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/secret/secret-introduction.md

# Manage secrets

The Snowflake REST [Secret API](/developer-guide/snowflake-rest-api/reference/secret.md) provides the following endpoints to manage Snowflake secrets:

Snowflake REST Secret API endpoints

| Endpoint | Description |
| --- | --- |
| `GET /api/v2/databases/database/schemas/`.`schema/secrets` | Lists secrets. |
| `POST /api/v2/databases/database/schemas/`.`schema/secrets` | Creates a secret. |
| `GET /api/v2/databases/database/schemas/`.`schema/secrets/name` | Fetches a secret. |
| `DELETE /api/v2/databases/database/schemas/`.`schema/secrets/name` | Deletes a secret. |

For reference documentation, see [Snowflake Secret API reference](/developer-guide/snowflake-rest-api/reference/secret.md).
