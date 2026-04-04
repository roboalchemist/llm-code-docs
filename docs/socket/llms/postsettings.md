# Source: https://docs.socket.dev/reference/postsettings.md

# Calculate settings

**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/updateorgsecuritypolicy) instead.

Get current settings for the requested organizations and default settings to allow deferrals.

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
      "name": "deprecated"
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
    "/settings": {
      "post": {
        "tags": [
          "deprecated"
        ],
        "summary": "Calculate settings",
        "deprecated": true,
        "operationId": "postSettings",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "organization": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    }
                  },
                  "description": ""
                },
                "description": ""
              }
            }
          },
          "description": "Array of organization selector objects (with `organization` field holding the organization ID) to get settings for",
          "required": false
        },
        "security": [
          {
            "bearerAuth": []
          },
          {
            "basicAuth": []
          }
        ],
        "description": "**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/updateorgsecuritypolicy) instead.\n\nGet current settings for the requested organizations and default settings to allow deferrals.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- No Scopes Required, but authentication is required",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "defaults": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "issueRules": {
                          "type": "object",
                          "additionalProperties": {
                            "type": "object",
                            "properties": {
                              "action": {
                                "type": "string",
                                "enum": [
                                  "error",
                                  "ignore",
                                  "warn"
                                ]
                              }
                            }
                          }
                        }
                      },
                      "required": [
                        "issueRules"
                      ]
                    },
                    "entries": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "description": "",
                        "properties": {
                          "start": {
                            "type": "string",
                            "description": "",
                            "default": "",
                            "nullable": true
                          },
                          "settings": {
                            "type": "object",
                            "additionalProperties": {
                              "type": "object",
                              "properties": {
                                "deferTo": {
                                  "type": "string",
                                  "nullable": true
                                },
                                "issueRules": {
                                  "type": "object",
                                  "nullable": false,
                                  "additionalProperties": {
                                    "type": "object",
                                    "nullable": false,
                                    "properties": {
                                      "action": {
                                        "type": "string",
                                        "enum": [
                                          "defer",
                                          "error",
                                          "ignore",
                                          "warn",
                                          "monitor"
                                        ]
                                      }
                                    },
                                    "required": [
                                      "action"
                                    ]
                                  }
                                }
                              },
                              "required": [
                                "deferTo",
                                "issueRules"
                              ]
                            }
                          }
                        },
                        "required": [
                          "settings",
                          "start"
                        ]
                      },
                      "description": ""
                    }
                  },
                  "required": [
                    "defaults",
                    "entries"
                  ]
                }
              }
            },
            "description": "Organization settings. Returned object contains default issue rules and an array of entries, with each entry representing an organization's settings."
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