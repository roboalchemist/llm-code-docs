# Source: https://developer.mixpanel.com/reference/list-lookup-tables.md

# List Lookup Tables

Get a list of Lookup Tables defined in the project.

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Ingestion API",
    "description": "APIs allowing for event-based tracking and user profile handling.",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "1.0.0",
    "contact": {
      "url": "https://mixpanel.com/get-support"
    }
  },
  "servers": [
    {
      "url": "https://{region}.mixpanel.com",
      "description": "Mixpanel's data collection server.",
      "variables": {
        "region": {
          "default": "api",
          "enum": [
            "api",
            "api-eu",
            "api-in"
          ],
          "description": "The server location to be used:\n  * `api` - The default (US) servers used for most projects\n  * `api-eu` - EU servers if you are enrolled in EU Data Residency\n  * `api-in` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "tags": [
    {
      "name": "Lookup Tables",
      "description": "Enrich existing event and profile properties"
    }
  ],
  "paths": {
    "/lookup-tables": {
      "get": {
        "operationId": "list-lookup-tables",
        "tags": [
          "Lookup Tables"
        ],
        "security": [
          {
            "ServiceAccount": []
          }
        ],
        "summary": "List Lookup Tables",
        "parameters": [
          {
            "in": "query",
            "name": "project_id",
            "required": true,
            "schema": {
              "default": "<YOUR_PROJECT_ID>",
              "type": "string"
            },
            "description": "The Mixpanel project_id, used to authenticate service account credentials."
          }
        ],
        "description": "Get a list of Lookup Tables defined in the project.",
        "responses": {
          "200": {
            "$ref": "#/components/responses/LookupTableList"
          },
          "401": {
            "$ref": "#/components/responses/StrictUnauthorized"
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "ServiceAccount": {
        "type": "http",
        "scheme": "basic",
        "description": "Service Account"
      }
    },
    "responses": {
      "LookupTableList": {
        "description": "The list of Lookup Tables.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "number"
                },
                "status": {
                  "type": "string"
                },
                "results": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "string",
                        "format": "uuid"
                      },
                      "name": {
                        "type": "string"
                      }
                    }
                  }
                }
              },
              "example": {
                "code": 200,
                "status": "OK",
                "results": [
                  {
                    "id": "55b4fb2b-e8de-466c-930f-8b36640b9b5e",
                    "name": "Accounts"
                  },
                  {
                    "id": "1297297a-43a7-4cac-82b0-635d2bd88aac",
                    "name": "Product Catalog"
                  }
                ]
              }
            }
          }
        }
      },
      "StrictUnauthorized": {
        "description": "A 401 response indicates invalid credentials.",
        "content": {
          "application/json": {
            "schema": {
              "type": "object",
              "properties": {
                "code": {
                  "type": "integer"
                },
                "error": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                }
              },
              "example": {
                "code": 401,
                "error": "Invalid credentials",
                "status": "Unauthorized"
              }
            }
          }
        }
      }
    }
  },
  "x-readme-deploy-id": "ingestion",
  "x-explorer-enabled": true,
  "x-proxy-enabled": true,
  "x-samples-enabled": true,
  "x-samples-languages": [
    "curl",
    "node",
    "ruby",
    "javascript",
    "python"
  ]
}
```