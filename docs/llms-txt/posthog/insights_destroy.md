# Source: https://posthog.com/docs/open-api-spec/insights_destroy.md

# insights_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/insights/{id}/
{
  "paths": {
    "/api/projects/{project_id}/insights/{id}/": {
      "delete": {
        "operationId": "insights_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
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
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this insight.",
            "required": true
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
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "insight:write"
            ]
          }
        ],
        "responses": {
          "405": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
