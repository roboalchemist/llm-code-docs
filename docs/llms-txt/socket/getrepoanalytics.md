# Source: https://docs.socket.dev/reference/getrepoanalytics.md

# Get repository analytics

**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/historicalalertstrend) instead.

Please implement against the [Historical dependencies](/reference/historicaldependenciestrend) or [Historical alerts](/reference/historicalalertstrend) endpoints.

Get analytics data regarding the number of alerts found in a single repository.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:
- report:write

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
    "/analytics/repo/{name}/{filter}": {
      "get": {
        "tags": [
          "deprecated"
        ],
        "summary": "Get repository analytics",
        "deprecated": true,
        "operationId": "getRepoAnalytics",
        "parameters": [
          {
            "name": "name",
            "in": "path",
            "required": true,
            "description": "",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "filter",
            "in": "path",
            "required": true,
            "description": "",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [
          {
            "bearerAuth": [
              "report:write"
            ]
          },
          {
            "basicAuth": [
              "report:write"
            ]
          }
        ],
        "description": "**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/historicalalertstrend) instead.\n\nPlease implement against the [Historical dependencies](/reference/historicaldependenciestrend) or [Historical alerts](/reference/historicalalertstrend) endpoints.\n\nGet analytics data regarding the number of alerts found in a single repository.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- report:write",
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
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "repository_id": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "created_at": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "organization_id": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "repository_name": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "total_critical_alerts": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "total_high_alerts": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "total_medium_alerts": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "total_low_alerts": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "total_critical_added": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "total_high_added": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "total_medium_added": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "total_low_added": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "total_critical_prevented": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "total_high_prevented": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "total_medium_prevented": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "total_low_prevented": {
                        "type": "integer",
                        "description": "",
                        "default": 0
                      },
                      "top_five_alert_types": {
                        "type": "object",
                        "default": {},
                        "additionalProperties": false
                      }
                    },
                    "required": [
                      "created_at",
                      "id",
                      "organization_id",
                      "repository_id",
                      "repository_name",
                      "top_five_alert_types",
                      "total_critical_added",
                      "total_critical_alerts",
                      "total_critical_prevented",
                      "total_high_added",
                      "total_high_alerts",
                      "total_high_prevented",
                      "total_low_added",
                      "total_low_alerts",
                      "total_low_prevented",
                      "total_medium_added",
                      "total_medium_alerts",
                      "total_medium_prevented"
                    ]
                  },
                  "description": ""
                }
              }
            },
            "description": "Socket analytics - repo-level data"
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