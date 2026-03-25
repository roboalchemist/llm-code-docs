# Source: https://developer.mixpanel.com/reference/get-retrieval.md

# Check Status of Retrieval

Checks the status of a data retrieval job

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
      "name": "Check Status of Retrieval",
      "description": "Checks the status of a data retrieval job"
    }
  ],
  "paths": {
    "/data-retrievals/v3.0/{tracking_id}": {
      "parameters": [
        {
          "$ref": "#/components/parameters/TrackingId"
        },
        {
          "$ref": "#/components/parameters/ProjectToken"
        }
      ],
      "get": {
        "operationId": "get-retrieval",
        "tags": [
          "Check Status of Retrieval"
        ],
        "summary": "Check Status of Retrieval",
        "description": "Checks the status of a data retrieval job",
        "responses": {
          "200": {
            "description": "Success",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/CheckRetrievalResponse"
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
      "CheckRetrievalResponse": {
        "title": "CheckRetrievalResponse",
        "description": "A JSON response object containing data about a retrieval job",
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
              "results": {
                "type": "string",
                "description": "Link to the export if retrieval job is completed. Will be an empty string if job is incomplete",
                "example": "linktoexportfile.com/9871287366712"
              },
              "distinct_ids": {
                "$ref": "#/components/schemas/DistinctIds"
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