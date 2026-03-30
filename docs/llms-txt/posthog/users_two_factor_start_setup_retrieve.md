# Source: https://posthog.com/docs/open-api-spec/users_two_factor_start_setup_retrieve.md

# users_two_factor_start_setup_retrieve

## OpenAPI

```json GET /api/users/{uuid}/two_factor_start_setup/
{
  "paths": {
    "/api/users/{uuid}/two_factor_start_setup/": {
      "get": {
        "operationId": "users_two_factor_start_setup_retrieve",
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
