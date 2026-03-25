# Source: https://posthog.com/docs/open-api-spec/mcp_server_installations_destroy.md

# mcp_server_installations_destroy

## OpenAPI

```json DELETE /api/environments/{project_id}/mcp_server_installations/{id}/
{
  "paths": {
    "/api/environments/{project_id}/mcp_server_installations/{id}/": {
      "delete": {
        "operationId": "mcp_server_installations_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this mcp server installation.",
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
          "mcp_store",
          "mcp_server_installations"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "project:read"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "mcp_store"
        ]
      }
    }
  }
}
```
