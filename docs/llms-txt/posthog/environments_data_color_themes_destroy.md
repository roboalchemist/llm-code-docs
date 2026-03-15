# Source: https://posthog.com/docs/open-api-spec/environments_data_color_themes_destroy.md

# environments_data_color_themes_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/data_color_themes/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/data_color_themes/{id}/": {
      "delete": {
        "operationId": "environments_data_color_themes_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this data color theme.",
            "required": true
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
        "deprecated": true,
        "x-explicit-tags": [
          "dashboards"
        ]
      }
    }
  }
}
```
