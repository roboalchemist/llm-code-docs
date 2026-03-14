# Source: https://help.cloudsmith.io/reference/packages_status.md

# Get the synchronization status for a package.

Get the synchronization status for a package.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Cloudsmith API (v1)",
    "description": "The API to the Cloudsmith Service",
    "termsOfService": "https://help.cloudsmith.io",
    "contact": {
      "name": "Cloudsmith Support",
      "url": "https://help.cloudsmith.io",
      "email": "support@cloudsmith.io"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "v1"
  },
  "security": [
    {
      "apikey": []
    },
    {
      "basic": []
    }
  ],
  "paths": {
    "/packages/{owner}/{repo}/{identifier}/status/": {
      "get": {
        "operationId": "packages_status",
        "summary": "Get the synchronization status for a package.",
        "description": "Get the synchronization status for a package.",
        "responses": {
          "200": {
            "description": "Retrieved status for specified package.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PackageStatus"
                }
              }
            }
          },
          "400": {
            "description": "Request could not be processed (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Missing or invalid parameters (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          }
        },
        "tags": [
          "packages"
        ]
      },
      "parameters": [
        {
          "name": "owner",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "repo",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "identifier",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    }
  },
  "servers": [
    {
      "url": "https://api.cloudsmith.io"
    }
  ],
  "components": {
    "securitySchemes": {
      "apikey": {
        "type": "apiKey",
        "name": "X-Api-Key",
        "in": "header"
      },
      "basic": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "ErrorDetail": {
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "An extended message for the response.",
            "type": "string",
            "minLength": 1
          },
          "fields": {
            "title": "Fields",
            "description": "A Dictionary of related errors where key: Field and value: Array of Errors related to that field",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "minLength": 1
              }
            }
          }
        }
      },
      "PackageStatus": {
        "type": "object",
        "properties": {
          "is_cancellable": {
            "title": "Is cancellable",
            "type": "boolean",
            "readOnly": true
          },
          "is_copyable": {
            "title": "Is copyable",
            "type": "boolean",
            "readOnly": true
          },
          "is_deleteable": {
            "title": "Is deleteable",
            "type": "boolean",
            "readOnly": true
          },
          "is_downloadable": {
            "title": "Is downloadable",
            "type": "boolean",
            "readOnly": true
          },
          "is_moveable": {
            "title": "Is moveable",
            "type": "boolean",
            "readOnly": true
          },
          "is_quarantinable": {
            "title": "Is quarantinable",
            "type": "boolean",
            "readOnly": true
          },
          "is_quarantined": {
            "title": "Is quarantined",
            "type": "boolean",
            "readOnly": true
          },
          "is_resyncable": {
            "title": "Is resyncable",
            "type": "boolean",
            "readOnly": true
          },
          "is_security_scannable": {
            "title": "Is security scannable",
            "type": "boolean",
            "readOnly": true
          },
          "is_sync_awaiting": {
            "title": "Is sync awaiting",
            "type": "boolean",
            "readOnly": true
          },
          "is_sync_completed": {
            "title": "Is sync completed",
            "type": "boolean",
            "readOnly": true
          },
          "is_sync_failed": {
            "title": "Is sync failed",
            "type": "boolean",
            "readOnly": true
          },
          "is_sync_in_flight": {
            "title": "Is sync in flight",
            "type": "boolean",
            "readOnly": true
          },
          "is_sync_in_progress": {
            "title": "Is sync in progress",
            "type": "boolean",
            "readOnly": true
          },
          "self_url": {
            "title": "Self url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "stage": {
            "title": "Stage",
            "description": "The synchronisation (in progress) stage of the package.",
            "type": "integer",
            "enum": [
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12
            ],
            "readOnly": true
          },
          "stage_str": {
            "title": "Stage str",
            "type": "string",
            "readOnly": true
          },
          "stage_updated_at": {
            "title": "Stage updated at",
            "description": "The datetime the package stage was updated at.",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "status": {
            "title": "Status",
            "description": "The synchronisation status of the package.",
            "type": "integer",
            "enum": [
              1,
              2,
              3,
              4,
              5,
              6,
              7
            ],
            "readOnly": true
          },
          "status_reason": {
            "title": "Status reason",
            "description": "A textual description for the synchronous status reason (if any",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "status_str": {
            "title": "Status str",
            "type": "string",
            "readOnly": true
          },
          "status_updated_at": {
            "title": "Status updated at",
            "description": "The datetime the package status was updated at.",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "sync_finished_at": {
            "title": "Sync finished at",
            "description": "The datetime the package sync was finished at.",
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "sync_progress": {
            "title": "Sync progress",
            "description": "Synchronisation progress (from 0-100)",
            "type": "integer",
            "readOnly": true
          }
        }
      }
    }
  }
}
```