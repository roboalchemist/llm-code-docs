# Source: https://posthog.com/docs/open-api-spec/llm_analytics_provider_keys_destroy.md

# llm_analytics_provider_keys_destroy

## OpenAPI

```json DELETE /api/environments/{project_id}/llm_analytics/provider_keys/{id}/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/provider_keys/{id}/": {
      "delete": {
        "operationId": "llm_analytics_provider_keys_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this llm provider key.",
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
          "llm_analytics"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "llm_provider_key:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
