# Source: https://docs.socket.dev/reference/getorganizations.md

# List organizations

Get information on the current organizations associated with the API token.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- No Scopes Required, but authentication is required

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
    "/organizations": {
      "get": {
        "tags": [
          "api-tokens"
        ],
        "summary": "List organizations",
        "operationId": "getOrganizations",
        "security": [
          {
            "bearerAuth": []
          },
          {
            "basicAuth": []
          }
        ],
        "description": "Get information on the current organizations associated with the API token.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- No Scopes Required, but authentication is required",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "organizations": {
                      "type": "object",
                      "additionalProperties": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "name": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "image": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "plan": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "slug": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "id",
                          "image",
                          "name",
                          "plan",
                          "slug"
                        ]
                      },
                      "properties": {},
                      "description": ""
                    }
                  },
                  "required": [
                    "organizations"
                  ]
                }
              }
            },
            "description": "Organizations information"
          },
          "401": {
            "$ref": "#/components/responses/SocketUnauthorized"
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