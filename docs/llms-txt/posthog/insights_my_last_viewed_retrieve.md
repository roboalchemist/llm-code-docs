# Source: https://posthog.com/docs/open-api-spec/insights_my_last_viewed_retrieve.md

# insights_my_last_viewed_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/insights/my_last_viewed/
{
  "paths": {
    "/api/projects/{project_id}/insights/my_last_viewed/": {
      "get": {
        "operationId": "insights_my_last_viewed_retrieve",
        "description": "Returns basic details about the last 5 insights viewed by this user. Most recently viewed first.",
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
          "insights"
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
