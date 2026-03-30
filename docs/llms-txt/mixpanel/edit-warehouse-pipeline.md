# Source: https://developer.mixpanel.com/reference/edit-warehouse-pipeline.md

# Edit Pipeline

This request edit the params for an export pipeline.


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
      "name": "Edit Pipelines",
      "description": "Edit the params for a pipeline from a project"
    }
  ],
  "paths": {
    "/nessie/pipeline/edit": {
      "post": {
        "tags": [
          "Edit Pipelines"
        ],
        "operationId": "edit-warehouse-pipeline",
        "summary": "Edit Pipeline",
        "description": "This request edit the params for an export pipeline.\n",
        "requestBody": {
          "required": true,
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "oneOf": [
                  {
                    "title": "Raw GCS Pipeline",
                    "$ref": "#/components/schemas/RawEditParams"
                  },
                  {
                    "title": "Raw Amazon S3 Pipeline",
                    "$ref": "#/components/schemas/RawEditParams"
                  },
                  {
                    "title": "Raw Azure Pipeline",
                    "$ref": "#/components/schemas/RawAzureEditParams"
                  },
                  {
                    "title": "Schematized BigQuery Pipeline",
                    "$ref": "#/components/schemas/BigQueryEditParams"
                  },
                  {
                    "title": "Schematized Snowflake Pipeline",
                    "$ref": "#/components/schemas/SchematizedEditParams"
                  },
                  {
                    "title": "Schematized AWS Pipeline",
                    "$ref": "#/components/schemas/SchematizedAWSEditParams"
                  },
                  {
                    "title": "Schematized Azure Pipeline",
                    "$ref": "#/components/schemas/SchematizedAzureEditParams"
                  },
                  {
                    "title": "Schematized GCS Pipeline",
                    "$ref": "#/components/schemas/SchematizedEditParams"
                  }
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
      "RawEditParams": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name that uniquely identifies the pipeline."
          },
          "project_id": {
            "$ref": "#/components/schemas/ProjectId"
          },
          "events": {
            "type": "string",
            "description": "A whitelist for the event(s) you intend to export. For multiple events, you will need to pass in each event name as separate `events` parameters like so: `--data 'events=event1' \\ --data 'events=event2'`\n\n\nPlease note that after this update, the sync of older dates to your data warehouse\n(if enabled) will only contain the new set of whitelisted events.\n"
          },
          "where": {
            "type": "string",
            "description": "A selector expression used to filter by events data, such as event properties.\n\nPlease note that after this update, the sync of older dates to your data warehouse (if enabled) will only contain events matching your new where clause."
          }
        },
        "required": [
          "name"
        ]
      },
      "SchematizedEditParams": {
        "allOf": [
          {
            "$ref": "#/components/schemas/RawEditParams"
          }
        ]
      },
      "AzureCommonEditParams": {
        "type": "object",
        "properties": {
          "azure_client_id": {
            "type": "string",
            "description": "`clientId` from the Service Principal credentials.\n"
          },
          "azure_client_secret": {
            "type": "string",
            "description": "`clientSecret` from the Service Principal credentials.\n"
          },
          "azure_tenant_id": {
            "type": "string",
            "description": "`tenantId` from the Service Principal credentials. This is specific to the Active Directory instance where the Service Principal resides.\n"
          }
        }
      },
      "RawAzureEditParams": {
        "allOf": [
          {
            "$ref": "#/components/schemas/RawEditParams"
          },
          {
            "$ref": "#/components/schemas/AzureCommonEditParams"
          }
        ]
      },
      "SchematizedAzureEditParams": {
        "allOf": [
          {
            "$ref": "#/components/schemas/SchematizedEditParams"
          },
          {
            "$ref": "#/components/schemas/AzureCommonEditParams"
          }
        ]
      },
      "BigQueryEditParams": {
        "allOf": [
          {
            "$ref": "#/components/schemas/SchematizedEditParams"
          },
          {
            "type": "object",
            "properties": {
              "bq_share_with_group": {
                "type": "array",
                "description": "Group account email addresses to share the data-set with if managed by mixpanel. e.g. bq-access-alias@somecompany.com.\n\nPlease note that this will only add new shares and won't remove the old ones.\n",
                "items": {
                  "type": "string"
                }
              }
            }
          }
        ]
      },
      "SchematizedAWSEditParams": {
        "allOf": [
          {
            "$ref": "#/components/schemas/SchematizedEditParams"
          },
          {
            "type": "object",
            "properties": {
              "glue_database": {
                "type": "string",
                "description": "The glue database to which the schema needs to be exported.\n"
              },
              "glue_role": {
                "type": "string",
                "description": "There is no default value. The role that needs to be assumed for updating glue  e.g. arn:aws:iam::<account-id>:role/example-glue-role\n"
              },
              "glue_table_prefix": {
                "type": "string",
                "description": "Prefix to add to table names when creating them.\n"
              }
            }
          }
        ]
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