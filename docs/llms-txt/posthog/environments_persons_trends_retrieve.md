# Source: https://posthog.com/docs/open-api-spec/environments_persons_trends_retrieve.md

# environments_persons_trends_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/persons/trends/
{
  "paths": {
    "/api/environments/{environment_id}/persons/trends/": {
      "get": {
        "operationId": "environments_persons_trends_retrieve",
        "description": "This endpoint is meant for reading and deleting persons. To create or update persons, we recommend using the [capture API](https://posthog.com/docs/api/capture), the `$set` and `$unset` [properties](https://posthog.com/docs/product-analytics/user-properties), or one of our SDKs.",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "query",
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "csv",
                "json"
              ]
            }
          }
        ],
        "tags": [
          "persons",
          "persons"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "persons"
        ]
      }
    }
  }
}
```
