# Source: https://posthog.com/docs/open-api-spec/customer_profile_configs_partial_update.md

# customer_profile_configs_partial_update

## OpenAPI

```json PATCH /api/environments/{project_id}/customer_profile_configs/{id}/
{
  "paths": {
    "/api/environments/{project_id}/customer_profile_configs/{id}/": {
      "patch": {
        "operationId": "customer_profile_configs_partial_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this customer profile config.",
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
          "customer_profile_configs"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedCustomerProfileConfig"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedCustomerProfileConfig"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedCustomerProfileConfig"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "customer_profile_config:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CustomerProfileConfig"
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
      "PatchedCustomerProfileConfig": {
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
