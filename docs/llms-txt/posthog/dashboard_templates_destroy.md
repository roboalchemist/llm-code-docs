# Source: https://posthog.com/docs/open-api-spec/dashboard_templates_destroy.md

# dashboard_templates_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/dashboard_templates/{id}/
{
  "paths": {
    "/api/projects/{project_id}/dashboard_templates/{id}/": {
      "delete": {
        "operationId": "dashboard_templates_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this dashboard template.",
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
          "core",
          "dashboard_templates"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "dashboard_template:write"
            ]
          }
        ],
        "responses": {
          "405": {
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
