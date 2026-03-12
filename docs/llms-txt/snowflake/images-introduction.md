# Source: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/image-repositories/images-introduction.md

# Manage image repositories

The Snowflake REST [Image Repository API reference](/developer-guide/snowflake-rest-api/reference/image-repository.md) provides the following Snowflake endpoints to access, update, and perform certain actions on Image Repository resource in Snowflake:

Snowflake REST Image Repositories API endpoints

| Endpoint | Description |
| --- | --- |
| `GET /api/v2/databases/database/schemas/`.`schema/image-repositories` | Lists available image repositories. |
| `POST /api/v2/databases/database/schemas/`.`schema/image-repositories` | Creates an image repository. |
| `GET /api/v2/databases/database/schemas/`.`schema/image-repositories/name` | Fetches an image repository. |
| `DELETE /api/v2/databases/database/schemas/`.`schema/image-repositories/name` | Deletes an image repository. |
| `GET /api/v2/databases/database/schemas/schema/image-repositories/name/images` | Lists images in the specified repository. |

For reference documentation, see [Snowflake Image Repository API reference](/developer-guide/snowflake-rest-api/reference/image-repository.md).
