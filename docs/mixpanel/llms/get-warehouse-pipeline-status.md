# Source: https://developer.mixpanel.com/reference/get-warehouse-pipeline-status.md

# Get Pipeline

Given the name of the pipeline this API returns the status of the pipeline. It returns the summary and status of all the recent run export jobs for the pipeline.

**Example Response:** Status with no Summary and a Filter

```sh
curl https://data.mixpanel.com/api/2.0/nessie/pipeline/status \
  -u API_SECRET: \
  -d name="YOUR_PIPELINE_NAME" \
  -d status="running"
```

**Example Response:** Status with no Summary and a Filter

```json
{
  "canceled": [
    {
      "name": "company-july-2016-backfill-hourly-monoschema",
      "state": "canceled",
      "last_finish": "0000-12-31T16:00:00-08:00",
      "run_at": "2016-07-26T00:00:00-07:00",
      "from_date": "2016-07-26T00:00:00-07:00",
      "to_date": "2016-07-26T00:00:00-07:00"
    },
  ]
}
```

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
    "/nessie/pipeline/status": {
      "get": {
        "operationId": "get-warehouse-pipeline-status",
        "summary": "Get Pipeline",
        "tags": [
          "Retrieve Pipelines"
        ],
        "description": "",
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
            "description": "The name that uniquely identifies the pipeline.",
            "required": true
          },
          {
            "in": "query",
            "name": "summary",
            "schema": {
              "type": "string"
            },
            "description": "Default: `false`. Only lists task count by status and no details."
          },
          {
            "in": "query",
            "name": "status",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "description": "Filters the tasks by the given status. Valid options for status are `pending`, `running`, `retried`, `failed`, `canceled`, and `timed_out`.\n"
          }
        ],
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/PipelineStatusResponse"
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
      "ProjectId": {
        "type": "number",
        "description": "Your project id (must be specified when using service account based authentication)"
      },
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
      },
      "PipelineStatusJobList": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "project_id": {
              "$ref": "#/components/schemas/ProjectId"
            },
            "name": {
              "type": "string"
            },
            "state": {
              "type": "string"
            },
            "last_finish": {
              "type": "string"
            },
            "run_at": {
              "type": "string"
            },
            "from_date": {
              "type": "string"
            },
            "to_date": {
              "type": "string"
            }
          }
        }
      },
      "PipelineStatusResponse": {
        "type": "object",
        "properties": {
          "canceled": {
            "$ref": "#/components/schemas/PipelineStatusJobList"
          },
          "retried": {
            "$ref": "#/components/schemas/PipelineStatusJobList"
          },
          "succeeded": {
            "$ref": "#/components/schemas/PipelineStatusJobList"
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