# Source: https://posthog.com/docs/open-api-spec/roles_destroy.md

# roles_destroy

## OpenAPI

```json DELETE /api/organizations/{organization_id}/roles/{id}/
{
  "paths": {
    "/api/organizations/{organization_id}/roles/{id}/": {
      "delete": {
        "operationId": "roles_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this role.",
            "required": true
          },
          {
            "in": "path",
            "name": "organization_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "core",
          "roles"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "organization:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
