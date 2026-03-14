# Source: https://docs.mystic.ai/reference/retrieve_v4_pipeline_families__pipeline_family_name__get.md

# Retrieve

Retrieve a pipeline family by name with its latest pipeline.
If the user owns the family, the latest pipeline may be a private pipeline,
otherwise it will only be public.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Mystic API",
    "version": "4.0.0"
  },
  "servers": [
    {
      "url": "https://www.mystic.ai"
    }
  ],
  "paths": {
    "/v4/pipeline-families/{pipeline_family_name}": {
      "get": {
        "tags": [
          "Pipeline Families"
        ],
        "summary": "Retrieve",
        "description": "Retrieve a pipeline family by name with its latest pipeline.\nIf the user owns the family, the latest pipeline may be a private pipeline,\notherwise it will only be public.",
        "operationId": "retrieve_v4_pipeline_families__pipeline_family_name__get",
        "parameters": [
          {
            "required": true,
            "schema": {
              "type": "string",
              "title": "Pipeline Family Name"
            },
            "name": "pipeline_family_name",
            "in": "path"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PipelineFamilyGet"
                }
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          },
          {
            "APIKeyCookie": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "type": "array",
            "title": "Detail"
          }
        },
        "type": "object",
        "title": "HTTPValidationError"
      },
      "PipelineFamilyGet": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "run_count": {
            "type": "integer",
            "title": "Run Count"
          },
          "description": {
            "type": "string",
            "title": "Description"
          },
          "latest_at": {
            "type": "string",
            "format": "date-time",
            "title": "Latest At"
          },
          "pipeline_id": {
            "type": "string",
            "title": "Pipeline Id"
          },
          "image_url": {
            "type": "string",
            "title": "Image Url"
          }
        },
        "type": "object",
        "required": [
          "name",
          "run_count",
          "latest_at",
          "pipeline_id"
        ],
        "title": "PipelineFamilyGet",
        "description": "Base model for schemas."
      },
      "ValidationError": {
        "properties": {
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "type": "array",
            "title": "Location"
          },
          "msg": {
            "type": "string",
            "title": "Message"
          },
          "type": {
            "type": "string",
            "title": "Error Type"
          }
        },
        "type": "object",
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError"
      }
    },
    "securitySchemes": {
      "HTTPBearer": {
        "type": "http",
        "scheme": "bearer"
      },
      "APIKeyCookie": {
        "type": "apiKey",
        "in": "cookie",
        "name": "access-token"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 102,
      "1": 30,
      "2": 82,
      "3": 233,
      "4": 116,
      "5": 201,
      "6": 20,
      "7": 0,
      "8": 75,
      "9": 32,
      "10": 117,
      "11": 11
    }
  }
}
```