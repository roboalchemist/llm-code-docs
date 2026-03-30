# Source: https://posthog.com/docs/open-api-spec/product_tours_draft_status_retrieve.md

# product_tours_draft_status_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/product_tours/{id}/draft_status/
{
  "paths": {
    "/api/projects/{project_id}/product_tours/{id}/draft_status/": {
      "get": {
        "operationId": "product_tours_draft_status_retrieve",
        "description": "Lightweight polling endpoint for draft change detection.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this product tour.",
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
          "product_tours"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "product_tour:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DraftStatusResponse"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "DraftStatusResponse": {
        "type": "object",
        "properties": {
          "updated_at": {
            "type": "string",
            "format": "date-time"
          },
          "has_draft": {
            "type": "boolean"
          }
        },
        "required": [
          "has_draft",
          "updated_at"
        ]
      }
    }
  }
}
```
