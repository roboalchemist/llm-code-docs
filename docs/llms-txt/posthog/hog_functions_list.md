# Source: https://posthog.com/docs/open-api-spec/hog_functions_list.md

# hog_functions_list

## OpenAPI

```json GET /api/projects/{project_id}/hog_functions/
{
  "paths": {
    "/api/projects/{project_id}/hog_functions/": {
      "get": {
        "operationId": "hog_functions_list",
        "parameters": [
          {
            "in": "query",
            "name": "created_at",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "in": "query",
            "name": "created_by",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "query",
            "name": "enabled",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "in": "query",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
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
          },
          {
            "name": "search",
            "required": false,
            "in": "query",
            "description": "A search term.",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "type",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "description": "Multiple values may be separated by commas.",
            "explode": false,
            "style": "form"
          },
          {
            "in": "query",
            "name": "updated_at",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          }
        ],
        "tags": [
          "hog_functions",
          "hog_functions"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "hog_function:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedHogFunctionMinimalList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "hog_functions"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedHogFunctionMinimalList": {
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
              "$ref": "#/components/schemas/HogFunctionMinimal"
            }
          }
        }
      },
      "HogFunctionMinimal": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "type": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "name": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "description": {
            "type": "string",
            "readOnly": true
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
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "enabled": {
            "type": "boolean",
            "readOnly": true
          },
          "hog": {
            "type": "string",
            "readOnly": true
          },
          "filters": {
            "readOnly": true,
            "nullable": true
          },
          "icon_url": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "template": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HogFunctionTemplate"
              }
            ],
            "readOnly": true
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HogFunctionStatus"
              }
            ],
            "readOnly": true,
            "nullable": true
          },
          "execution_order": {
            "type": "integer",
            "readOnly": true,
            "nullable": true
          }
        },
        "required": [
          "created_at",
          "created_by",
          "description",
          "enabled",
          "execution_order",
          "filters",
          "hog",
          "icon_url",
          "id",
          "name",
          "status",
          "template",
          "type",
          "updated_at"
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
      "HogFunctionTemplate": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique template identifier (e.g. 'template-slack')."
          },
          "name": {
            "type": "string",
            "description": "Display name of the template.",
            "maxLength": 400
          },
          "description": {
            "type": "string",
            "nullable": true,
            "description": "What this template does."
          },
          "code": {
            "type": "string",
            "description": "Source code of the template."
          },
          "code_language": {
            "type": "string",
            "description": "Programming language: 'hog' or 'javascript'.",
            "maxLength": 20
          },
          "inputs_schema": {
            "description": "Schema defining configurable inputs for functions created from this template."
          },
          "type": {
            "type": "string",
            "description": "Function type this template creates.",
            "maxLength": 50
          },
          "status": {
            "type": "string",
            "description": "Lifecycle status: alpha, beta, stable, deprecated, or hidden.",
            "maxLength": 20
          },
          "category": {
            "description": "Category tags for organizing templates."
          },
          "free": {
            "type": "boolean",
            "description": "Whether available on free plans."
          },
          "icon_url": {
            "type": "string",
            "nullable": true,
            "description": "URL for the template's icon."
          },
          "filters": {
            "nullable": true,
            "description": "Default event filters."
          },
          "masking": {
            "nullable": true,
            "description": "Default PII masking configuration."
          },
          "mapping_templates": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/HogFunctionMappingTemplate"
            },
            "nullable": true,
            "description": "Pre-defined mapping configurations for destination templates."
          }
        },
        "required": [
          "code",
          "id",
          "inputs_schema",
          "name",
          "type"
        ]
      },
      "HogFunctionStatus": {
        "type": "object",
        "properties": {
          "state": {
            "$ref": "#/components/schemas/HogFunctionStatusStateEnum"
          },
          "tokens": {
            "type": "integer"
          }
        },
        "required": [
          "state",
          "tokens"
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
      "HogFunctionMappingTemplate": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of this mapping template."
          },
          "include_by_default": {
            "type": "boolean",
            "nullable": true,
            "description": "Whether this mapping is enabled by default."
          },
          "filters": {
            "nullable": true,
            "description": "Event filters specific to this mapping."
          },
          "inputs": {
            "nullable": true,
            "description": "Input values specific to this mapping."
          },
          "inputs_schema": {
            "nullable": true,
            "description": "Additional input schema fields specific to this mapping."
          }
        },
        "required": [
          "name"
        ]
      },
      "HogFunctionStatusStateEnum": {
        "enum": [
          0,
          1,
          2,
          3,
          11,
          12
        ],
        "type": "integer",
        "description": "* `0` - 0\n* `1` - 1\n* `2` - 2\n* `3` - 3\n* `11` - 11\n* `12` - 12"
      }
    }
  }
}
```
