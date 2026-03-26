# Source: https://docs.socket.dev/reference/getorgwebhook.md

# Get webhook

Get a webhook for the specified organization.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- webhooks:list

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
      "name": "webhooks"
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
    "/orgs/{org_slug}/webhooks/{webhook_id}": {
      "get": {
        "tags": [
          "webhooks"
        ],
        "summary": "Get webhook",
        "externalDocs": {
          "description": "Webhooks documentation",
          "url": "https://docs.socket.dev/docs/webhooks"
        },
        "operationId": "getOrgWebhook",
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
            "name": "webhook_id",
            "in": "path",
            "required": true,
            "description": "The ID of the webhook",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "webhooks:list"
            ]
          },
          {
            "basicAuth": [
              "webhooks:list"
            ]
          }
        ],
        "description": "Get a webhook for the specified organization.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- webhooks:list",
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
                      "description": "The ID of the webhook",
                      "default": ""
                    },
                    "created_at": {
                      "type": "string",
                      "description": "The creation date of the webhook",
                      "default": ""
                    },
                    "updated_at": {
                      "type": "string",
                      "description": "The last update date of the webhook",
                      "default": ""
                    },
                    "name": {
                      "type": "string",
                      "description": "The name of the webhook",
                      "default": ""
                    },
                    "description": {
                      "type": "string",
                      "description": "The description of the webhook",
                      "default": "",
                      "nullable": true
                    },
                    "url": {
                      "type": "string",
                      "description": "The URL where webhook events will be sent",
                      "default": ""
                    },
                    "secret": {
                      "type": "string",
                      "description": "The signing key used to sign webhook payloads",
                      "default": "",
                      "nullable": true
                    },
                    "events": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "description": "The event types to subscribe to",
                        "default": ""
                      },
                      "description": "Array of event names"
                    },
                    "headers": {
                      "type": "object",
                      "description": "Custom headers to include in webhook requests",
                      "default": null,
                      "nullable": true
                    },
                    "filters": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "repositoryIds": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "description": "Repository IDs to filter events",
                            "default": ""
                          },
                          "description": "Array of repository IDs",
                          "nullable": true
                        }
                      },
                      "required": [
                        "repositoryIds"
                      ],
                      "nullable": true
                    }
                  },
                  "required": [
                    "created_at",
                    "description",
                    "events",
                    "filters",
                    "headers",
                    "id",
                    "name",
                    "secret",
                    "updated_at",
                    "url"
                  ]
                }
              }
            },
            "description": "Webhook details"
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