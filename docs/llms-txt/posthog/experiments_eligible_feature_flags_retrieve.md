# Source: https://posthog.com/docs/open-api-spec/experiments_eligible_feature_flags_retrieve.md

# experiments_eligible_feature_flags_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/experiments/eligible_feature_flags/
{
  "paths": {
    "/api/projects/{project_id}/experiments/eligible_feature_flags/": {
      "get": {
        "operationId": "experiments_eligible_feature_flags_retrieve",
        "description": "Returns a paginated list of feature flags eligible for use in experiments.\n\nEligible flags must:\n- Be multivariate with at least 2 variants\n- Have \"control\" as the first variant key\n\nQuery parameters:\n- search: Filter by flag key or name (case insensitive)\n- limit: Number of results per page (default: 20)\n- offset: Pagination offset (default: 0)\n- active: Filter by active status (\"true\" or \"false\")\n- created_by_id: Filter by creator user ID\n- order: Sort order field\n- evaluation_runtime: Filter by evaluation runtime\n- has_evaluation_tags: Filter by presence of evaluation tags (\"true\" or \"false\")",
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
          "experiments",
          "experiments"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "feature_flag:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": [
          "experiments"
        ]
      }
    }
  }
}
```
