# Source: https://help.cloudsmith.io/reference/metrics_entitlements_account_list.md

# View for listing entitlement token metrics, across an account.

View for listing entitlement token metrics, across an account.

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
    "/metrics/entitlements/{owner}/": {
      "get": {
        "operationId": "metrics_entitlements_account_list",
        "summary": "View for listing entitlement token metrics, across an account.",
        "description": "View for listing entitlement token metrics, across an account.",
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
            "name": "finish",
            "in": "query",
            "description": "Include metrics upto and including this UTC date or UTC datetime. For example '2020-12-31' or '2021-12-13T00:00:00Z'.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "start",
            "in": "query",
            "description": "Include metrics from and including this UTC date or UTC datetime. For example '2020-12-31' or '2021-12-13T00:00:00Z'.",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "tokens",
            "in": "query",
            "description": "A comma seperated list of tokens (slug perm) to include in the results.",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Retrieved the metrics for entitlements.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EntitlementUsageMetrics"
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
          "metrics"
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
      "CommonBandwidthMetricsValue": {
        "description": "Average bandwidth usage in the specified period, e.g. a day",
        "required": [
          "display",
          "value"
        ],
        "type": "object",
        "properties": {
          "display": {
            "title": "Display",
            "description": "Bandwidth usage value",
            "type": "string",
            "maxLength": 64,
            "minLength": 1
          },
          "units": {
            "title": "Units",
            "description": "Unit of measurement e.g. bytes",
            "type": "string",
            "default": "bytes",
            "minLength": 1
          },
          "value": {
            "title": "Value",
            "description": "Human readable version of display value",
            "type": "integer"
          }
        }
      },
      "CommonBandwidthMetrics": {
        "required": [
          "average",
          "highest",
          "lowest",
          "total"
        ],
        "type": "object",
        "properties": {
          "average": {
            "$ref": "#/components/schemas/CommonBandwidthMetricsValue"
          },
          "highest": {
            "$ref": "#/components/schemas/CommonBandwidthMetricsValue"
          },
          "lowest": {
            "$ref": "#/components/schemas/CommonBandwidthMetricsValue"
          },
          "total": {
            "$ref": "#/components/schemas/CommonBandwidthMetricsValue"
          }
        }
      },
      "CommonDownloadsMetricsValue": {
        "required": [
          "value"
        ],
        "type": "object",
        "properties": {
          "value": {
            "title": "Value",
            "type": "integer"
          }
        }
      },
      "CommonDownloadsMetrics": {
        "required": [
          "average",
          "highest",
          "lowest",
          "total"
        ],
        "type": "object",
        "properties": {
          "average": {
            "$ref": "#/components/schemas/CommonDownloadsMetricsValue"
          },
          "highest": {
            "$ref": "#/components/schemas/CommonDownloadsMetricsValue"
          },
          "lowest": {
            "$ref": "#/components/schemas/CommonDownloadsMetricsValue"
          },
          "total": {
            "$ref": "#/components/schemas/CommonDownloadsMetricsValue"
          }
        }
      },
      "CommonMetrics": {
        "required": [
          "bandwidth",
          "downloads"
        ],
        "type": "object",
        "properties": {
          "active": {
            "title": "Active",
            "description": "Number of packages with at least 1 download",
            "type": "integer",
            "default": 0
          },
          "bandwidth": {
            "$ref": "#/components/schemas/CommonBandwidthMetrics"
          },
          "downloads": {
            "$ref": "#/components/schemas/CommonDownloadsMetrics"
          },
          "inactive": {
            "title": "Inactive",
            "description": "Packages with zero downloads",
            "type": "integer",
            "default": 0
          },
          "total": {
            "title": "Total",
            "description": "Total number of packages in repo",
            "type": "integer",
            "default": 0
          }
        }
      },
      "EntitlementUsageMetrics": {
        "required": [
          "tokens"
        ],
        "type": "object",
        "properties": {
          "tokens": {
            "$ref": "#/components/schemas/CommonMetrics"
          }
        }
      }
    }
  }
}
```