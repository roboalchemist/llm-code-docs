# Source: https://posthog.com/docs/open-api-spec/dashboard_templates_json_schema_retrieve.md

# dashboard_templates_json_schema_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/dashboard_templates/json_schema/
{
  "paths": {
    "/api/projects/{project_id}/dashboard_templates/json_schema/": {
      "get": {
        "operationId": "dashboard_templates_json_schema_retrieve",
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
          "core",
          "dashboard_templates"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
