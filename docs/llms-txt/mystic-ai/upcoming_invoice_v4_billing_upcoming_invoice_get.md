# Source: https://docs.mystic.ai/reference/upcoming_invoice_v4_billing_upcoming_invoice_get.md

# Upcoming Invoice

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Mystic API",
    "version": "4.0.0"
  },
  "servers": [
    {
      "url": "https://www.mystic.ai"
    }
  ],
  "paths": {
    "/v4/billing/upcoming-invoice": {
      "get": {
        "tags": [
          "Billing"
        ],
        "summary": "Upcoming Invoice",
        "operationId": "upcoming_invoice_v4_billing_upcoming_invoice_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/GetUpcomingInvoice"
                }
              }
            }
          }
        },
        "security": [
          {
            "HTTPBearer": []
          },
          {
            "APIKeyCookie": []
          }
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "GetUpcomingInvoice": {
        "properties": {
          "credits_used": {
            "type": "integer",
            "title": "Credits Used"
          },
          "credits_total": {
            "type": "integer",
            "title": "Credits Total"
          },
          "start_date": {
            "type": "string",
            "format": "date-time",
            "title": "Start Date"
          },
          "end_date": {
            "type": "string",
            "format": "date-time",
            "title": "End Date"
          }
        },
        "type": "object",
        "required": [
          "credits_used",
          "credits_total",
          "start_date",
          "end_date"
        ],
        "title": "GetUpcomingInvoice",
        "description": "Details about a customer's upcoming invoice, including free credit usage in\ncents and billing period"
      }
    },
    "securitySchemes": {
      "HTTPBearer": {
        "type": "http",
        "scheme": "bearer"
      },
      "APIKeyCookie": {
        "type": "apiKey",
        "in": "cookie",
        "name": "access-token"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": true
  },
  "_id": {
    "buffer": {
      "0": 102,
      "1": 30,
      "2": 82,
      "3": 233,
      "4": 116,
      "5": 201,
      "6": 20,
      "7": 0,
      "8": 75,
      "9": 32,
      "10": 117,
      "11": 11
    }
  }
}
```