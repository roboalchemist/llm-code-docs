# Source: https://docs.akeyless.io/reference/get-cert-challenge.md

# /get-cert-challenge

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "The purpose of this application is to provide access to Akeyless API.",
    "title": "Akeyless API",
    "contact": {
      "name": "Akeyless",
      "url": "http://akeyless.io",
      "email": "support@akeyless.io"
    },
    "version": "3.0"
  },
  "paths": {
    "/get-cert-challenge": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "get-cert-challenge",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/GetCertChallenge"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/getCertChallengeResponse"
          },
          "400": {
            "$ref": "#/components/responses/errorResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        },
        "x-generate-protobuf": "true"
      }
    }
  },
  "servers": [
    {
      "url": "https://api.akeyless.io"
    }
  ],
  "components": {
    "responses": {
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
            }
          }
        }
      },
      "getCertChallengeResponse": {
        "description": "getCertChallengeResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/GetCertChallengeOutput"
            }
          }
        }
      }
    },
    "schemas": {
      "GetCertChallenge": {
        "description": "GetCertChallenge is a command that gets a challenge for certificate authentication",
        "type": "object",
        "properties": {
          "access-id": {
            "description": "Access ID",
            "type": "string",
            "x-go-name": "AccessID"
          },
          "cert-data": {
            "description": "Certificate data encoded in base64. Used if file was not provided.",
            "type": "string",
            "x-go-name": "CertData"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "GetCertChallengeOutput": {
        "type": "object",
        "properties": {
          "challenge": {
            "type": "string",
            "x-go-name": "Challenge"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "JSONError": {
        "type": "object",
        "title": "JSONError wraps an error with JSON object.",
        "properties": {
          "error": {
            "type": "string",
            "x-go-name": "Err"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client"
      }
    }
  }
}
```