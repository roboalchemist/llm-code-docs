# Source: https://posthog.com/docs/open-api-spec/customer_profile_configs_list.md

# customer_profile_configs_list

## OpenAPI

```json GET /api/environments/{project_id}/customer_profile_configs/
{
  "paths": {
    "/api/environments/{project_id}/customer_profile_configs/": {
      "get": {
        "operationId": "customer_profile_configs_list",
        "parameters": [
          {
            "name": "limit",
            "required": false,
            "in": "query",
            "description": "Number of results to return per page.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "offset",
            "required": false,
            "in": "query",
            "description": "The initial index from which to return the results.",
            "schema": {
              "type": "integer"
            }
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
          "customer_profile_configs"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "customer_profile_config:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedCustomerProfileConfigList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "customer_analytics"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedCustomerProfileConfigList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=400&limit=100"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?offset=200&limit=100"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomerProfileConfig"
            }
          }
        }
      },
      "CustomerProfileConfig": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "scope": {
            "$ref": "#/components/schemas/CustomerProfileConfigScopeEnum"
          },
          "content": {
            "nullable": true
          },
          "sidebar": {
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "id",
          "scope",
          "updated_at"
        ]
      },
      "CustomerProfileConfigScopeEnum": {
        "enum": [
          "person",
          "group_0",
          "group_1",
          "group_2",
          "group_3",
          "group_4"
        ],
        "type": "string",
        "description": "* `person` - Person\n* `group_0` - Group 0\n* `group_1` - Group 1\n* `group_2` - Group 2\n* `group_3` - Group 3\n* `group_4` - Group 4"
      }
    }
  }
}
```
