# Source: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/artifact-repository/artifact-repository-introduction.md

# Manage artifact repositories

The Snowflake REST [Artifact Repository API](/developer-guide/snowflake-rest-api/reference/artifact-repository.md) provides the following endpoints to access, update, and perform certain actions on Artifact Repository resources.

Snowflake REST Artifact Repository API endpoints

| Endpoint | Description |
| --- | --- |
| `GET /api/v2/databases/database/schemas/`.`schema/artifact-repositories` | Lists available artifact repositories. |
| `POST /api/v2/databases/database/schemas/`.`schema/artifact-repositories` | Creates an artifact repository. |
| `GET /api/v2/databases/database/schemas/`.`schema/artifact-repositories/name` | Fetches an artifact repository. |
| `DELETE /api/v2/databases/database/schemas/`.`schema/artifact-repositories/name` | Deletes an artifact repository. |
| `PUT /api/v2/databases/database/schemas/`.`schema/artifact-repositories/name` | Creates or updates an artifact repository. |
| `POST /api/v2/databases/database/schemas/`.`schema/artifact-repositories/name:rename` | Renames an artifact repository. |

For reference documentation, see [Snowflake Artifact Repository API reference](/developer-guide/snowflake-rest-api/reference/artifact-repository.md).
