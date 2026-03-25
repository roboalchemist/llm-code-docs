# Source: https://posthog.com/docs/open-api-spec/integrations_linkedin_ads_conversion_rules_retrieve.md

# integrations_linkedin_ads_conversion_rules_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/integrations/{id}/linkedin_ads_conversion_rules/
{
  "paths": {
    "/api/projects/{project_id}/integrations/{id}/linkedin_ads_conversion_rules/": {
      "get": {
        "operationId": "integrations_linkedin_ads_conversion_rules_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this integration.",
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
          "integrations"
        ],
        "responses": {
          "200": {
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
