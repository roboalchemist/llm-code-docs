# Source: https://posthog.com/docs/open-api-spec/max_tools_create_and_query_insight_create.md

# max_tools_create_and_query_insight_create

## OpenAPI

```json POST /api/environments/{project_id}/max_tools/create_and_query_insight/
{
  "paths": {
    "/api/environments/{project_id}/max_tools/create_and_query_insight/": {
      "post": {
        "operationId": "max_tools_create_and_query_insight_create",
        "parameters": [
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
          "max_tools"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "insight:read",
              "query:read"
            ]
          },
          {
            "PersonalAPIKeyAuth": [
              "insight:read",
              "query:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
