# Source: https://posthog.com/docs/open-api-spec/integrations_authorize_retrieve.md

# integrations_authorize_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/integrations/authorize/
{
  "paths": {
    "/api/projects/{project_id}/integrations/authorize/": {
      "get": {
        "operationId": "integrations_authorize_retrieve",
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
