# Source: https://posthog.com/docs/open-api-spec/environments_hog_functions_invocations_create.md

# environments_hog_functions_invocations_create

## OpenAPI

```json POST /api/environments/{environment_id}/hog_functions/{id}/invocations/
{
  "paths": {
    "/api/environments/{environment_id}/hog_functions/{id}/invocations/": {
      "post": {
        "operationId": "environments_hog_functions_invocations_create",
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
            "description": "A UUID string identifying this hog function.",
            "required": true
          }
        ],
        "tags": [
          "hog_functions",
          "hog_functions"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/HogFunctionInvocation"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/HogFunctionInvocation"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/HogFunctionInvocation"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "hog_function:write"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HogFunctionInvocation"
                }
              }
            },
            "description": ""
          }
        },
        "deprecated": true,
        "x-explicit-tags": [
          "hog_functions"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "HogFunctionInvocation": {
        "type": "object",
        "properties": {
          "configuration": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HogFunction"
              }
            ],
            "writeOnly": true,
            "description": "Full function configuration to test."
          },
          "globals": {
            "type": "object",
            "additionalProperties": {},
            "writeOnly": true,
            "description": "Mock global variables available during test invocation."
          },
          "clickhouse_event": {
            "type": "object",
            "additionalProperties": {},
            "writeOnly": true,
            "description": "Mock ClickHouse event data to test the function with."
          },
          "mock_async_functions": {
            "type": "boolean",
            "writeOnly": true,
            "default": true,
            "description": "When true (default), async functions like fetch() are simulated."
          },
          "status": {
            "type": "string",
            "readOnly": true,
            "description": "Invocation result status."
          },
          "logs": {
            "type": "array",
            "items": {},
            "readOnly": true,
            "description": "Execution logs from the test invocation."
          },
          "invocation_id": {
            "type": "string",
            "nullable": true,
            "description": "Optional invocation ID for correlation."
          }
        },
        "required": [
          "configuration",
          "logs",
          "status"
        ]
      },
      "HogFunction": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true
          },
          "type": {
            "nullable": true,
            "description": "Function type: destination, site_destination, internal_destination, source_webhook, warehouse_source_webhook, site_app, or transformation.\n\n* `destination` - Destination\n* `site_destination` - Site Destination\n* `internal_destination` - Internal Destination\n* `source_webhook` - Source Webhook\n* `warehouse_source_webhook` - Warehouse Source Webhook\n* `site_app` - Site App\n* `transformation` - Transformation",
            "oneOf": [
              {
                "$ref": "#/components/schemas/HogFunctionTypeEnum"
              },
              {
                "$ref": "#/components/schemas/NullEnum"
              }
            ]
          },
          "name": {
            "type": "string",
            "nullable": true,
            "description": "Display name for the function.",
            "maxLength": 400
          },
          "description": {
            "type": "string",
            "description": "Human-readable description of what this function does."
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
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
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "enabled": {
            "type": "boolean",
            "description": "Whether the function is active and processing events."
          },
          "deleted": {
            "type": "boolean",
            "writeOnly": true,
            "description": "Soft-delete flag. Set to true to archive the function."
          },
          "hog": {
            "type": "string",
            "description": "Source code. Hog language for most types; TypeScript for site_destination and site_app."
          },
          "bytecode": {
            "readOnly": true,
            "nullable": true
          },
          "transpiled": {
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "inputs_schema": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/InputsSchemaItem"
            },
            "description": "Schema defining the configurable input parameters for this function."
          },
          "inputs": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/InputsItem"
            },
            "description": "Values for each input defined in inputs_schema."
          },
          "filters": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HogFunctionFilters"
              }
            ],
            "description": "Event filters that control which events trigger this function."
          },
          "masking": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HogFunctionMasking"
              }
            ],
            "nullable": true,
            "description": "PII masking configuration with TTL, threshold, and hash expression."
          },
          "mappings": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Mappings"
            },
            "nullable": true,
            "description": "Event-to-destination field mappings. Only for destination and site_destination types."
          },
          "icon_url": {
            "type": "string",
            "nullable": true,
            "description": "URL for the function's icon displayed in the UI."
          },
          "template": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HogFunctionTemplate"
              }
            ],
            "readOnly": true
          },
          "template_id": {
            "type": "string",
            "writeOnly": true,
            "nullable": true,
            "description": "ID of the template to create this function from.",
            "maxLength": 400
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HogFunctionStatus"
              }
            ],
            "readOnly": true,
            "nullable": true
          },
          "execution_order": {
            "type": "integer",
            "maximum": 32767,
            "minimum": 0,
            "nullable": true,
            "description": "Execution priority for transformations. Lower values run first."
          },
          "_create_in_folder": {
            "type": "string",
            "writeOnly": true,
            "title": " create in folder"
          },
          "batch_export_id": {
            "type": "string",
            "format": "uuid",
            "nullable": true,
            "readOnly": true
          }
        },
        "required": [
          "batch_export_id",
          "bytecode",
          "created_at",
          "created_by",
          "id",
          "status",
          "template",
          "transpiled",
          "updated_at"
        ]
      },
      "HogFunctionTypeEnum": {
        "enum": [
          "destination",
          "site_destination",
          "internal_destination",
          "source_webhook",
          "warehouse_source_webhook",
          "site_app",
          "transformation"
        ],
        "type": "string",
        "description": "* `destination` - Destination\n* `site_destination` - Site Destination\n* `internal_destination` - Internal Destination\n* `source_webhook` - Source Webhook\n* `warehouse_source_webhook` - Warehouse Source Webhook\n* `site_app` - Site App\n* `transformation` - Transformation"
      },
      "NullEnum": {
        "enum": [
          null
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
      "InputsSchemaItem": {
        "type": "object",
        "properties": {
          "type": {
            "$ref": "#/components/schemas/InputsSchemaItemTypeEnum"
          },
          "key": {
            "type": "string"
          },
          "label": {
            "type": "string"
          },
          "choices": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "required": {
            "type": "boolean",
            "default": false
          },
          "default": {},
          "secret": {
            "type": "boolean",
            "default": false
          },
          "hidden": {
            "type": "boolean",
            "default": false
          },
          "description": {
            "type": "string"
          },
          "integration": {
            "type": "string"
          },
          "integration_key": {
            "type": "string"
          },
          "requires_field": {
            "type": "string"
          },
          "integration_field": {
            "type": "string"
          },
          "requiredScopes": {
            "type": "string"
          },
          "templating": {
            "$ref": "#/components/schemas/InputsSchemaItemTemplatingEnum"
          }
        },
        "required": [
          "key",
          "type"
        ]
      },
      "InputsItem": {
        "type": "object",
        "properties": {
          "value": {},
          "templating": {
            "$ref": "#/components/schemas/InputsItemTemplatingEnum"
          },
          "bytecode": {
            "type": "array",
            "items": {},
            "readOnly": true
          },
          "order": {
            "type": "integer",
            "readOnly": true
          },
          "transpiled": {
            "readOnly": true
          }
        },
        "required": [
          "bytecode",
          "order",
          "transpiled"
        ]
      },
      "HogFunctionFilters": {
        "type": "object",
        "properties": {
          "source": {
            "allOf": [
              {
                "$ref": "#/components/schemas/HogFunctionFiltersSourceEnum"
              }
            ],
            "default": "events"
          },
          "actions": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "events": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "data_warehouse": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "properties": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": {}
            }
          },
          "bytecode": {
            "nullable": true
          },
          "transpiled": {},
          "filter_test_accounts": {
            "type": "boolean"
          },
          "bytecode_error": {
            "type": "string"
          }
        }
      },
      "HogFunctionMasking": {
        "type": "object",
        "properties": {
          "ttl": {
            "type": "integer",
            "maximum": 86400,
            "minimum": 60,
            "description": "Time-to-live in seconds for the masking cache (60–86400)."
          },
          "threshold": {
            "type": "integer",
            "nullable": true,
            "description": "Optional threshold count before masking applies."
          },
          "hash": {
            "type": "string",
            "description": "Hog expression used to compute the masking hash."
          },
          "bytecode": {
            "nullable": true,
            "description": "Compiled bytecode for the hash expression. Auto-generated."
          }
        },
        "required": [
          "hash",
          "ttl"
        ]
      },
      "Mappings": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "inputs_schema": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/InputsSchemaItem"
            }
          },
          "inputs": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/InputsItem"
            }
          },
          "filters": {
            "$ref": "#/components/schemas/HogFunctionFilters"
          }
        }
      },
      "HogFunctionTemplate": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique template identifier (e.g. 'template-slack')."
          },
          "name": {
            "type": "string",
            "description": "Display name of the template.",
            "maxLength": 400
          },
          "description": {
            "type": "string",
            "nullable": true,
            "description": "What this template does."
          },
          "code": {
            "type": "string",
            "description": "Source code of the template."
          },
          "code_language": {
            "type": "string",
            "description": "Programming language: 'hog' or 'javascript'.",
            "maxLength": 20
          },
          "inputs_schema": {
            "description": "Schema defining configurable inputs for functions created from this template."
          },
          "type": {
            "type": "string",
            "description": "Function type this template creates.",
            "maxLength": 50
          },
          "status": {
            "type": "string",
            "description": "Lifecycle status: alpha, beta, stable, deprecated, or hidden.",
            "maxLength": 20
          },
          "category": {
            "description": "Category tags for organizing templates."
          },
          "free": {
            "type": "boolean",
            "description": "Whether available on free plans."
          },
          "icon_url": {
            "type": "string",
            "nullable": true,
            "description": "URL for the template's icon."
          },
          "filters": {
            "nullable": true,
            "description": "Default event filters."
          },
          "masking": {
            "nullable": true,
            "description": "Default PII masking configuration."
          },
          "mapping_templates": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/HogFunctionMappingTemplate"
            },
            "nullable": true,
            "description": "Pre-defined mapping configurations for destination templates."
          }
        },
        "required": [
          "code",
          "id",
          "inputs_schema",
          "name",
          "type"
        ]
      },
      "HogFunctionStatus": {
        "type": "object",
        "properties": {
          "state": {
            "$ref": "#/components/schemas/HogFunctionStatusStateEnum"
          },
          "tokens": {
            "type": "integer"
          }
        },
        "required": [
          "state",
          "tokens"
        ]
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
      },
      "InputsSchemaItemTypeEnum": {
        "enum": [
          "string",
          "number",
          "boolean",
          "dictionary",
          "choice",
          "json",
          "integration",
          "integration_field",
          "email",
          "native_email",
          "posthog_assignee",
          "posthog_ticket_tags"
        ],
        "type": "string",
        "description": "* `string` - string\n* `number` - number\n* `boolean` - boolean\n* `dictionary` - dictionary\n* `choice` - choice\n* `json` - json\n* `integration` - integration\n* `integration_field` - integration_field\n* `email` - email\n* `native_email` - native_email\n* `posthog_assignee` - posthog_assignee\n* `posthog_ticket_tags` - posthog_ticket_tags"
      },
      "InputsSchemaItemTemplatingEnum": {
        "enum": [
          true,
          false,
          "hog",
          "liquid"
        ],
        "description": "* `True` - True\n* `False` - False\n* `hog` - hog\n* `liquid` - liquid"
      },
      "InputsItemTemplatingEnum": {
        "enum": [
          "hog",
          "liquid"
        ],
        "type": "string",
        "description": "* `hog` - hog\n* `liquid` - liquid"
      },
      "HogFunctionFiltersSourceEnum": {
        "enum": [
          "events",
          "person-updates",
          "data-warehouse-table"
        ],
        "type": "string",
        "description": "* `events` - events\n* `person-updates` - person-updates\n* `data-warehouse-table` - data-warehouse-table"
      },
      "HogFunctionMappingTemplate": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "Name of this mapping template."
          },
          "include_by_default": {
            "type": "boolean",
            "nullable": true,
            "description": "Whether this mapping is enabled by default."
          },
          "filters": {
            "nullable": true,
            "description": "Event filters specific to this mapping."
          },
          "inputs": {
            "nullable": true,
            "description": "Input values specific to this mapping."
          },
          "inputs_schema": {
            "nullable": true,
            "description": "Additional input schema fields specific to this mapping."
          }
        },
        "required": [
          "name"
        ]
      },
      "HogFunctionStatusStateEnum": {
        "enum": [
          0,
          1,
          2,
          3,
          11,
          12
        ],
        "type": "integer",
        "description": "* `0` - 0\n* `1` - 1\n* `2` - 2\n* `3` - 3\n* `11` - 11\n* `12` - 12"
      }
    }
  }
}
```
