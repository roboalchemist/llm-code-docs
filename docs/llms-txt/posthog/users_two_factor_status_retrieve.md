# Source: https://posthog.com/docs/open-api-spec/users_two_factor_status_retrieve.md

# users_two_factor_status_retrieve

## OpenAPI

```json GET /api/users/{uuid}/two_factor_status/
{
  "paths": {
    "/api/users/{uuid}/two_factor_status/": {
      "get": {
        "operationId": "users_two_factor_status_retrieve",
        "description": "Get current 2FA status including backup codes if enabled",
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
          "200": {
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
