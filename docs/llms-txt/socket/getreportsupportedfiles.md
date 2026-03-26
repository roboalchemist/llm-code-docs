# Source: https://docs.socket.dev/reference/getreportsupportedfiles.md

# Get supported files for report

**This endpoint is deprecated.** Deprecated since 2023-01-15. Use the [successor version](https://docs.socket.dev/reference/getsupportedfiles) instead.

This route has been moved to the `orgs/{org_slug}/supported-files` endpoint.

Get a list of supported files for project report generation.
Files are categorized first by environment (e.g. NPM or PyPI), then by name.

Files whose names match the patterns returned by this endpoint can be uploaded for report generation.
Examples of supported filenames include `package.json`, `package-lock.json`, and `yarn.lock`.

This endpoint consumes 1 unit of your quota.

This endpoint requires the following org token scopes:

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
    }
  },
  "paths": {
    "/report/supported": {
      "get": {
        "tags": [
          "deprecated"
        ],
        "summary": "Get supported files for report",
        "deprecated": true,
        "operationId": "getReportSupportedFiles",
        "security": [],
        "description": "**This endpoint is deprecated.** Deprecated since 2023-01-15. Use the [successor version](https://docs.socket.dev/reference/getsupportedfiles) instead.\n\nThis route has been moved to the `orgs/{org_slug}/supported-files` endpoint.\n\nGet a list of supported files for project report generation.\nFiles are categorized first by environment (e.g. NPM or PyPI), then by name.\n\nFiles whose names match the patterns returned by this endpoint can be uploaded for report generation.\nExamples of supported filenames include `package.json`, `package-lock.json`, and `yarn.lock`.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "additionalProperties": {
                    "type": "object",
                    "additionalProperties": {
                      "type": "object",
                      "additionalProperties": false,
                      "description": "",
                      "properties": {
                        "pattern": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        }
                      },
                      "required": [
                        "pattern"
                      ]
                    },
                    "properties": {},
                    "description": ""
                  },
                  "properties": {},
                  "description": ""
                }
              }
            },
            "description": "Glob patterns used to match supported files"
          },
          "400": {
            "$ref": "#/components/responses/SocketBadRequest"
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