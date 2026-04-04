# Source: https://posthog.com/docs/open-api-spec/llm_analytics_models_retrieve.md

# llm_analytics_models_retrieve

## OpenAPI

```json GET /api/environments/{project_id}/llm_analytics/models/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/models/": {
      "get": {
        "operationId": "llm_analytics_models_retrieve",
        "description": "List available models for a provider.",
        "parameters": [
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
              "llm_provider_key:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "llm_analytics"
        ]
      }
    }
  }
}
```
