# Source: https://posthog.com/docs/open-api-spec/insight_variables_destroy.md

# insight_variables_destroy

## OpenAPI

```json DELETE /api/projects/{project_id}/insight_variables/{id}/
{
  "paths": {
    "/api/projects/{project_id}/insight_variables/{id}/": {
      "delete": {
        "operationId": "insight_variables_destroy",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this insight variable.",
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
          "insight_variables"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "insight_variable:write"
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
