# Source: https://posthog.com/docs/open-api-spec/feature_flags_remote_config_retrieve.md

# feature_flags_remote_config_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/feature_flags/{id}/remote_config/
{
  "paths": {
    "/api/projects/{project_id}/feature_flags/{id}/remote_config/": {
      "get": {
        "operationId": "feature_flags_remote_config_retrieve",
        "description": "Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/feature-flags) for more information on feature flags.\n\nIf you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.",
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
