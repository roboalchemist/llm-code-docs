# Source: https://posthog.com/docs/open-api-spec/warehouse_saved_queries_list.md

# warehouse_saved_queries_list

## OpenAPI

```json GET /api/projects/{project_id}/warehouse_saved_queries/
{
  "paths": {
    "/api/projects/{project_id}/warehouse_saved_queries/": {
      "get": {
        "operationId": "warehouse_saved_queries_list",
        "description": "Create, Read, Update and Delete Warehouse Tables.",
        "parameters": [
          {
            "name": "page",
            "required": false,
            "in": "query",
            "description": "A page number within the paginated result set.",
            "schema": {
              "type": "integer"
            }
          },
          {
            "in": "path",
            "name": "project_id",
            "required": true,
            "schema": {
              "type": "string"
            },
            "description": "Project ID of the project you're trying to access. To find the ID of the project, make a call to /api/projects/."
          },
          {
            "name": "search",
            "required": false,
            "in": "query",
            "description": "A search term.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "tags": [
          "data_warehouse",
          "warehouse_saved_queries"
        ],
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "warehouse_view:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PaginatedDataWarehouseSavedQueryMinimalList"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "data_warehouse"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "PaginatedDataWarehouseSavedQueryMinimalList": {
        "type": "object",
        "required": [
          "count",
          "results"
        ],
        "properties": {
          "count": {
            "type": "integer",
            "example": 123
          },
          "next": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?page=4"
          },
          "previous": {
            "type": "string",
            "nullable": true,
            "format": "uri",
            "example": "http://api.example.org/accounts/?page=2"
          },
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/DataWarehouseSavedQueryMinimal"
            }
          }
        }
      },
      "DataWarehouseSavedQueryMinimal": {
        "type": "object",
        "description": "Lightweight serializer for list views - excludes large query field to reduce memory usage.",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "deleted": {
            "type": "boolean",
            "readOnly": true,
            "nullable": true
          },
          "name": {
            "type": "string",
            "readOnly": true
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
          "deleted",
          "id",
          "is_materialized",
          "last_run_at",
          "latest_error",
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
