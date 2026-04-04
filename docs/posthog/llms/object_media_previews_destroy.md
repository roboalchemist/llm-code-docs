# Source: https://posthog.com/docs/open-api-spec/object_media_previews_destroy.md

# object_media_previews_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/object_media_previews/{id}/
{
  "paths": {
    "/api/projects/{project_id}/object_media_previews/{id}/": {
      "delete": {
        "operationId": "object_media_previews_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this object media preview.",
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
          "object_media_previews"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "event_definition:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
