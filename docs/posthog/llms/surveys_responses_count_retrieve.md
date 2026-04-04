# Source: https://posthog.com/docs/open-api-spec/surveys_responses_count_retrieve.md

# surveys_responses_count_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/surveys/responses_count/
{
  "paths": {
    "/api/projects/{project_id}/surveys/responses_count/": {
      "get": {
        "operationId": "surveys_responses_count_retrieve",
        "description": "Get response counts for all surveys.\n\nArgs:\n    exclude_archived: Optional boolean to exclude archived responses (default: false, includes archived)\n    survey_ids: Optional comma-separated list of survey IDs to filter by\n\nReturns:\n    Dictionary mapping survey IDs to response counts",
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
          "surveys",
          "surveys"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "survey:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "surveys"
        ]
      }
    }
  }
}
```
