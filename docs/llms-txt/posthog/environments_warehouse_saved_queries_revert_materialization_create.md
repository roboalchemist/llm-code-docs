# Source: https://posthog.com/docs/open-api-spec/environments_warehouse_saved_queries_revert_materialization_create.md

# environments_warehouse_saved_queries_revert_materialization_create

## OpenAPI

```json POST /api/environments/{environment_id}/warehouse_saved_queries/{id}/revert_materialization/
{
  "paths": {
    "/api/environments/{environment_id}/warehouse_saved_queries/{id}/revert_materialization/": {
      "post": {
        "operationId": "environments_warehouse_saved_queries_revert_materialization_create",
        "description": "Undo materialization, revert back to the original view.\n(i.e. delete the materialized table and the schedule)",
        "parameters": [
          {
            "in": "path",
            "name": "environment_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Deprecated. Use /api/projects/{project_id}/ instead."
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "description": "A UUID string identifying this data warehouse saved query.",
            "required": true
          }
        ],
        "tags": [
          "data_warehouse",
          "warehouse_saved_queries"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/DataWarehouseSavedQuery"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/DataWarehouseSavedQuery"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/DataWarehouseSavedQuery"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "warehouse_view:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DataWarehouseSavedQuery"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "data_warehouse"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "DataWarehouseSavedQuery": {
        "type": "object",
        "description": "Shared methods for DataWarehouseSavedQuery serializers.\n\nThis mixin is intended to be used with serializers.ModelSerializer subclasses.",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "deleted": {
            "type": "boolean",
            "nullable": true
          },
          "name": {
            "type": "string",
            "maxLength": 128
          },
          "query": {
            "nullable": true,
            "description": "HogQL query"
          },
          "created_by": {
            "allOf": [
              {
                "$ref": "#/components/schemas/UserBasic"
              }
            ],
            "readOnly": true
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "sync_frequency": {
            "type": "string",
            "readOnly": true
          },
          "columns": {
            "type": "string",
            "readOnly": true
          },
          "status": {
            "readOnly": true,
            "nullable": true,
            "description": "The status of when this SavedQuery last ran.\n\n* `Cancelled` - Cancelled\n* `Modified` - Modified\n* `Completed` - Completed\n* `Failed` - Failed\n* `Running` - Running",
            "oneOf": [
              {
                "$ref": "#/components/schemas/StatusD5cEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "last_run_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "readOnly": true
          },
          "managed_viewset_kind": {
            "type": "string",
            "readOnly": true
          },
          "latest_error": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "edited_history_id": {
            "type": "string",
            "writeOnly": true,
            "nullable": true
          },
          "latest_history_id": {
            "type": "string",
            "readOnly": true
          },
          "soft_update": {
            "type": "boolean",
            "writeOnly": true,
            "nullable": true
          },
          "is_materialized": {
            "type": "boolean",
            "readOnly": true,
            "nullable": true
          },
          "origin": {
            "readOnly": true,
            "nullable": true,
            "description": "Where this SavedQuery is created.\n\n* `data_warehouse` - Data Warehouse\n* `endpoint` - Endpoint\n* `managed_viewset` - Managed Viewset",
            "oneOf": [
              {
                "$ref": "#/components/schemas/OriginEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          }
        },
        "required": [
          "columns",
          "created_at",
          "created_by",
          "id",
          "is_materialized",
          "last_run_at",
          "latest_error",
          "latest_history_id",
          "managed_viewset_kind",
          "name",
          "origin",
          "status",
          "sync_frequency"
        ]
      },
      "UserBasic": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "uuid": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "distinct_id": {
            "type": "string",
            "nullable": true,
            "maxLength": 200
          },
          "first_name": {
            "type": "string",
            "maxLength": 150
          },
          "last_name": {
            "type": "string",
            "maxLength": 150
          },
          "email": {
            "type": "string",
            "format": "email",
            "title": "Email address",
            "maxLength": 254
          },
          "is_email_verified": {
            "type": "boolean",
            "nullable": true
          },
          "hedgehog_config": {
            "type": "object",
            "additionalProperties": {},
            "nullable": true,
            "readOnly": true
          },
          "role_at_organization": {
            "nullable": true,
            "oneOf": [
              {
                "$ref": "#/components/schemas/RoleAtOrganizationEnum"
              },
              {
                "$ref": "#/components/schemas/BlankEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          }
        },
        "required": [
          "email",
          "hedgehog_config",
          "id",
          "uuid"
        ]
      },
      "StatusD5cEnum": {
        "enum": [
          "Cancelled",
          "Modified",
          "Completed",
          "Failed",
          "Running"
        ],
        "type": "string",
        "description": "* `Cancelled` - Cancelled\n* `Modified` - Modified\n* `Completed` - Completed\n* `Failed` - Failed\n* `Running` - Running"
      },
      "NullEnum": {
        "enum": [
          null
        ]
      },
      "OriginEnum": {
        "enum": [
          "data_warehouse",
          "endpoint",
          "managed_viewset"
        ],
        "type": "string",
        "description": "* `data_warehouse` - Data Warehouse\n* `endpoint` - Endpoint\n* `managed_viewset` - Managed Viewset"
      },
      "RoleAtOrganizationEnum": {
        "enum": [
          "engineering",
          "data",
          "product",
          "founder",
          "leadership",
          "marketing",
          "sales",
          "other"
        ],
        "type": "string",
        "description": "* `engineering` - Engineering\n* `data` - Data\n* `product` - Product Management\n* `founder` - Founder\n* `leadership` - Leadership\n* `marketing` - Marketing\n* `sales` - Sales / Success\n* `other` - Other"
      },
      "BlankEnum": {
        "enum": [
          ""
        ]
      }
    }
  }
}
```
