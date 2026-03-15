# Source: https://posthog.com/docs/open-api-spec/environments_integrations_github_branches_retrieve.md

# environments_integrations_github_branches_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/integrations/{id}/github_branches/
{
  "paths": {
    "/api/environments/{environment_id}/integrations/{id}/github_branches/": {
      "get": {
        "operationId": "environments_integrations_github_branches_retrieve",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this integration.",
            "required": true
          },
          {
            "in": "query",
            "name": "repo",
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "description": "Repository in owner/repo format",
            "required": true
          }
        ],
        "tags": [
          "core",
          "integrations"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "integration:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GitHubBranchesResponse"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "core"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "GitHubBranchesResponse": {
        "type": "object",
        "properties": {
          "branches": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "List of branch names"
          }
        },
        "required": [
          "branches"
        ]
      }
    }
  }
}
```
