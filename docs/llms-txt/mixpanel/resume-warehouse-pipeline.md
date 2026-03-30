# Source: https://developer.mixpanel.com/reference/resume-warehouse-pipeline.md

# Resume Pipeline

For a given pipeline name, this request resumes the pipeline if it's paused

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
      "name": "Resume Pipelines",
      "description": "Resume a paused pipeline"
    }
  ],
  "paths": {
    "/nessie/pipeline/resume": {
      "post": {
        "tags": [
          "Resume Pipelines"
        ],
        "summary": "Resume Pipeline",
        "operationId": "resume-warehouse-pipeline",
        "description": "For a given pipeline name, this request resumes the pipeline if it's paused",
        "requestBody": {
          "required": true,
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "The name that uniquely identifies the pipeline."
                  },
                  "project_id": {
                    "$ref": "#/components/schemas/ProjectId"
                  }
                },
                "required": [
                  "name"
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Success"
          },
          "401": {
            "$ref": "#/components/responses/Unauthorized"
          },
          "403": {
            "$ref": "#/components/responses/Forbidden"
          },
          "404": {
            "$ref": "#/components/responses/NotFound"
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
      },
      "NotFound": {
        "description": "Not Found",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
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