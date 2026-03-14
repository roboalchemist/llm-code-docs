# Source: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/stream/stream-introduction.md

# Manage streams

The Snowflake REST [Stream API](/developer-guide/snowflake-rest-api/reference/stream.md) provides the following endpoints to access, update, and perform certain actions on Stream resources.

Snowflake REST Stream API endpoints

| Endpoint | Description |
| --- | --- |
| `GET /api/v2/databases/database/schemas/`.`schema/streams` | Lists available streams. |
| `POST /api/v2/databases/database/schemas/`.`schema/streams` | Creates a stream. |
| `GET /api/v2/databases/database/schemas/`.`schema/streams/name` | Fetches a stream. |
| `DELETE /api/v2/databases/database/schemas/`.`schema/streams/name` | Deletes a stream. |
| `POST /api/v2/databases/database/schemas/`.`schema/streams/name:clone` | Clones a stream. |

For reference documentation, see [Snowflake Stream API reference](/developer-guide/snowflake-rest-api/reference/stream.md).
