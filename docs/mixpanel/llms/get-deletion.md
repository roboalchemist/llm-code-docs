# Source: https://developer.mixpanel.com/reference/get-deletion.md

# Check Status of Deletion

Checks the status of an existing deletion task

# OpenAPI definition

```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "GDPR API",
    "description": "The following retrieval and deletion API is made for GDPR and CCPA compliance.",
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "contact": {
      "url": "https://mixpanel.com/get-support"
    },
    "version": "3.0.0"
  },
  "servers": [
    {
      "url": "https://{regionAndDomain}.com/api/app",
      "description": "Mixpanel's application API server.",
      "variables": {
        "regionAndDomain": {
          "default": "mixpanel",
          "enum": [
            "mixpanel",
            "eu.mixpanel",
            "in.mixpanel"
          ],
          "description": "The server location to be used:\n  * `mixpanel` - The default (US) servers used for most projects\n  * `eu.mixpanel` - EU servers if you are enrolled in EU Data Residency\n  * `in.mixpanel` - India servers if you are enrolled in India Data Residency\n"
        }
      }
    }
  ],
  "security": [
    {
      "OAuthToken": []
    }
  ],
  "tags": [
    {
      "name": "Check Status of Deletion",
      "description": "Checks the status of an existing deletion task"
    }
  ],
  "paths": {
    "/data-deletions/v3.0/{tracking_id}": {
      "parameters": [
        {
          "$ref": "#/components/parameters/TrackingId"
        },
        {
          "$ref": "#/components/parameters/ProjectToken"
        }
      ],
      "get": {
        "operationId": "get-deletion",
        "tags": [
          "Check Status of Deletion"
        ],
        "summary": "Check Status of Deletion",
        "description": "Checks the status of an existing deletion task",
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CheckDeletionResponse"
                }
              }
            }
          },
          "401": {
            "$ref": "#/components/responses/401Unauthorized"
          },
          "403": {
            "$ref": "#/components/responses/403Forbidden"
          }
        }
      }
    }
  },
  "components": {
    "securitySchemes": {
      "OAuthToken": {
        "type": "http",
        "scheme": "bearer",
        "description": "OAuth Token"
      }
    },
    "schemas": {
      "CheckDeletionResponse": {
        "title": "CheckDeletionResponse",
        "description": "A JSON response object containing data about a data deletion job",
        "type": "object",
        "additionalProperties": false,
        "required": [
          "status",
          "results"
        ],
        "properties": {
          "status": {
            "$ref": "#/components/schemas/ResponseStatus"
          },
          "results": {
            "$ref": "#/components/schemas/DeletionJobResult"
          }
        }
      },
      "DeletionJobResult": {
        "title": "DeletionJobResult",
        "description": "Details about a deletion job",
        "type": "object",
        "additionalProperties": false,
        "required": [
          "tracking_id",
          "status",
          "requesting_user",
          "compliance_type",
          "project_id",
          "date_requested",
          "distinct_ids"
        ],
        "properties": {
          "tracking_id": {
            "type": "string",
            "description": "The tracking id of the deletion job"
          },
          "status": {
            "type": "string",
            "description": "The status of the job.",
            "enum": [
              "PENDING",
              "STAGING",
              "STARTED",
              "SUCCESS",
              "FAILURE",
              "REVOKED",
              "NOT_FOUND",
              "UNKNOWN"
            ],
            "example": "SUCCESS"
          },
          "requesting_user": {
            "type": "string",
            "description": "The user that created the deletion job request"
          },
          "compliance_type": {
            "type": "string",
            "description": "GDPR or CCPA"
          },
          "project_id": {
            "type": "number",
            "description": "The id of the project this job is for"
          },
          "date_requested": {
            "type": "string",
            "description": "The timestamp when the deletion job was requested"
          },
          "distinct_ids": {
            "$ref": "#/components/schemas/DistinctIds"
          }
        },
        "example": {
          "tracking_id": "job tracking_id",
          "status": "SUCCESS",
          "requesting_user": "user@mail.com",
          "compliance_type": "GDPR",
          "project_id": "your project ID",
          "date_requested": "YYYY-MM-DDTHH:MM:SS",
          "distinct_ids": [
            "distinct_id_1",
            "distinct_id_2"
          ]
        }
      },
      "ResponseStatus": {
        "type": "string",
        "description": "The status of the response",
        "example": "ok"
      },
      "DistinctIds": {
        "type": "array",
        "items": {
          "type": "string",
          "description": "Distinct IDs involved in the request"
        },
        "example": [
          "distinct_id_1",
          "distinct_id_2",
          "distinct_id_3"
        ]
      },
      "ErrorResponse": {
        "type": "object",
        "properties": {
          "error": {
            "type": "string",
            "description": "Details about the error that occurred"
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
      "401Unauthorized": {
        "description": "Unauthorized",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/ErrorResponse"
            }
          }
        }
      },
      "403Forbidden": {
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
  }
}
```