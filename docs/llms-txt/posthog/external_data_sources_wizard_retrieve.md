# Source: https://posthog.com/docs/open-api-spec/external_data_sources_wizard_retrieve.md

# external_data_sources_wizard_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/external_data_sources/wizard/
{
  "paths": {
    "/api/projects/{project_id}/external_data_sources/wizard/": {
      "get": {
        "operationId": "external_data_sources_wizard_retrieve",
        "description": "Create, Read, Update and Delete External data Sources.",
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
          "data_warehouse",
          "external_data_sources"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "data_warehouse"
        ]
      }
    }
  }
}
```
