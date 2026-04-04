# Source: https://developer.mixpanel.com/reference/add-service-accounts-to-projects.md

# Add Service Accounts To Projects

Adds a list of service account ids to a list of project ids with the specified role

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
    "/organizations/{organizationId}/service-accounts/add-to-project": {
      "parameters": [
        {
          "$ref": "#/components/parameters/organizationId"
        }
      ],
      "post": {
        "tags": [
          "Project Membership"
        ],
        "summary": "Add Service Accounts To Projects",
        "description": "Adds a list of service account ids to a list of project ids with the specified role",
        "operationId": "add-service-accounts-to-projects",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/AddServiceAccountsToProjectsRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Service accounts added to projects",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "$ref": "#/components/schemas/ResponseStatusOk"
                    }
                  }
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
      "AddServiceAccountsToProjectsRequest": {
        "type": "object",
        "properties": {
          "projects": {
            "type": "array",
            "description": "List of project/roles",
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
              },
              "required": [
                "id",
                "role"
              ]
            }
          },
          "service_account_ids": {
            "type": "array",
            "description": "List of service account ids",
            "items": {
              "type": "integer"
            }
          }
        },
        "required": [
          "projects",
          "service_account_ids"
        ]
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