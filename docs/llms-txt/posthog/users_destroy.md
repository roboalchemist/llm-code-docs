# Source: https://posthog.com/docs/open-api-spec/users_destroy.md

# users_destroy

## OpenAPI

```json DELETE /api/users/{uuid}/
{
  "paths": {
    "/api/users/{uuid}/": {
      "delete": {
        "operationId": "users_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "uuid",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "core",
          "users"
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
