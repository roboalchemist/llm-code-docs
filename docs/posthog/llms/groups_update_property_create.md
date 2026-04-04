# Source: https://posthog.com/docs/open-api-spec/groups_update_property_create.md

# groups_update_property_create

## OpenAPI

```json POST /api/projects/{project_id}/groups/update_property/
{
  "paths": {
    "/api/projects/{project_id}/groups/update_property/": {
      "post": {
        "operationId": "groups_update_property_create",
        "parameters": [
          {
            "in": "query",
            "name": "group_key",
            "schema": {
              "type": "string"
            },
            "description": "Specify the key of the group to find",
            "required": true
          },
          {
            "in": "query",
            "name": "group_type_index",
            "schema": {
              "type": "integer"
            },
            "description": "Specify the group type to find",
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
          "groups"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Group"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Group"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Group"
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
