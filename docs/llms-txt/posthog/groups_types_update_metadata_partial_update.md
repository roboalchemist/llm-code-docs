# Source: https://posthog.com/docs/open-api-spec/groups_types_update_metadata_partial_update.md

# groups_types_update_metadata_partial_update

## OpenAPI

```json PATCH /api/projects/{project_id}/groups_types/update_metadata/
{
  "paths": {
    "/api/projects/{project_id}/groups_types/update_metadata/": {
      "patch": {
        "operationId": "groups_types_update_metadata_partial_update",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedGroupType"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedGroupType"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedGroupType"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "No response body"
          }
        },
        "x-explicit-tags": []
      }
    }
  },
  "components": {
    "schemas": {
      "PatchedGroupType": {
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
        }
      }
    }
  }
}
```
