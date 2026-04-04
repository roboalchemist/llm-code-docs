# Source: https://posthog.com/docs/open-api-spec/query_destroy.md

# query_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/query/{id}/
{
  "paths": {
    "/api/projects/{project_id}/query/{id}/": {
      "delete": {
        "operationId": "query_destroy",
        "description": "(Experimental)",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string"
            },
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
          "query"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "query:read"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "Query cancelled"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
