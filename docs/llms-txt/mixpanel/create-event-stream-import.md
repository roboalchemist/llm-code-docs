# Source: https://developer.mixpanel.com/reference/create-event-stream-import.md

# Create Event Stream Import

Create a new warehouse import for event data.

Event stream imports sync event data from your warehouse table to Mixpanel.
Each row in your table becomes an event in Mixpanel.

## Sync Modes

- **time_based**: Incrementally syncs new rows based on an insert time column
- **mirror_mode**: Detects changes in the source table and mirrors them to Mixpanel
- **full_sync**: Re-syncs all data on each run
- **one_time**: Syncs data once and does not repeat

## Required Column Mappings

You must specify either:
- `event_name`: A static event name for all rows
- `event_column_name`: The column containing the event name

For B2B projects, `company_column_name` is also required.

## Scheduling

- **run_every** (integer): Sync frequency in nanoseconds. Allowed values:
  - Trigger via API: `0`
  - Hourly: `3600000000000` (60 * 60 * 10^9)
  - Daily: `86400000000000` (24 * 60 * 60 * 10^9)
  - Weekly: `604800000000000` (7 * 24 * 60 * 60 * 10^9)
- **databricks_params** (object): Databricks-specific cluster configuration (only for Databricks sources)


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
    "/projects/{projectId}/warehouse-sources/imports/event-stream": {
      "post": {
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          }
        ],
        "operationId": "create-event-stream-import",
        "tags": [
          "Warehouse Imports"
        ],
        "summary": "Create an event stream import",
        "description": "Create a new warehouse import for event data.\n\nEvent stream imports sync event data from your warehouse table to Mixpanel.\nEach row in your table becomes an event in Mixpanel.\n\n## Sync Modes\n\n- **time_based**: Incrementally syncs new rows based on an insert time column\n- **mirror_mode**: Detects changes in the source table and mirrors them to Mixpanel\n- **full_sync**: Re-syncs all data on each run\n- **one_time**: Syncs data once and does not repeat\n\n## Required Column Mappings\n\nYou must specify either:\n- `event_name`: A static event name for all rows\n- `event_column_name`: The column containing the event name\n\nFor B2B projects, `company_column_name` is also required.\n\n## Scheduling\n\n- **run_every** (integer): Sync frequency in nanoseconds. Allowed values:\n  - Trigger via API: `0`\n  - Hourly: `3600000000000` (60 * 60 * 10^9)\n  - Daily: `86400000000000` (24 * 60 * 60 * 10^9)\n  - Weekly: `604800000000000` (7 * 24 * 60 * 60 * 10^9)\n- **databricks_params** (object): Databricks-specific cluster configuration (only for Databricks sources)\n",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreateEventStreamImportRequest"
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
                    },
                    "results": {
                      "$ref": "#/components/schemas/WarehouseImportDetail"
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
      "PropertyMappings": {
        "type": "object",
        "nullable": true,
        "additionalProperties": {
          "type": "string"
        }
      },
      "DatabricksClusterConfig": {
        "type": "object",
        "nullable": true,
        "additionalProperties": false,
        "properties": {
          "spark_version": {
            "type": "string",
            "description": "Spark runtime version (e.g., '15.4.x-scala2.12')"
          },
          "node_type_id": {
            "type": "string",
            "description": "Instance type for worker nodes (e.g., 'n2-standard-4' for GCP)"
          },
          "driver_node_type_id": {
            "type": "string",
            "nullable": true,
            "description": "Instance type for driver node (defaults to node_type_id if not set)"
          },
          "num_workers": {
            "type": "integer",
            "minimum": 0,
            "description": "Fixed number of worker nodes"
          },
          "autoscale": {
            "type": "object",
            "nullable": true,
            "additionalProperties": false,
            "description": "Autoscaling configuration (overrides num_workers if set)",
            "properties": {
              "min_workers": {
                "type": "integer",
                "minimum": 0
              },
              "max_workers": {
                "type": "integer",
                "minimum": 1
              }
            }
          },
          "spark_conf": {
            "type": "object",
            "nullable": true,
            "additionalProperties": {
              "type": "string"
            },
            "description": "Spark configuration key-value pairs"
          },
          "spark_env_vars": {
            "type": "object",
            "nullable": true,
            "additionalProperties": {
              "type": "string"
            },
            "description": "Environment variables (PYSPARK_PYTHON is always included)"
          },
          "data_security_mode": {
            "type": "string",
            "nullable": true,
            "enum": [
              "USER_ISOLATION",
              "SINGLE_USER",
              "NONE",
              "LEGACY_TABLE_ACL",
              "LEGACY_PASSTHROUGH",
              "LEGACY_SINGLE_USER",
              "LEGACY_SINGLE_USER_STANDARD"
            ],
            "description": "Data security mode for the cluster"
          },
          "single_user_name": {
            "type": "string",
            "nullable": true,
            "description": "Required if data_security_mode is SINGLE_USER"
          },
          "custom_tags": {
            "type": "object",
            "nullable": true,
            "additionalProperties": {
              "type": "string"
            },
            "description": "Custom tags (provider=mixpanel is always added)"
          },
          "policy_id": {
            "type": "string",
            "nullable": true,
            "description": "Cluster policy ID"
          },
          "instance_pool_id": {
            "type": "string",
            "nullable": true,
            "description": "Instance pool ID for worker nodes"
          },
          "driver_instance_pool_id": {
            "type": "string",
            "nullable": true,
            "description": "Instance pool ID for driver node"
          },
          "enable_elastic_disk": {
            "type": "boolean",
            "nullable": true,
            "description": "Enable autoscaling local storage"
          },
          "runtime_engine": {
            "type": "string",
            "nullable": true,
            "enum": [
              "STANDARD",
              "PHOTON"
            ],
            "description": "Runtime engine (STANDARD or PHOTON)"
          },
          "aws_attributes": {
            "type": "object",
            "nullable": true,
            "description": "AWS-specific cluster configuration"
          },
          "azure_attributes": {
            "type": "object",
            "nullable": true,
            "description": "Azure-specific cluster configuration"
          },
          "gcp_attributes": {
            "type": "object",
            "nullable": true,
            "description": "GCP-specific cluster configuration"
          },
          "init_scripts": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "object"
            },
            "description": "Cluster initialization scripts"
          }
        }
      },
      "DatabricksParams": {
        "type": "object",
        "nullable": true,
        "properties": {
          "export_cluster_config": {
            "$ref": "#/components/schemas/DatabricksClusterConfig"
          }
        }
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
      "WarehouseImportDetail": {
        "allOf": [
          {
            "$ref": "#/components/schemas/WarehouseImport"
          },
          {
            "type": "object",
            "properties": {
              "event_name": {
                "type": "string",
                "nullable": true
              },
              "event_column_name": {
                "type": "string",
                "nullable": true
              },
              "time_column_name": {
                "type": "string",
                "nullable": true
              },
              "user_column_name": {
                "type": "string",
                "nullable": true
              },
              "insert_time_column_name": {
                "type": "string",
                "nullable": true
              },
              "property_mappings": {
                "$ref": "#/components/schemas/PropertyMappings"
              },
              "group_key": {
                "type": "string",
                "nullable": true
              },
              "group_id_column": {
                "type": "string",
                "nullable": true
              },
              "databricks_params": {
                "$ref": "#/components/schemas/DatabricksParams"
              }
            }
          }
        ]
      },
      "CreateEventStreamImportRequest": {
        "type": "object",
        "required": [
          "import_type",
          "warehouse_source_id",
          "table_params",
          "time_column_name",
          "sync_mode"
        ],
        "properties": {
          "import_type": {
            "type": "string",
            "enum": [
              "event_stream"
            ]
          },
          "warehouse_source_id": {
            "type": "integer"
          },
          "table_params": {
            "$ref": "#/components/schemas/TableParams"
          },
          "event_name": {
            "type": "string"
          },
          "event_column_name": {
            "type": "string"
          },
          "time_column_name": {
            "type": "string"
          },
          "user_column_name": {
            "type": "string"
          },
          "company_column_name": {
            "type": "string",
            "description": "Required for B2B projects. The column containing the company identifier."
          },
          "device_column_name": {
            "type": "string",
            "nullable": true
          },
          "sync_mode": {
            "$ref": "#/components/schemas/SyncMode"
          },
          "run_every": {
            "$ref": "#/components/schemas/SyncFrequency"
          },
          "insert_time_column_name": {
            "type": "string",
            "nullable": true
          },
          "property_mappings": {
            "$ref": "#/components/schemas/PropertyMappings"
          },
          "databricks_params": {
            "$ref": "#/components/schemas/DatabricksParams"
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
  }
}
```