# Source: https://posthog.com/docs/open-api-spec/environments_hog_flows_destroy.md

# environments_hog_flows_destroy

## OpenAPI

```json DELETE /api/environments/{environment_id}/hog_flows/{id}/
{
  "paths": {
    "/api/environments/{environment_id}/hog_flows/{id}/": {
      "delete": {
        "operationId": "environments_hog_flows_destroy",
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
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this hog flow.",
            "required": true
          }
        ],
        "tags": [
          "workflows",
          "hog_flows"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "hog_flow:write"
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
          "workflows"
        ]
      }
    }
  }
}
```
