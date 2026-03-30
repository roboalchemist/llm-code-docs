# Source: https://developers.activecampaign.com/reference/bulk-import-status-info.md

# Bulk import status info

This endpoint returns a specific bulk import's status including the contact IDs of any newly created contacts, and emails of any contacts that failed to be created.

> 🧠 Add a short delay between creating a bulk import and calling for it's status
>
> If this endpoint is called *immediately* (less than a second) after a bulk import call, the `status` in the return may be `false` (a boolean), because the system has not yet set a status on the batch.

```json GET /import/info (Example RESPONSE)
{
  "status":"completed",
  "success":["123","124","125","126"],
  "failure":[
    "invalid.email@invalidDomain", 
    "invalid'character@example.com"
  ]
}
```

The `status` field may contain the following values:

| `Status`      | Description                                                                              |
| :------------ | :--------------------------------------------------------------------------------------- |
| `waiting`     | The import has been received but has not received a `uuid` and processing has not begun. |
| `claimed`     | The import batch has received a `uuid` but processing has not begun.                     |
| `active`      | The import batch is currently being processed.                                           |
| `completed`   | The import batch has completed processing.                                               |
| `failed`      | The import batch has failed and can no longer be retried.                                |
| `interrupted` | The import batch was interrupted due to failures and will not be retried.                |

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
    "/import/info": {
      "get": {
        "summary": "Bulk import status info",
        "description": "",
        "operationId": "bulk-import-status-info",
        "parameters": [
          {
            "name": "batchId",
            "in": "query",
            "schema": {
              "type": "string"
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
                    "value": "{\n  \"status\":\"completed\",\n  \"success\":[\"123\",\"124\",\"125\",\"126\"],\n  \"failure\":[\n    \"invalid.email@invalidDomain\", \n    \"invalid'character@example.com\"\n  ]\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": {
                      "type": "string",
                      "example": "completed"
                    },
                    "success": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "123"
                      }
                    },
                    "failure": {
                      "type": "array",
                      "items": {
                        "type": "string",
                        "example": "invalid.email@invalidDomain"
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
                  "Bad Request": {
                    "value": "{\"success\":0,\"message\":\"'batchId' is a required field.\"}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "integer",
                      "example": 0,
                      "default": 0
                    },
                    "message": {
                      "type": "string",
                      "example": "'batchId' is a required field."
                    }
                  }
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