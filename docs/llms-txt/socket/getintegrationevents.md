# Source: https://docs.socket.dev/reference/getintegrationevents.md

# Get integration events

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- integration:list

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
      "name": "org-settings"
    }
  ],
  "components": {
    "responses": {
      "SocketBadRequest": {
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
        "description": "Bad request"
      },
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
      "SocketNotFoundResponse": {
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
        "description": "Resource not found"
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
    "/orgs/{org_slug}/settings/integrations/{integration_id}/events": {
      "get": {
        "tags": [
          "org-settings"
        ],
        "summary": "Get integration events",
        "operationId": "getIntegrationEvents",
        "parameters": [
          {
            "name": "org_slug",
            "in": "path",
            "required": true,
            "description": "The slug of the organization",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "integration_id",
            "in": "path",
            "required": true,
            "description": "The id of the integration",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "integration:list"
            ]
          },
          {
            "basicAuth": [
              "integration:list"
            ]
          }
        ],
        "description": "This endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- integration:list",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "additionalProperties": false,
                    "description": "",
                    "properties": {
                      "id": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "integration_id": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "type": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "payload": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {}
                      },
                      "status_code": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "error": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "sent_at": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "retry_info": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "additionalProperties": false,
                          "description": "",
                          "properties": {
                            "status_code": {
                              "type": "integer",
                              "description": "",
                              "default": 0
                            },
                            "error": {
                              "type": "string",
                              "description": "",
                              "default": ""
                            },
                            "sent_at": {
                              "type": "string",
                              "description": "",
                              "default": ""
                            }
                          },
                          "required": [
                            "error",
                            "sent_at",
                            "status_code"
                          ]
                        },
                        "description": ""
                      },
                      "created_at": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "updated_at": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      }
                    },
                    "required": [
                      "created_at",
                      "error",
                      "id",
                      "integration_id",
                      "payload",
                      "retry_info",
                      "sent_at",
                      "status_code",
                      "type",
                      "updated_at"
                    ]
                  },
                  "description": ""
                }
              }
            },
            "description": "Lists events for the specified integration. The authenticated user must be a member of the organization."
          },
          "400": {
            "$ref": "#/components/responses/SocketBadRequest"
          },
          "401": {
            "$ref": "#/components/responses/SocketUnauthorized"
          },
          "403": {
            "$ref": "#/components/responses/SocketForbidden"
          },
          "404": {
            "$ref": "#/components/responses/SocketNotFoundResponse"
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