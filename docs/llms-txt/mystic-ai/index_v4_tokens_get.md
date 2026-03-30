# Source: https://docs.mystic.ai/reference/index_v4_tokens_get.md

# Index

Retrieve a Catalyst API Bearer token for an authenticated user.

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
    "/v4/tokens": {
      "get": {
        "tags": [
          "Tokens"
        ],
        "summary": "Index",
        "description": "Retrieve a Catalyst API Bearer token for an authenticated user.",
        "operationId": "index_v4_tokens_get",
        "parameters": [
          {
            "required": false,
            "schema": {
              "type": "boolean",
              "title": "All Team",
              "default": false
            },
            "name": "all_team",
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
                  "$ref": "#/components/schemas/Paginated_TokenGet_"
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
      "Paginated_TokenGet_": {
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
              "$ref": "#/components/schemas/TokenGet"
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
        "title": "Paginated[TokenGet]",
        "description": "Response for paginated resource lists."
      },
      "TokenGet": {
        "properties": {
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
          "value": {
            "type": "string",
            "title": "Value"
          },
          "name": {
            "type": "string",
            "title": "Name"
          },
          "expires_at": {
            "type": "string",
            "format": "date-time",
            "title": "Expires At"
          },
          "last_used": {
            "type": "string",
            "format": "date-time",
            "title": "Last Used"
          },
          "is_active": {
            "type": "boolean",
            "title": "Is Active"
          },
          "is_enabled": {
            "type": "boolean",
            "title": "Is Enabled"
          },
          "team_id": {
            "type": "string",
            "title": "Team Id"
          }
        },
        "type": "object",
        "required": [
          "id",
          "created_at",
          "updated_at",
          "value",
          "name",
          "is_active",
          "is_enabled"
        ],
        "title": "TokenGet",
        "description": "API token representation when returned from an API call."
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