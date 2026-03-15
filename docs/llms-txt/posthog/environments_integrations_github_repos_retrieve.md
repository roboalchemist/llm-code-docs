# Source: https://posthog.com/docs/open-api-spec/environments_integrations_github_repos_retrieve.md

# environments_integrations_github_repos_retrieve

## OpenAPI

```json GET /api/environments/{environment_id}/integrations/{id}/github_repos/
{
  "paths": {
    "/api/environments/{environment_id}/integrations/{id}/github_repos/": {
      "get": {
        "operationId": "environments_integrations_github_repos_retrieve",
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
        "deprecated": true,
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
