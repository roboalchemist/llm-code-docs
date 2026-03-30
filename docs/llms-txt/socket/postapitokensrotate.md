# Source: https://docs.socket.dev/reference/postapitokensrotate.md

# Rotate API Token

Rotate an API Token

This endpoint consumes 10 units of your quota.

This endpoint requires the following org token scopes:
- api-tokens:rotate

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "Specification of the Socket API endpoints",
    "title": "API Endpoints",
    "version": "0"
  },
  "servers": [
    {
      "url": "https://api.socket.dev/v0"
    }
  ],
  "tags": [
    {
      "name": "api-tokens"
    }
  ],
  "components": {
    "responses": {
      "SocketUnauthorized": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Unauthorized"
      },
      "SocketForbidden": {
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        },
        "description": "Insufficient max_quota for API method"
      },
      "SocketTooManyRequestsResponse": {
        "description": "Insufficient quota for API route",
        "headers": {
          "Retry-After": {
            "description": "Retry contacting the endpoint *at least* after seconds.\nSee https://tools.ietf.org/html/rfc7231#section-7.1.3",
            "schema": {
              "format": "int32",
              "type": "integer"
            }
          }
        },
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "additionalProperties": false,
              "description": "",
              "properties": {
                "error": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "message": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "details": {
                      "type": "object",
                      "description": "",
                      "default": null,
                      "nullable": true
                    }
                  },
                  "required": [
                    "details",
                    "message"
                  ]
                }
              },
              "required": [
                "error"
              ]
            }
          }
        }
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "description": "Organization Tokens can be passed as a Bearer token"
      },
      "basicAuth": {
        "type": "http",
        "scheme": "basic",
        "description": "Organization Tokens can be passed as the user field in basic auth"
      }
    }
  },
  "paths": {
    "/orgs/{org_slug}/api-tokens/rotate": {
      "post": {
        "tags": [
          "api-tokens"
        ],
        "summary": "Rotate API Token",
        "operationId": "postAPITokensRotate",
        "parameters": [
          {
            "name": "org_slug",
            "in": "path",
            "required": true,
            "description": "The slug of the organization",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "uuid": {
                    "type": "string",
                    "description": "The stable group UUID of the API token to rotate",
                    "default": "",
                    "format": "uuid"
                  },
                  "token": {
                    "type": "string",
                    "description": "",
                    "default": ""
                  },
                  "hash": {
                    "type": "string",
                    "description": "",
                    "default": ""
                  }
                },
                "description": "The API Token identifier to rotate. Provide uuid (recommended), token, or hash. May provide uuid+hash together for validation."
              }
            }
          },
          "description": "The API Token identifier to rotate. Provide uuid (recommended), token, or hash. May provide uuid+hash together for validation.",
          "required": false
        },
        "security": [
          {
            "bearerAuth": [
              "api-tokens:rotate"
            ]
          },
          {
            "basicAuth": [
              "api-tokens:rotate"
            ]
          }
        ],
        "description": "Rotate an API Token\n\nThis endpoint consumes 10 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- api-tokens:rotate",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "id": {
                      "type": "string",
                      "description": "The database ID of the new API token",
                      "default": ""
                    },
                    "group_uuid": {
                      "type": "string",
                      "description": "The stable group UUID (unchanged after rotation)",
                      "default": "",
                      "format": "uuid"
                    },
                    "created_by": {
                      "type": "string",
                      "description": "ID of the Socket user who created the API Token",
                      "default": "",
                      "format": "uuid",
                      "nullable": true
                    },
                    "token": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "hash": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    }
                  },
                  "required": [
                    "created_by",
                    "group_uuid",
                    "hash",
                    "id",
                    "token"
                  ]
                }
              }
            },
            "description": "The replacement API Token with its stable UUID, new token value, and hash"
          },
          "401": {
            "$ref": "#/components/responses/SocketUnauthorized"
          },
          "403": {
            "$ref": "#/components/responses/SocketForbidden"
          },
          "429": {
            "$ref": "#/components/responses/SocketTooManyRequestsResponse"
          }
        },
        "x-readme": {}
      }
    }
  }
}
```