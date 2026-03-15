# Source: https://posthog.com/docs/open-api-spec/llm_analytics_evaluation_config_set_active_key_create.md

# llm_analytics_evaluation_config_set_active_key_create

## OpenAPI

```json POST /api/environments/{project_id}/llm_analytics/evaluation_config/set_active_key/
{
  "paths": {
    "/api/environments/{project_id}/llm_analytics/evaluation_config/set_active_key/": {
      "post": {
        "operationId": "llm_analytics_evaluation_config_set_active_key_create",
        "description": "Set the active provider key for evaluations",
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
