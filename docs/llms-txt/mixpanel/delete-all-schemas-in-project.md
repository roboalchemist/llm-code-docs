# Source: https://developer.mixpanel.com/reference/delete-all-schemas-in-project.md

# Delete all Schemas

Delete all schemas in a project

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Lexicon Schemas API",
    "description": "Use schemas to sync your data dictionary with Mixpanel. Schemas can be used to populate Lexicon and provide additional context for your data.",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "contact": {
      "url": "https://mixpanel.com/get-support"
    },
    "version": "1.0.0"
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
      "name": "Delete Schemas",
      "description": "Remove a schema from a project"
    }
  ],
  "paths": {
    "/projects/{projectId}/schemas": {
      "parameters": [
        {
          "$ref": "#/components/parameters/projectId"
        }
      ],
      "delete": {
        "operationId": "delete-all-schemas-in-project",
        "tags": [
          "Delete Schemas"
        ],
        "summary": "Delete all Schemas",
        "description": "Delete all schemas in a project",
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DeleteSchemasResponse"
                }
              }
            }
          },
          "401": {
            "$ref": "#/components/responses/401Unauthorized"
          },
          "403": {
            "$ref": "#/components/responses/403Forbidden"
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
      "DeleteSchemasResponse": {
        "type": "object",
        "properties": {
          "results": {
            "type": "object",
            "properties": {
              "delete_count": {
                "type": "integer"
              }
            }
          },
          "status": {
            "type": "string",
            "enum": [
              "ok"
            ]
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