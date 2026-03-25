# Source: https://posthog.com/docs/open-api-spec/roles_role_memberships_destroy.md

# roles_role_memberships_destroy

## OpenAPI

```json DELETE /api/organizations/{organization_id}/roles/{role_id}/role_memberships/{id}/
{
  "paths": {
    "/api/organizations/{organization_id}/roles/{role_id}/role_memberships/{id}/": {
      "delete": {
        "operationId": "roles_role_memberships_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this role membership.",
            "required": true
          },
          {
            "in": "path",
            "name": "organization_id",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "in": "path",
            "name": "role_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "organizations",
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
          "organizations"
        ]
      }
    }
  }
}
```
