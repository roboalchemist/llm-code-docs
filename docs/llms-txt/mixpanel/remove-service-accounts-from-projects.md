# Source: https://developer.mixpanel.com/reference/remove-service-accounts-from-projects.md

# Remove Service Accounts From Projects

Removes a list of service account ids from a list of project ids

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
    "/organizations/{organizationId}/service-accounts/remove-from-project": {
      "parameters": [
        {
          "$ref": "#/components/parameters/organizationId"
        }
      ],
      "post": {
        "tags": [
          "Project Membership"
        ],
        "summary": "Remove Service Accounts From Projects",
        "description": "Removes a list of service account ids from a list of project ids",
        "operationId": "remove-service-accounts-from-projects",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RemoveServiceAccountsFromProjectsRequest"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Service accounts removed from projects",
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
      "RemoveServiceAccountsFromProjectsRequest": {
        "type": "object",
        "properties": {
          "projects": {
            "type": "array",
            "description": "A list of projects and service accounts to remove",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "integer",
                  "description": "The project id to remove the service account from"
                },
                "service_account_ids": {
                  "type": "array",
                  "description": "The list of service account ids to remove from the project",
                  "items": {
                    "type": "integer"
                  }
                }
              },
              "required": [
                "id",
                "service_account_ids"
              ]
            }
          }
        },
        "required": [
          "projects"
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