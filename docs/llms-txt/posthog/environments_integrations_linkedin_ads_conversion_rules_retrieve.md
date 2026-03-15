# Source: https://posthog.com/docs/open-api-spec/environments_integrations_linkedin_ads_conversion_rules_retrieve.md

# environments_integrations_linkedin_ads_conversion_rules_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/integrations/{id}/linkedin_ads_conversion_rules/
{
  "paths": {
    "/api/environments/{environment_id}/integrations/{id}/linkedin_ads_conversion_rules/": {
      "get": {
        "operationId": "environments_integrations_linkedin_ads_conversion_rules_retrieve",
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
            "description": "A unique integer value identifying this integration.",
            "required": true
          }
        ],
        "tags": [
          "core",
          "integrations"
        ],
        "responses": {
          "200": {
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
