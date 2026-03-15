# Source: https://posthog.com/docs/open-api-spec/annotations_update.md

# annotations_update

## OpenAPI

```json PUT /api/projects/{project_id}/annotations/{id}/
{
  "paths": {
    "/api/projects/{project_id}/annotations/{id}/": {
      "put": {
        "operationId": "annotations_update",
        "description": "Create, Read, Update and Delete annotations. [See docs](https://posthog.com/docs/data/annotations) for more information on annotations.",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "integer"
            },
            "description": "A unique integer value identifying this annotation.",
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
          "annotations"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Annotation"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Annotation"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Annotation"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "annotation:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Annotation"
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
      "Annotation": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "content": {
            "type": "string",
            "nullable": true,
            "description": "Annotation text shown on charts to describe the change, release, or incident.",
            "maxLength": 8192
          },
          "date_marker": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "When this annotation happened (ISO 8601 timestamp). Used to position it on charts."
          },
          "creation_type": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CreationTypeEnum"
              }
            ],
            "description": "Who created this annotation. Use `USR` for user-created notes and `GIT` for bot/deployment notes.\n\n* `USR` - user\n* `GIT` - GitHub"
          },
          "dashboard_item": {
            "type": "integer",
            "nullable": true
          },
          "dashboard_id": {
            "type": "integer",
            "nullable": true
          },
          "dashboard_name": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "insight_short_id": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "insight_name": {
            "type": "string",
            "nullable": true,
            "readOnly": true
          },
          "insight_derived_name": {
            "type": "string",
            "nullable": true,
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
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "deleted": {
            "type": "boolean",
            "description": "Soft-delete flag. Set to true to hide the annotation, or false to restore it."
          },
          "scope": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AnnotationScopeEnum"
              }
            ],
            "description": "Annotation visibility scope: `project`, `organization`, `dashboard`, or `dashboard_item`. `recording` is deprecated and rejected.\n\n* `dashboard_item` - insight\n* `dashboard` - dashboard\n* `project` - project\n* `organization` - organization\n* `recording` - recording"
          }
        },
        "required": [
          "created_at",
          "created_by",
          "dashboard_name",
          "id",
          "insight_derived_name",
          "insight_name",
          "insight_short_id",
          "updated_at"
        ]
      },
      "CreationTypeEnum": {
        "enum": [
          "USR",
          "GIT"
        ],
        "type": "string",
        "description": "* `USR` - user\n* `GIT` - GitHub"
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
      "AnnotationScopeEnum": {
        "enum": [
          "dashboard_item",
          "dashboard",
          "project",
          "organization",
          "recording"
        ],
        "type": "string",
        "description": "* `dashboard_item` - insight\n* `dashboard` - dashboard\n* `project` - project\n* `organization` - organization\n* `recording` - recording"
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
