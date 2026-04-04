# Source: https://docs.mystic.ai/reference/index_v4_pipeline_families_get.md

# Index

List pipeline families. Depending on parameters this can mean all public
families, or a user's specific families.
Can also be ordered and filtered based on family name.

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
    "/v4/pipeline-families": {
      "get": {
        "tags": [
          "Pipeline Families"
        ],
        "summary": "Index",
        "description": "List pipeline families. Depending on parameters this can mean all public\nfamilies, or a user's specific families.\nCan also be ordered and filtered based on family name.",
        "operationId": "index_v4_pipeline_families_get",
        "parameters": [
          {
            "required": false,
            "schema": {
              "type": "string",
              "title": "User Id"
            },
            "name": "user_id",
            "in": "query"
          },
          {
            "required": false,
            "schema": {
              "allOf": [
                {
                  "$ref": "#/components/schemas/OrderBy"
                }
              ],
              "default": "popular"
            },
            "name": "order_by",
            "in": "query"
          },
          {
            "required": false,
            "schema": {
              "type": "string",
              "maxLength": 255,
              "title": "Search"
            },
            "name": "search",
            "in": "query"
          },
          {
            "required": false,
            "schema": {
              "type": "integer",
              "title": "Skip",
              "default": 0
            },
            "name": "skip",
            "in": "query"
          },
          {
            "required": false,
            "schema": {
              "type": "integer",
              "title": "Limit",
              "default": 20
            },
            "name": "limit",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Paginated_PipelineFamilyGet_"
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
      "OrderBy": {
        "enum": [
          "popular",
          "recent"
        ],
        "title": "OrderBy",
        "description": "An enumeration."
      },
      "Paginated_PipelineFamilyGet_": {
        "properties": {
          "skip": {
            "type": "integer",
            "minimum": 0,
            "title": "Skip"
          },
          "limit": {
            "type": "integer",
            "maximum": 1000,
            "minimum": 1,
            "title": "Limit"
          },
          "total": {
            "type": "integer",
            "minimum": 0,
            "title": "Total"
          },
          "data": {
            "items": {
              "$ref": "#/components/schemas/PipelineFamilyGet"
            },
            "type": "array",
            "title": "Data"
          }
        },
        "type": "object",
        "required": [
          "skip",
          "limit",
          "total",
          "data"
        ],
        "title": "Paginated[PipelineFamilyGet]",
        "description": "Response for paginated resource lists."
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