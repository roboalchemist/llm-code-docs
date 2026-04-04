# Source: https://posthog.com/docs/open-api-spec/environments_external_data_sources_wizard_retrieve.md

# environments_external_data_sources_wizard_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/external_data_sources/wizard/
{
  "paths": {
    "/api/environments/{environment_id}/external_data_sources/wizard/": {
      "get": {
        "operationId": "environments_external_data_sources_wizard_retrieve",
        "description": "Create, Read, Update and Delete External data Sources.",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          }
        ],
        "tags": [
          "data_warehouse",
          "external_data_sources"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "data_warehouse"
        ]
      }
    }
  }
}
```
