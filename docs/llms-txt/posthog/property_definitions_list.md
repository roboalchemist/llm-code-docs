# Source: https://posthog.com/docs/open-api-spec/property_definitions_list.md

# property_definitions_list

## OpenAPI

```json GET /api/projects/{project_id}/property_definitions/
{
  "paths": {
    "/api/projects/{project_id}/property_definitions/": {
      "get": {
        "operationId": "property_definitions_list",
        "parameters": [
          {
            "in": "query",
            "name": "event_names",
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "description": "If sent, response value will have `is_seen_on_filtered_events` populated. JSON-encoded"
          },
          {
            "in": "query",
            "name": "exclude_core_properties",
            "schema": {
              "type": "boolean",
              "default": false
            },
            "description": "Whether to exclude core properties"
          },
          {
            "in": "query",
            "name": "exclude_hidden",
            "schema": {
              "type": "boolean",
              "default": false
            },
            "description": "Whether to exclude properties marked as hidden"
          },
          {
            "in": "query",
            "name": "excluded_properties",
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "description": "JSON-encoded list of excluded properties"
          },
          {
            "in": "query",
            "name": "filter_by_event_names",
            "schema": {
              "type": "boolean",
              "nullable": true
            },
            "description": "Whether to return only properties for events in `event_names`"
          },
          {
            "in": "query",
            "name": "group_type_index",
            "schema": {
              "type": "integer"
            },
            "description": "What group type is the property for. Only should be set if `type=group`"
          },
          {
            "in": "query",
            "name": "is_feature_flag",
            "schema": {
              "type": "boolean",
              "nullable": true
            },
            "description": "Whether to return only (or excluding) feature flag properties"
          },
          {
            "in": "query",
            "name": "is_numerical",
            "schema": {
              "type": "boolean",
              "nullable": true
            },
            "description": "Whether to return only (or excluding) numerical property definitions"
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
          },
          {
            "in": "query",
            "name": "properties",
            "schema": {
              "type": "string",
              "minLength": 1
            },
            "description": "Comma-separated list of properties to filter"
          },
          {
            "in": "query",
            "name": "search",
            "schema": {
              "type": "string"
            },
            "description": "Searches properties by name"
          },
          {
            "in": "query",
            "name": "type",
            "schema": {
              "enum": [
                "event",
                "person",
                "group",
                "session"
              ],
              "type": "string",
              "default": "event",
              "minLength": 1
            },
            "description": "What property definitions to return\n\n* `event` - event\n* `person` - person\n* `group` - group\n* `session` - session"
          }
        ],
        "tags": [
          "core",
          "property_definitions"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "property_definition:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedEnterprisePropertyDefinitionList"
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
      "PaginatedEnterprisePropertyDefinitionList": {
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
              "$ref": "#/components/schemas/EnterprisePropertyDefinition"
            }
          }
        }
      },
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
