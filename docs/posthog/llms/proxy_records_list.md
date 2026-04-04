# Source: https://posthog.com/docs/open-api-spec/proxy_records_list.md

# proxy_records_list

## OpenAPI

```json GET /api/organizations/{organization_id}/proxy_records/
{
  "paths": {
    "/api/organizations/{organization_id}/proxy_records/": {
      "get": {
        "operationId": "proxy_records_list",
        "description": "List all reverse proxies configured for the organization. Returns proxy records along with the maximum number allowed by the current plan.",
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
        "security": [
          {
            "PersonalAPIKeyAuth": [
              "organization:read"
            ]
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/ProxyRecordListResponse"
                  }
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
      "ProxyRecordListResponse": {
        "type": "object",
        "properties": {
          "results": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ProxyRecord"
            }
          },
          "max_proxy_records": {
            "type": "integer",
            "description": "Maximum number of proxy records allowed for this organization's current plan."
          }
        },
        "required": [
          "max_proxy_records",
          "results"
        ]
      },
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
