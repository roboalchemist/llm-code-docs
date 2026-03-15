# Source: https://posthog.com/docs/open-api-spec/cohorts_remove_person_from_static_cohort_partial_update.md

# cohorts_remove_person_from_static_cohort_partial_update

## OpenAPI

```json PATCH /api/projects/{project_id}/cohorts/{id}/remove_person_from_static_cohort/
{
  "paths": {
    "/api/projects/{project_id}/cohorts/{id}/remove_person_from_static_cohort/": {
      "patch": {
        "operationId": "cohorts_remove_person_from_static_cohort_partial_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this cohort.",
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
          "cohorts"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedRemovePersonRequest"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedRemovePersonRequest"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedRemovePersonRequest"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "cohort:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "description": "No response body"
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
      "PatchedRemovePersonRequest": {
        "type": "object",
        "properties": {
          "person_id": {
            "type": "string",
            "format": "uuid",
            "description": "Person UUID to remove from the cohort"
          }
        }
      }
    }
  }
}
```
