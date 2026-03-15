# Source: https://posthog.com/docs/open-api-spec/endpoints_retrieve_2.md

# endpoints_retrieve_2

## OpenAPI

```json GET /api/projects/{project_id}/endpoints/{name}/
{
  "paths": {
    "/api/projects/{project_id}/endpoints/{name}/": {
      "get": {
        "operationId": "endpoints_retrieve_2",
        "description": "Retrieve an endpoint, or a specific endpoint version.",
        "parameters": [
          {
            "in": "path",
            "name": "name",
            "schema": {
              "type": "string",
              "description": "URL-safe name for the endpoint"
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
          "endpoints",
          "endpoints"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "endpoint:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "endpoints"
        ]
      }
    }
  }
}
```
