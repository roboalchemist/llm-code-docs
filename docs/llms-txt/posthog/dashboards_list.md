# Source: https://posthog.com/docs/open-api-spec/dashboards_list.md

# dashboards_list

## OpenAPI

```json GET /api/projects/{project_id}/dashboards/
{
  "paths": {
    "/api/projects/{project_id}/dashboards/": {
      "get": {
        "operationId": "dashboards_list",
        "parameters": [
          {
            "in": "query",
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "json",
                "txt"
              ]
            }
          },
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
          "core",
          "dashboards"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "dashboard:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedDashboardBasicList"
                }
              },
              "text/event-stream": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedDashboardBasicList"
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
      "PaginatedDashboardBasicList": {
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
              "$ref": "#/components/schemas/DashboardBasic"
            }
          }
        }
      },
      "DashboardBasic": {
        "type": "object",
        "description": "Serializer mixin that handles tags for objects.",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "readOnly": true,
            "nullable": true,
            "description": "Name of the dashboard."
          },
          "description": {
            "type": "string",
            "readOnly": true,
            "description": "Description of the dashboard."
          },
          "pinned": {
            "type": "boolean",
            "readOnly": true,
            "description": "Whether the dashboard is pinned to the top of the list."
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "last_accessed_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "last_viewed_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "is_shared": {
            "type": "boolean",
            "readOnly": true
          },
          "deleted": {
            "type": "boolean",
            "readOnly": true
          },
          "creation_mode": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CreationModeEnum"
              }
            ],
            "readOnly": true
          },
          "tags": {
            "type": "array",
            "items": {}
          },
          "restriction_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/DashboardRestrictionLevel"
              }
            ],
            "readOnly": true,
            "description": "Controls who can edit the dashboard.\n\n* `21` - Everyone in the project can edit\n* `37` - Only those invited to this dashboard can edit"
          },
          "effective_restriction_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/EffectiveRestrictionLevelEnum"
              }
            ],
            "readOnly": true
          },
          "effective_privilege_level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/EffectivePrivilegeLevelEnum"
              }
            ],
            "readOnly": true
          },
          "user_access_level": {
            "type": "string",
            "nullable": true,
            "readOnly": true,
            "description": "The effective access level the user has for this object"
          },
          "access_control_version": {
            "type": "string",
            "readOnly": true
          },
          "last_refresh": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "team_id": {
            "type": "integer",
            "readOnly": true
          }
        },
        "required": [
          "access_control_version",
          "created_at",
          "created_by",
          "creation_mode",
          "deleted",
          "description",
          "effective_privilege_level",
          "effective_restriction_level",
          "id",
          "is_shared",
          "last_accessed_at",
          "last_refresh",
          "last_viewed_at",
          "name",
          "pinned",
          "restriction_level",
          "team_id",
          "user_access_level"
        ]
      },
      "UserBasic": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 200
          },
          "first_name": {
            "type": "string",
            "maxLength": 150
          },
          "last_name": {
            "type": "string",
            "maxLength": 150
          },
          "email": {
            "type": "string",
            "format": "email",
            "title": "Email address",
            "maxLength": 254
          },
          "is_email_verified": {
            "type": "boolean",
            "nullable": true
          },
          "hedgehog_config": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "role_at_organization": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/RoleAtOrganizationEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          }
        },
        "required": [
          "email",
          "hedgehog_config",
          "id",
          "uuid"
        ]
      },
      "CreationModeEnum": {
        "enum": [
          "default",
          "template",
          "duplicate",
          "unlisted"
        ],
        "type": "string",
        "description": "* `default` - Default\n* `template` - Template\n* `duplicate` - Duplicate\n* `unlisted` - Unlisted (product-embedded)"
      },
      "DashboardRestrictionLevel": {
        "enum": [
          21,
          37
        ],
        "type": "integer",
        "description": "* `21` - Everyone in the project can edit\n* `37` - Only those invited to this dashboard can edit"
      },
      "EffectiveRestrictionLevelEnum": {
        "enum": [
          21,
          37
        ],
        "type": "integer"
      },
      "EffectivePrivilegeLevelEnum": {
        "enum": [
          21,
          37
        ],
        "type": "integer"
      },
      "RoleAtOrganizationEnum": {
        "enum": [
          "engineering",
          "data",
          "product",
          "founder",
          "leadership",
          "marketing",
          "sales",
          "other"
        ],
        "type": "string",
        "description": "* `engineering` - Engineering\n* `data` - Data\n* `product` - Product Management\n* `founder` - Founder\n* `leadership` - Leadership\n* `marketing` - Marketing\n* `sales` - Sales / Success\n* `other` - Other"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      },
      "NullEnum": {
        "enum": [
          null
        ]
      }
    }
  }
}
```
