# Source: https://posthog.com/docs/open-api-spec/persons_cohorts_retrieve.md

# persons_cohorts_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/persons/cohorts/
{
  "paths": {
    "/api/projects/{project_id}/persons/cohorts/": {
      "get": {
        "operationId": "persons_cohorts_retrieve",
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
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "person:read",
              "cohort:read"
            ]
          }
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
