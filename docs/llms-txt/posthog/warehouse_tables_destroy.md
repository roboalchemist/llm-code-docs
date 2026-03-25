# Source: https://posthog.com/docs/open-api-spec/warehouse_tables_destroy.md

# warehouse_tables_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/warehouse_tables/{id}/
{
  "paths": {
    "/api/projects/{project_id}/warehouse_tables/{id}/": {
      "delete": {
        "operationId": "warehouse_tables_destroy",
        "description": "Create, Read, Update and Delete Warehouse Tables.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this data warehouse table.",
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
        "x-explicit-tags": []
      }
    }
  }
}
```
