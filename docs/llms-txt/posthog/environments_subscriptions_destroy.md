# Source: https://posthog.com/docs/open-api-spec/environments_subscriptions_destroy.md

# environments_subscriptions_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/subscriptions/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/subscriptions/{id}/": {
      "delete": {
        "operationId": "environments_subscriptions_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this subscription.",
            "required": true
          }
        ],
        "tags": [
          "core",
          "subscriptions"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "subscription:write"
            ]
          }
        ],
        "responses": {
          "405": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
