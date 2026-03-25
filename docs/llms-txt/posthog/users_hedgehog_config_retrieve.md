# Source: https://posthog.com/docs/open-api-spec/users_hedgehog_config_retrieve.md

# users_hedgehog_config_retrieve

## OpenAPI

```json GET /api/users/{uuid}/hedgehog_config/
{
  "paths": {
    "/api/users/{uuid}/hedgehog_config/": {
      "get": {
        "operationId": "users_hedgehog_config_retrieve",
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
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "user:read"
            ]
          }
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
