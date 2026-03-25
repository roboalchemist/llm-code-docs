# Source: https://posthog.com/docs/open-api-spec/external_data_sources_destroy.md

# external_data_sources_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/external_data_sources/{id}/
{
  "paths": {
    "/api/projects/{project_id}/external_data_sources/{id}/": {
      "delete": {
        "operationId": "external_data_sources_destroy",
        "description": "Create, Read, Update and Delete External data Sources.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this external data source.",
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
        "x-explicit-tags": [
          "data_warehouse"
        ]
      }
    }
  }
}
```
