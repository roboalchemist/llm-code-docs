# Source: https://posthog.com/docs/open-api-spec/integrations_github_branches_retrieve.md

# integrations_github_branches_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/integrations/{id}/github_branches/
{
  "paths": {
    "/api/projects/{project_id}/integrations/{id}/github_branches/": {
      "get": {
        "operationId": "integrations_github_branches_retrieve",
        "parameters": [
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
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
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
