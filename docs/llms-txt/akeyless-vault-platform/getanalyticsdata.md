# Source: https://docs.akeyless.io/reference/getanalyticsdata.md

# /get-analytics-data

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "The purpose of this application is to provide access to Akeyless API.",
    "title": "Akeyless API",
    "contact": {
      "name": "Akeyless",
      "url": "http://akeyless.io",
      "email": "support@akeyless.io"
    },
    "version": "3.0"
  },
  "paths": {
    "/get-analytics-data": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "getAnalyticsData",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/getAnalyticsData"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/getAnalyticsDataResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        }
      }
    }
  },
  "servers": [
    {
      "url": "https://api.akeyless.io"
    }
  ],
  "components": {
    "responses": {
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
            }
          }
        }
      },
      "getAnalyticsDataResponse": {
        "description": "getAnalyticsDataResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/AllAnalyticsData"
            }
          }
        }
      }
    },
    "schemas": {
      "AllAnalyticsData": {
        "type": "object",
        "properties": {
          "analytics_data": {
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            },
            "x-go-name": "AnalyticsData"
          },
          "certificates_expiry_data": {
            "$ref": "#/components/schemas/CertificateAnalyticAggregation"
          },
          "clients_usage_reports": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/ClientsUsageReport"
            },
            "x-go-name": "ClientsUsageReports"
          },
          "date_updated": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "DateUpdated"
          },
          "usage_reports": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/components/schemas/UsageReportSummary"
            },
            "x-go-name": "UsageReports"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "CertificateAnalyticAggregation": {
        "type": "object",
        "properties": {
          "account_id": {
            "type": "string",
            "x-go-name": "AccountId"
          },
          "ca_counts": {
            "type": "object",
            "additionalProperties": {
              "type": "integer",
              "format": "int32"
            },
            "x-go-name": "CaCounts"
          },
          "risk_counts": {
            "type": "object",
            "additionalProperties": {
              "type": "integer",
              "format": "int32"
            },
            "x-go-name": "RiskCounts"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/microservices/common/certificate_analytics"
      },
      "ClientUsageInfo": {
        "type": "object",
        "properties": {
          "access_id": {
            "type": "string",
            "x-go-name": "AccessId"
          },
          "access_type": {
            "type": "string",
            "x-go-name": "AccessType"
          },
          "auth_method_name": {
            "type": "string",
            "x-go-name": "AuthMethodName"
          },
          "client_unique_id": {
            "type": "string",
            "x-go-name": "ClientUniqueId"
          },
          "exceeded_clients": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ExceededClients"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/logan"
      },
      "ClientsUsageReport": {
        "type": "object",
        "properties": {
          "account_id": {
            "type": "string",
            "x-go-name": "AccountID"
          },
          "clients": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ClientUsageInfo"
            },
            "x-go-name": "Clients"
          },
          "product": {
            "$ref": "#/components/schemas/Product"
          },
          "time": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "Time"
          },
          "total_clients": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TotalClients"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/logan"
      },
      "JSONError": {
        "type": "object",
        "title": "JSONError wraps an error with JSON object.",
        "properties": {
          "error": {
            "type": "string",
            "x-go-name": "Err"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client"
      },
      "Product": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "UsageReportSummary": {
        "type": "object",
        "properties": {
          "clients_by_auth_method_types": {
            "type": "object",
            "additionalProperties": {
              "type": "integer",
              "format": "int64"
            },
            "x-go-name": "ClientsByAuthMethodTypes"
          },
          "product": {
            "$ref": "#/components/schemas/Product"
          },
          "secrets_by_types": {
            "type": "object",
            "additionalProperties": {
              "type": "integer",
              "format": "int64"
            },
            "x-go-name": "SecretsByTypes"
          },
          "time": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "Time"
          },
          "total_clients": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TotalClients"
          },
          "total_secrets": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TotalSecrets"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/akeyless-api/logan"
      },
      "getAnalyticsData": {
        "type": "object",
        "title": "getAnalyticsData is a command that returns analytics information.",
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```