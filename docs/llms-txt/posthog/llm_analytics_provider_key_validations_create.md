# Source: https://posthog.com/docs/open-api-spec/llm_analytics_provider_key_validations_create.md

# llm_analytics_provider_key_validations_create

## OpenAPI

```json POST /api/environments/{project_id}/llm_analytics/provider_key_validations/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/provider_key_validations/": {
      "post": {
        "operationId": "llm_analytics_provider_key_validations_create",
        "description": "Validate LLM provider API keys without persisting them",
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
              "llm_provider_key:write"
            ]
          }
        ],
        "responses": {
          "201": {
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
