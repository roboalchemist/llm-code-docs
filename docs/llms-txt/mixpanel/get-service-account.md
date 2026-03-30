# Source: https://developer.mixpanel.com/reference/get-service-account.md

# Get Service Account

Return service account details by id

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Service Accounts API",
    "description": "Endpoints for managing service accounts programmatically.",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "1.0.0",
    "contact": {
      "url": "https://mixpanel.com/get-support"
    }
  },
  "servers": [
    {
      "url": "https://{regionAndDomain}.com/api/app",
      "description": "Mixpanel's application API server.",
      "variables": {
        "regionAndDomain": {
          "default": "mixpanel",
          "enum": [
            "mixpanel",
            "eu.mixpanel",
            "in.mixpanel"
          ],
          "description": "The server location to be used:\n  * `mixpanel` - The default (US) servers used for most projects\n  * `eu.mixpanel` - EU servers if you are enrolled in EU Data Residency\n  * `in.mixpanel` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "security": [
    {
      "ServiceAccount": []
    }
  ],
  "tags": [
    {
      "name": "Retrieve Service Accounts",
      "description": "Get details about an organization's service account"
    }
  ],
  "paths": {
    "/organizations/{organizationId}/service-accounts/{serviceAccountId}": {
      "parameters": [
        {
          "$ref": "#/components/parameters/organizationId"
        },
        {
          "$ref": "#/components/parameters/serviceAccountId"
        }
      ],
      "get": {
        "tags": [
          "Retrieve Service Accounts"
        ],
        "summary": "Get Service Account",
        "description": "Return service account details by id",
        "operationId": "get-service-account",
        "responses": {
          "200": {
            "description": "successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ServiceAccountRead"
                }
              }
            }
          },
          "401": {
            "$ref": "#/components/responses/401Unauthorized"
          },
          "403": {
            "$ref": "#/components/responses/403Forbidden"
          },
          "404": {
            "$ref": "#/components/responses/404NotFound"
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "ServiceAccount": {
        "type": "http",
        "scheme": "basic",
        "description": "Service Account"
      }
    },
    "schemas": {
      "ServiceAccountRead": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "The unique identifier for this service account"
          },
          "username": {
            "type": "string",
            "description": "The username of the service account"
          },
          "last_used": {
            "type": "string",
            "format": "date-time",
            "description": "The date/time this service account was last used for authentication"
          },
          "expires": {
            "type": "string",
            "format": "date-time",
            "description": "The date/time this service account will expire"
          },
          "creator": {
            "type": "integer",
            "description": "The Mixpanel user id that created this service account"
          },
          "created": {
            "type": "string",
            "format": "date-time",
            "description": "The date/time this service account was created"
          },
          "user": {
            "type": "integer",
            "description": "The Mixpanel user id that this serivce account represents. This is only used internally and is safe to ignore."
          }
        }
      },
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "description": "Details about the error that occurred"
          },
          "status": {
            "type": "string",
            "enum": [
              "error"
            ]
          }
        }
      }
    },
    "responses": {
      "401Unauthorized": {
        "description": "Unauthorized",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      },
      "403Forbidden": {
        "description": "Forbidden",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      },
      "404NotFound": {
        "description": "Not Found",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      }
    }
  },
  "x-explorer-enabled": true,
  "x-proxy-enabled": true,
  "x-samples-enabled": true,
  "x-samples-languages": [
    "curl",
    "node",
    "ruby",
    "javascript",
    "python"
  ]
}
```