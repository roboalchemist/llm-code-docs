# Source: https://posthog.com/docs/open-api-spec/proxy_records_create.md

# proxy_records_create

## OpenAPI

```json POST /api/organizations/{organization_id}/proxy_records/
{
  "paths": {
    "/api/organizations/{organization_id}/proxy_records/": {
      "post": {
        "operationId": "proxy_records_create",
        "description": "Create a new managed reverse proxy. Provide the domain you want to proxy through. The response includes the CNAME target you need to add as a DNS record. Once the CNAME is configured, the proxy will be automatically verified and provisioned.",
        "parameters": [
          {
            "in": "path",
            "name": "organization_id",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true
          }
        ],
        "tags": [
          "reverse_proxy",
          "proxy_records"
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/ProxyRecord"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/ProxyRecord"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/ProxyRecord"
              }
            }
          },
          "required": true
        },
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "organization:write"
            ]
          }
        ],
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ProxyRecord"
                }
              }
            },
            "description": ""
          }
        },
        "x-explicit-tags": [
          "reverse_proxy"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "ProxyRecord": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "readOnly": true,
            "description": "Unique identifier for the proxy record."
          },
          "domain": {
            "type": "string",
            "description": "The custom domain to proxy through, e.g. 'e.example.com'. Must be a valid subdomain you control."
          },
          "target_cname": {
            "type": "string",
            "readOnly": true,
            "description": "The CNAME target to add as a DNS record for your domain. Point your domain's CNAME to this value."
          },
          "status": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ProxyRecordStatusEnum"
              }
            ],
            "readOnly": true,
            "description": "Current provisioning status. Values: waiting (DNS verification pending), issuing (SSL certificate being issued), valid (proxy is live and working), warning (proxy has issues but is operational), erroring (proxy setup failed), deleting (removal in progress), timed_out (DNS verification timed out).\n\n* `waiting` - Waiting\n* `issuing` - Issuing\n* `valid` - Valid\n* `warning` - Warning\n* `erroring` - Erroring\n* `deleting` - Deleting\n* `timed_out` - Timed Out"
          },
          "message": {
            "type": "string",
            "readOnly": true,
            "nullable": true,
            "description": "Human-readable status message with details about errors or warnings, if any."
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "description": "When this proxy record was created."
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "description": "When this proxy record was last updated."
          },
          "created_by": {
            "type": "integer",
            "readOnly": true,
            "description": "ID of the user who created this proxy record."
          }
        },
        "required": [
          "created_at",
          "created_by",
          "domain",
          "id",
          "message",
          "status",
          "target_cname",
          "updated_at"
        ]
      },
      "ProxyRecordStatusEnum": {
        "enum": [
          "waiting",
          "issuing",
          "valid",
          "warning",
          "erroring",
          "deleting",
          "timed_out"
        ],
        "type": "string",
        "description": "* `waiting` - Waiting\n* `issuing` - Issuing\n* `valid` - Valid\n* `warning` - Warning\n* `erroring` - Erroring\n* `deleting` - Deleting\n* `timed_out` - Timed Out"
      }
    }
  }
}
```
