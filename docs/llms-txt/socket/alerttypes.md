# Source: https://docs.socket.dev/reference/alerttypes.md

# Alert Types Metadata

For an array of alert type identifiers, returns metadata for each alert type. Optionally, specify a language via the 'language' query parameter.

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
      }
    }
  },
  "paths": {
    "/alert-types": {
      "post": {
        "tags": [
          "metadata",
          "full-scans",
          "diff-scans"
        ],
        "summary": "Alert Types Metadata",
        "operationId": "alertTypes",
        "parameters": [
          {
            "name": "language",
            "in": "query",
            "required": false,
            "description": "Language for alert metadata",
            "schema": {
              "type": "string",
              "enum": [
                "ach-UG",
                "de-DE",
                "en-US",
                "es-ES",
                "fr-FR",
                "it-IT"
              ],
              "default": "en-US"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "type": "string",
                  "description": "",
                  "default": ""
                },
                "description": ""
              }
            }
          },
          "required": false
        },
        "security": [],
        "description": "For an array of alert type identifiers, returns metadata for each alert type. Optionally, specify a language via the 'language' query parameter.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:",
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
                      "type": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "title": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "description": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "suggestion": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "emoji": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "nextStepTitle": {
                        "type": "string",
                        "description": "",
                        "default": ""
                      },
                      "props": {
                        "type": "object",
                        "additionalProperties": {
                          "type": "string",
                          "description": "",
                          "default": ""
                        },
                        "properties": {},
                        "description": "",
                        "nullable": true
                      }
                    },
                    "required": [
                      "description",
                      "emoji",
                      "nextStepTitle",
                      "props",
                      "suggestion",
                      "title",
                      "type"
                    ]
                  },
                  "description": ""
                }
              }
            },
            "description": "Metadata for the requested alert types"
          },
          "400": {
            "$ref": "#/components/responses/SocketBadRequest"
          }
        },
        "x-readme": {}
      }
    }
  }
}
```