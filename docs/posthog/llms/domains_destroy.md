# Source: https://posthog.com/docs/open-api-spec/domains_destroy.md

# domains_destroy

## OpenAPI

```json DELETE /api/organizations/{organization_id}/domains/{id}/
{
  "paths": {
    "/api/organizations/{organization_id}/domains/{id}/": {
      "delete": {
        "operationId": "domains_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this domain.",
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
          "domains"
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
