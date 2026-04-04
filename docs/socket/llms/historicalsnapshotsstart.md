# Source: https://docs.socket.dev/reference/historicalsnapshotsstart.md

# Start historical data snapshot job (Beta)

This API endpoint is used to start a historical snapshot job.
While snapshots are typically taken multiple times a day for paid plans and once a day for free plans, this endpoint can be used to start an "on demand" snapshot job to ensure the latest data is collected and stored for historical purposes.

An historical snapshot will contain details and raw data for the following resources:

- Repositories
- Alerts
- Dependencies
- Artifacts
- Users
- Settings

Historical snapshot data is bucketed to the nearest day which is described in more detail at: [Historical Data Endpoints](/reference/historical-data-endpoints)

This endpoint consumes 10 units of your quota.

This endpoint requires the following org token scopes:
- historical:snapshots-start

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
      "name": "org-snapshots"
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
    "/orgs/{org_slug}/historical/snapshots": {
      "post": {
        "tags": [
          "org-snapshots"
        ],
        "summary": "Start historical data snapshot job (Beta)",
        "operationId": "historicalSnapshotsStart",
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
        "security": [
          {
            "bearerAuth": [
              "historical:snapshots-start"
            ]
          },
          {
            "basicAuth": [
              "historical:snapshots-start"
            ]
          }
        ],
        "description": "This API endpoint is used to start a historical snapshot job.\nWhile snapshots are typically taken multiple times a day for paid plans and once a day for free plans, this endpoint can be used to start an \"on demand\" snapshot job to ensure the latest data is collected and stored for historical purposes.\n\nAn historical snapshot will contain details and raw data for the following resources:\n\n- Repositories\n- Alerts\n- Dependencies\n- Artifacts\n- Users\n- Settings\n\nHistorical snapshot data is bucketed to the nearest day which is described in more detail at: [Historical Data Endpoints](/reference/historical-data-endpoints)\n\nThis endpoint consumes 10 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- historical:snapshots-start",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "",
                  "properties": {
                    "requestId": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "requestedBy": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    },
                    "requestedAt": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    }
                  },
                  "required": [
                    "requestId",
                    "requestedAt",
                    "requestedBy"
                  ]
                }
              }
            },
            "description": "The details of the snapshot job request."
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