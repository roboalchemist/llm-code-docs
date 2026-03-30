# Source: https://posthog.com/docs/open-api-spec/environments_persons_properties_timeline_retrieve.md

# environments_persons_properties_timeline_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/persons/{id}/properties_timeline/
{
  "paths": {
    "/api/environments/{environment_id}/persons/{id}/properties_timeline/": {
      "get": {
        "operationId": "environments_persons_properties_timeline_retrieve",
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
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this person.",
            "required": true
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
