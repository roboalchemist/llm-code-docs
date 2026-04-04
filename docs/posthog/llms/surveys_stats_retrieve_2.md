# Source: https://posthog.com/docs/open-api-spec/surveys_stats_retrieve_2.md

# surveys_stats_retrieve_2

## OpenAPI

```json GET /api/projects/{project_id}/surveys/{id}/stats/
{
  "paths": {
    "/api/projects/{project_id}/surveys/{id}/stats/": {
      "get": {
        "operationId": "surveys_stats_retrieve_2",
        "description": "Get survey response statistics for a specific survey.\n\nArgs:\n    date_from: Optional ISO timestamp for start date (e.g. 2024-01-01T00:00:00Z)\n    date_to: Optional ISO timestamp for end date (e.g. 2024-01-31T23:59:59Z)\n    exclude_archived: Optional boolean to exclude archived responses (default: false, includes archived)\n\nReturns:\n    Survey statistics including event counts, unique respondents, and conversion rates",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this survey.",
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
