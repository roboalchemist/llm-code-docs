# Source: https://posthog.com/docs/open-api-spec/property_definitions_update.md

# property_definitions_update

## OpenAPI

```json PUT /api/projects/{project_id}/property_definitions/{id}/
{
  "paths": {
    "/api/projects/{project_id}/property_definitions/{id}/": {
      "put": {
        "operationId": "property_definitions_update",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this property definition.",
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
          "property_definitions"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/EnterprisePropertyDefinition"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/EnterprisePropertyDefinition"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/EnterprisePropertyDefinition"
              }
            }
          }
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "property_definition:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EnterprisePropertyDefinition"
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
      "EnterprisePropertyDefinition": {
        "type": "object",
        "description": "Serializer mixin that handles tags for objects.",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "name": {
            "type": "string",
            "readOnly": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "tags": {
            "type": "array",
            "items": {}
          },
          "is_numerical": {
            "type": "boolean",
            "readOnly": true
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "updated_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "is_seen_on_filtered_events": {
            "type": "boolean",
            "readOnly": true,
            "nullable": true
          },
          "property_type": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/EnterprisePropertyDefinitionPropertyTypeEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "verified": {
            "type": "boolean"
          },
          "verified_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "verified_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "hidden": {
            "type": "boolean",
            "nullable": true
          }
        },
        "required": [
          "id",
          "is_numerical",
          "is_seen_on_filtered_events",
          "name",
          "updated_at",
          "updated_by",
          "verified_at",
          "verified_by"
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
      "EnterprisePropertyDefinitionPropertyTypeEnum": {
        "enum": [
          "DateTime",
          "String",
          "Numeric",
          "Boolean",
          "Duration"
        ],
        "type": "string",
        "description": "* `DateTime` - DateTime\n* `String` - String\n* `Numeric` - Numeric\n* `Boolean` - Boolean\n* `Duration` - Duration"
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
      }
    }
  }
}
```
