# Source: https://posthog.com/docs/open-api-spec/groups_create.md

# groups_create

## OpenAPI

```json POST /api/projects/{project_id}/groups/
{
  "paths": {
    "/api/projects/{project_id}/groups/": {
      "post": {
        "operationId": "groups_create",
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
          "core",
          "groups"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateGroup"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/CreateGroup"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/CreateGroup"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "group:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Group"
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
      "CreateGroup": {
        "type": "object",
        "properties": {
          "group_type_index": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648
          },
          "group_key": {
            "type": "string",
            "maxLength": 400
          },
          "group_properties": {
            "nullable": true
          }
        },
        "required": [
          "group_key",
          "group_type_index"
        ]
      },
      "Group": {
        "type": "object",
        "properties": {
          "group_type_index": {
            "type": "integer",
            "maximum": 2147483647,
            "minimum": -2147483648
          },
          "group_key": {
            "type": "string",
            "maxLength": 400
          },
          "group_properties": {},
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          }
        },
        "required": [
          "created_at",
          "group_key",
          "group_type_index"
        ]
      }
    }
  }
}
```
