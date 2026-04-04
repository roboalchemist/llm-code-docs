# Source: https://posthog.com/docs/open-api-spec/is_generating_demo_data_retrieve_2.md

# is_generating_demo_data_retrieve_2

## OpenAPI

```json GET /api/projects/{project_id}/environments/{id}/is_generating_demo_data/
{
  "paths": {
    "/api/projects/{project_id}/environments/{id}/is_generating_demo_data/": {
      "get": {
        "operationId": "is_generating_demo_data_retrieve_2",
        "description": "Deprecated: use /api/environments/{id}/ instead.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this environment (aka team).",
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
          "environments"
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
