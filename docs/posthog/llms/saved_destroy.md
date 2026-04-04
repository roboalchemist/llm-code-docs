# Source: https://posthog.com/docs/open-api-spec/saved_destroy.md

# saved_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/saved/{short_id}/
{
  "paths": {
    "/api/projects/{project_id}/saved/{short_id}/": {
      "delete": {
        "operationId": "saved_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
        "parameters": [
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
          },
          {
            "in": "path",
            "name": "short_id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "saved"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "heatmap:write"
            ]
          }
        ],
        "responses": {
          "405": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  }
}
```
