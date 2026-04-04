# Source: https://docs.socket.dev/reference/searchdependencies.md

# Search dependencies

Search for any dependency that is being used in your organization.

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
      "name": "dependencies"
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
    "/dependencies/search": {
      "post": {
        "tags": [
          "dependencies"
        ],
        "summary": "Search dependencies",
        "operationId": "searchDependencies",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "limit": {
                    "type": "integer",
                    "description": "",
                    "default": 50,
                    "minimum": 1,
                    "maximum": 100
                  },
                  "offset": {
                    "type": "integer",
                    "description": "",
                    "default": 0,
                    "minimum": 0
                  },
                  "purls": {
                    "type": "array",
                    "items": {
                      "type": "string",
                      "description": "PURLs to filter results with",
                      "default": ""
                    },
                    "description": ""
                  }
                },
                "required": [
                  "limit",
                  "offset"
                ]
              }
            }
          },
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
        "description": "Search for any dependency that is being used in your organization.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- No Scopes Required, but authentication is required",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "end": {
                      "type": "boolean",
                      "default": false,
                      "description": ""
                    },
                    "limit": {
                      "type": "integer",
                      "description": "",
                      "default": 1000
                    },
                    "offset": {
                      "type": "integer",
                      "description": "",
                      "default": 0
                    },
                    "purlFilters": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "valid": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "description": "Successfully parsed PURLs",
                            "default": ""
                          },
                          "description": ""
                        },
                        "invalid": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "description": "PURLs that could not be parsed",
                            "default": ""
                          },
                          "description": ""
                        }
                      },
                      "required": [
                        "invalid",
                        "valid"
                      ]
                    },
                    "rows": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "additionalProperties": false,
                        "properties": {
                          "branch": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "direct": {
                            "type": "boolean",
                            "default": false,
                            "description": ""
                          },
                          "id": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "name": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "repository": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "type": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "namespace": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "version": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "release": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          },
                          "workspace": {
                            "type": "string",
                            "description": "",
                            "default": ""
                          }
                        },
                        "required": [
                          "branch",
                          "direct",
                          "id",
                          "name",
                          "repository",
                          "type"
                        ]
                      },
                      "description": ""
                    }
                  },
                  "required": [
                    "end",
                    "limit",
                    "offset",
                    "purlFilters",
                    "rows"
                  ]
                }
              }
            },
            "description": "Search dependencies response"
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