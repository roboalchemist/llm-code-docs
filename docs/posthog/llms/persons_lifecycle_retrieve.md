# Source: https://posthog.com/docs/open-api-spec/persons_lifecycle_retrieve.md

# persons_lifecycle_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/persons/lifecycle/
{
  "paths": {
    "/api/projects/{project_id}/persons/lifecycle/": {
      "get": {
        "operationId": "persons_lifecycle_retrieve",
        "description": "This endpoint is meant for reading and deleting persons. To create or update persons, we recommend using the [capture API](https://posthog.com/docs/api/capture), the `$set` and `$unset` [properties](https://posthog.com/docs/product-analytics/user-properties), or one of our SDKs.",
        "parameters": [
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
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
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
        "x-explicit-tags": [
          "persons"
        ]
      }
    }
  }
}
```
