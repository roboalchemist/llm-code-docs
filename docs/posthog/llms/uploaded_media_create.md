# Source: https://posthog.com/docs/open-api-spec/uploaded_media_create.md

# uploaded_media_create

## OpenAPI

```json POST /api/projects/{project_id}/uploaded_media/
{
  "paths": {
    "/api/projects/{project_id}/uploaded_media/": {
      "post": {
        "operationId": "uploaded_media_create",
        "description": "\n    When object storage is available this API allows upload of media which can be used, for example, in text cards on dashboards.\n\n    Uploaded media must have a content type beginning with 'image/' and be less than 4MB.\n    ",
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
          "uploaded_media"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "uploaded_media:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
