# Source: https://posthog.com/docs/open-api-spec/warehouse_saved_queries_destroy.md

# warehouse_saved_queries_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/warehouse_saved_queries/{id}/
{
  "paths": {
    "/api/projects/{project_id}/warehouse_saved_queries/{id}/": {
      "delete": {
        "operationId": "warehouse_saved_queries_destroy",
        "description": "Create, Read, Update and Delete Warehouse Tables.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this data warehouse saved query.",
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
          "warehouse_saved_queries"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "warehouse_view:write"
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
