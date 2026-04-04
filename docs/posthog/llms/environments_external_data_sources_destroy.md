# Source: https://posthog.com/docs/open-api-spec/environments_external_data_sources_destroy.md

# environments_external_data_sources_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/external_data_sources/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/external_data_sources/{id}/": {
      "delete": {
        "operationId": "environments_external_data_sources_destroy",
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
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this external data source.",
            "required": true
          }
        ],
        "tags": [
          "data_warehouse",
          "external_data_sources"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "external_data_source:write"
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
          "data_warehouse"
        ]
      }
    }
  }
}
```
