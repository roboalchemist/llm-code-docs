# Source: https://posthog.com/docs/open-api-spec/surveys_stats_retrieve.md

# surveys_stats_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/surveys/stats/
{
  "paths": {
    "/api/projects/{project_id}/surveys/stats/": {
      "get": {
        "operationId": "surveys_stats_retrieve",
        "description": "Get aggregated response statistics across all surveys.\n\nArgs:\n    date_from: Optional ISO timestamp for start date (e.g. 2024-01-01T00:00:00Z)\n    date_to: Optional ISO timestamp for end date (e.g. 2024-01-31T23:59:59Z)\n\nReturns:\n    Aggregated statistics across all surveys including total counts and rates",
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
