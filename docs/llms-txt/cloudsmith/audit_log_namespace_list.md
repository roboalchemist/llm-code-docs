# Source: https://help.cloudsmith.io/reference/audit_log_namespace_list.md

# Lists audit log entries for a specific namespace.

Lists audit log entries for a specific namespace.

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
    "/audit-log/{owner}/": {
      "get": {
        "operationId": "audit_log_namespace_list",
        "summary": "Lists audit log entries for a specific namespace.",
        "description": "Lists audit log entries for a specific namespace.",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "description": "A page number within the paginated result set.",
            "required": false,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "page_size",
            "in": "query",
            "description": "Number of results to return per page.",
            "required": false,
            "schema": {
              "type": "integer"
            }
          },
          {
            "name": "query",
            "in": "query",
            "description": "A search term for querying events, actors, or timestamps of log records.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieved the list of audit log entries",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/NamespaceAuditLog"
                  }
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
          "402": {
            "description": "Audit logs are not active; upgrade your account!",
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
          "audit-log"
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
      "GeoIpLocation": {
        "required": [
          "city",
          "continent",
          "country",
          "postal_code"
        ],
        "type": "object",
        "properties": {
          "city": {
            "title": "City",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "continent": {
            "title": "Continent",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "country": {
            "title": "Country",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "country_code": {
            "title": "Country code",
            "type": "string",
            "readOnly": true
          },
          "latitude": {
            "title": "Latitude",
            "type": "string",
            "format": "decimal",
            "nullable": true
          },
          "longitude": {
            "title": "Longitude",
            "type": "string",
            "format": "decimal",
            "nullable": true
          },
          "postal_code": {
            "title": "Postal code",
            "type": "string",
            "minLength": 1,
            "nullable": true
          }
        }
      },
      "NamespaceAuditLog": {
        "required": [
          "actor",
          "actor_ip_address",
          "actor_location",
          "actor_slug_perm",
          "context",
          "event",
          "event_at",
          "object",
          "object_kind",
          "object_slug_perm",
          "target",
          "target_kind"
        ],
        "type": "object",
        "properties": {
          "actor": {
            "title": "Actor",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "actor_ip_address": {
            "title": "Actor ip address",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "actor_kind": {
            "title": "Actor kind",
            "type": "string",
            "readOnly": true
          },
          "actor_location": {
            "$ref": "#/components/schemas/GeoIpLocation"
          },
          "actor_slug_perm": {
            "title": "Actor slug perm",
            "type": "string",
            "minLength": 1,
            "nullable": true
          },
          "actor_url": {
            "title": "Actor url",
            "type": "string",
            "format": "uri",
            "readOnly": true,
            "nullable": true
          },
          "context": {
            "title": "Context",
            "type": "string",
            "minLength": 1
          },
          "event": {
            "title": "Event",
            "type": "string",
            "minLength": 1
          },
          "event_at": {
            "title": "Event at",
            "type": "string",
            "format": "date-time"
          },
          "object": {
            "title": "Object",
            "type": "string",
            "minLength": 1
          },
          "object_kind": {
            "title": "Object kind",
            "type": "string",
            "minLength": 1
          },
          "object_slug_perm": {
            "title": "Object slug perm",
            "type": "string",
            "minLength": 1
          },
          "target": {
            "title": "Target",
            "type": "string",
            "minLength": 1
          },
          "target_kind": {
            "title": "Target kind",
            "type": "string",
            "minLength": 1
          },
          "target_slug_perm": {
            "title": "Target slug perm",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "maxLength": 24,
            "nullable": true
          },
          "uuid": {
            "title": "Uuid",
            "type": "string",
            "format": "uuid",
            "readOnly": true
          }
        }
      }
    }
  }
}
```