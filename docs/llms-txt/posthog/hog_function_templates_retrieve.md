# Source: https://posthog.com/docs/open-api-spec/hog_function_templates_retrieve.md

# hog_function_templates_retrieve

## OpenAPI

```json GET /api/projects/{project_id}/hog_function_templates/{template_id}/
{
  "paths": {
    "/api/projects/{project_id}/hog_function_templates/{template_id}/": {
      "get": {
        "operationId": "hog_function_templates_retrieve",
        "parameters": [
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
            "in": "path",
            "name": "template_id",
            "schema": {
              "type": "string"
            },
            "required": true
          }
        ],
        "tags": [
          "hog_function_templates",
          "hog_function_templates"
        ],
        "security": [
          {}
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HogFunctionTemplate"
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
