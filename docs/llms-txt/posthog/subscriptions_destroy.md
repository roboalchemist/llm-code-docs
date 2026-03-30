# Source: https://posthog.com/docs/open-api-spec/subscriptions_destroy.md

# subscriptions_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/subscriptions/{id}/
{
  "paths": {
    "/api/projects/{project_id}/subscriptions/{id}/": {
      "delete": {
        "operationId": "subscriptions_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this subscription.",
            "required": true
          },
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
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
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
