# Source: https://docs.socket.dev/reference/getsupportedfiles.md

# Get supported file types

Get a list of supported files for full scan generation.
Files are categorized first by environment (e.g. NPM or PyPI), then by name.

Files whose names match the patterns returned by this endpoint can be uploaded for report generation.
Examples of supported filenames include `package.json`, `package-lock.json`, and `yarn.lock`.

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
      "name": "full-scans"
    },
    {
      "name": "diff-scans"
    },
    {
      "name": "metadata"
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
    "/orgs/{org_slug}/supported-files": {
      "get": {
        "tags": [
          "metadata",
          "full-scans",
          "diff-scans"
        ],
        "summary": "Get supported file types",
        "operationId": "getSupportedFiles",
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
            "bearerAuth": []
          },
          {
            "basicAuth": []
          }
        ],
        "description": "Get a list of supported files for full scan generation.\nFiles are categorized first by environment (e.g. NPM or PyPI), then by name.\n\nFiles whose names match the patterns returned by this endpoint can be uploaded for report generation.\nExamples of supported filenames include `package.json`, `package-lock.json`, and `yarn.lock`.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:\n- No Scopes Required, but authentication is required",
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