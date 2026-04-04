# Source: https://posthog.com/docs/open-api-spec/error_tracking_releases_hash_retrieve.md

# error_tracking_releases_hash_retrieve

## OpenAPI

```json GET /api/environments/{project_id}/error_tracking/releases/hash/{hash_id}/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/releases/hash/{hash_id}/": {
      "get": {
        "operationId": "error_tracking_releases_hash_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "hash_id",
            "schema": {
              "type": "string"
            },
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
          "error_tracking",
          "error_tracking"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "error_tracking:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "error_tracking"
        ]
      }
    }
  }
}
```
