# Source: https://posthog.com/docs/open-api-spec/environments_endpoints_destroy.md

# environments_endpoints_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/endpoints/{name}/
{
  "paths": {
    "/api/environments/{environment_id}/endpoints/{name}/": {
      "delete": {
        "operationId": "environments_endpoints_destroy",
        "description": "Delete an endpoint and clean up materialized query.",
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
            "name": "name",
            "schema": {
              "type": "string",
              "description": "URL-safe name for the endpoint"
            },
            "required": true
          }
        ],
        "tags": [
          "endpoints",
          "endpoints"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "endpoint:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "endpoints"
        ]
      }
    }
  }
}
```
