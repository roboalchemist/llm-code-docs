# Source: https://posthog.com/docs/open-api-spec/web_vitals_retrieve.md

# web_vitals_retrieve

## OpenAPI

```json GET /api/environments/{project_id}/web_vitals/
{
  "paths": {
    "/api/environments/{project_id}/web_vitals/": {
      "get": {
        "operationId": "web_vitals_retrieve",
        "description": "Get web vitals for a specific pathname.\nToolbar accesses this via OAuth (handled by TeamAndOrgViewSetMixin.get_authenticators).",
        "parameters": [
          {
            "in": "query",
            "name": "pathname",
            "schema": {
              "type": "string"
            },
            "description": "Filter web vitals by pathname",
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
          "web_vitals"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "query:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
