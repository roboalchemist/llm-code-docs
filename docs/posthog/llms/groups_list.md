# Source: https://posthog.com/docs/open-api-spec/groups_list.md

# groups_list

## OpenAPI

```json GET /api/projects/{project_id}/groups/
{
  "paths": {
    "/api/projects/{project_id}/groups/": {
      "get": {
        "operationId": "groups_list",
        "description": "List all groups of a specific group type. You must pass ?group_type_index= in the URL. To get a list of valid group types, call /api/:project_id/groups_types/",
        "parameters": [
          {
            "name": "cursor",
            "required": false,
            "in": "query",
            "description": "The pagination cursor value.",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "group_type_index",
            "schema": {
              "type": "integer"
            },
            "description": "Specify the group type to list",
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
            "name": "search",
            "schema": {
              "type": "string"
            },
            "description": "Search the group name",
            "required": true
          }
        ],
        "tags": [
          "core",
          "groups"
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
                  "$ref": "#/components/schemas/PaginatedGroupList"
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
      "PaginatedGroupList": {
        "type": "object",
        "required": [
          "results"
        ],
        "properties": {
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?cursor=cD00ODY%3D\""
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?cursor=cj0xJnA9NDg3"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Group"
            }
          }
        }
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
