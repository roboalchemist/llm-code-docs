# Source: https://docs.akeyless.io/reference/rawcreds.md

# /raw-creds

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
    "/raw-creds": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "rawCreds",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/rawCreds"
              }
            }
          },
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/rawCredsResponse"
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
      "rawCredsResponse": {
        "description": "rawCredsResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/SystemAccessCredentialsReplyObj"
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
      "MFAType": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "SystemAccessCredentialsReplyObj": {
        "type": "object",
        "title": "Combination of three temporary credentials signed by Auth for accessing Auth, UAM and KFMs instances.",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessId"
          },
          "auth_creds": {
            "description": "Temporary credentials for accessing Auth",
            "type": "string",
            "x-go-name": "AuthAccessCredentials"
          },
          "expiry": {
            "description": "Credentials expiration date",
            "type": "integer",
            "format": "int64",
            "x-go-name": "Expiry"
          },
          "kfm_creds": {
            "description": "Temporary credentials for accessing the KFMs instances",
            "type": "string",
            "x-go-name": "KFMsAccessCredentials"
          },
          "need_mfa_app_first_config": {
            "description": "If the user didn't complete to configure the MFA app",
            "type": "boolean",
            "x-go-name": "NeedMfaAppFirstConfig"
          },
          "required_mfa": {
            "$ref": "#/components/schemas/MFAType"
          },
          "token": {
            "description": "Credentials tmp token",
            "type": "string",
            "x-go-name": "Token"
          },
          "uam_creds": {
            "description": "Temporary credentials for accessing the UAM service",
            "type": "string",
            "x-go-name": "UAMAccessCredentials"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/auth"
      },
      "rawCreds": {
        "type": "object",
        "title": "rawCreds is a command that returns raw Akeyless access credentials.",
        "properties": {
          "access-id": {
            "type": "string",
            "x-go-name": "AccessID"
          },
          "access-key": {
            "type": "string",
            "x-go-name": "AccessKey"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```