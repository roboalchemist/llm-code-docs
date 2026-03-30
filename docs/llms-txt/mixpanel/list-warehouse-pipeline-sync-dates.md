# Source: https://developer.mixpanel.com/reference/list-warehouse-pipeline-sync-dates.md

# List Pipeline Logs

This endpoint returns the timestamps of all syncs grouped by date.

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "Data Pipelines API",
    "description": "Create and manage a continious pipeline with an external warehouse.",
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
      "url": "https://{server}.mixpanel.com/api/2.0",
      "description": "Mixpanel's data export server.",
      "variables": {
        "server": {
          "default": "data",
          "enum": [
            "data",
            "data-eu",
            "data-in"
          ],
          "description": "The server location to be used:\n  * `data` - The default (US) servers used for most projects\n  * `data-eu` - EU servers if you are enrolled in EU Data Residency\n  * `data-in` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "security": [
    {
      "ServiceAccount": []
    },
    {
      "ProjectSecret": []
    }
  ],
  "tags": [
    {
      "name": "Retrieve Pipelines",
      "description": "Get information about Pipelines"
    }
  ],
  "paths": {
    "/nessie/pipeline/timeline": {
      "get": {
        "operationId": "list-warehouse-pipeline-sync-dates",
        "tags": [
          "Retrieve Pipelines"
        ],
        "summary": "List Pipeline Logs",
        "description": "This endpoint returns the timestamps of all syncs grouped by date.",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
          },
          {
            "in": "query",
            "name": "name",
            "schema": {
              "type": "string"
            },
            "description": "The name that uniquely identifies the pipeline."
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "examples": {
                  "example": {
                    "value": {
                      "day_syncs": [
                        {
                          "date": "2019-08-19",
                          "sync_times": [
                            "2019-08-19 14:27:46.044605 -0700 PDT"
                          ],
                          "status": "synced"
                        },
                        {
                          "date": "2019-08-20",
                          "sync_times": [
                            " 2019-08-20 14:33:09.315098 -0700 PDT"
                          ],
                          "status": "synced"
                        }
                      ]
                    }
                  }
                }
              }
            }
          },
          "401": {
            "$ref": "#/components/responses/Unauthorized"
          },
          "403": {
            "$ref": "#/components/responses/Forbidden"
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
      },
      "ProjectSecret": {
        "type": "http",
        "scheme": "basic",
        "description": "Project Secret"
      }
    },
    "schemas": {
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string"
          },
          "status": {
            "type": "string",
            "enum": [
              "error"
            ]
          }
        }
      }
    },
    "responses": {
      "Unauthorized": {
        "description": "Unauthorized",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      },
      "Forbidden": {
        "description": "Forbidden",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      }
    },
    "parameters": {
      "projectId": {
        "in": "query",
        "name": "project_id",
        "schema": {
          "type": "integer"
        },
        "description": "Required if using service account to authenticate request.",
        "required": true
      }
    }
  },
  "x-readme-deploy-id": "data-pipelines-api",
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