# Source: https://posthog.com/docs/open-api-spec/integrations_domain_connect_check_retrieve.md

# integrations_domain_connect_check_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/integrations/domain-connect/check/
{
  "paths": {
    "/api/projects/{project_id}/integrations/domain-connect/check/": {
      "get": {
        "operationId": "integrations_domain_connect_check_retrieve",
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
