# Source: https://posthog.com/docs/open-api-spec/evaluations_destroy.md

# evaluations_destroy

## OpenAPI

```json DELETE /api/environments/{project_id}/evaluations/{id}/
{
  "paths": {
    "/api/environments/{project_id}/evaluations/{id}/": {
      "delete": {
        "operationId": "evaluations_destroy",
        "description": "Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this evaluation.",
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
          "evaluations"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "evaluation:write"
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
