# Source: https://posthog.com/docs/open-api-spec/destroy_2.md

# destroy_2

## OpenAPI

```json DELETE /api/organizations/{organization_id}/projects/{id}/
{
  "paths": {
    "/api/organizations/{organization_id}/projects/{id}/": {
      "delete": {
        "operationId": "destroy_2",
        "description": "Projects for the current organization.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer",
              "maximum": 9223372036854776000,
              "minimum": -9223372036854776000,
              "format": "int64"
            },
            "description": "A unique value identifying this project.",
            "required": true
          },
          {
            "in": "path",
            "name": "organization_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "core",
          "projects"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "project:write"
            ]
          }
        ],
        "responses": {
          "204": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  }
}
```
