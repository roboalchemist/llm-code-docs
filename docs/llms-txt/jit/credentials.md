# Source: https://docs.jit.io/reference/credentials.md

# Authenticate your client credentials

This endpoint validates the Client ID and secret and then issues a temporary JWT for the API.

To obtain your client credentials, go to `Settings -> Users & Permissions -> API Tokens` in the JIT platform.

**NOTE**: The provided token remains valid for 24 hours. After this period, reauthenticate it via this endpoint.

For more information, refer to [Generating API Tokens](https://docs.jit.io/docs/managing-users#generating-api-tokens)

# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Jit Public APIs",
    "description": "Jit Public APIs.\n\nThe API requires that you log in first and obtain a JWT authentication bearer token:\n\nJIT Platform generates CLIENT_ID and SECRET under `Settings -> Users & Permissions -> API Tokens`\n\n For more information, refer to [Users and Permissions](https://docs.jit.io/docs/managing-users#generating-api-tokens)",
    "version": "1",
    "termsOfService": "https://www.jit.io/legal/terms"
  },
  "servers": [
    {
      "url": "https://api.jit.io",
      "description": "Jit API domain"
    }
  ],
  "externalDocs": {
    "url": "https://docs.jit.io/docs",
    "description": "Jit docs"
  },
  "security": [
    {
      "bearerAuth": []
    }
  ],
  "tags": [
    {
      "name": "Authentication",
      "description": "The authentication endpoint is designed to validate the clientId and secret provided by the user. Upon successful validation, it generates and returns a JWT (JSON Web Token) which can be used for subsequent API requests to authorize and identify the caller.",
      "externalDocs": {
        "url": "https://docs.jit.io/docs/managing-users#generating-api-tokens",
        "description": "Learn about obtaining API keys"
      }
    }
  ],
  "paths": {
    "/authentication/login": {
      "post": {
        "summary": "Authenticate your client credentials",
        "description": "This endpoint validates the Client ID and secret and then issues a temporary JWT for the API.\n\nTo obtain your client credentials, go to `Settings -> Users & Permissions -> API Tokens` in the JIT platform.\n\n**NOTE**: The provided token remains valid for 24 hours. After this period, reauthenticate it via this endpoint.\n\nFor more information, refer to [Generating API Tokens](https://docs.jit.io/docs/managing-users#generating-api-tokens)",
        "operationId": "credentials",
        "parameters": [],
        "tags": [
          "Authentication"
        ],
        "security": [
          {}
        ],
        "requestBody": {
          "description": "The Client ID and secret pair for authentication",
          "required": false,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/AuthenticateClientCredentialsRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "API token response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AuthenticateUsingApiTokenResponse"
                }
              }
            },
            "headers": {}
          },
          "400": {
            "description": "Bad request",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/BadRequest"
                }
              }
            },
            "headers": {}
          },
          "401": {
            "description": "Unauthorized",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Unauthorized"
                }
              }
            },
            "headers": {}
          },
          "500": {
            "description": "Internal server error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/InternalServerError"
                }
              }
            },
            "headers": {}
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "BadRequest": {
        "title": "ValidationErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "INVALID_INPUT",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable message containing fields that failed validation.",
            "example": "sample_field1: ensure this value is greater than or equal to 5\ninner_object -> sample_field2: field required",
            "type": "string"
          },
          "invalid_parameters": {
            "title": "Input parameters to errors map",
            "description": "Dictionary mapping input parameter for their corresponding error messages for programmatic use.\n\n**Important**: This dictionary should match your input. Parameters with invalid inputs display their respective messages.",
            "nullable": true,
            "example": {
              "sample_field1": "ensure this value is greater than or equal to 5",
              "inner_object": {
                "sample_field2": "field required"
              }
            },
            "type": "object"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "InternalServerError": {
        "title": "InternalErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "INTERNAL_SERVER_ERROR",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Some error message indicating the issue that occurred",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      },
      "AuthenticateClientCredentialsRequest": {
        "title": "AuthenticateClientCredentialsRequest",
        "type": "object",
        "properties": {
          "clientId": {
            "title": "Client ID",
            "description": "The Client ID for authentication, obtained as part of a key pair from this guide",
            "minLength": 1,
            "example": "CLIENT_ID",
            "type": "string"
          },
          "secret": {
            "title": "Secret",
            "description": "The Secret for authentication, obtained as part of a key pair from this guide",
            "minLength": 1,
            "example": "SECRET",
            "type": "string"
          }
        },
        "required": [
          "clientId",
          "secret"
        ]
      },
      "AuthenticateUsingApiTokenResponse": {
        "title": "AuthenticateUsingApiTokenResponse",
        "type": "object",
        "properties": {
          "accessToken": {
            "title": "Access token",
            "description": "The access token for all JIT APIs.\n\nProvide this as a `Bearer <accessToken>` header in the API requests.",
            "example": "<JWT_TOKEN>",
            "readOnly": true,
            "type": "string"
          },
          "tokenType": {
            "title": "Token type",
            "description": "Currently inactive - Do not use this field.",
            "nullable": true,
            "readOnly": true
          },
          "refreshToken": {
            "title": "Refresh token",
            "description": "Currently inactive - Reauthenticate after the access token expires.",
            "example": "1c64e7db-e1e1-4de6-a5de-0241ffd3cb55",
            "readOnly": true,
            "type": "string"
          },
          "expiresIn": {
            "title": "Token expiration duration",
            "description": "Duration in seconds the access token is valid.",
            "example": 86400,
            "format": "seconds",
            "readOnly": true,
            "type": "integer"
          },
          "expires": {
            "title": "Token expiration date",
            "description": "The expiration date and time of the token.\n\nThis parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/Greenwich_Mean_Time\" target=\"_blank\" rel=\"noopener noreferrer\">GMT</a> format.",
            "example": "Fri, 27 Oct 2023 10:22:38 GMT",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          }
        },
        "required": [
          "accessToken",
          "refreshToken",
          "expiresIn",
          "expires"
        ]
      },
      "Unauthorized": {
        "title": "UnauthorizedErrorResponse",
        "type": "object",
        "properties": {
          "error": {
            "title": "Error code",
            "description": "Machine readable error code.",
            "example": "UNAUTHORIZED",
            "type": "string"
          },
          "message": {
            "title": "Error message",
            "description": "Human readable error message.",
            "example": "Unauthorized",
            "type": "string"
          }
        },
        "required": [
          "error",
          "message"
        ]
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 103,
      "1": 96,
      "2": 119,
      "3": 178,
      "4": 114,
      "5": 109,
      "6": 158,
      "7": 128,
      "8": 238,
      "9": 252,
      "10": 241,
      "11": 194
    }
  }
}
```