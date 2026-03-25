# Source: https://posthog.com/docs/open-api-spec/notebooks_kernel_dataframe_retrieve.md

# notebooks_kernel_dataframe_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/notebooks/{short_id}/kernel/dataframe/
{
  "paths": {
    "/api/projects/{project_id}/notebooks/{short_id}/kernel/dataframe/": {
      "get": {
        "operationId": "notebooks_kernel_dataframe_retrieve",
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
