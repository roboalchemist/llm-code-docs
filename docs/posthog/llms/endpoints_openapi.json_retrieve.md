# Source: https://posthog.com/docs/open-api-spec/endpoints_openapi.json_retrieve.md

# endpoints_openapi.json_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/endpoints/{name}/openapi.json/
{
  "paths": {
    "/api/projects/{project_id}/endpoints/{name}/openapi.json/": {
      "get": {
        "operationId": "endpoints_openapi.json_retrieve",
        "description": "Get OpenAPI 3.0 specification for this endpoint. Use this to generate typed SDK clients.",
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
