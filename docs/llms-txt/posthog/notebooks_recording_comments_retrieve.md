# Source: https://posthog.com/docs/open-api-spec/notebooks_recording_comments_retrieve.md

# notebooks_recording_comments_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/notebooks/recording_comments/
{
  "paths": {
    "/api/projects/{project_id}/notebooks/recording_comments/": {
      "get": {
        "operationId": "notebooks_recording_comments_retrieve",
        "description": "The API for interacting with Notebooks. This feature is in early access and the API can have breaking changes without announcement.",
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
          "notebooks"
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "notebooks"
        ]
      }
    }
  }
}
```
