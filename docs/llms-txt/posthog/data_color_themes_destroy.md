# Source: https://posthog.com/docs/open-api-spec/data_color_themes_destroy.md

# data_color_themes_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/data_color_themes/{id}/
{
  "paths": {
    "/api/projects/{project_id}/data_color_themes/{id}/": {
      "delete": {
        "operationId": "data_color_themes_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this data color theme.",
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
          "dashboards",
          "data_color_themes"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "project:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "dashboards"
        ]
      }
    }
  }
}
```
