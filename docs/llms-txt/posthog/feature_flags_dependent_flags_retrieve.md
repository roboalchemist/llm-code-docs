# Source: https://posthog.com/docs/open-api-spec/feature_flags_dependent_flags_retrieve.md

# feature_flags_dependent_flags_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/feature_flags/{id}/dependent_flags/
{
  "paths": {
    "/api/projects/{project_id}/feature_flags/{id}/dependent_flags/": {
      "get": {
        "operationId": "feature_flags_dependent_flags_retrieve",
        "description": "Get other active flags that depend on this flag.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this feature flag.",
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
          "feature_flags",
          "feature_flags"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "feature_flag:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "feature_flags"
        ]
      }
    }
  }
}
```
