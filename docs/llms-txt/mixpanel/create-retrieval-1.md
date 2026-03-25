# Source: https://developer.mixpanel.com/reference/create-retrieval-1.md

# Create a Retrieval

Creates a data retrieval job.

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
      "name": "Create a Retrieval",
      "description": "Creates a data retrieval job"
    }
  ],
  "paths": {
    "/data-retrievals/v3.0": {
      "post": {
        "parameters": [
          {
            "$ref": "#/components/parameters/ProjectToken"
          }
        ],
        "operationId": "create-retrieval",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "distinct_ids": {
                    "$ref": "#/components/schemas/DistinctIds"
                  },
                  "compliance_type": {
                    "$ref": "#/components/schemas/ComplianceType"
                  },
                  "disclosure_type": {
                    "$ref": "#/components/schemas/DisclosureType"
                  }
                }
              }
            }
          }
        },
        "tags": [
          "Create a Retrieval"
        ],
        "summary": "Create a Retrieval",
        "description": "Creates a data retrieval job.",
        "responses": {
          "201": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/JobCreated"
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
      "JobCreated": {
        "title": "JobCreated",
        "description": "A JSON response object containing the task_id of the retrieval/deletion job.",
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
            "type": "object",
            "properties": {
              "task_id": {
                "type": "string",
                "description": "The task_id of the retrieval/deletion job.",
                "example": "job-tracking-id"
              }
            }
          }
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
      "ComplianceType": {
        "type": "string",
        "description": "Select CCPA or GDPR. Default is GDPR."
      },
      "DisclosureType": {
        "type": "string",
        "description": "Only required if compliance_type = CCPA. Can be Data, Categories, or Sources. Default is Data."
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
    "parameters": {
      "ProjectToken": {
        "name": "token",
        "in": "query",
        "schema": {
          "type": "string"
        },
        "description": "Your project token",
        "required": true
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