# Source: https://posthog.com/docs/open-api-spec/early_access_feature_destroy.md

# early_access_feature_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/early_access_feature/{id}/
{
  "paths": {
    "/api/projects/{project_id}/early_access_feature/{id}/": {
      "delete": {
        "operationId": "early_access_feature_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this early access feature.",
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
          "early_access_features",
          "early_access_feature"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "early_access_feature:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "early_access_features"
        ]
      }
    }
  }
}
```
