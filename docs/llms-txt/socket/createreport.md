# Source: https://docs.socket.dev/reference/createreport.md

# Create a report

**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/createorgfullscan) instead.

Deprecated: Use `/orgs/{org_slug}/full-scans` instead.

Upload a lockfile to get your project analyzed by Socket.
You can upload multiple lockfiles in the same request, but each filename must be unique.

The name of the file must be in the supported list.

For example, these are valid filenames: `package.json`, `folder/package.json` and `deep/nested/folder/package.json`.

This endpoint consumes 100 units of your quota.

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
    "/report/upload": {
      "put": {
        "tags": [
          "deprecated"
        ],
        "summary": "Create a report",
        "deprecated": true,
        "operationId": "createReport",
        "parameters": [
          {
            "name": "workspace",
            "in": "query",
            "required": false,
            "description": "The workspace of the repository to associate the full-scan with.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "multipart/form-data": {
              "schema": {
                "type": "object",
                "additionalProperties": {
                  "type": "string",
                  "default": {
                    "type": "Buffer",
                    "data": []
                  },
                  "format": "binary",
                  "description": ""
                },
                "properties": {
                  "issueRules": {
                    "type": "object",
                    "additionalProperties": {
                      "type": "boolean",
                      "default": false,
                      "description": ""
                    },
                    "properties": {},
                    "description": ""
                  }
                },
                "description": ""
              }
            }
          },
          "required": false
        },
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
        "description": "**This endpoint is deprecated.** Use the [successor version](https://docs.socket.dev/reference/createorgfullscan) instead.\n\nDeprecated: Use `/orgs/{org_slug}/full-scans` instead.\n\nUpload a lockfile to get your project analyzed by Socket.\nYou can upload multiple lockfiles in the same request, but each filename must be unique.\n\nThe name of the file must be in the supported list.\n\nFor example, these are valid filenames: `package.json`, `folder/package.json` and `deep/nested/folder/package.json`.\n\nThis endpoint consumes 100 units of your quota.\n\nThis endpoint requires the following org token scopes:\n- report:write",
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
                      "description": "",
                      "default": ""
                    },
                    "url": {
                      "type": "string",
                      "description": "",
                      "default": ""
                    }
                  },
                  "required": [
                    "id",
                    "url"
                  ]
                }
              }
            },
            "description": "ID and URL of the project report"
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