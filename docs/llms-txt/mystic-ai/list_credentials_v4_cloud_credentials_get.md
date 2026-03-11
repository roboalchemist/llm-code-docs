# Source: https://docs.mystic.ai/reference/list_credentials_v4_cloud_credentials_get.md

# List Credentials

List all credentials belonging to a user

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Mystic API",
    "version": "4.0.0"
  },
  "servers": [
    {
      "url": "https://www.mystic.ai"
    }
  ],
  "paths": {
    "/v4/cloud/credentials": {
      "get": {
        "tags": [
          "Cloud",
          "credentials"
        ],
        "summary": "List Credentials",
        "description": "List all credentials belonging to a user",
        "operationId": "list_credentials_v4_cloud_credentials_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "items": {
                    "$ref": "#/components/schemas/CredentialGet"
                  },
                  "type": "array",
                  "title": "Response List Credentials V4 Cloud Credentials Get"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          },
          {
            "APIKeyCookie": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "CredentialGet": {
        "properties": {
          "id": {
            "type": "string",
            "title": "Id"
          },
          "provider": {
            "type": "string",
            "title": "Provider"
          },
          "auth_error": {
            "type": "boolean",
            "title": "Auth Error"
          }
        },
        "type": "object",
        "required": [
          "id",
          "provider",
          "auth_error"
        ],
        "title": "CredentialGet",
        "description": "Base model for schemas."
      }
    },
    "securitySchemes": {
      "HTTPBearer": {
        "type": "http",
        "scheme": "bearer"
      },
      "APIKeyCookie": {
        "type": "apiKey",
        "in": "cookie",
        "name": "access-token"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 102,
      "1": 30,
      "2": 82,
      "3": 233,
      "4": 116,
      "5": 201,
      "6": 20,
      "7": 0,
      "8": 75,
      "9": 32,
      "10": 117,
      "11": 11
    }
  }
}
```