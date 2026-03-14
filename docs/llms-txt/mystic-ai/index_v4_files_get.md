# Source: https://docs.mystic.ai/reference/index_v4_files_get.md

# Index

Retrieve a paginated set of pipeline file instances.

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
    "/v4/files": {
      "get": {
        "tags": [
          "Files"
        ],
        "summary": "Index",
        "description": "Retrieve a paginated set of pipeline file instances.",
        "operationId": "index_v4_files_get",
        "parameters": [
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
                  "$ref": "#/components/schemas/Paginated_Any_"
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
      "Paginated_Any_": {
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
            "items": {},
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
        "title": "Paginated[Any]",
        "description": "Response for paginated resource lists."
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