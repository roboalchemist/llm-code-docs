# Source: https://posthog.com/docs/open-api-spec/invites_destroy.md

# invites_destroy

## OpenAPI

```json DELETE /api/organizations/{organization_id}/invites/{id}/
{
  "paths": {
    "/api/organizations/{organization_id}/invites/{id}/": {
      "delete": {
        "operationId": "invites_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this organization invite.",
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
          "invites"
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
