# Source: https://posthog.com/docs/open-api-spec/groups_types_list.md

# groups_types_list

## OpenAPI

```json GET /api/projects/{project_id}/groups_types/
{
  "paths": {
    "/api/projects/{project_id}/groups_types/": {
      "get": {
        "operationId": "groups_types_list",
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
          "groups_types"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "group:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/GroupType"
                  }
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
      "GroupType": {
        "type": "object",
        "properties": {
          "group_type": {
            "type": "string",
            "readOnly": true
          },
          "group_type_index": {
            "type": "integer",
            "readOnly": true
          },
          "name_singular": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "name_plural": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "detail_dashboard": {
            "type": "integer",
            "nullable": true
          },
          "default_columns": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          }
        },
        "required": [
          "group_type",
          "group_type_index"
        ]
      }
    }
  }
}
```
