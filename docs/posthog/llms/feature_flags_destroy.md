# Source: https://posthog.com/docs/open-api-spec/feature_flags_destroy.md

# feature_flags_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/feature_flags/{id}/
{
  "paths": {
    "/api/projects/{project_id}/feature_flags/{id}/": {
      "delete": {
        "operationId": "feature_flags_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
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
              "feature_flag:write"
            ]
          }
        ],
        "responses": {
          "405": {
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
