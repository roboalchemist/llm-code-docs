# Source: https://posthog.com/docs/open-api-spec/integrations_github_repos_retrieve.md

# integrations_github_repos_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/integrations/{id}/github_repos/
{
  "paths": {
    "/api/projects/{project_id}/integrations/{id}/github_repos/": {
      "get": {
        "operationId": "integrations_github_repos_retrieve",
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
                  "$ref": "#/components/schemas/GitHubReposResponse"
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
      "GitHubReposResponse": {
        "type": "object",
        "properties": {
          "repositories": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/GitHubRepo"
            }
          }
        },
        "required": [
          "repositories"
        ]
      },
      "GitHubRepo": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "full_name": {
            "type": "string"
          }
        },
        "required": [
          "full_name",
          "id",
          "name"
        ]
      }
    }
  }
}
```
