# Source: https://posthog.com/docs/open-api-spec/members_destroy.md

# members_destroy

## OpenAPI

```json DELETE /api/organizations/{organization_id}/members/{user__uuid}/
{
  "paths": {
    "/api/organizations/{organization_id}/members/{user__uuid}/": {
      "delete": {
        "operationId": "members_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "organization_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          },
          {
            "in": "path",
            "name": "user__uuid",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "core",
          "members"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "organization_member:write"
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
