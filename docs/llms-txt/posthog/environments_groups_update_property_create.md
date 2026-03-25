# Source: https://posthog.com/docs/open-api-spec/environments_groups_update_property_create.md

# environments_groups_update_property_create

## OpenAPI

```json POST /api/environments/{environment_id}/groups/update_property/
{
  "paths": {
    "/api/environments/{environment_id}/groups/update_property/": {
      "post": {
        "operationId": "environments_groups_update_property_create",
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
        "deprecated": true,
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
