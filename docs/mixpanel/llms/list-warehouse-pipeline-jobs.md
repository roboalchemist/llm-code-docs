# Source: https://developer.mixpanel.com/reference/list-warehouse-pipeline-jobs.md

# List Pipelines

This API endpoint returns the list of all the pipelines scheduled for a project.

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
    "/nessie/pipeline/jobs": {
      "get": {
        "operationId": "list-warehouse-pipeline-jobs",
        "tags": [
          "Retrieve Pipelines"
        ],
        "summary": "List Pipelines",
        "description": "This API endpoint returns the list of all the pipelines scheduled for a project.",
        "parameters": [
          {
            "$ref": "#/components/parameters/projectId"
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
                      "9876543210": [
                        {
                          "name": "events-daily-bigquery-monoschema",
                          "Dispatcher": "backfill",
                          "last_dispatched": "2019-02-01 12:00:00 US/Pacific",
                          "frequency": "hourly",
                          "sync_enabled": "true"
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