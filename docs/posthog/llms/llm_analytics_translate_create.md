# Source: https://posthog.com/docs/open-api-spec/llm_analytics_translate_create.md

# llm_analytics_translate_create

## OpenAPI

```json POST /api/environments/{project_id}/llm_analytics/translate/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/translate/": {
      "post": {
        "operationId": "llm_analytics_translate_create",
        "description": "Translate text to target language.",
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
              "llm_analytics:write"
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
