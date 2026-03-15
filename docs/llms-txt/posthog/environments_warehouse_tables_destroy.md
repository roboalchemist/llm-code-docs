# Source: https://posthog.com/docs/open-api-spec/environments_warehouse_tables_destroy.md

# environments_warehouse_tables_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/warehouse_tables/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/warehouse_tables/{id}/": {
      "delete": {
        "operationId": "environments_warehouse_tables_destroy",
        "description": "Create, Read, Update and Delete Warehouse Tables.",
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
            "description": "A UUID string identifying this data warehouse table.",
            "required": true
          }
        ],
        "tags": [
          "warehouse_tables"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "warehouse_table:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": []
      }
    }
  }
}
```
