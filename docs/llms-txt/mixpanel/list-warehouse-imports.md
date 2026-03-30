# Source: https://developer.mixpanel.com/reference/list-warehouse-imports.md

# List Warehouse Imports

Returns a list of all warehouse imports configured for the project.

Each import includes metadata about the import configuration, sync status,
and job scheduling information.


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
    "/projects/{projectId}/warehouse-sources/imports": {
      "get": {
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          }
        ],
        "operationId": "list-warehouse-imports",
        "tags": [
          "Warehouse Imports"
        ],
        "summary": "List all warehouse imports",
        "description": "Returns a list of all warehouse imports configured for the project.\n\nEach import includes metadata about the import configuration, sync status,\nand job scheduling information.\n",
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
                    },
                    "results": {
                      "type": "array",
                      "items": {
                        "$ref": "#/components/schemas/WarehouseImport"
                      }
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
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "SyncMode": {
        "type": "string",
        "enum": [
          "time_based",
          "mirror_mode",
          "full_sync",
          "one_time"
        ]
      },
      "SyncFrequency": {
        "type": "integer",
        "description": "Sync frequency in nanoseconds. Only these values are accepted:\n- `0` - API-triggered only (use the manual-sync endpoint to trigger)\n- `3600000000000` - Hourly\n- `86400000000000` - Daily\n- `604800000000000` - Weekly\n",
        "enum": [
          0,
          3600000000000,
          86400000000000,
          604800000000000
        ]
      },
      "ImportType": {
        "type": "string",
        "enum": [
          "event_sync",
          "event_stream",
          "people",
          "groups",
          "lookup_table"
        ]
      },
      "TableParams": {
        "type": "object",
        "description": "Table location parameters (structure depends on warehouse type)"
      },
      "WarehouseImport": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer"
          },
          "import_type": {
            "$ref": "#/components/schemas/ImportType"
          },
          "sync_mode": {
            "$ref": "#/components/schemas/SyncMode"
          },
          "created": {
            "type": "string",
            "format": "date-time"
          },
          "creator_id": {
            "type": "integer"
          },
          "creator_name": {
            "type": "string"
          },
          "creator_email": {
            "type": "string"
          },
          "warehouse_source_id": {
            "type": "integer"
          },
          "table_params": {
            "$ref": "#/components/schemas/TableParams"
          },
          "paused": {
            "type": "boolean"
          },
          "run_every": {
            "allOf": [
              {
                "$ref": "#/components/schemas/SyncFrequency"
              }
            ]
          },
          "last_dispatch": {
            "type": "integer",
            "nullable": true
          },
          "is_deleted": {
            "type": "boolean"
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
  }
}
```