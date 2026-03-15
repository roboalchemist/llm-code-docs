# Source: https://posthog.com/docs/open-api-spec/error_tracking_git_provider_file_links_resolve_gitlab_retrieve.md

# error_tracking_git_provider_file_links_resolve_gitlab_retrieve

## OpenAPI

```json GET /api/environments/{project_id}/error_tracking/git-provider-file-links/resolve_gitlab/
{
  "paths": {
    "/api/environments/{project_id}/error_tracking/git-provider-file-links/resolve_gitlab/": {
      "get": {
        "operationId": "error_tracking_git_provider_file_links_resolve_gitlab_retrieve",
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
          "error_tracking"
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
