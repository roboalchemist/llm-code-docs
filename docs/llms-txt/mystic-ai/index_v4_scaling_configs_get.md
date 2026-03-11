# Source: https://docs.mystic.ai/reference/index_v4_scaling_configs_get.md

# Index

Retrieve a paginated set of scaling configurations

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
    "/v4/scaling-configs": {
      "get": {
        "tags": [
          "Scaling configurations"
        ],
        "summary": "Index",
        "description": "Retrieve a paginated set of scaling configurations",
        "operationId": "index_v4_scaling_configs_get",
        "parameters": [
          {
            "required": false,
            "schema": {
              "type": "boolean",
              "title": "Public",
              "default": false
            },
            "name": "public",
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
          },
          {
            "required": false,
            "schema": {
              "type": "string",
              "pattern": "[^:]*(:(asc|desc))?$",
              "title": "Order By"
            },
            "name": "order_by",
            "in": "query"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Paginated_ScalingConfigGetWithPipelineCount_"
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
      "Paginated_ScalingConfigGetWithPipelineCount_": {
        "properties": {
          "skip": {
            "type": "integer",
            "minimum": 0,
            "title": "Skip"
          },
          "limit": {
            "type": "integer",
            "maximum": 10000,
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
              "$ref": "#/components/schemas/ScalingConfigGetWithPipelineCount"
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
        "title": "Paginated[ScalingConfigGetWithPipelineCount]",
        "description": "Response model for a paginated set of a given resource."
      },
      "ScalingConfigGetWithPipelineCount": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "minimum_nodes": {
            "type": "integer",
            "minimum": 0,
            "title": "Minimum Nodes",
            "default": 0
          },
          "maximum_nodes": {
            "type": "integer",
            "minimum": 0,
            "title": "Maximum Nodes",
            "default": 100
          },
          "type": {
            "$ref": "#/components/schemas/ScalingConfigType"
          },
          "args": {
            "type": "object",
            "title": "Args"
          },
          "id": {
            "type": "string",
            "title": "Id"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "title": "Created At"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "title": "Updated At"
          },
          "pipeline_count": {
            "type": "integer",
            "title": "Pipeline Count"
          }
        },
        "type": "object",
        "required": [
          "name",
          "type",
          "args",
          "id",
          "created_at",
          "updated_at",
          "pipeline_count"
        ],
        "title": "ScalingConfigGetWithPipelineCount",
        "description": "Base model for schemas."
      },
      "ScalingConfigType": {
        "type": "string",
        "enum": [
          "windows"
        ],
        "title": "ScalingConfigType",
        "description": "An enumeration."
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