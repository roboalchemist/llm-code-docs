# Source: https://help.cloudsmith.io/reference/broadcasts_create_broadcast_token.md

# Create a broadcast token.

Create a broadcast token.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Cloudsmith API (v1)",
    "description": "The API to the Cloudsmith Service",
    "termsOfService": "https://help.cloudsmith.io",
    "contact": {
      "name": "Cloudsmith Support",
      "url": "https://help.cloudsmith.io",
      "email": "support@cloudsmith.io"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "v1"
  },
  "security": [
    {
      "apikey": []
    },
    {
      "basic": []
    }
  ],
  "paths": {
    "/broadcasts/{org}/broadcast-token/": {
      "post": {
        "operationId": "broadcasts_create_broadcast_token",
        "summary": "Create a broadcast token.",
        "description": "Create a broadcast token.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/BroadcastTokenInput"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BroadcastToken"
                }
              }
            }
          },
          "201": {
            "description": "Created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BroadcastToken"
                }
              }
            }
          },
          "400": {
            "description": "Request could not be processed (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "404": {
            "description": "Entitlement token not found",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Entitlement token parameter is required.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          }
        },
        "tags": [
          "broadcasts"
        ]
      },
      "parameters": [
        {
          "name": "org",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    }
  },
  "servers": [
    {
      "url": "https://api.cloudsmith.io"
    }
  ],
  "components": {
    "securitySchemes": {
      "apikey": {
        "type": "apiKey",
        "name": "X-Api-Key",
        "in": "header"
      },
      "basic": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "ErrorDetail": {
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "An extended message for the response.",
            "type": "string",
            "minLength": 1
          },
          "fields": {
            "title": "Fields",
            "description": "A Dictionary of related errors where key: Field and value: Array of Errors related to that field",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "minLength": 1
              }
            }
          }
        }
      },
      "BroadcastTokenInput": {
        "required": [
          "entitlement_token"
        ],
        "type": "object",
        "properties": {
          "entitlement_token": {
            "title": "Entitlement token",
            "description": "Repository entitlement token used to authorize the creation of a broadcast token",
            "type": "string",
            "minLength": 1
          },
          "expires_in": {
            "title": "Expires in",
            "description": "Token expiry time in seconds (optional, defaults to 3600 seconds)",
            "type": "integer",
            "minimum": 1
          }
        }
      },
      "BroadcastToken": {
        "type": "object",
        "properties": {
          "expires_at": {
            "title": "Expires at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "token": {
            "title": "Token",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          }
        }
      }
    }
  }
}
```