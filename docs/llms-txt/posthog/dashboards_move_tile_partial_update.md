# Source: https://posthog.com/docs/open-api-spec/dashboards_move_tile_partial_update.md

# dashboards_move_tile_partial_update

## OpenAPI

```json PATCH /api/projects/{project_id}/dashboards/{id}/move_tile/
{
  "paths": {
    "/api/projects/{project_id}/dashboards/{id}/move_tile/": {
      "patch": {
        "operationId": "dashboards_move_tile_partial_update",
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
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this dashboard.",
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
          "dashboards"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/PatchedDashboard"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/PatchedDashboard"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/PatchedDashboard"
              }
            }
          }
        },
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
      "PatchedDashboard": {
        "type": "object",
        "description": "Serializer mixin that handles tags for objects.",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "nullable": true,
            "maxLength": 400
          },
          "description": {
            "type": "string"
          },
          "pinned": {
            "type": "boolean"
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
            "type": "boolean"
          },
          "creation_mode": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CreationModeEnum"
              }
            ],
            "readOnly": true
          },
          "filters": {
            "type": "object",
            "additionalProperties": {},
            "readOnly": true
          },
          "variables": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "breakdown_colors": {
            "description": "Custom color mapping for breakdown values."
          },
          "data_color_theme_id": {
            "type": "integer",
            "nullable": true,
            "description": "ID of the color theme used for chart visualizations."
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
            "minimum": 0,
            "maximum": 32767
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
            "nullable": true
          },
          "persisted_filters": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "persisted_variables": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "team_id": {
            "type": "integer",
            "readOnly": true
          },
          "quick_filter_ids": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "nullable": true,
            "description": "List of quick filter IDs associated with this dashboard"
          },
          "tiles": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            },
            "nullable": true,
            "readOnly": true
          },
          "use_template": {
            "type": "string",
            "writeOnly": true,
            "description": "Template key to create the dashboard from a predefined template."
          },
          "use_dashboard": {
            "type": "integer",
            "writeOnly": true,
            "nullable": true,
            "description": "ID of an existing dashboard to duplicate."
          },
          "delete_insights": {
            "type": "boolean",
            "writeOnly": true,
            "default": false,
            "description": "When deleting, also delete insights that are only on this dashboard."
          },
          "_create_in_folder": {
            "type": "string",
            "writeOnly": true,
            "title": " create in folder"
          }
        }
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
