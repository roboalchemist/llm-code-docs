# Source: https://posthog.com/docs/open-api-spec/feature_flags_matching_ids_retrieve.md

# feature_flags_matching_ids_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/feature_flags/matching_ids/
{
  "paths": {
    "/api/projects/{project_id}/feature_flags/matching_ids/": {
      "get": {
        "operationId": "feature_flags_matching_ids_retrieve",
        "description": "Get IDs of all feature flags matching the current filters.\nUses the same filtering logic as the list endpoint.\nReturns only IDs that the user has permission to edit.",
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
