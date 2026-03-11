# Source: https://developers.activecampaign.com/reference/bulk-delete-accounts.md

# Bulk delete accounts

Delete an existing account

List accounts to delete by appending `?ids[]=ACCOUNT_ID` to the end of the url parameters.

**Example**: `https://{{yourAccountName}}.api-us1.com/api/3/accounts/bulk_delete?ids[]=123&ids[]=456&ids[]=789`

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "v3",
    "version": "3"
  },
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "variables": {
        "youraccountname": {
          "default": "youraccountname"
        }
      }
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "Api-Token",
        "in": "header",
        "x-default": ""
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/accounts/bulk_delete": {
      "delete": {
        "summary": "Bulk delete accounts",
        "description": "Delete an existing account",
        "operationId": "bulk-delete-accounts",
        "parameters": [
          {
            "name": "[]ids",
            "in": "query",
            "description": "An integer id of the account to be deleted",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"meta\": {\n        \"success\": true\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "meta": {
                      "type": "object",
                      "properties": {
                        "success": {
                          "type": "boolean",
                          "example": true,
                          "default": true
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": false,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```