# Source: https://docs.socket.dev/reference/getopenapi.md

# Returns the OpenAPI definition

Retrieve the API specification in an Openapi JSON format.

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
      "name": "metadata"
    }
  ],
  "components": {
    "responses": {
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
    "/openapi": {
      "get": {
        "tags": [
          "metadata"
        ],
        "summary": "Returns the OpenAPI definition",
        "operationId": "getOpenAPI",
        "security": [],
        "description": "Retrieve the API specification in an Openapi JSON format.\n\nThis endpoint consumes 1 unit of your quota.\n\nThis endpoint requires the following org token scopes:",
        "responses": {
          "200": {
            "content": {
              "application/json": {}
            },
            "description": "OpenAPI specification"
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