# Source: https://developer.mixpanel.com/reference/delete-warehouse-import.md

# Delete Warehouse Import

Deletes a warehouse import and optionally deletes the imported data.

When `delete_data: true` is specified, an event deletion request will be
created to remove the imported events from Mixpanel.


# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Warehouse Connectors API",
    "description": "Connect an external warehouse to import events, users, groups, and lookup tables.\n\nThis API allows you to manage warehouse imports from external data warehouses including\nBigQuery, Snowflake, Redshift, Databricks, and PostgreSQL.\n",
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
      "name": "Warehouse Imports",
      "description": "Manage warehouse data imports"
    }
  ],
  "paths": {
    "/projects/{projectId}/warehouse-sources/imports/{importId}": {
      "delete": {
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "$ref": "#/components/parameters/importId"
          }
        ],
        "operationId": "delete-warehouse-import",
        "tags": [
          "Warehouse Imports"
        ],
        "summary": "Delete a warehouse import",
        "description": "Deletes a warehouse import and optionally deletes the imported data.\n\nWhen `delete_data: true` is specified, an event deletion request will be\ncreated to remove the imported events from Mixpanel.\n",
        "requestBody": {
          "required": false,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "delete_data": {
                    "type": "boolean",
                    "description": "Whether to also delete the imported data from Mixpanel",
                    "default": false
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success",
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
    "schemas": {
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
    "securitySchemes": {
      "ServiceAccount": {
        "type": "http",
        "scheme": "basic",
        "description": "Service Account"
      }
    },
    "parameters": {
      "projectId": {
        "in": "path",
        "name": "projectId",
        "schema": {
          "type": "integer"
        },
        "required": true,
        "description": "Your project id (eg: 12345)"
      },
      "importId": {
        "in": "path",
        "name": "importId",
        "schema": {
          "type": "integer"
        },
        "required": true,
        "description": "Your warehouse import id (eg: 12345)"
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
  }
}
```