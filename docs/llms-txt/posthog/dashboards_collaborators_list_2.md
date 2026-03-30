# Source: https://posthog.com/docs/open-api-spec/dashboards_collaborators_list_2.md

# dashboards_collaborators_list_2

## OpenAPI

```json GET /api/projects/{project_id}/dashboards/{dashboard_id}/collaborators/
{
  "paths": {
    "/api/projects/{project_id}/dashboards/{dashboard_id}/collaborators/": {
      "get": {
        "operationId": "dashboards_collaborators_list_2",
        "parameters": [
          {
            "in": "path",
            "name": "dashboard_id",
            "schema": {
              "type": "integer"
            },
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
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/DashboardCollaborator"
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
      "DashboardCollaborator": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "dashboard_id": {
            "type": "integer",
            "readOnly": true
          },
          "user": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "level": {
            "allOf": [
              {
                "$ref": "#/components/schemas/DashboardRestrictionLevel"
              }
            ],
            "minimum": 0,
            "maximum": 32767
          },
          "added_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "user_uuid": {
            "type": "string",
            "format": "uuid",
            "writeOnly": true
          }
        },
        "required": [
          "added_at",
          "dashboard_id",
          "id",
          "level",
          "updated_at",
          "user",
          "user_uuid"
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
      "DashboardRestrictionLevel": {
        "enum": [
          21,
          37
        ],
        "type": "integer",
        "description": "* `21` - Everyone in the project can edit\n* `37` - Only those invited to this dashboard can edit"
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
