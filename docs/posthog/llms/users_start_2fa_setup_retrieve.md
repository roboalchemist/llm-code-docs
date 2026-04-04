# Source: https://posthog.com/docs/open-api-spec/users_start_2fa_setup_retrieve.md

# users_start_2fa_setup_retrieve

## OpenAPI

```json GET /api/users/{uuid}/start_2fa_setup/
{
  "paths": {
    "/api/users/{uuid}/start_2fa_setup/": {
      "get": {
        "operationId": "users_start_2fa_setup_retrieve",
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
