# Source: https://developer.mixpanel.com/reference/create-service-account.md

# Create Service Account

Create a new service account for your organization and optionally add it to one or more projects in your organization

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
      "name": "Create Service Accounts",
      "description": "Operations to add service accounts to an organization"
    }
  ],
  "paths": {
    "/organizations/{organizationId}/service-accounts": {
      "parameters": [
        {
          "$ref": "#/components/parameters/organizationId"
        }
      ],
      "post": {
        "tags": [
          "Create Service Accounts"
        ],
        "summary": "Create Service Account",
        "description": "Create a new service account for your organization and optionally add it to one or more projects in your organization",
        "operationId": "create-service-account",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ServiceAccountWrite"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Service account successfully created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CreateServiceAccountResponse"
                }
              }
            }
          },
          "400": {
            "$ref": "#/components/responses/400BadRequest"
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
      "RoleEnum": {
        "type": "string",
        "description": "The service account's role",
        "enum": [
          "owner",
          "admin",
          "analyst",
          "consumer"
        ]
      },
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
      "ServiceAccountWrite": {
        "type": "object",
        "required": [
          "username"
        ],
        "properties": {
          "username": {
            "type": "string",
            "description": "A descriptive name for the service account"
          },
          "role": {
            "$ref": "#/components/schemas/RoleEnum"
          },
          "expires": {
            "type": "string",
            "format": "date-time",
            "description": "The datetime that the service account should expire"
          },
          "projects": {
            "type": "array",
            "description": "A list of projects to make this serivce account a member of",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "The project id to add the service account to"
                },
                "role": {
                  "$ref": "#/components/schemas/RoleEnum"
                }
              }
            }
          }
        }
      },
      "CreateServiceAccountResponse": {
        "type": "object",
        "properties": {
          "results": {
            "allOf": [
              {
                "type": "object",
                "properties": {
                  "token": {
                    "type": "string",
                    "description": "The secret key for this service account. Note: This cannot be recovered so you should immediately store this somewhere secure."
                  }
                }
              },
              {
                "$ref": "#/components/schemas/ServiceAccountRead"
              }
            ]
          },
          "status": {
            "$ref": "#/components/schemas/ResponseStatusOk"
          }
        }
      },
      "ResponseStatusOk": {
        "type": "string",
        "description": "\"ok\" if the request succeeded, \"error\" otherwise.",
        "example": "ok",
        "enum": [
          "ok"
        ]
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
      },
      "400BadRequest": {
        "description": "Bad request",
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