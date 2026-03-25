# Source: https://posthog.com/docs/open-api-spec/public_hog_function_templates_list.md

# public_hog_function_templates_list

## OpenAPI

```json GET /api/public_hog_function_templates/
{
  "paths": {
    "/api/public_hog_function_templates/": {
      "get": {
        "operationId": "public_hog_function_templates_list",
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
            "in": "query",
            "name": "template_id",
            "schema": {
              "type": "string"
            },
            "description": "Filter to a specific template by its template_id. Deprecated templates are excluded from list results; use the retrieve endpoint to look up a template by ID regardless of status."
          },
          {
            "in": "query",
            "name": "type",
            "schema": {
              "type": "string"
            },
            "description": "Filter by template type (e.g. destination, email, sms_provider, broadcast). Defaults to destination if neither type nor types is provided."
          },
          {
            "in": "query",
            "name": "types",
            "schema": {
              "type": "string"
            },
            "description": "Comma-separated list of template types to include (e.g. destination,email,sms_provider)."
          }
        ],
        "tags": [
          "hog_function_templates",
          "public_hog_function_templates"
        ],
        "security": [
          {}
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedHogFunctionTemplateList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "hog_function_templates"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedHogFunctionTemplateList": {
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
              "$ref": "#/components/schemas/HogFunctionTemplate"
            }
          }
        }
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
      }
    }
  }
}
```
