# Source: https://developer.mixpanel.com/reference/list-project-service-accounts.md

# List Service Accounts For Project

Retrieve a list of service accounts that are members of the specified project

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
      "name": "Project Membership",
      "description": "Add/remove service accounts to/from projects"
    }
  ],
  "paths": {
    "/projects/{projectId}/service-accounts": {
      "parameters": [
        {
          "$ref": "#/components/parameters/projectId"
        }
      ],
      "get": {
        "tags": [
          "Project Membership"
        ],
        "summary": "List Service Accounts For Project",
        "description": "Retrieve a list of service accounts that are members of the specified project",
        "operationId": "list-project-service-accounts",
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ListServiceAccountsForProjectResponse"
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
      "ListServiceAccountsForProjectResponse": {
        "type": "object",
        "properties": {
          "results": {
            "type": "array",
            "items": {
              "allOf": [
                {
                  "$ref": "#/components/schemas/ServiceAccountRead"
                },
                {
                  "type": "object",
                  "properties": {
                    "hasSensitiveAccess": {
                      "type": "boolean",
                      "description": "Wether or not the service account has access to classified data. See https://help.mixpanel.com/hc/en-us/articles/360044295131-Data-Classification"
                    },
                    "role": {
                      "$ref": "#/components/schemas/RoleEnum"
                    },
                    "role_order": {
                      "type": "integer",
                      "description": "This is only used internally and is safe to ignore"
                    },
                    "target_type": {
                      "type": "string",
                      "description": "The grant type that gives the service account membership to the project (usually \"individual\")",
                      "enum": [
                        "individual",
                        "team",
                        "organization"
                      ]
                    },
                    "email": {
                      "type": "string",
                      "description": "This is only used internally and is safe to ignore"
                    }
                  }
                }
              ]
            }
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