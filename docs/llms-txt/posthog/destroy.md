# Source: https://posthog.com/docs/open-api-spec/destroy.md

# destroy

## OpenAPI

```json DELETE /api/organizations/{id}/
{
  "paths": {
    "/api/organizations/{id}/": {
      "delete": {
        "operationId": "destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this organization.",
            "required": true
          }
        ],
        "tags": [
          "organizations",
          "organizations"
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
