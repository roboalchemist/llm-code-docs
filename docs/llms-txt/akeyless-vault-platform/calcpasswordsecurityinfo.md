# Source: https://docs.akeyless.io/reference/calcpasswordsecurityinfo.md

# /calc-password-security-info

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
    "/calc-password-security-info": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "calcPasswordSecurityInfo",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/calcPasswordSecurityInfo"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/calcPasswordSecurityInfoResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        }
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
      "calcPasswordSecurityInfoResponse": {
        "description": "calcPasswordSecurityInfoResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/PasswordSecurityInfo"
            }
          }
        }
      },
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
            }
          }
        }
      }
    },
    "schemas": {
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
      },
      "PasswordBreachInfo": {
        "type": "object",
        "properties": {
          "breach_check_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "BreachCheckDate"
          },
          "breach_count": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "BreachCount"
          },
          "breach_suggestions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PasswordBreachSuggestion"
            },
            "x-go-name": "BreachSuggestions"
          },
          "status": {
            "$ref": "#/components/schemas/PasswordBreachStatus"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordBreachStatus": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordBreachSuggestion": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordScoreInfo": {
        "type": "object",
        "properties": {
          "score": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Score"
          },
          "status": {
            "$ref": "#/components/schemas/PasswordScoreStatus"
          },
          "suggestions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PasswordScoreSuggestion"
            },
            "x-go-name": "Suggestions"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordScoreStatus": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordScoreSuggestion": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "PasswordSecurityInfo": {
        "type": "object",
        "properties": {
          "breach_info": {
            "$ref": "#/components/schemas/PasswordBreachInfo"
          },
          "score_info": {
            "$ref": "#/components/schemas/PasswordScoreInfo"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "calcPasswordSecurityInfo": {
        "type": "object",
        "title": "calcPasswordSecurityInfo is a command that calculates password score.",
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "min_length": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "MinLength"
          },
          "password": {
            "type": "string",
            "x-go-name": "Password"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```